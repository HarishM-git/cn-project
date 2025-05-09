import requests
import socket
import time
import psutil

def get_system_usage():
    """
    Get the total CPU and memory usage of the system, and the top 5 processes by CPU and memory usage.
    """
    top_cpu_processes = []
    total_cpu_from_processes = 0.0

    for proc in psutil.process_iter(['name', 'cpu_percent']):
        try:
            proc_cpu_percent = proc.cpu_percent(interval=0.1) 
            if proc_cpu_percent > 0 and proc.info['name'].lower() not in ['system idle process', 'idle', 'system']:
                top_cpu_processes.append({
                    'name': proc.info['name'],
                    'cpu_percent': round(proc_cpu_percent, 2)
                })
                total_cpu_from_processes += proc_cpu_percent
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):

            continue
        

    top_cpu_processes = sorted(top_cpu_processes, key=lambda x: x['cpu_percent'], reverse=True)[:5]

    total_cpu_percentage = min(total_cpu_from_processes, 100.0)  
    
    memory_usage = psutil.virtual_memory().percent


    top_memory_processes = []
    
    for proc in psutil.process_iter(['name', 'memory_percent']):
        try:
            
            proc_memory_percent = proc.info['memory_percent']
            top_memory_processes.append({
                'name': proc.info['name'],
                'memory_percent': proc_memory_percent
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue

        top_memory_processes = sorted(top_memory_processes, key=lambda x: x['memory_percent'], reverse=True)[:5]

    return round(total_cpu_percentage, 3), memory_usage, top_cpu_processes, top_memory_processes

def send_usage_data(cpu_usage, memory_usage, top_cpu_processes, top_memory_processes):
    """
    Send the system usage data to a specified server endpoint.
    """
    url = 'http://127.0.0.1:5500/usage'
    
    hostname = socket.gethostname() 
    ip_address = socket.gethostbyname(hostname) 
    
    data = {     
        'hostname': hostname,
        'ip_address': ip_address,
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage,
        'top_cpu_processes': top_cpu_processes,
        'top_memory_processes': top_memory_processes
    }
    
    print('Data:', data)

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        
        print('Data sent successfully:', response)
    except requests.RequestException as e:
        print(f"Failed to send data: {e}")

def main():
    while True:
        print('Working...')
        cpu_usage, memory_usage, top_cpu_processes, top_memory_processes = get_system_usage()
        send_usage_data(cpu_usage, memory_usage, top_cpu_processes, top_memory_processes)
        time.sleep(20)  

if __name__ == "__main__":
    main()
 