My Cybersecurity Home Lab — 0xsamra 


About Me

 Aspiring SOC Analyst | BSIT Cybersecurity student | 0xsamra 

Lab Environment 

 Host OS: Windows
 Virtualization: VirtualBox
 VMs: Kali Linux, Parrot OS, Metasploitable2, Ubuntu Server (Wazuh) 

Tools I've Worked With

 Wazuh (SIEM)
 Wireshark (Network Analysis) 
 Nmap (Network Scanning) 
 Metasploit (Exploitation) 
 Burp Suite (Web Security) 

Practical Exercises Completed

TryHackMe SOC Fundamentals 
TryHackMe Defensive Security Intro 
TryHackMe Junior Security Analyst Intro 
Linux log analysis (auth.log, journalctl) 
Windows Event Viewer investigation 
SQL Injection, XSS testing on DVWA/Juice Shop
Wireshark traffic capture and protocol filtering (HTTP, DNS, TCP) 
Network protocol analysis (HTTP, HTTPS, SSH, RDP, DNS, FTP, SMB, SMTP) 
TryHackMe SOC Level 1 Path — Room 2 completed 
 
 Investigation Log 

 Ticket #001
 Date: June 30, 2026
 Analyst: Samra (0xsamra)
 Severity: Critical
Summary:
A critical alert was triggered for IP 221.181.185.159, identified as a China-based address with prior involvement in 4 documented cyberattacks. The IP attempted unauthorized SSH login access.
Evidence:
SIEM logs flagged the source IP under Critical severity, showing repeated SSH login attempts consistent with known malicious activity associated with this IP.
Action Taken:
The IP was investigated using IP Hunter, confirming its malicious history. The alert was escalated to Will Griffin (Senior Security Analyst) for review. The IP was subsequently blocked on the firewall, with a comment added documenting the action and justification.
Status: Closed — Threat contained, no further action required.
Ticket #002 
 Date: July 4, 2026
Alert: RDP Brute Force Attempt
Source IP: 185.234.219.4
Target: Internal Windows Server (Port 3389)
Severity: High
Summary:
47 failed RDP login attempts detected at 3AM within 5 minutes — consistent with automated brute force attack. No authorized access scheduled.
Action: IP investigated, escalated to SOC L2, 
blocked at firewall.
Status: Closed — Threat contained.

 Key Knowledge
 Critical Ports for SOC Analysts
| Protocol | Port | Risk |
|---|---|---|
| SSH | 22 | Brute force |
| RDP | 3389 | Most attacked globally |
| SMB | 445 | EternalBlue/Ransomware |
| DNS | 53 | Data exfiltration |
| FTP | 21 | Plain text credentials |

Currently Learning 

TryHackMe SOC Level 1 path 
ISC2 CC certification prep 

Certifications In Progress 

CEH — Expected August 2026 
NAVTTC Cybersecurity — Expected August 2026 
ISC2 CC — In preparation 

 Connect

 LinkedIn: www.linkedin.com/in/samrasharafatali 
 TryHackMe: tryhackme.com/profile/0xsamra 
 GitHub: github.com/0xsamra/home_lab
