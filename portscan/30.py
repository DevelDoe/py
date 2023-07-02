import time

# Get the current timestamp
current_timestamp = time.time()

# Subtract 31 days (31 * 24 * 60 * 60 seconds) to get a timestamp more than 30 days in the past
past_timestamp = current_timestamp - (31 * 24 * 60 * 60)

print(past_timestamp)