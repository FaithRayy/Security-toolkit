# Security-toolkit
A small collection of Security-orientated Python scripts.

- password_auditor.py: Run and input a potential password, and receive tips to improve its complexity if needed.
  - Uses the rockyou.txt wordlist for an additional check (rockyou.txt not included in repo. The file will need to be acquired separately).
  - Also securely uses the "Have I Been Pwned" API to search for whether the potential password has been found in a breach.
  - *Password tips based on the standards published by Virginia Polytechnic Institute and State University*
