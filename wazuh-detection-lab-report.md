# Wazuh Detection Lab — Full Report
**Date:** September 2026
**Analyst:** Samra Sharafat Ali (0xsamra)

## Objective
Build and operate a home SIEM lab using Wazuh to
detect real attack patterns and develop SOC analyst
skills in alert triage and incident documentation.

## Environment Setup
| Component | Details |
|---|---|
| SIEM Platform | Wazuh 4.7.5 |
| Server OS | Ubuntu 26.04.1 LTS |
| Server IP | 192.168.56.102 |
| Agent | Kali Linux (kali-agent) |
| Host Machine | HP EliteBook 16GB RAM |

## Attacks Simulated & Detected

### 1. SSH Brute Force
- **Tool:** Hydra / manual SSH attempts
- **Command:** for i in {1..10}; do ssh wronguser@IP; done
- **Wazuh Rule Triggered:** [rule ID you saw]
- **Alert Level:** [level you saw]
- **MITRE ATT&CK:** T1110 — Brute Force

### 2. Port Scanning
- **Tool:** Nmap
- **Command:** nmap -sS 192.168.56.102
- **Wazuh Rule Triggered:** [rule ID]
- **Alert Level:** [level]
- **MITRE ATT&CK:** T1595 — Active Scanning

### 3. File Integrity Violation
- **File Modified:** /etc/passwd
- **Detection Method:** Wazuh Integrity Monitoring
- **Alert Level:** Critical
- **MITRE ATT&CK:** T1136 — Create Account

## Custom Rules Written
- Rule 100001 — SSH authentication failures
- Rule 100002 — Sudo privilege escalation

## Key Findings
[what you learned from running these simulations]

## Conclusion
[what this lab demonstrates about your SOC skills]
