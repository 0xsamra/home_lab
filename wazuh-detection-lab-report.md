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
- **Tool:** Hydra 
- **Command:** for i in {1..10}; do ssh wronguser@IP; done
- **Wazuh Rule Triggered:** 5760
- **Alert Level:** 5
- **MITRE ATT&CK:** T1110 — Brute Force
---

<img width="947" height="407" alt="SSH project 1" src="https://github.com/user-attachments/assets/f35e8d25-f3a0-4563-851e-67b8cde8cb00" />

---

<img width="943" height="323" alt="SSH project2" src="https://github.com/user-attachments/assets/6ee24d02-e6ea-4d82-ae17-3f7dc8c3ccbd" />

---

<img width="674" height="404" alt="SSH project3" src="https://github.com/user-attachments/assets/5bd64d25-a6f1-47d1-9fbc-46b21ea7e8c1" />

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

---

<img width="1280" height="800" alt="FIM ubuntu alert" src="https://github.com/user-attachments/assets/af838054-cf28-4fd1-8a4b-b6ba9147f90c" />

---

<img width="947" height="409" alt="FIM wazuh" src="https://github.com/user-attachments/assets/90ce2744-1181-4fab-b2f5-70f5c2ca201e" />
---

## Custom Rules Written
- Rule 100001 — SSH authentication failures
- Rule 100002 — Sudo privilege escalation

## Key Findings
[what you learned from running these simulations]

## Conclusion
[what this lab demonstrates about your SOC skills]
