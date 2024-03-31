# Asks the user to input the number of colleges they want to compare
num_colleges = int(input("How many colleges are you choosing between?: "))

# Collects the names of the colleges
def college_names(): 
    colleges = []
    # Loop through each college to collect its name
    for i in range(num_colleges):
        # Prompt the user to input the name of each college
        college_name = input(f"Enter the name of college {i+1}: ")
        # Append the name of the college to the list of colleges
        colleges.append((college_name))
    return colleges

# Store the names of the colleges in a list
colleges = college_names()

# Asks the user to input the most important factors
factors = input("Name the most important factors to you separated by commas: ")

# Split the input string by commas to get a list of factors
elements = factors.split(',')

# Convert the elements into a list with elements stripped of whitespace and titlecased 
factors = [element.strip().title() for element in elements]

# Creates an empty dictionary to store the factors and their importance rankings provided by the user
importance_rankings = {}

# Collects the importance rankings for each factor
def factor_importance_ranking():
    # Iterate through each factor to collect its importance ranking
    for factor in factors: 
        # Ensures valid input 
        while True:
            try:
                # Asks the user to rank the importance of the factor on a scale of 0 to 100
                importance = round(int(input(f"On a scale of 1 to 100, how important is {factor}: ")) * 0.1, 2)
                # Check if the input is within the valid range
                if 0 <= importance <= 100:
                    # Store the importance ranking for the factor in the dictionary
                    importance_rankings[factor] = importance
                    break
                else:
                    print("Please enter a number between 0 and 100.")
            except ValueError:
                print("Please enter a valid integer.")    

# Call the function to collect the importance rankings for each factor
factor_importance_ranking()

# Initialize an empty dictionary to store points for each college
college_points = {college: 0 for college in colleges}

# Function to compare colleges for each factor and assign points
def compare_colleges():
    for college in colleges:
        print(f"\nComparing colleges for {college}:")
        for factor in factors:
            rating = input(f"How does {college} compare to the other colleges in {factor}? (Better/Similar/Worse): ").strip().lower()
            if rating == "better":
                college_points[college] += 1 * importance_rankings[factor]
            elif rating == "similar":
#Iterates over each college in the list colleges, Filters out the current college being evaluated, Adds the filtered colleges to a new list similar_colleges
                similar_colleges = [c for c in colleges if c != college]
# Calculate points for similar colleges based on factor importance, Ensure current college receives points even if no similar colleges exist
                points_per_college = importance_rankings[factor] / (len(similar_colleges) + 1)
# Initiate a loop that iterates over each college in the similar_colleges list.
                for similar_college in similar_colleges:
#Distributed points evenly among similar colleges, giving them each a portion of the total points calculated based on the importance of the factor.
                    college_points[similar_college] += points_per_college

# Call the function to compare colleges and assign points
compare_colleges()

# Print points for each college
print("\nPoints for each college:")
for college, points in college_points.items():
    print(f"{college}: {points} points")