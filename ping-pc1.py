import subprocess
import time

# Function to ping and display the output
def ping(address):
    # Start a ping process
    process = subprocess.Popen(['ping', address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return process

# Ping 192.168.
for _ in range(10):
    print(f"Pinging 192.168.0.210...")
    process = ping('192.168.23.1')
    
    for line in process.stdout:
        print(line.strip())  # Print each line of output
    
    time.sleep(1)  # Wait for 1 second between pings

# Ensure the process is finished
process.wait()
