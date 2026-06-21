# Cybersecurity Fundamentals

A collection of beginner-friendly Python cybersecurity scripts built using Python's standard library.

## Repository Structure

```text
cybersecurity-fundamentals/
│
├── README.md
├── port_scanner.py
├── password_hasher.py
└── file_hash_checker.py
```

## Requirements

* Python 3.x
* No external libraries required

Verify your Python installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

## 1. Port Scanner (`port_scanner.py`)

### Description

A basic TCP port scanner that uses Python's built-in `socket` library to check whether common ports on a target host are open.

### Features

* Scans common ports such as:

  * 21 (FTP)
  * 22 (SSH)
  * 23 (Telnet)
  * 25 (SMTP)
  * 53 (DNS)
  * 80 (HTTP)
  * 110 (POP3)
  * 443 (HTTPS)
* Uses TCP connection attempts to determine port status.
* No third-party packages required.

### Run the Script

```bash
python port_scanner.py
```

or

```bash
python3 port_scanner.py
```

### Example

```text
Enter target IP or hostname: scanme.nmap.org
Scanning scanme.nmap.org...
Port 22 is OPEN
Port 80 is OPEN
```

---

## 2. Password Hasher (`password_hasher.py`)

### Description

A simple utility that converts a user-provided password into a SHA-256 hash using Python's built-in `hashlib` module.

### Features

* Uses SHA-256 hashing.
* Demonstrates secure password hashing concepts.
* Useful for learning how passwords are stored and verified.

### Run the Script

```bash
python password_hasher.py
```

or

```bash
python3 password_hasher.py
```

### Example

```text
Enter password: MyPassword123

SHA-256 Hash:
a7c4f2d6...
```

---

## 3. File Hash Checker (`file_hash_checker.py`)

### Description

Calculates the SHA-256 hash of a file and displays the result. This can be used to verify file integrity and detect file modifications.

### Features

* Reads files in chunks for efficiency.
* Generates SHA-256 hashes.
* Handles missing files gracefully.

### Run the Script

```bash
python file_hash_checker.py
```

or

```bash
python3 file_hash_checker.py
```

### Example

```text
Enter file path: sample.txt

SHA-256:
8a7d2e6f...
```

---

## Educational Purpose

These scripts are designed to demonstrate foundational cybersecurity concepts:

* Network reconnaissance through port scanning
* Cryptographic hashing using SHA-256
* File integrity verification

## Disclaimer

These scripts are provided for educational and authorized testing purposes only. Do not use them against systems or networks without explicit permission.
