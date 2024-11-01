import random
from datetime import datetime, timedelta

# Define the possible error codes and user IDs
errors = ["ERROR_404", "ERROR_500", "ERROR_403", "ERROR_502"]
users = ["user123", "user456", "user789", "user101"]

# Define the number of log entries to generate
num_entries = 1000  # You can adjust this for more or fewer entries

# Open the file in write mode
with open("logs/sample_log.txt", "w") as f:
    for _ in range(num_entries):
        # Generate a random timestamp within the last 24 hours
        timestamp = datetime.now() - timedelta(seconds=random.randint(0, 86400))
        # Format the timestamp
        timestamp_str = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        # Randomly choose a user ID and error code
        user = random.choice(users)
        error = random.choice(errors)
        # Write the formatted log entry to the file
        f.write(f"{timestamp_str} {user} {error}\n")

print("Log file generated successfully!")
