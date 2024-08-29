import csv
import subprocess

def ping_ip(ip_address):
    command = ['ping', '-c', '1', ip_address]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.returncode == 0

def process_ips(input_file, output_file):
    successful_pings = []
    unsuccessful_pings = []

    with open(input_file, 'r') as file:
        ips = file.readlines()
        
    for ip in ips:
        ip = ip.strip()
        if not ip:
            continue
        if ping_ip(ip):
            successful_pings.append(ip)
        else:
            unsuccessful_pings.append(ip)
    
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Successful Pings'])
        writer.writerows([[ip] for ip in successful_pings])
        writer.writerow([])
        writer.writerow(['Unsuccessful Pings'])
        writer.writerows([[ip] for ip in unsuccessful_pings])

# Usage
input_file = 'ips.txt'  # Replace with your input file path
output_file = 'ping_results.csv'  # Replace with your output file path

process_ips(input_file, output_file)
print("Ping results generated successfully!")
