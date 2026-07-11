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

 ###Ticket #001
 
 **Date:** June 30, 2026
 
 **Analyst:** Samra (0xsamra)
 
 **Severity:** Critical
 
**Summary:**

A critical alert was triggered for IP 221.181.185.159, identified as a China-based address with prior involvement in 4 documented cyberattacks. The IP attempted unauthorized SSH login access.

**Evidence:**

SIEM logs flagged the source IP under Critical severity, showing repeated SSH login attempts consistent with known malicious activity associated with this IP.

**Action Taken:**

The IP was investigated using IP Hunter, confirming its malicious history. The alert was escalated to Will Griffin (Senior Security Analyst) for review. The IP was subsequently blocked on the firewall, with a comment added documenting the action and justification.

**Status:** Closed — Threat contained, no further action required.

###Ticket #002 

**Date:** July 4, 2026

**Alert:** RDP Brute Force Attempt

**Source IP:** 185.234.219.4

**Target:** Internal Windows Server (Port 3389)

**Severity:** High

**Summary:**

47 failed RDP login attempts detected at 3AM within 5 minutes — consistent with automated brute force attack. No authorized access scheduled.

**Action:** 

IP investigated, escalated to SOC L2, 
blocked at firewall.

**Status:**

Closed — Threat contained.

###Ticket #003

**Date:** July 07, 2026

**Analyst:** Samra (0xsamra)

**Severity:** High

**Summary:**

An employee reported their workstation running unusually slow. Investigation revealed an unknown process "svchost32.exe" consuming 90% CPU. The process was created at 2AM with no authorized personnel present and no scheduled tasks approved for that timeframe. The legitimate Windows process is "svchost.exe" — the extra "32" indicates a likely malware impersonation.

**Evidence:**

SIEM logs flagged the unauthorized process "svchost32.exe" under High severity, showing abnormal CPU consumption of 90% initiated at 2AM. No scheduled tasks or authorized processes matched this activity during that window.

**Action Taken:**

The process was investigated using a process scanner, confirming it as unauthorized and suspicious. The affected machine was isolated from the network to 
prevent potential lateral movement. The alert was escalated to SOC L2 Analyst for deeper investigation and malware analysis.

**Status:** Open — Threat contained, pending further investigation by SOC L2.

###Ticket #004 — OSINT Threat Intelligence Report

**Date:** July 11, 2026

**Analyst:** Samra (0xsamra)

**Type:** Threat Intelligence Investigation

**Severity:** High

**Target IP:** 185.234.219.4

**WHOIS Findings:**

WHOIS lookup performed on Kali Linux identified IP 185.234.219.4 as registered in Switzerland however belonging to a Lithuanian organization — "IT Business Solutions, MB." This geographic mismatch is a significant red flag. The abuse contact provided was a personal Gmail address (andrius.peteraitis@gmail.com) rather than a corporate email, indicating lack of legitimate organizational accountability. The IP block was allocated in November 2023 under ASN AS211415.

**VirusTotal / AbuseIPDB Findings:**

VirusTotal identified the IP as belonging to "Karolio IT Paslaugos, UAB," registered in Austria with organizational presence in Lithuania. Usage type was confirmed as Data Center/Web Hosting — not a residential or corporate user IP, consistent with attack infrastructure.
AbuseIPDB confirmed 6 independent abuse reports from 6 distinct sources across China, Poland, USA, Netherlands and Germany. First reported on March 14, 2026. Attack categories include SSH Brute Force, Port Scanning, and Credential Stuffing. The IP was flagged by ThreatBook Intelligence as VPN/Proxy infrastructure and was caught in an SSH honeypot (endlessh tarpit), confirming active malicious behavior.

**Nmap Findings:**

Network Mapper scan of all 1000 ports returned no response — all ports filtered. The host was confirmed active but fully firewalled, indicating deliberately hardened attack infrastructure. This is consistent with attacker-controlled systems that probe outbound while blocking inbound reconnaissance.
**Traceroute Findings:**
Traceroute reached only Hop 1 (10.0.2.2 — VirtualBox gateway). All subsequent hops returned no response, indicating the attacker's network is deliberately dropping ICMP packets to prevent route tracing. This is a further indicator of intentionally hidden infrastructure.

**SOC Verdict:** CONFIRMED MALICIOUS 🚨

**Supporting evidence:**

Geographic mismatch between registration and organization
Personal Gmail abuse contact — not legitimate business
Data center IP — not associated with real end user
6 independent reports from 5 countries
Confirmed SSH brute force and credential stuffing activity
VPN/Proxy infrastructure concealing true origin
Caught in SSH honeypot
All ports hardened against inbound scanning

**Recommended Action:**

Based on confirmed malicious activity, the IP was escalated to SOC L2 Analyst for review. The IP was permanently blocked at the firewall. A formal abuse report was submitted to AbuseIPDB. The IP has been added to the threat intelligence blocklist for ongoing monitoring.

**Status:**

Closed — Threat contained and reported.

 Key Knowledge
 
 Critical Ports for SOC Analysts
| Protocol | Port | Risk |
|---|---|---|
| SSH | 22 | Brute force |
| RDP | 3389 | Most attacked globally |
| SMB | 445 | EternalBlue/Ransomware |
| DNS | 53 | Data exfiltration |
| FTP | 21 | Plain text credentials |

 Cyber Kill Chain
| Stage | Attacker Action | SOC Response |
|---|---|---|
| Reconnaissance | Gathering target info | Monitor scanning activity |
| Weaponization | Creating malware | Threat intelligence feeds |
| Delivery | Phishing email/USB | Email filtering |
| Exploitation | Triggering vulnerability | Patch management, EDR |
| Installation | Installing backdoor | Antivirus, behavioral analysis |
| C2 | Attacker controls system | Block suspicious outbound traffic |
| Actions on Objectives | Stealing data/ransomware | DLP, network segmentation |

Currently Learning 

- TryHackMe SOC Level 1 path
- ISC2 CC certification prep
- Fortinet NSE — Introduction to Threat Landscape (completed)
- Fortinet Technical Introduction to Cybersecurity (in progress)
  
Certifications In Progress 

CEH — Expected August 2026 
NAVTTC Cybersecurity — Expected August 2026 
ISC2 CC — In preparation 

 Connect

 LinkedIn: www.linkedin.com/in/samrasharafatali 
 TryHackMe: tryhackme.com/profile/0xsamra 
 GitHub: github.com/0xsamra/home_lab
