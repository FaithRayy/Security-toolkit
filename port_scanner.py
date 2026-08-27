import socket
import sys

def main(fromPort, toPort):
    # The target of the scan is the localhost 
    target = "localhost"

    # Ports from the given range are checked if they're open
    for port in range(fromPort, toPort):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Quick connection is attempted for each port
        connection.settimeout(0.5)
        result = connection.connect_ex((target, port))

        if result == 0:
            print(f"Port {port}: open")
        connection.close()

if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a port range of 'from' and 'to' - only.")
    
    fromPort = int(args[1])
    toPort = int(args[2])
    main(fromPort, toPort)