import subprocess
import platform
import time

def get_cpu_usage():
    """
    Get CPU usage percentage using PowerShell command.
    """
    if platform.system() == "Windows":
        # Run PowerShell command to get CPU load percentage
        result = subprocess.run(["powershell", "-Command", "(Get-WmiObject Win32_Processor).LoadPercentage"], capture_output=True, text=True)
        output = result.stdout.strip()
        print("PowerShell Output:")
        print(output)  # Debug: print the raw output
        
        try:
            return float(output)  # Convert the output to a float
        except ValueError:
            print(f"Error converting '{output}' to float.")
            return 0.0

    else:
        raise NotImplementedError("Unsupported operating system")

def main():
    while True:
        cpu_usage = get_cpu_usage()

        print(f"CPU Usage: {cpu_usage}%")

if __name__ == "__main__":
    main()
