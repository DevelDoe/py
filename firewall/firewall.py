import socket

# Define the IP address and port to listen on
HOST = '127.0.0.1'
PORT = 8080

def main():
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the specified address and port
    sock.bind((HOST, PORT))

    # Start listening for incoming connections
    sock.listen(1)
    print(f"Firewall is now active. Listening on {HOST}:{PORT}...")

    while True:
        # Accept incoming connections
        conn, addr = sock.accept()
        print(f"Incoming connection from: {addr[0]}:{addr[1]}")

        # Check if the incoming connection is on port 445 (Windows SMB)
        if addr[1] != 445:
            # Block the connection
            conn.close()
            print("Connection blocked.")
        else:
            # Allow the connection
            print("Connection allowed.")

if __name__ == '__main__':
    main()
