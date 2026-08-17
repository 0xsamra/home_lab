# My Cybersecurity Home Lab — 0xsamra

---

## About Me
Aspiring SOC Analyst | BSIT Cybersecurity student | 0xsamra

---

## Lab Environment
- Host OS: Windows
- Virtualization: VirtualBox
- VMs: Kali Linux, Parrot OS, Metasploitable2, Ubuntu Server (Wazuh)

---

## Tools I've Worked With
- Wazuh (SIEM)
- Wireshark (Network Analysis)
- Nmap (Network Scanning)
- Metasploit (Exploitation)
- Burp Suite (Web Security)
- VirusTotal (Threat Intelligence)
- AbuseIPDB (IP Reputation)
- ThreatFox (Malware IOC Database)
- URLScan.io (URL Analysis)
- Shodan (Passive Reconnaissance)

---

## Practical Exercises Completed

### TryHackMe Rooms
- TryHackMe SOC Fundamentals ✅
- TryHackMe Defensive Security Intro ✅
- TryHackMe Junior Security Analyst Intro ✅
- TryHackMe SOC Level 1 Path — In Progress
- TryHackMe Intro to Cyber Threat Intel ✅
- TryHackMe Threat Intelligence Tools ✅
- TryHackMe Pyramid of Pain ✅

### Log Analysis
- Linux log analysis (auth.log, journalctl)
- Windows Event Viewer investigation
- Advanced log analysis (grep, awk, tail, journalctl filters)
- Log field extraction and IP identification

### Network Analysis
- Wireshark traffic capture and protocol filtering (HTTP, DNS, TCP)
- Network protocol analysis (HTTP, HTTPS, SSH, RDP, DNS, FTP, SMB, SMTP)
- PCAP forensic analysis — credential extraction and attacker behavior identification
- Network discovery scanning with Nmap
- Institutional network reconnaissance (ping sweep)

### OSINT & Threat Intelligence
- IP investigation using WHOIS, Nmap, Traceroute, VirusTotal, AbuseIPDB
- Domain investigation using WHOIS, URLScan, ThreatFox
- Phishing email analysis — header inspection, IOC extraction
- Threat actor campaign correlation across multiple incidents

### Vulnerability & Exploitation (Lab Only)
- SQL Injection, XSS, IDOR testing on DVWA/Juice Shop
- Metasploit framework usage on Metasploitable2
- Brute force simulation using Hydra
- Password cracking with CUPP

### SOC Operations
- SIEM alert triage and investigation
- Incident ticket writing (INC-001 through INC-009)
- Phishing email analysis and header investigation
- C2 beaconing detection
- Brute force pattern recognition
- Impossible travel detection
- Credential theft scenario analysis

---

## Investigation Log

### Ticket #001

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

---

### Ticket #002

**Date:** July 4, 2026
**Alert:** RDP Brute Force Attempt
**Source IP:** 185.234.219.4
**Target:** Internal Windows Server (Port 3389)
**Severity:** High

**Summary:**
47 failed RDP login attempts detected at 3AM within 5 minutes — consistent with automated brute force attack. No authorized access scheduled.

**Action:**
IP investigated, escalated to SOC L2, blocked at firewall.

**Status:** Closed — Threat contained.

---

### Ticket #003

**Date:** July 07, 2026
**Analyst:** Samra (0xsamra)
**Severity:** High

**Summary:**
An employee reported their workstation running unusually slow. Investigation revealed an unknown process "svchost32.exe" consuming 90% CPU. The process was created at 2AM with no authorized personnel present and no scheduled tasks approved for that timeframe. The legitimate Windows process is "svchost.exe" — the extra "32" indicates a likely malware impersonation.

**Evidence:**
SIEM logs flagged the unauthorized process "svchost32.exe" under High severity, showing abnormal CPU consumption of 90% initiated at 2AM. No scheduled tasks or authorized processes matched this activity during that window.

**Action Taken:**
The process was investigated using a process scanner, confirming it as unauthorized and suspicious. The affected machine was isolated from the network to prevent potential lateral movement. The alert was escalated to SOC L2 Analyst for deeper investigation and malware analysis.

**Status:** Open — Threat contained, pending further investigation by SOC L2.

---

### Ticket #004 — OSINT Threat Intelligence Report

**Date:** July 11, 2026
**Analyst:** Samra (0xsamra)
**Type:** Threat Intelligence Investigation
**Severity:** High
**Target IP:** 185.234.219.4

**WHOIS Findings:**
WHOIS lookup performed on Kali Linux identified IP 185.234.219.4 as registered in Switzerland however belonging to a Lithuanian organization — "IT Business Solutions, MB." This geographic mismatch is a significant red flag. The abuse contact provided was a personal Gmail address (andrius.peteraitis@gmail.com) rather than a corporate email, indicating lack of legitimate organizational accountability. The IP block was allocated in November 2023 under ASN AS211415.

**VirusTotal / AbuseIPDB Findings:**
VirusTotal identified the IP as belonging to "Karolio IT Paslaugos, UAB," registered in Austria with organizational presence in Lithuania. Usage type was confirmed as Data Center/Web Hosting — not a residential or corporate user IP, consistent with attack infrastructure. AbuseIPDB confirmed 6 independent abuse reports from 6 distinct sources across China, Poland, USA, Netherlands and Germany. First reported on March 14, 2026. Attack categories include SSH Brute Force, Port Scanning, and Credential Stuffing. The IP was flagged by ThreatBook Intelligence as VPN/Proxy infrastructure and was caught in an SSH honeypot (endlessh tarpit), confirming active malicious behavior.

**Nmap Findings:**
Network Mapper scan of all 1000 ports returned no response — all ports filtered. The host was confirmed active but fully firewalled, indicating deliberately hardened attack infrastructure.

**Traceroute Findings:**
Traceroute reached only Hop 1 (10.0.2.2 — VirtualBox gateway). All subsequent hops returned no response, indicating deliberately hidden infrastructure.

**SOC Verdict:** CONFIRMED MALICIOUS 🚨

**Supporting Evidence:**
- Geographic mismatch between registration and organization
- Personal Gmail abuse contact — not legitimate business
- Data center IP — not associated with real end user
- 6 independent reports from 5 countries
- Confirmed SSH brute force and credential stuffing activity
- VPN/Proxy infrastructure concealing true origin
- Caught in SSH honeypot
- All ports hardened against inbound scanning

**Status:** Closed — Threat contained and reported.

---

### Ticket #005 — PCAP Traffic Analysis

**Date:** July 15, 2026
**Analyst:** Samra (0xsamra)
**Severity:** High
**Type:** Practice — Traffic Analysis

**Summary:**
A pcap file captured during a previous DVWA lab session was analyzed using Wireshark. Investigation revealed unencrypted HTTP traffic containing multiple successful login attempts against a DVWA web application. The attacker gained unauthorized access twice across three separate TCP sessions.

**Evidence:**
- **Source IP:** 192.168.56.101 (Attacker — Kali Linux)
- **Target IP:** 192.168.56.102 (Victim — DVWA/Metasploitable)
- **Protocol:** HTTP (unencrypted), TCP
- **Port Targeted:** 80

**HTTP Findings:**
- Login credentials transmitted over plain HTTP — no HTTPS encryption
- Credentials visible in plaintext within Wireshark
- Two successful POST requests to `/dvwa/login.php` confirmed
- Attacker demonstrated prior knowledge of exact target path
- Following successful login, attacker navigated to `/dvwa/index.php`
- Active exploitation session confirmed

**TCP Findings:**
- Three separate TCP sessions established and properly terminated
- Clean FIN/ACK handshakes — deliberate controlled behavior
- Each session followed complete SYN → SYN/ACK → ACK → FIN/ACK lifecycle
- Manual interaction confirmed — not automated scanning

**Recommended Actions:**
- Enforce HTTPS — disable plain HTTP immediately
- Implement strong password policy
- Enable account lockout after failed login attempts
- Monitor for repeated POST requests to login pages
- Implement Web Application Firewall (WAF)

**Status:** Practice Exercise — Closed

---

### Ticket #006 — C2 DNS Beaconing Detection

**Ticket ID:** INC-006
**Title:** Suspected Command-and-Control (C2) DNS Beaconing Detected
**Date/Time Detected:** July 28, 2026 — 10:37 AM
**Analyst:** Samra Sharafat Ali (0xsamra)
**Severity:** High
**Status:** Closed

**Incident Summary:**
The SIEM generated an alert after detecting repeated outbound DNS queries from an internal workstation to a domain identified as known Command-and-Control (C2) infrastructure. The DNS requests occur every 60 seconds, consistent with automated beaconing behavior commonly associated with malware. The affected workstation is assigned to an HR employee who reported no unusual activity.

**Affected Asset:**

| Field | Detail |
|---|---|
| **Host** | HR Employee Workstation |
| **Department** | Human Resources |
| **Detection Source** | SIEM |
| **Indicator** | Repeated outbound DNS queries to known C2 domain |

**Indicators of Compromise (IOCs):**
- Outbound DNS requests to a domain flagged as C2 infrastructure
- Beaconing interval of approximately 60 seconds
- Potential malware communication with attacker-controlled server

**Action Taken:**
- Workstation immediately isolated from the network pending investigation
- Malicious domain and associated IPs blocked at firewall and DNS filter
- Alert escalated to SOC L2 Analyst for forensic analysis
- HR employee notified and credential reset initiated
- Endpoint malware scan launched and forensic evidence collected

**Status:** Closed — Contained, escalated to SOC L2 for investigation
**Type:** Practice Scenario

---

### Ticket #007 — Unauthorized Account Creation

**Ticket ID:** INC-007
**Title:** Unauthorized Administrator Account Creation on Critical Database Server
**Date/Time Detected:** August 04, 2026 — 11:45 PM
**Analyst:** Samra (0xsamra)
**Severity:** Critical
**Status:** Open — Under Investigation

**Incident Summary:**
SIEM detected creation of a new administrator account named **"admin_backup"** on a critical database server at 11:45 PM. No change management ticket exists for this action and the IT team has no knowledge of this account creation. The affected server hosts sensitive customer financial data.

**Affected Asset:**

| Field | Detail |
|---|---|
| **Host** | Critical Database Server |
| **Data Hosted** | Customer Financial Data |
| **Detection Source** | SIEM |
| **Unauthorized Account** | admin_backup |
| **Time of Creation** | 11:45 PM |

**Indicators of Compromise (IOCs):**
- Unauthorized administrator account "admin_backup" created outside business hours
- No change management ticket associated with account creation
- IT team has no knowledge of this action
- Creation time (11:45 PM) inconsistent with normal administrative activity

**Action Taken:**
- Unauthorized account "admin_backup" immediately disabled pending investigation
- Alert escalated to SOC L2 Analyst for deeper forensic investigation
- IT team notified and change management team alerted
- Server access logs pulled for review of all activity around account creation time

**Status:** Open — Account disabled, escalated to SOC L2
**Type:** Detection — Unauthorized Privilege Escalation / Persistence

---

### Ticket #008 — VPN Brute Force Attack

**Ticket ID:** INC-008
**Title:** VPN Brute Force Attack with Successful Unauthorized Login
**Date/Time Detected:** August 05, 2026 — 2:00 AM
**Analyst:** Samra (0xsamra)
**Severity:** Critical
**Status:** Open — Under Investigation

**Incident Summary:**
SIEM detected over 500 failed login attempts against the company VPN portal from a single IP address **45.33.32.156** over a 10-minute window at 2:00 AM. Following the failed attempts, one successful login was recorded. The compromised account belongs to a senior finance manager currently on vacation abroad.

**Affected Assets:**

| Field | Detail |
|---|---|
| **Host** | Company VPN Portal |
| **Compromised Account** | Senior Finance Manager |
| **Detection Source** | SIEM |
| **Detection Time** | 2:00 AM — August 05, 2026 |
| **Suspected IP** | 45.33.32.156 |
| **Attack Duration** | 10 minutes |

**Indicators of Compromise (IOCs):**
- 500+ failed VPN login attempts from single IP in 10 minutes
- One successful login immediately following brute force activity
- Login at 2:00 AM — inconsistent with normal business hours
- Account owner confirmed abroad on vacation

**Action Taken:**
- IP 45.33.32.156 immediately blocked at firewall
- Compromised VPN account disabled pending investigation
- Active VPN session terminated immediately
- Alert escalated to SOC L2 Analyst for forensic investigation
- Finance manager notified through secure out-of-band channel

**Status:** Open — Account disabled, session terminated, escalated to SOC L2
**Type:** Detection — Brute Force / Unauthorized Access / Potential Data Breach

---

### Ticket #009 — Microsoft 365 Account Compromise

**Ticket ID:** INC-009
**Title:** Suspected Microsoft 365 Account Compromise via Phishing
**Date/Time Detected:** August 07, 2026 — 30 minutes post credential submission
**Analyst:** Samra Sharafat Ali (0xsamra)
**Severity:** High
**Status:** Open — Under Investigation

**Incident Summary:**
A user based in Karachi received a phishing email impersonating Microsoft IT Support requesting they update their Office 365 credentials. The user submitted credentials on the linked page. 30 minutes later, SIEM detected a successful login from a Romanian IP — inconsistent with the user's location in Karachi.

**Affected Asset:**

| Field | Detail |
|---|---|
| **Target** | Microsoft 365 User Account |
| **User Location** | Karachi, Pakistan |
| **Suspicious Login Location** | Romania |
| **Attack Vector** | Phishing / Credential Theft |
| **Detection Source** | SIEM |
| **Time Gap** | ~30 minutes between credential submission and unauthorized login |

**Indicators of Compromise (IOCs):**
- Phishing email impersonating Microsoft IT Support
- User submitted credentials to malicious harvesting page
- Successful login from Romanian IP — impossible travel scenario
- 30-minute window consistent with manual attacker use of stolen credentials

**Containment Actions Taken:**
- Affected user's Microsoft 365 password reset immediately
- All active sessions and authentication tokens revoked
- Unauthorized MFA methods and registered devices reviewed and removed
- Phishing URL and domain blocked across email security and firewall
- Phishing email removed from all affected mailboxes

**Primary IOCs:**

| IOC Type | Detail |
|---|---|
| **Attack Vector** | Phishing email impersonating Microsoft IT Support |
| **Phishing URL** | Malicious credential harvesting page — under investigation |
| **Source IP** | Romanian IP — outside expected user region |
| **Compromised Account** | Microsoft 365 user — Karachi, Pakistan |

**Status:** Open — Containment complete, forensic investigation ongoing
**Type:** Phishing / Credential Theft / Unauthorized Account Access

# Security Incident Ticket — INC-010

**Ticket ID:** INC-010
**Title:** Fileless Malware Attack via PowerShell Encoded Command
**Date/Time Detected:** August 09, 2026 — 6:00 PM
**Analyst:** Samra Sharafat Ali (0xsamra)
**Severity:** Critical
**Status:** Open — Under Investigation

---

## Incident Summary

SIEM detected PowerShell executing an encoded command on an accountant's workstation
at 6:00 PM. The command connected to external IP **91.92.128.47**, downloaded a
malicious file, and executed it directly in memory without writing to disk —
consistent with a **fileless malware attack** designed to evade traditional
antivirus detection.

---

## Affected Asset

| Field | Detail |
|---|---|
| **Host** | Accountant's Workstation |
| **Department** | Finance / Accounting |
| **Detection Source** | SIEM |
| **Detection Time** | 6:00 PM — August 09, 2026 |
| **Process** | PowerShell — encoded command execution |
| **External IP** | 91.92.128.47 |
| **Execution Method** | In-memory / Fileless — no file written to disk |
| **IT Change Ticket** | None — unauthorized activity |

---

## Indicators of Compromise (IOCs)

- PowerShell executing encoded/obfuscated command on accountant workstation
- Outbound connection to external IP 91.92.128.47
- File downloaded and executed in memory — fileless execution
- No IT change management ticket exists for this activity
- Activity at 6:00 PM — end of business hours, reduced monitoring window

---

## Initial Analysis

Fileless malware attacks operate entirely in memory — leaving no files on disk for
traditional antivirus to detect. This technique is increasingly common in targeted
attacks against financial departments. Key concerns:

- PowerShell encoded commands are used to obfuscate malicious activity
- In-memory execution bypasses file-based security controls
- Finance department targeting suggests data theft or financial fraud intent
- No IT authorization confirms this is unauthorized activity

---

## Action Taken

- Affected workstation immediately isolated from network
- PowerShell command decoded and process tree investigated
- External IP 91.92.128.47 blocked at firewall
- PowerShell, authentication, and network logs pulled for analysis
- Checked for lateral movement from compromised workstation
- Forensic evidence preserved before any remediation
- Incident escalated to IR team for deeper investigation

---

## Recommendations

1. Decode and fully analyze the PowerShell encoded command
2. Run OSINT on 91.92.128.47 — determine attacker infrastructure
3. Check for credential theft or lateral movement to other systems
4. Review all finance systems for unauthorized access
5. Implement PowerShell Constrained Language Mode across organization
6. Enable Script Block Logging for all PowerShell activity
7. Deploy EDR solution capable of detecting in-memory threats

---

## Impact Assessment

Potential compromise of accountant workstation with possible exposure or theft
of sensitive financial data. Fileless execution method suggests a sophisticated
and targeted attack rather than opportunistic malware.

---

**Status:** Open — Workstation isolated, IR team engaged
**Type:** Fileless Malware / PowerShell Attack / Potential Financial Data Breach
---

## Investigation Reports

### 1. OSINT Report — IP 185.234.219.4
- **Type:** Threat Intelligence / OSINT
- **Verdict:** Malicious 🚨
- **Tools:** WHOIS, Nmap, Traceroute, VirusTotal, AbuseIPDB
- [View Full Report](osint-report-185.234.219.4.md)

### 2. OSINT Report — Domain emotet.com
- **Type:** Threat Intelligence / OSINT
- **Verdict:** Non-Malicious ✅
- **Tools:** WHOIS, NSLOOKUP, VirusTotal, ThreatFox, URLScan
- [View Full Report](osint-report-emotet.com.md)

### 3. OSINT Report — IP 45.33.32.156
- **Type:** Threat Intelligence / OSINT
- **Verdict:** Legitimate Public Test Server ✅
- **Tools:** WHOIS, Nmap, VirusTotal, AbuseIPDB
- [View Full Report](osint-report-45.33.32.156.md)

---

## Key Knowledge

### Critical Ports for SOC Analysts

| Protocol | Port | Risk |
|---|---|---|
| SSH | 22 | Brute force |
| RDP | 3389 | Most attacked globally |
| SMB | 445 | EternalBlue/Ransomware |
| DNS | 53 | Data exfiltration |
| FTP | 21 | Plain text credentials |
| HTTP | 80 | Unencrypted traffic |
| HTTPS | 443 | Encrypted — harder to inspect |
| SMTP | 25 | Phishing delivery |

### Cyber Kill Chain

| Stage | Attacker Action | SOC Response |
|---|---|---|
| Reconnaissance | Gathering target info | Monitor scanning activity |
| Weaponization | Creating malware | Threat intelligence feeds |
| Delivery | Phishing email/USB | Email filtering |
| Exploitation | Triggering vulnerability | Patch management, EDR |
| Installation | Installing backdoor | Antivirus, behavioral analysis |
| C2 | Attacker controls system | Block suspicious outbound traffic |
| Actions on Objectives | Stealing data/ransomware | DLP, network segmentation |

### Network Defense Concepts

| Concept | Function | SOC Relevance |
|---|---|---|
| IDS | Detects intrusions — alerts only | Passive monitoring |
| IPS | Detects AND blocks intrusions | Active blocking |
| WAF | Filters web application traffic | Blocks SQLi, XSS |
| DLP | Prevents data leaving network | Stops exfiltration |
| NAC | Controls who joins the network | Blocks rogue devices |
| SOAR | Automates SOC responses | Reduces manual work |
| EDR | Monitors endpoints for threats | Endpoint detection |
| XDR | EDR + network + cloud combined | Next gen detection |

### Windows Event IDs — SOC Reference

| Event ID | Meaning | Significance |
|---|---|---|
| 4624 | Successful login | Baseline — track anomalies |
| 4625 | Failed login | Brute force indicator |
| 4634 | Logoff | Session tracking |
| 4648 | Login with explicit credentials | Lateral movement indicator |
| 4672 | Admin privileges assigned | Privilege escalation |
| 4688 | New process created | Malware execution |
| 4698 | Scheduled task created | Persistence mechanism |
| 4732 | User added to admin group | Privilege escalation |
| 1102 | Audit log cleared | Attacker covering tracks 🚨 |

### Phishing Red Flags

| Indicator | Example |
|---|---|
| Spoofed sender domain | paypa1.com instead of paypal.com |
| Suspicious Reply-To | harvest@malicious-domain.ru |
| Malicious URL | http://paypal-secure-login.malicious-domain.ru |
| Urgency language | "URGENT: Account suspended in 24 hours" |
| Generic greeting | "Dear Customer" instead of your name |
| HTTP not HTTPS | Unencrypted credential submission page |

---

## Currently Learning
- TryHackMe SOC Level 1 path
- Fortinet NSE — Introduction to Threat Landscape ✅ Completed
- Fortinet NSE — Cybersecurity and Cloud Fundamentals ✅ Completed
- Google Cybersecurity Certificate — In Progress

---

## Certifications Earned
- ✅ Fortinet — Introduction to the Threat Landscape (July 2026)
- ✅ Fortinet — Cybersecurity and Cloud Fundamentals (July 2026)

## Certifications In Progress
- CEH — Expected August 2026
- NAVTTC Cybersecurity — Expected August 2026

---

## Connect
- **LinkedIn:** [linkedin.com/in/samrasharafatali](https://www.linkedin.com/in/samrasharafatali)
- **TryHackMe:** [tryhackme.com/p/0xsamra](https://tryhackme.com/p/0xsamra)
- **GitHub:** [github.com/0xsamra/home_lab](https://github.com/0xsamra/home_lab)
