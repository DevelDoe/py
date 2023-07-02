import subprocess

def get_active_users():
    active_users = []
    try:
        # Run the "query user" command to get the list of active sessions
        result = subprocess.check_output(['query', 'user']).decode('utf-8')
        
        # Split the output into lines and skip the header
        lines = result.split('\n')[1:]
        
        # Process each line to extract the username
        for line in lines:
            parts = line.split()
            if len(parts) >= 3:
                username = parts[0]
                active_users.append(username)
    
    except subprocess.CalledProcessError:
        print("Error retrieving active users.")
    
    return active_users

def get_logged_in_users():
    logged_in_users = []
    try:
        # Read the file to get the previously logged-in users
        with open('logged_in_users.txt', 'r') as file:
            for line in file:
                user = line.strip()
                logged_in_users.append(user)
    
    except FileNotFoundError:
        print("No previous logged-in users found.")
    
    return logged_in_users

def save_logged_in_users(users):
    try:
        # Write the current logged-in users to the file
        with open('logged_in_users.txt', 'w') as file:
            for user in users:
                file.write(user + '\n')
    
    except IOError:
        print("Error saving logged-in users.")

# Get the active users
active_users = get_active_users()

# Get the previously logged-in users
logged_in_users = get_logged_in_users()

# Print the active users
print("Active Users:")
if active_users:
    for user in active_users:
        print(user)
else:
    print("No active users found.")

# Determine the newly logged-in users
newly_logged_in_users = set(active_users) - set(logged_in_users)

# Print the report of newly logged-in users
print("\nReport of Newly Logged-In Users:")
if newly_logged_in_users:
    for user in newly_logged_in_users:
        print(user)
else:
    print("No newly logged-in users found.")

# Save the current active users as the logged-in users for the next run
save_logged_in_users(active_users)
