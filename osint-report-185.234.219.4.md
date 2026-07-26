# OSINT Investigation Report

**Target IP:** 185.234.219.4
**Date:** July 2026
**Analyst:** Samra (0xsamra)
**Classification:** Suspicious/Malicious

---

##  Executive Summary:
IP 185.234.219.4 was investigated following an RDP brute force alert. WHOIS data reveals the IP belongs to a small Lithuanian IT company with a suspicious country registration mismatch — registered in Switzerland but operated from Lithuania. OSINT findings confirm this IP is highly likely malicious attack infrastructure, having been flagged multiple times across threat intelligence platforms. The IP was newly allocated in November 2023, consistent with infrastructure created specifically for malicious activity. 

---

## Investigation Methodology
Tools used:
- WHOIS lookup (Kali Linux terminal)
- Nmap port scan (Kali Linux terminal)
- Traceroute (Kali Linux terminal)
- VirusTotal (virustotal.com)
- AbuseIPDB (abuseipdb.com)

---

## Findings

### WHOIS Analysis
- **Organization:** IT Business Solutions, MB
- **Registered Country:** Switzerland (CH)
- **Operating Country:** Lithuania (LT)
- **Abuse Contact:** andrius.peteraitis@gmail.com (personal Gmail — not corporate)
- **IP Allocated:** November 2023 (newly created infrastructure)
- **ASN:** AS211415

### Nmap Analysis
- All 1000 ports filtered — no response
- Host is confirmed up but deliberately hidden
- No services exposed to external scanning
- Indicates hardened attack infrastructure

### Traceroute Analysis
- Blocked at every hop after local gateway (10.0.2.2)
- 22 hops all returning * * * (ICMP blocked)
- Deliberately hidden network path

### VirusTotal Analysis
- 1 out of 91 security vendors flagged as malicious
- Flagged as: Malicious infrastructure

### AbuseIPDB Analysis
- **Total reports:** 6
- **Attack types:** SSH Brute Force, Port Scanning, VPN/Proxy
- **First seen:** March 14, 2026
- **Notable reports:**
  - ThreatBook.io: Identified as VPN/Proxy/CDN infrastructure
  - Multiple SSH brute force attempts across US, NL, PL, DE servers
  - Fail2Ban triggered on multiple honeypots
  - Invalid user attempts (adm1n) — automated credential stuffing

---

## Verdict
**Classification: MALICIOUS** 🚨

This IP is confirmed malicious attack infrastructure based on:
1. Country registration mismatch (CH/LT)
2. Personal Gmail abuse contact — not legitimate business
3. SSH brute force reported across 6 independent servers
4. VPN/Proxy classification — used to hide attacker identity
5. Newly allocated IP (Nov 2023) — created for attack use
6. All ports filtered — hardened attack server

---

## Recommendations
- Block IP 185.234.219.4 at firewall immediately
- Alert all SSH-exposed servers to watch for this IP
- Add to threat intelligence blocklist
- Monitor for related IPs in same subnet (185.234.219.0/24)
- Report to AbuseIPDB if further activity detected

---

## IOCs (Indicators of Compromise)
- **IP:** 185.234.219.4
- **ASN:** AS211415
- **Organization:** IT Business Solutions MB
- **Attack types:** SSH Brute Force, Port Scanning
- **First malicious activity:** March 14, 2026
- **Abuse contact:** andrius.peteraitis@gmail.com

