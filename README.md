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

---

## Practical Exercises Completed
- TryHackMe SOC Fundamentals
- TryHackMe Defensive Security Intro
- TryHackMe Junior Security Analyst Intro
- Linux log analysis (auth.log, journalctl)
- Windows Event Viewer investigation
- SQL Injection, XSS testing on DVWA/Juice Shop
- Wireshark traffic capture and protocol filtering (HTTP, DNS, TCP)
- Network protocol analysis (HTTP, HTTPS, SSH, RDP, DNS, FTP, SMB, SMTP)
- TryHackMe SOC Level 1 Path — Room 2 completed

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
Network Mapper scan of all 1000 ports returned no response — all ports filtered. The host was confirmed active but fully firewalled, indicating deliberately hardened attack infrastructure. This is consistent with attacker-controlled systems that probe outbound while blocking inbound reconnaissance.

**Traceroute Findings:**
Traceroute reached only Hop 1 (10.0.2.2 — VirtualBox gateway). All subsequent hops returned no response, indicating the attacker's network is deliberately dropping ICMP packets to prevent route tracing. This is a further indicator of intentionally hidden infrastructure.

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

**Recommended Action:**
Based on confirmed malicious activity, the IP was escalated to SOC L2 Analyst for review. The IP was permanently blocked at the firewall. A formal abuse report was submitted to AbuseIPDB. The IP has been added to the threat intelligence blocklist for ongoing monitoring.

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

### Ticket #006 — Security Incident 

**Ticket ID:** INC-006
**Title:** Suspected Command-and-Control (C2) DNS Beaconing Detected
**Date/Time Detected:** July 28, 2026 — 10:37 AM
**Analyst:** Samra Sharafat Ali (0xsamra)
**Severity:** High
**Status:** Closed

---

## Incident Summary

The SIEM generated an alert after detecting repeated outbound DNS queries from an internal workstation to a domain identified as known Command-and-Control (C2) infrastructure. The DNS requests occur every 60 seconds, consistent with automated beaconing behavior commonly associated with malware.

The affected workstation is assigned to an HR employee who reported no unusual activity or suspicious behavior on the device.

---

## Affected Asset

| Field | Detail |
|---|---|
| **Host** | HR Employee Workstation |
| **Department** | Human Resources |
| **Detection Source** | SIEM |
| **Indicator** | Repeated outbound DNS queries to known C2 domain |

---

## Indicators of Compromise (IOCs)

- Outbound DNS requests to a domain flagged as C2 infrastructure
- Beaconing interval of approximately 60 seconds
- Potential malware communication with attacker-controlled server

---

## Initial Analysis

The regular 60-second interval of DNS requests strongly suggests automated malware beaconing rather than normal user activity. Since the destination domain is already classified as malicious, the workstation may be compromised and attempting to communicate with an attacker-controlled server. The HR employee's lack of awareness is consistent with silent background malware operation.

---

## Action Taken

- Workstation immediately isolated from the network pending investigation
- Malicious domain and associated IPs blocked at firewall and DNS filter
- Alert escalated to SOC L2 Analyst for forensic analysis
- HR employee notified and credential reset initiated
- Endpoint malware scan launched and forensic evidence collected

---

## Recommendations

1. Review DNS, network, and endpoint logs for additional malicious activity
2. Monitor environment for similar beaconing from other internal hosts
3. Conduct full forensic investigation to determine infection vector
4. Assess scope — determine if other workstations contacted same C2 domain
5. Submit IOCs to threat intelligence platform for broader monitoring

---

## Conclusion

Evidence indicates a likely malware infection communicating with a known C2 server through periodic DNS beaconing. Containment actions have been taken. Forensic investigation is underway to determine full scope and prevent further compromise.

---

**Status:** Closed — Contained, escalated to SOC L2 for investigation
**Type:** Practice Scenario

# Security Incident Ticket — INC-007

**Ticket ID:** INC-007
**Title:** Unauthorized Administrator Account Creation on Critical Database Server
**Date/Time Detected:** August 04, 2026 — 11:45 PM
**Analyst:** Samra (0xsamra)
**Severity:** Critical
**Status:** Open — Under Investigation

---

## Incident Summary

SIEM detected creation of a new administrator account named **"admin_backup"** on a
critical database server at 11:45 PM. No change management ticket exists for this
action and the IT team has no knowledge of this account creation. The affected server
hosts sensitive customer financial data, making this a critical priority incident.

---

## Affected Asset

| Field | Detail |
|---|---|
| **Host** | Critical Database Server |
| **Data hosted** | Customer Financial Data |
| **Detection Source** | SIEM |
| **Unauthorized Account** | admin_backup |
| **Time of Creation** | 11:45 PM |

---

## Indicators of Compromise (IOCs)

- Unauthorized administrator account "admin_backup" created outside business hours
- No change management ticket associated with account creation
- IT team has no knowledge of this action
- Account created on server hosting sensitive financial data
- Creation time (11:45 PM) inconsistent with normal administrative activity

---

## Initial Analysis

The creation of an administrator account outside business hours with no change
management approval is a significant red flag. This behavior is consistent with:
- An attacker establishing persistence after initial compromise
- A malicious insider creating a backdoor account
- Privilege escalation following unauthorized access

The timing (11:45 PM) and lack of documentation strongly suggest unauthorized
activity rather than legitimate administrative work.

---

## Action Taken

- Unauthorized account "admin_backup" immediately disabled pending investigation
- Alert escalated to SOC L2 Analyst for deeper forensic investigation
- IT team notified and change management team alerted
- Server access logs pulled for review of all activity around account creation time
- Network connections to/from server monitored for suspicious activity

---

## Recommendations

1. Perform full forensic investigation to identify account creator
2. Review all actions performed using "admin_backup" account
3. Check for additional unauthorized accounts or backdoors
4. Review server access logs for signs of prior compromise
5. Implement alerts for all privileged account creations going forward
6. Enforce change management policy for all administrative actions

---

## Conclusion

Unauthorized administrator account creation on a financial data server outside
business hours with no documentation is a critical security incident. Immediate
containment actions taken. Full forensic investigation underway to determine
origin, scope, and intent.

---

**Status:** Open — Account disabled, escalated to SOC L2
**Type:** Detection — Unauthorized Privilege Escalation / Persistence

# Security Incident Ticket — INC-008

**Ticket ID:** INC-008
**Title:** VPN Brute Force Attack with Successful Unauthorized Login
**Date/Time Detected:** August 05, 2026 — 2:00 AM
**Analyst:** Samra (0xsamra)
**Severity:** Critical
**Status:** Open — Under Investigation

---

## Incident Summary

SIEM detected over 500 failed login attempts against the company VPN portal from a
single IP address **45.33.32.156** over a 10-minute window at 2:00 AM — consistent
with an automated brute force attack. Following the failed attempts, **one successful
login was recorded from the same IP**. The compromised account belongs to a senior
finance manager who is currently on vacation abroad, making legitimate access highly
unlikely.

---

## Affected Assets

| Field | Detail |
|---|---|
| **Host** | Company VPN Portal |
| **Compromised Account** | Senior Finance Manager |
| **Detection Source** | SIEM |
| **Detection Time** | 2:00 AM — August 05, 2026 |
| **Suspected IP** | 45.33.32.156 |
| **Attack Duration** | 10 minutes |

---

## Indicators of Compromise (IOCs)

- 500+ failed VPN login attempts from single IP in 10 minutes
- One successful login immediately following brute force activity
- Login at 2:00 AM — inconsistent with normal business hours
- Account owner confirmed abroad on vacation — cannot be legitimate login
- Single source IP — consistent with automated credential stuffing tool
- IP: 45.33.32.156 — requires threat intelligence lookup

---

## Initial Analysis

The successful login following 500 failed attempts at 2:00 AM is a critical security
incident. This pattern is consistent with:
- Automated brute force or credential stuffing attack
- Attacker gaining unauthorized access to VPN using compromised credentials
- Potential data exfiltration targeting financial data accessible via this account

The account owner's confirmed absence abroad makes any legitimate login from this
IP impossible. This is an active compromise requiring immediate containment.

---

## Action Taken

- IP **45.33.32.156** immediately blocked at firewall
- Compromised VPN account disabled pending investigation
- Active VPN session terminated immediately
- Alert escalated to SOC L2 Analyst for forensic investigation
- VPN access logs pulled for review of all activity post-login
- Network connections monitored for data exfiltration activity
- Finance manager notified through secure out-of-band channel
- All credentials associated with this account flagged for mandatory reset

---

## Recommendations

1. Investigate what data was accessed during the unauthorized VPN session
2. Run threat intelligence lookup on 45.33.32.156
3. Check for lateral movement from the VPN entry point
4. Review all finance systems for unauthorized access post-login
5. Implement MFA on VPN portal immediately to prevent recurrence
6. Enable geo-blocking or impossible travel detection on VPN
7. Audit all other accounts for similar brute force patterns

---

## Conclusion

A confirmed unauthorized VPN login following automated brute force activity
represents an active security breach. The account owner's confirmed absence
eliminates any possibility of legitimate access. Immediate containment actions
have been taken. Full forensic investigation is underway to determine scope
of access and potential data exposure.

---

**Status:** Open — Account disabled, session terminated, escalated to SOC L2
**Type:** Detection — Brute Force / Unauthorized Access / Potential Data Breach


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


---

## Investigation Reports

### 1. OSINT Report — IP 185.234.219.4
- **Type:** Threat Intelligence / OSINT
- **Verdict:** Malicious
- **Tools:** WHOIS, Nmap, Traceroute, VirusTotal, AbuseIPDB
- [View Full Report](osint-report-185.234.219.4.md)

- ### 2. OSINT Report — Domain emotet.com
- **Type:** Threat Intelligence / OSINT
- **Verdict:** Non-Malicious ✅
- **Tools:** WHOIS, NSLOOKUP, VirusTotal, ThreatFox, URLScan
- [View Full Report](osint-report-emotet.com.md)

---

## Currently Learning
- TryHackMe SOC Level 1 path
- ISC2 CC certification prep
- Fortinet NSE — Introduction to Threat Landscape ✅ Completed

---

## Certifications Earned
- ✅ Fortinet — Introduction to the Threat Landscape (July 2026)
- ✅ Fortinet — Cybersecurity and Cloud Fundamentals (July 2026)

## Certifications In Progress
- CEH — Expected August 2026
- NAVTTC Cybersecurity — Expected August 2026
- ISC2 CC — In preparation

---

## Connect
- **LinkedIn:** [linkedin.com/in/samrasharafatali](https://www.linkedin.com/in/samrasharafatali)
- **TryHackMe:** [tryhackme.com/p/0xsamra](https://tryhackme.com/p/0xsamra)
- **GitHub:** [github.com/0xsamra/home_lab](https://github.com/0xsamra/home_lab)
