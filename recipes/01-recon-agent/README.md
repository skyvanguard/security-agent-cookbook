# Recipe 01: Recon Agent

An AI-powered reconnaissance agent that automates the initial phases of security assessment.

## What it does

1. **Subdomain Enumeration** - Discovers subdomains using subfinder
2. **Port Scanning** - Identifies open ports using nmap
3. **Technology Detection** - Detects web technologies using httpx
4. **AI Analysis** - Uses an LLM to analyze findings and generate a professional report

## Prerequisites

```bash
pip install openai python-dotenv

# Security tools (optional but recommended)
# subfinder: https://github.com/projectdiscovery/subfinder
# nmap: https://nmap.org/download
# httpx: https://github.com/projectdiscovery/httpx
```

## Usage

```bash
python agent.py --target example.com
python agent.py --target example.com --output my_report.md
```

## How it works

```
Target Domain
    |
    v
[1] Subdomain Enumeration (subfinder)
    |
    v
[2] Port Scanning (nmap)
    |
    v
[3] Technology Detection (httpx)
    |
    v
[AI] LLM Analysis & Report Generation
    |
    v
Markdown Report
```

## Authorization

Always ensure you have explicit authorization before scanning any target.
