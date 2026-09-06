# Security-toolkit
A small collection of Security-orientated Python scripts.

- password_auditor.py: Run and input a potential password, and receive tips to improve its complexity if needed.
  - Uses the rockyou.txt wordlist for an additional check (rockyou.txt not included in repo. The file will need to be acquired separately).
  - Also securely uses the "Have I Been Pwned" API to search for whether the potential password has been found in a breach.
  - *Password tips based on the standards published by Virginia Polytechnic Institute and State University*
  - Run: ``python password_auditor.py``

- port_scanner.py: Given a range of two numbers, this Python program will scan and return all open ports within that range.
  - Run: ``python port_scanner.py <from_port_number> <to_port_number>``
  - Example: ``python port_scanner.py 40 700``

- file_integrity_check.py: Given a text file, this program will calculate a SHA-256 hash for the file, and when the program is run again, it will compare the given text file with the hash and alert if a change to the file has been made.
  - Run: ``python file_integrity_check.py <file_name.txt>``
  - Example: ``python file_integrity_check.py file.txt``

- systemAndGeo.py: Run and output the system OS, IP address, MAC address, and ISP, along with the associated city, state, country, and timezone.
  - Uses API from "ipify.org" and "IP-API.com" to receive the public IP address and geolocation, respectively.
  - Note: The information provided is not transferred in any way outside of the program/localhost. Any selling, trading, or otherwise transfer of such information is outside the scope of this script's purpose.
  - Run: ``python systemAndGeo.py``

- auth_logs_mac.py: macOS-specific program that exports an Excel sheet of authentication logs from the past given hours.
  - The output Excel sheet contains all cases of authentication logs, including authentication required to download/delete certain files and applications, and failed/successful logins, with a count of how many attempts it took.
  - Run: ``python3 auth_logs_mac.py <number of hours>h``
  - Example: ``python3 auth_logs_mac.py 5h``

- log_analyzer(windows)v1.py: Windows-Specific program that exports a CSV file of authentication logs based on a given requested number of logs, amount of hours passed, or a timeframe.
  - The output begins as an Out-GridView. Then the user can select all or select individually which logs they would like exported to the CSV file. Then select "OK".
  - Uses the Get-EventLog PowerShell tool (legacy tool), and is not available in PowerShell 6, 7+. Only works for PowerShell 5.1 and older
  - Run and return the last <number> logs (3 digits max): ``python <number of hours>``
  - Example: ``python 5``
  - Run and return logs based on the last <number> hours (3 digits max): ``python <number of hours>h``
  - Example: ``python 5h``
  - Run and return logs based on a timeframe: ``python <M/DD/YYYY>-<M/DD/YYYY>``
  - Example: ``python 8/29/2026-9/3/2026``
