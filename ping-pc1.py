import subprocess
import time

def ping(address):
    process = subprocess.Popen(['ping', address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return process

for _ in range(10):
    print(f"Pinging 192.168.0.210...")
    process = ping('192.168.23.1')
    
    for line in process.stdout:
        print(line.strip())  
    
    time.sleep(1)  
process.wait()
