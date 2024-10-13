import psutil
import time

CPU_THRESHOLD = 0.1
MEMORY_THRESHOLD = 500 * 1024 * 1024 
def check_vpcs_usage():
    for proc in psutil.process_iter(['name', 'cpu_percent', 'memory_info']):
        if 'vpcs' in proc.info['name']:
            cpu_usage = proc.info['cpu_percent']
            memory_usage = proc.info['memory_info'].rss
            print(f"VPCS Process: CPU: {cpu_usage}%, Memory: {memory_usage / 1024 / 1024}MB")
            if cpu_usage >= CPU_THRESHOLD or memory_usage >= MEMORY_THRESHOLD:
                print("\t\t\t\t\tAlert: High CPU or Memory usage detected!")
                
 
while True:
    check_vpcs_usage()
    time.sleep(5)   