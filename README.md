
# IP Address Subnet Grouper

This script reads a list of IP addresses with associated counts, groups them by subnet, and writes the aggregated results to an output file.

## Features

- Supports both IPv4 and IPv6 addresses.
- Groups IPs by `/24` prefix for IPv4 and `/64` prefix for IPv6.
- Handles errors in input gracefully by skipping invalid lines.

![Screenshot 2025-01-08 131157](https://github.com/user-attachments/assets/739a6db2-0dbb-4e2c-9247-d419d1b1ecaa)

## Requirements

- Python 3.x
- `ipaddress` module (comes pre-installed with Python 3.x)

## Input File Format

The input file should be a plain text file where each line contains:
1. A count (integer)
2. An IP address (IPv4 or IPv6)

Example:
```
10 192.168.1.1
5 192.168.1.2
8 fe80::1
```

## Output File Format

The output file will list:
1. The aggregated count
2. The corresponding subnet

Example:
```
15 192.168.1.0/24
8 fe80::/64
```

## Usage

1. Place your input file in the `files/` directory and name it `input.txt`.
2. Run the script:
   ```bash
   python script.py
   ```
3. The output will be saved in the `files/` directory as `output.txt`.

## File Paths

- Input file: `files/input.txt`
- Output file: `files/output.txt`

## How It Works

1. Reads the input file line by line.
2. Parses the count and IP address.
3. Determines the subnet for each IP:
   - `/24` for IPv4
   - `/64` for IPv6
4. Aggregates the counts by subnet.
5. Writes the results to the output file.

## License

This project is open-source and available under the MIT License.

## Acknowledgments

Special thanks to Python's built-in `ipaddress` module for simplifying IP address handling.
