import itertools

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
        colleges.append(college_name)  # Fixed parentheses here
    return colleges

# Store the names of the colleges in a list
colleges = college_names()

# Asks the user to input the most important factors
factors_input = input("Name the most important factors to you separated by commas: ")

# Split the input string by commas to get a list of factors
factors = [factor.strip().title() for factor in factors_input.split(',')]

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
    # Iterate over each combination of colleges
    for college1, college2 in itertools.combinations(colleges, 2):
        # Print the comparison being made
        print(f"\nComparing {college1} and {college2}:")
        # Iterate over each factor
        for factor in factors:
            # Ask the user to compare the two colleges for the current factor
            rating = input(f"How does {college1} compare to {college2} in {factor}? (Better/Similar/Worse): ").strip().lower()
            # Assign points based on the user's input
            if rating == "better":
                college_points[college1] += 1 * importance_rankings[factor]
            elif rating == "similar":
                # Calculate points for similar colleges based on factor importance
                points_per_college = importance_rankings[factor] / 2
                # Distribute points evenly among similar colleges
                college_points[college1] += points_per_college
                college_points[college2] += points_per_college
            elif rating == "worse":
                college_points[college2] += 1 * importance_rankings[factor]

# Call the function to compare colleges and assign points
compare_colleges()

# Print total points for each college
print("\nTotal points for each college:")
for college, points in college_points.items():
    print(f"{college}: {points} points")
