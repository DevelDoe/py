import socket
import argparse
import sys
import os
import time

# Define the target host and port range to scan
target_host = 'localhost'
start_port = 1
end_port = 9999

# Create an argument parser for the verbose flag
parser = argparse.ArgumentParser(description='Port Scanner')
parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose mode')
args = parser.parse_args()

# Define the path to the file that keeps track of the last execution timestamp
last_execution_file = "last_execution.txt"

# Check if the file exists
if os.path.isfile(last_execution_file):
    # Read the timestamp from the file
    with open(last_execution_file, 'r') as file:
        last_execution_timestamp = float(file.read())

    # Get the current timestamp
    current_timestamp = time.time()

    # Calculate the time difference in days
    days_passed = (current_timestamp - last_execution_timestamp) / (24 * 60 * 60)

    # Check if less than 30 days have passed since the last execution
    if days_passed < 30:
        sys.exit()

# Store the current timestamp in the file
with open(last_execution_file, 'w') as file:
    file.write(str(time.time()))

# List to store open ports
open_ports = []

# Perform port scanning
for port in range(start_port, end_port + 1):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout value for the connection attempt
        sock.settimeout(2)

        # Attempt to connect to the target host and port
        result = sock.connect_ex((target_host, port))

        # Print the port being scanned in verbose mode
        if args.verbose:
            print(f"\rScanning port {port}... ", end='', flush=True)

        # Check if the port is open
        if result == 0:
            open_ports.append(port)

        # Close the socket connection
        sock.close()

    except socket.error:
        print(f"Error connecting to port {port}")

# Display open ports summary
print("\nScanning completed.")
print("\nOpen Ports Summary:")
if open_ports:
    for port in open_ports:
        print(f"Port {port} is open")
else:
    print("No open ports found.")

# Wait for user to press Enter before exiting
input("Press Enter to exit...")
