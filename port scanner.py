import sys
import socket
from datetime import datetime

# Define the Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Converts Hostname to IPV4
else:
    print("Invalid amout of arguments.")
    print("Syntax: python2 portscanner.py <ip>")

# Banner
print("-" * 50)
print("Scanner target" + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 443):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(.5)
        result = s.connect_ex((target, port))  # returns an error indicator
        if result == 0:
            print("Port {} is open".format(port))
            print("Running")
        s.close()

except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to server.")
    sys.exit()
