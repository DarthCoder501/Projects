import re
from dateutil import parser
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import pickle
from datetime import timedelta
from pypdf import PdfReader
import docx
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Function to extract text from a file (PDF or DOCX)
def extract_text(file_path):
    if file_path.endswith('.pdf'):
        reader = PdfReader(file_path)
        extracted_text = ""
        for i in range(len(reader.pages)):
            extracted_text += reader.pages[i].extract_text()
        return extracted_text
    
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    full_text.append(cell.text)
        return '\n'.join(full_text)
    
    else:
        with open(file_path, 'r') as file:
            return file.read()

# Function to identify the section of the syllabus that contains the course schedule
def identify_schedule_section(text):
    potential_keywords = ["COURSE SCHEDULE", "Timeline", "Important Dates", "Class Schedule", "Agenda"]
    for keyword in potential_keywords:
        match = re.search(rf'{keyword}(.*?)(?=\n\n|Final Exam:|End of Class)', text, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()

    logging.info("Potential schedule sections found:")
    sections = re.findall(r'(.*?(?:\n\d{1,2}\s\w+|\n\w+\s\d{1,2}))', text, re.DOTALL)
    for i, section in enumerate(sections):
        logging.info(f"Section {i+1}:")
        logging.info(section[:500])  # Print the first 500 characters of the section for context
        logging.info("\n" + "-"*40 + "\n")

    choice = int(input(f"Select the correct section (1-{len(sections)}), or 0 to abort: "))
    if 0 < choice <= len(sections):
        return sections[choice-1]
    else:
        return None

# Enhanced date and event extraction
def extract_dates_events(text):
    date_event_pairs = []
    date_pattern = r"""
    (
        (?:
            \b(?:\d{1,2})(?:st|nd|rd|th)?[ ]?(?:-|/|\s)?(?:\d{1,2})(?:-|/|\s)?(?:\d{2,4})?\b |
            \b(?:\d{1,2})(?:st|nd|rd|th)?[ ]?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[ ]?(?:\d{2,4})?\b |
            \b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[ ]\d{1,2}(?:st|nd|rd|th)?[ ]?(?:,?[ ]?\d{2,4})?\b |
            \b(?:January|February|March|April|May|June|July|August|September|October|November|December)[ ]\d{1,2}(?:st|nd|rd|th)?[ ]?(?:,?[ ]?\d{2,4})?\b
        )
    )
    """
    date_pattern = re.compile(date_pattern, re.VERBOSE)
    lines = text.split('\n')
    current_date = None
    
    for line in lines:
        date_match = date_pattern.search(line)
        if date_match:
            try:
                current_date = parser.parse(date_match.group())
                event = line[date_match.end():].strip()
                if event:
                    date_event_pairs.append((event, current_date))
                    logging.debug(f"Extracted: Event '{event}' on {current_date}")
            except Exception as e:
                logging.warning(f"Failed to parse date: {date_match.group()}. Error: {str(e)}")
        elif current_date and line.strip():
            date_event_pairs.append((line.strip(), current_date))
            logging.debug(f"Extracted: Event '{line.strip()}' on {current_date}")
    
    return date_event_pairs

# Function to create reminder times for each event based on its date
def create_reminders(event_date):
    intervals = [1, 3, 7, 14, 30]
    reminders = [(event_date - timedelta(days=i)) for i in intervals]
    return reminders

# Google Calendar API authentication function
SCOPES = ['https://www.googleapis.com/auth/calendar']

def authenticate_google_calendar():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service

# Function to add events to Google Calendar
def add_to_google_calendar(event_name, event_date, reminders):
    service = authenticate_google_calendar()
    event = {
        'summary': event_name,
        'start': {'dateTime': event_date.isoformat(), 'timeZone': 'America/New_York'},
        'end': {'dateTime': (event_date + timedelta(hours=1)).isoformat(), 'timeZone': 'America/New_York'},
        'reminders': {
            'useDefault': False,
            'overrides': [{'method': 'popup', 'minutes': int((event_date - reminder).total_seconds() // 60)} for reminder in reminders],
        },
    }
    try:
        created_event = service.events().insert(calendarId='primary', body=event).execute()
        logging.info(f'Event created: {created_event.get("htmlLink")}')
    except Exception as e:
        logging.error(f"Failed to create event: {event_name} on {event_date}. Error: {str(e)}")

# Main function to process the syllabus and add events to Google Calendar
def process_syllabus():
    file_path = input("Please provide the full path to the syllabus file (PDF or DOCX): ")
    text = extract_text(file_path)
    course_schedule_text = identify_schedule_section(text)
    
    if course_schedule_text:
        logging.info(f"Identified Schedule Section:\n{course_schedule_text[:500]}...")  # Debugging: Print the start of the schedule section
        
        date_event_pairs = extract_dates_events(course_schedule_text)
        logging.info(f"Extracted {len(date_event_pairs)} date-event pairs")
        
        for event_name, event_date in date_event_pairs:
            reminders = create_reminders(event_date)
            logging.info(f"Adding event: {event_name} on {event_date}")
            add_to_google_calendar(event_name, event_date, reminders)
    else:
        logging.warning("Could not identify the course schedule section.")

if __name__ == "__main__":
    process_syllabus()
