"""
Recipe 01: Recon Agent
Enumerates subdomains, detects technologies, and identifies open ports.

Usage:
    python agent.py --target example.com
"""

import argparse
import json
import subprocess
import sys
import os
from pathlib import Path

try:
    from openai import OpenAI
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent.parent / ".env")
except ImportError:
    print("Install deps: pip install openai python-dotenv")
    sys.exit(1)


def run_command(cmd: list[str], timeout: int = 60) -> str:
    """Run a shell command and return output."""
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return result.stdout or result.stderr
    except FileNotFoundError:
        return f"Tool not found: {cmd[0]}. Install it first."
    except subprocess.TimeoutExpired:
        return f"Command timed out after {timeout}s"


def enumerate_subdomains(target: str) -> list[str]:
    """Find subdomains using subfinder or fallback to DNS."""
    output = run_command(["subfinder", "-d", target, "-silent"])
    if "not found" in output.lower():
        output = run_command(["nslookup", target])
    return [line.strip() for line in output.splitlines() if line.strip()]


def check_ports(target: str, ports: str = "80,443,8080,8443,22,21,3306") -> str:
    """Scan common ports using nmap."""
    output = run_command(["nmap", "-Pn", "-p", ports, "--open", target], timeout=120)
    if "not found" in output.lower():
        return f"nmap not installed. Target: {target}, Ports to check: {ports}"
    return output


def detect_technologies(target: str) -> str:
    """Detect web technologies using httpx or curl."""
    output = run_command([
        "httpx", "-u", f"https://{target}",
        "-title", "-tech-detect", "-status-code", "-silent"
    ])
    if "not found" in output.lower():
        output = run_command(["curl", "-sI", f"https://{target}"])
    return output


def analyze_with_llm(target: str, subdomains: list[str], ports: str, tech: str) -> str:
    """Use LLM to analyze recon results and provide insights."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    subs_text = "\n".join(subdomains[:20]) if subdomains else "None found"

    prompt = f"""You are a cybersecurity reconnaissance analyst. Analyze these results for {target}:

## Subdomains Found ({len(subdomains)})
{subs_text}

## Port Scan Results
{ports}

## Technology Detection
{tech}

Provide:
1. Summary of findings
2. Potential attack surface
3. Recommended next steps for authorized testing
4. Risk assessment (Low/Medium/High/Critical)

Format as a professional recon report in markdown."""

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL", "gpt-4o"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content


def main():
    parser = argparse.ArgumentParser(description="AI-powered Recon Agent")
    parser.add_argument("--target", required=True, help="Target domain to scan")
    parser.add_argument("--output", default="recon_report.md", help="Output file")
    args = parser.parse_args()

    target = args.target
    print(f"[*] Starting recon on: {target}")
    print(f"[!] Ensure you have authorization to scan this target\n")

    print("[1/3] Enumerating subdomains...")
    subdomains = enumerate_subdomains(target)
    print(f"      Found {len(subdomains)} subdomains")

    print("[2/3] Scanning ports...")
    ports = check_ports(target)

    print("[3/3] Detecting technologies...")
    tech = detect_technologies(target)

    print("[*] Analyzing results with AI...")
    report = analyze_with_llm(target, subdomains, ports, tech)

    Path(args.output).write_text(f"# Recon Report: {target}\n\n{report}", encoding="utf-8")
    print(f"\n[+] Report saved to: {args.output}")
    print(report)


if __name__ == "__main__":
    main()
