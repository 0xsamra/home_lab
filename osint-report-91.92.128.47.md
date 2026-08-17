# OSINT Investigation Report — #4

**Target IP:** 91.92.128.47
**Date:** August 17, 2026
**Analyst:** Samra Sharafat Ali (0xsamra)
**Related Ticket:** INC-010
**Classification:** Suspicious — Requires Incident Response

---

## Executive Summary

IP **91.92.128.47** was investigated as part of Ticket #010, where SIEM detected
an encoded PowerShell command on an accountant's workstation downloading and
executing a payload from this external IP directly in memory — consistent with
a fileless malware attack.

WHOIS reveals the IP belongs to **Redcluster LTD** via **VPSAG** hosting,
registered in Bulgaria with organizational presence in Cyprus. VirusTotal returned
0/91 detections however the IP is hosted on a **data center/VPS infrastructure**
commonly abused by threat actors. AbuseIPDB shows 0 reports with 0% confidence —
however absence from reputation databases does not eliminate risk when behavioral
evidence from the SIEM is strong.

The strongest evidence of compromise is the **behavior observed on the workstation**
— not the IP reputation alone.

---

## Investigation Methodology

- WHOIS lookup (Kali Linux terminal)
- VirusTotal (virustotal.com)
- AbuseIPDB (abuseipdb.com)

---

## Findings

### WHOIS Analysis
- **IP Range:** 91.92.128.0 — 91.92.128.127
- **Network Name:** VPSAG-COM
- **Website:** vpsag.com
- **Country:** BG (Bulgaria)
- **Organization:** ORG-RL322-RIPE (Redcluster LTD)
- **Org Type:** LIR (Local Internet Registry)
- **Org Country:** CY (Cyprus)
- **Registration Number:** HE 307801
- **Abuse Contact:** admin@redcluster.net / +357.960.768.77
- **Created:** March 16, 2021
- **Last Modified:** January 03, 2023
- **Source:** RIPE NCC
- **Note:** Law enforcement inquiries directed to admin@redcluster.net

### VirusTotal Analysis
- **Detection Ratio:** 0/91 — No security vendor flagged as malicious
- **Network:** 91.92.128.0/24
- **ASN:** 44901
- **AS Label:** Belcloud LTD
- **Regional Internet Registry:** RIPE NCC
- **Country:** BG (Bulgaria)
- **Continent:** EU (Europe)
- **TLS Certificate Subject:** auth-dev.m-go.voyage (suspicious domain)
- **Certificate Issuer:** Let's Encrypt
- **JARM Fingerprint:** 15d3fd16d29d000042d43d000000fe02290512647416dcf0a400ccbc0b6b
- **Note:** Despite 0 detections the TLS certificate subject
  `auth-dev.m-go.voyage` is suspicious and warrants further investigation

### AbuseIPDB Analysis
- **Abuse Confidence Score:** 0%
- **Total Reports:** 0 — Not found in database
- **ISP:** Redcluster LTD
- **Usage Type:** Data Center / Web Hosting / Transit
- **ASN:** AS44901
- **Domain:** redcluster.net
- **Country:** Bulgaria
- **City:** Sofia, Sofia-Capital

---

## Key Observations

### 🚨 Suspicious TLS Certificate
VirusTotal shows a TLS certificate with subject `auth-dev.m-go.voyage` —
this is not a typical legitimate business domain. The subdomain structure
`auth-dev` suggests an authentication or credential harvesting endpoint.
This warrants immediate further investigation.

### Infrastructure Profile
- Bulgarian IP hosted under Cyprus-registered organization
- VPS/Data center infrastructure — commonly used for attack staging
- Multiple organization layers (VPSAG → Redcluster → Cyprus) adds
  complexity to attribution — a common attacker technique
- Law enforcement contact exists — IP is traceable

### Absence of Reputation Data
- 0 AbuseIPDB reports and 0 VirusTotal detections does NOT mean clean
- Newly deployed attack infrastructure often has no reputation history
- The behavioral evidence from SIEM (PowerShell + encoded command +
  in-memory execution) is significantly more reliable than reputation scores

---

## Correlation With Ticket #010

This IP is directly tied to a confirmed suspicious incident:

| Event | Detail |
|---|---|
| Detection | SIEM alert — August 09, 2026 6:00 PM |
| Process | PowerShell executing encoded command |
| Action | Connected to 91.92.128.47 |
| Payload | Downloaded and executed in memory |
| Disk writes | None — fileless execution |
| Authorization | No IT change management ticket |
| Target | Accountant workstation — financial data at risk |

The combination of **encoded PowerShell + external VPS IP + in-memory
execution + no authorization** is a confirmed high-risk incident pattern.

---

## Verdict

**Classification: SUSPICIOUS — Treat as Malicious Pending Investigation 🚨**

While reputation databases show no prior reports, the behavioral context
from Ticket #010 combined with:
- VPS/data center infrastructure (common attack staging)
- Multi-layer organization obscuring true ownership
- Suspicious TLS certificate domain (auth-dev.m-go.voyage)
- No legitimate business purpose identified

...makes this IP a **significant IOC** that should be treated as malicious
until proven otherwise.

---

## Recommended SOC Actions

1. Block IP 91.92.128.47 at firewall immediately
2. Investigate TLS certificate domain `auth-dev.m-go.voyage` as additional IOC
3. Search SIEM for any other internal hosts contacting this IP
4. Decode the PowerShell encoded command for full payload analysis
5. Investigate process tree on accountant workstation
6. Check for lateral movement from compromised workstation
7. Review accountant's recent file access and authentication activity
8. Submit IP to AbuseIPDB to contribute to community threat intelligence
9. Escalate to incident response team for full forensic investigation

---

## IOCs

| IOC Type | Value |
|---|---|
| **IP Address** | 91.92.128.47 |
| **IP Range** | 91.92.128.0/24 |
| **ASN** | AS44901 |
| **Organization** | Redcluster LTD / VPSAG |
| **Country** | Bulgaria (BG) |
| **TLS Subject** | auth-dev.m-go.voyage |
| **Related Ticket** | INC-010 |
| **Attack Type** | Fileless Malware / PowerShell Download |

---

**Final Classification:** Suspicious — Block and Investigate
**Related Incident:** INC-010 — Fileless Malware Attack via PowerShell
