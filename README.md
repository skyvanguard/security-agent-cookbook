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

A hands-on collection of **recipes** for building AI agents that perform real cybersecurity tasks. Each recipe is a self-contained, working example you can run, modify, and learn from.

No theory walls. No toy examples. **Real agents, real tools, real security.**

---

## Recipes

### Beginner

| # | Recipe | What it does | Stack |
|---|--------|-------------|-------|
| 01 | [**Recon Agent**](recipes/01-recon-agent/) | Enumerates subdomains, detects technologies, scans ports, then uses an LLM to analyze the full attack surface and generate a professional recon report | Python, subfinder, httpx, nmap, OpenAI |
| 02 | [**CVE Lookup Agent**](recipes/02-cve-lookup/) | Natural language vulnerability research — ask "What critical CVEs affect Apache 2.4?" and get NVD data, EPSS exploit probability, and public exploit status in one answer | Python, NVD API, EPSS API, Claude tool_use |
| 03 | [**Phishing Analyzer**](recipes/03-phishing-analyzer/) | Multi-layer email analysis: header extraction, URL scanning via VirusTotal, SPF/DKIM/DMARC verification, and LLM-powered social engineering detection with confidence scoring | Python, VirusTotal API, CrewAI |
| 04 | [**Security News Digest**](recipes/04-security-news-digest/) | Daily automated briefing — aggregates RSS feeds from Bleeping Computer, The Hacker News, CISA advisories, categorizes threats, and delivers an executive summary to Slack or markdown | Python, RSS feeds, LangChain, Slack API |

### Intermediate

| # | Recipe | What it does | Stack |
|---|--------|-------------|-------|
| 05 | [**Nuclei AI Triager**](recipes/05-nuclei-triager/) | Ingests Nuclei scan JSON output, enriches findings with EPSS scores and CISA KEV data, then reasons about business context to rank vulnerabilities by real-world exploitability | Python, Nuclei, EPSS API, CISA KEV, LangGraph |
| 06 | [**Log Analysis RAG**](recipes/06-log-analysis-rag/) | SIEM copilot — indexes security logs in a vector DB, then answers natural language queries like "Show suspicious connections to non-standard ports in the last 24 hours" with correlation analysis | Python, ChromaDB, LangChain RAG, embeddings |
| 07 | [**IaC Security Scanner**](recipes/07-iac-scanner/) | Analyzes Terraform and Kubernetes manifests for misconfigurations using Checkov/Trivy, then an LLM explains the real risk of each finding and generates remediation PRs | Python, Checkov, Trivy, GitHub API, OpenAI Agents SDK |
| 08 | [**Threat Intel RAG (MITRE ATT&CK)**](recipes/08-threat-intel-rag/) | Indexes the full MITRE ATT&CK knowledge base into a vector store — answer questions like "What techniques does APT29 use for persistence?" and map IoCs to TTPs with detection suggestions | Python, MITRE ATT&CK STIX, ChromaDB, LangChain RAG |

### Advanced

| # | Recipe | What it does | Stack |
|---|--------|-------------|-------|
| 09 | [**Multi-Agent Pentest Pipeline**](recipes/09-pentest-pipeline/) | Orchestrates a team of specialized agents (recon, scanner, exploiter, reporter) that coordinate a full penetration test through shared memory and handoffs | Python, CrewAI/LangGraph, nmap, Nuclei, Docker, MCP |
| 10 | [**SOC Alert Triage Agent**](recipes/10-soc-triage/) | Autonomous Tier-1 SOC analyst — consumes SIEM alerts in real-time, investigates IoCs against threat intel feeds, classifies true/false positives, and escalates complex cases to humans | Python, LangGraph, Splunk/Elastic API, VirusTotal, Shodan |
| 11 | [**Malware Analysis Assistant**](recipes/11-malware-analysis/) | Full analysis pipeline: string extraction, YARA matching, static analysis via Ghidra MCP, sandbox detonation, VirusTotal lookup — produces a report with TTPs mapped to MITRE ATT&CK | Python, YARA, Ghidra MCP, VirusTotal API, Docker |
| 12 | [**CTF Auto-Solver**](recipes/12-ctf-solver/) | Autonomous CTF player for web, crypto, forensics, and reversing — plan-and-execute architecture that selects tools, iterates on failed attempts, and learns from each challenge | Python, LangGraph, pwntools, z3, CyberChef, Docker |

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/skyvanguard/security-agent-cookbook.git
cd security-agent-cookbook

# Install base dependencies
pip install -e .

# Configure your LLM provider
cp .env.example .env
# Edit .env with your API keys

# Run your first recipe
cd recipes/01-recon-agent
python agent.py --target example.com
```

---

## Supported LLM Providers

| Provider | Models | Local? |
|----------|--------|--------|
| OpenAI | GPT-4o, GPT-4o-mini | No |
| Anthropic | Claude Sonnet 4.5, Claude Haiku | No |
| DeepSeek | DeepSeek-Chat, DeepSeek-Coder | No |
| Ollama | Llama, Qwen, Mistral, any GGUF | Yes |
| Google | Gemini Pro, Gemini Flash | No |

## Frameworks Covered

| Framework | Used in Recipes |
|-----------|----------------|
| LangChain / LangGraph | #01, #04, #05, #06, #08, #09, #10, #12 |
| CrewAI | #03, #09 |
| OpenAI Agents SDK | #02, #07 |
| Claude tool_use | #02, #07, #11 |
| MCP Servers | #09, #11 |
| RAG (ChromaDB) | #06, #08 |

---

## Project Structure

```
security-agent-cookbook/
├── recipes/
│   ├── 01-recon-agent/
│   │   ├── agent.py            # Main agent code
│   │   ├── README.md           # Recipe docs + example output
│   │   └── requirements.txt    # Recipe-specific deps
│   ├── 02-cve-lookup/
│   └── .../
├── shared/
│   ├── llm.py                  # LLM provider abstraction
│   ├── tools.py                # Common security tools wrapper
│   └── report.py               # Report generation utilities
├── .env.example
├── pyproject.toml
└── README.md
```

---

## Philosophy

1. **Each recipe works standalone** — no monolithic framework to learn
2. **Real tools, not mocks** — agents interact with actual security tools
3. **Provider agnostic** — swap LLMs with a single env variable
4. **Educational first** — code is commented and explained
5. **Responsible by default** — built-in scope checking and authorization reminders

---

## Contributing

We welcome new recipes! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Disclaimer

All recipes are for **authorized security testing and educational purposes only**. Always obtain proper authorization before testing systems you do not own.

---

<p align="center">
  <i>Built by <a href="https://github.com/skyvanguard">@skyvanguard</a></i><br>
  <sub>Cybersecurity & AI Researcher | TryHackMe Top 1% Global</sub>
</p>
