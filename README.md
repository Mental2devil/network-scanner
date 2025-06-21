Network Vulnerability Scanner
A Python-based network scanning tool that automates the identification of open ports, running services, and potential vulnerabilities using Nmap. Designed for ethical hacking and cybersecurity analysis, this project demonstrates skills in network security, Python programming, and data processing.
Features

Port Scanning: Scans specified port ranges (e.g., 1-1000) using Nmap’s TCP SYN scan (-sS) for efficient detection of open ports.
Service Detection: Identifies services (e.g., HTTP, SSH) and their versions on open ports using Nmap’s service detection (-sV).
Vulnerability Checks: Flags potential vulnerabilities by identifying insecure services (e.g., FTP, Telnet) and simulating CVE-based checks (e.g., CVE-2021-41773 for Apache).
Result Export: Saves scan results to both text (scan_results.txt) and CSV (scan_results.csv) files for analysis.
Input Validation: Validates user-provided port ranges and handles invalid inputs gracefully.
Error Handling: Robust error management for hostname resolution, scan failures, and network issues.

Prerequisites

Python 3.6+
Nmap (command-line tool)
Python libraries: python-nmap

Installation

Install Nmap:

On Ubuntu/Debian:sudo apt-get update
sudo apt-get install nmap


On macOS (with Homebrew):brew install nmap


On Windows, download and install from Nmap’s official site.


Install Python dependencies:
pip install python-nmap


Clone the repository:
git clone https://github.com/your-username/network-vulnerability-scanner.git
cd network-vulnerability-scanner



Usage

Run the script:python network_scanner.py


Follow the prompts:
Enter a target hostname or IP (e.g., scanme.nmap.org for testing).
Enter a port range (e.g., 1-100) or a single port (e.g., 80). Press Enter for default (1-1000).


View results:
Console output displays open ports, services, versions, and potential vulnerabilities.
Results are saved to scan_results.txt and scan_results.csv in the project directory.



Example
$ python network_scanner.py
Enter target hostname or IP (e.g., scanme.nmap.org): scanme.nmap.org
Enter port range (e.g., 1-1000) or press Enter for default (1-1000): 1-100

Resolved scanme.nmap.org to IP: 45.33.32.156
Starting scan on 45.33.32.156 at 2025-06-21 08:56:00

Host: 45.33.32.156 (scanme.nmap.org)
State: up

Protocol: tcp
Port: 22    State: open    Service: ssh    Version: OpenSSH 6.6.1p1
Port: 80    State: open    Service: http   Version: Apache httpd 2.4.7
⚠️ Possible CVE-2021-41773 (Apache < 2.4.51) on port 80

Scan Summary for 45.33.32.156:
Open Ports Found: 2
Ports: [22, 80]
Scan completed at 2025-06-21 08:56:05
Results saved to 'scan_results.csv'
Results saved to 'scan_results.txt'

Running in Google Colab

Open a new notebook in Google Colab.
Copy and paste the network_scanner.py code into a code cell.
Run the cell to install dependencies and execute the scan.
Download scan_results.txt and scan_results.csv from Colab’s file system (left sidebar).

Note: Colab’s cloud environment may have network restrictions. For best results, run locally or use a test target like scanme.nmap.org.
Files

network_scanner.py: Main script for scanning and processing results.
scan_results.txt: Text file containing scan summary and Nmap command details.
scan_results.csv: CSV file with detailed port information (Host, Port, State, Service, Version).

Ethical and Legal Considerations

Authorized Use Only: Scanning networks without explicit permission is illegal and unethical. Use this tool only on systems you own or have written consent to scan (e.g., scanme.nmap.org).
Testing: Use scanme.nmap.org, a public test target provided by Nmap, or set up a local VM (e.g., Metasploitable) for safe experimentation.
Compliance: Adhere to local laws and regulations, such as the Computer Fraud and Abuse Act (CFAA) in the US.

Future Enhancements

Integrate a real CVE database (e.g., via cve-search or an API) for accurate vulnerability checks.
Add a simple GUI using Tkinter or a web interface with Flask.
Support for advanced Nmap scans (e.g., OS detection, script scanning).

Contributing
Contributions are welcome! Please:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m "Add feature").
Push to the branch (git push origin feature-branch).
Open a pull request.



Built with Nmap and python-nmap.
Inspired by cybersecurity practices for ethical hacking and network auditing.


