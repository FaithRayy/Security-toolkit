# Security-toolkit
A small collection of Security-orientated Python scripts.

- password_auditor.py: Run and input a potential password, and receive tips to improve its complexity if needed.
  - Uses the rockyou.txt wordlist for an additional check (rockyou.txt not included in repo. The file will need to be acquired separately).
  - Also securely uses the "Have I Been Pwned" API to search for whether the potential password has been found in a breach.
  - *Password tips based on the standards published by Virginia Polytechnic Institute and State University*
  - Run: ``python password_auditor.py``

- port_scanner.py: Given a range of two numbers, this Python program will scan and return all open ports within that range.
  - Run: ``python port_scanner.py <from_port_number> <to_port_number>``

- file_integrity_check.py: Given a text file, this program will calculate a SHA-256 hash for the file, and when the program is run again, it will compare the given text file with the hash and alert if a change to the file has been made.
  - Run: ``python file_integrity_check/py <file_name.txt>``

- systemAndGeo.py: Run and receive the system OS, IP address, MAC address, and ISP, along with the associated city, state, country, and timezone.
  - Uses API from "ipify.org" and "IP-API.com" to receive the public IP address and geolocation, respectively.
  - Run: ``python systemAndGeo.py``

- auth_logs_mac.py: Mac-specific program that exports an Excel sheet of authentication logs from the past given hours.
  - Run: ``auth_logs_mac.py <number of hours>h``
