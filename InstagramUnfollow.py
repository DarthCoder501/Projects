import json
import csv

# Load follower data
with open('followers_1.json', 'r') as f:
    followers_data = json.load(f)

# Load following data
with open('following.json', 'r') as g:
    following_data = json.load(g)

# Initialize lists to store all followers and following
followers_list = []
following_list = []

# Add followers to the followers_list
for follower in followers_data:
    if 'string_list_data' in follower and len(follower['string_list_data']) > 0:
        followers_list.append(follower['string_list_data'][0]['value'])

# Add following to the following_list
if 'relationships_following' in following_data:
    for following in following_data['relationships_following']:
        if 'string_list_data' in following and len(following['string_list_data']) > 0:
            following_list.append(following['string_list_data'][0]['value'])

# Sort both lists
followers_list.sort()
following_list.sort()

# Print the number of followers and following to debug if data is right
print(f"Followers count: {len(followers_list)}")
print(f"Following count: {len(following_list)}")

# Create a list to store users who don't follow back
unfollow = [user for user in following_list if user not in followers_list]

# Save the unfollow list to a CSV file
with open('unfollow_list.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Username"])  # Write header
    for user in unfollow:
        writer.writerow([user])

print("Unfollow list saved to 'unfollow_list.csv'.")
# Print the list of accounts that don't follow back
print("Accounts that don't follow back:")
print(unfollow)
