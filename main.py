import ipaddress
from collections import defaultdict

# File paths
input_file_path = "files/input.txt"
output_file_path = "files/output.txt"

# Function to calculate subnet
def get_subnet(ip, prefix):
    ip_obj = ipaddress.ip_address(ip)
    if isinstance(ip_obj, ipaddress.IPv4Address):
        subnet = ipaddress.ip_network(f"{ip}/{prefix}", strict=False)
    elif isinstance(ip_obj, ipaddress.IPv6Address):
        subnet = ipaddress.ip_network(f"{ip}/{prefix}", strict=False)
    else:
        raise ValueError(f"Unknown IP type: {ip}")
    return str(subnet)

# Read and group IPs by subnet
subnet_counts = defaultdict(int)

with open(input_file_path, "r") as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) != 2:
            continue
        
        count, ip = parts
        try:
            count = int(count)
            subnet = get_subnet(ip, 24 if ":" not in ip else 64)
            subnet_counts[subnet] += count
        except ValueError as e:
            print(f"Skipping line due to error: {line.strip()} ({e})")

with open(output_file_path, "w") as file:
    for subnet, total_count in sorted(subnet_counts.items()):
        file.write(f"{total_count} {subnet}\n")

print(f"Grouped data saved to {output_file_path}.")
