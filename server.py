from flask import Flask, request, jsonify
from tabulate import tabulate
import pyautogui as pag

app = Flask(__name__)

cpu_threshold = 10

memory_threshold = 50

@app.route('/', methods=['GET'])
def hello():
    return "Hello, Flask server is running!"
@app.route('/usage', methods=['POST'])
def update_usage():
    data = request.get_json()

    hostname = data.get('hostname')
    ip_address = data.get('ip_address')
    cpu_usage = data.get('cpu_usage')
    memory_usage = data.get('memory_usage')
    top_cpu_processes = data.get('top_cpu_processes')
    top_memory_processes = data.get('top_memory_processes')

    print(f"Data received from Host: {hostname} (IP: {ip_address})")
    print(f"Current CPU Usage: {cpu_usage}%")
    print(f"Current Memory Usage: {memory_usage}%")

    top_cpu_process_name = top_cpu_processes[0]['name'] if top_cpu_processes else None
    top_memory_process_name = top_memory_processes[0]['name'] if top_memory_processes else None

    if top_cpu_processes:
        print("\nTop Processes by CPU Usage:")
        print(tabulate([[proc['name'], proc['cpu_percent']] for proc in top_cpu_processes],
                       headers=['Process Name', 'CPU Usage (%)'],
                       tablefmt='grid')) 

    if top_memory_processes:
        print("\nTop Processes by Memory Usage:")
        print(tabulate([[proc['name'], proc['memory_percent']] for proc in top_memory_processes],
                       headers=['Process Name', 'Memory Usage (%)'],
                       tablefmt='grid'))

    print(f"Top CPU Process: {top_cpu_process_name}")
    print(f"Top Memory Process: {top_memory_process_name}")

    if cpu_usage >= cpu_threshold:
        print(f"Alert: CPU usage is {cpu_usage}%")
        pag.alert(text=f"KILL {top_cpu_process_name} PROCESS TO RUN SMOOTHLY".upper(), title="ALERT CPU USAGE".upper())

    if memory_usage >= memory_threshold:
        print(f"Alert: Memory usage is {memory_usage}%")
        pag.alert(text=f"KILL {top_memory_process_name} PROCESS TO RUN SMOOTHLY".upper(), title="ALERT MEMORY USAGE".upper())

    return jsonify({
        'status': 'success',
        'top_cpu_process': top_cpu_process_name,
        'top_memory_process': top_memory_process_name
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True)
