# Security Agent Cookbook

```
 _____ _____ _____ _____ _____ _____ _____ _____
|   __|   __|     |  |  | __  |     |_   _|  |  |
|__   |   __|   --|  |  |    -|-   -| | | |_   _|
|_____|_____|_____|_____|__|__|_____| |_|   |_|

          AGENT COOKBOOK
```

<div align="center">

**Practical recipes for building cybersecurity AI agents with LLMs**

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

---

## What is this?

A hands-on collection of **recipes** for building AI agents that perform real cybersecurity tasks. Each recipe is a self-contained, working example that you can run, modify, and learn from.

No theory walls. No toy examples. **Real agents, real tools, real security.**

---

## Recipes

### Beginner

| # | Recipe | What it does | Tools |
|---|--------|-------------|-------|
| 01 | [Recon Agent](recipes/01-recon-agent/) | Enumerates subdomains, detects technologies, and identifies open ports for a target domain | Python, httpx, subfinder |
| 02 | [CVE Analyzer](recipes/02-cve-analyzer/) | Takes a CVE ID, fetches details from NVD, and explains the vulnerability with remediation steps | Python, NVD API |
| 03 | [Header Inspector](recipes/03-header-inspector/) | Analyzes HTTP security headers and scores a website's security posture | Python, requests |
| 04 | [Log Anomaly Detector](recipes/04-log-anomaly-detector/) | Monitors log files and uses an LLM to identify suspicious patterns and potential intrusions | Python, watchdog |

### Intermediate

| # | Recipe | What it does | Tools |
|---|--------|-------------|-------|
| 05 | [Nuclei AI Triager](recipes/05-nuclei-ai-triager/) | Runs Nuclei scans, then uses an LLM to prioritize findings by real-world exploitability | Python, Nuclei |
| 06 | [OSINT Profiler](recipes/06-osint-profiler/) | Gathers public information about a target (emails, subdomains, social media) and builds an intelligence report | Python, theHarvester, Sherlock |
| 07 | [Malware Analyzer](recipes/07-malware-analyzer/) | Static analysis of suspicious files — extracts strings, checks hashes against VirusTotal, explains behavior | Python, YARA, VirusTotal API |
| 08 | [Security RAG Assistant](recipes/08-security-rag/) | A RAG-powered assistant that answers questions from your own security documentation, playbooks, and policies | Python, ChromaDB, LangChain |

### Advanced

| # | Recipe | What it does | Tools |
|---|--------|-------------|-------|
| 09 | [Bug Bounty Recon Pipeline](recipes/09-bb-recon-pipeline/) | Full automated recon: subdomain enum → alive check → port scan → tech detect → vuln scan → AI-prioritized report | Python, subfinder, httpx, Nuclei |
| 10 | [Multi-Agent Pentest Team](recipes/10-multi-agent-pentest/) | Swarm of specialized agents (recon, scanner, exploit, reporter) that coordinate a penetration test | Python, OpenAI Agents SDK |
| 11 | [Network Traffic Analyzer](recipes/11-traffic-analyzer/) | Captures and analyzes network traffic with AI to detect anomalies, C2 beacons, and data exfiltration | Python, Scapy, pyshark |
| 12 | [Incident Response Orchestrator](recipes/12-ir-orchestrator/) | Automated incident response: triages alerts, gathers evidence, contains threats, generates timeline report | Python, Wazuh API |

---

## Quick Start

### Prerequisites

```bash
# Python 3.10+
python --version

# Install base dependencies
pip install security-agent-cookbook

# Or clone and install
git clone https://github.com/skyvanguard/security-agent-cookbook.git
cd security-agent-cookbook
pip install -e .
```

### Configure your LLM

```bash
# Create .env with your preferred provider
cp .env.example .env

# Supports: OpenAI, Anthropic, DeepSeek, Ollama (local)
```

### Run your first recipe

```bash
# Run the Recon Agent
cd recipes/01-recon-agent
python agent.py --target example.com
```

---

## Project Structure

```
security-agent-cookbook/
├── recipes/
│   ├── 01-recon-agent/
│   │   ├── agent.py          # Main agent code
│   │   ├── README.md          # Recipe documentation
│   │   ├── requirements.txt   # Recipe-specific deps
│   │   └── example_output/    # Sample output
│   ├── 02-cve-analyzer/
│   │   └── ...
│   └── .../
├── shared/
│   ├── llm.py                 # LLM provider abstraction
│   ├── tools.py               # Common security tools wrapper
│   └── report.py              # Report generation utilities
├── .env.example
├── pyproject.toml
└── README.md
```

---

## Supported LLM Providers

| Provider | Models | Local? |
|----------|--------|--------|
| OpenAI | GPT-4o, GPT-4o-mini | No |
| Anthropic | Claude Sonnet, Claude Haiku | No |
| DeepSeek | DeepSeek-Chat, DeepSeek-Coder | No |
| Ollama | Llama, Qwen, Mistral, any GGUF | Yes |
| Google | Gemini Pro, Gemini Flash | No |

---

## Philosophy

1. **Each recipe works standalone** — no monolithic framework to learn
2. **Real tools, not mocks** — agents interact with actual security tools
3. **Provider agnostic** — swap LLMs with a single env variable
4. **Educational first** — code is commented and explained
5. **Responsible by default** — built-in scope checking and authorization

---

## Contributing

We welcome new recipes! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Recipe Template

Every recipe should include:
- `agent.py` — The main agent implementation
- `README.md` — What it does, how to run it, example output
- `requirements.txt` — Recipe-specific dependencies
- `example_output/` — Sample output so users know what to expect

---

## Disclaimer

All recipes are designed for **authorized security testing and educational purposes only**. Always obtain proper authorization before testing systems you do not own. The authors are not responsible for misuse.

---

<p align="center">
  <i>Built by <a href="https://github.com/skyvanguard">@skyvanguard</a></i><br>
  <sub>Cybersecurity & AI Researcher | TryHackMe Top 1% Global</sub>
</p>
