# IP Reputation Checker

Python CLI tool that checks an IP against AbuseIPDB and VirusTotal and prints a combined report.

## Setup
    python3 -m venv venv && source venv/bin/activate
    pip install -r requirements.txt
    export ABUSEIPDB_KEY="your_key"
    export VT_KEY="your_key"

## Usage
    python3 ip-checker.py 8.8.8.8

## Features
- Input validation, request timeouts, error handling
- API keys read from environment variables (never hardcoded)
