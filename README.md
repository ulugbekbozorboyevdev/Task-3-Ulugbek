# Phishing Triage Toolkit

A beginner-friendly Python project designed to identify potential phishing messages by analyzing suspicious keywords and URLs.

## Project Overview

Phishing is a type of cyberattack in which attackers use deceptive messages to trick people into revealing sensitive information or visiting unsafe websites.

This project demonstrates basic phishing awareness and message analysis using Python.

## Features

- **Keyword Detection:** Identifies suspicious words and phrases commonly associated with phishing.
- **URL Extraction:** Extracts HTTP and HTTPS links from messages.
- **HTTP Detection:** Warns when a URL uses an insecure HTTP connection.
- **IP Address Detection:** Identifies URLs that use IP addresses instead of domain names.
- **URL Shortener Detection:** Recognizes common URL-shortening services.
- **Risk Classification:** Assigns a basic risk level based on the number of detected suspicious keywords.

## Project Structure

```text
phishing-triage-toolkit/
│
├── main.py
├── detector.py
├── checklist.md
├── README.md
│
└── examples/
    ├── phishing_emails.txt
    └── legitimate_emails.txt
```

## Technologies Used

- Python
- Regular Expressions (`re`)
- URL Parsing (`urllib.parse`)
- IP Address Validation (`ipaddress`)

All libraries used by the current analyzer are included in Python's standard library.

## How to Run

1. Make sure Python is installed.
2. Clone or download this repository.
3. Open the project folder in your terminal.
4. Run the program:

```bash
python main.py
```

5. Enter a message when prompted.
6. Review the analysis results.

## Example

**Input:**

```text
URGENT! Your account suspended.
Verify your account immediately:
http://example.com/login
```

**Possible output:**

```text
Warning: URL uses insecure HTTP

This message may be a phishing attempt.

Detected keywords:
urgent, account suspended, verify your account

Risk level: Medium
```

## Important Limitations

This tool uses basic keyword matching and URL characteristics to identify potential warning signs.

- A suspicious keyword does not necessarily mean a message is malicious.
- HTTPS does not guarantee that a website is trustworthy.
- URL shorteners are not automatically malicious.
- The tool does not verify website reputation or determine whether a URL is actually malicious.
- The risk level is a simple educational score, not a verified phishing probability.

Always verify suspicious messages through official communication channels.

## Learning Objectives

- Understand common phishing techniques.
- Practice Python string handling and regular expressions.
- Learn basic URL analysis.
- Develop cybersecurity awareness and analytical thinking.

## Project Type

Educational cybersecurity project — Phishing Awareness Analysis.
