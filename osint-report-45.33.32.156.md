# OSINT Investigation Report

**Target IP:** 45.33.32.156
**Date:** August 7, 2026
**Analyst:** Samra Sharafat Ali (0xsamra)
**Classification:** Legitimate Public Test Server

---

## Executive Summary

IP **45.33.32.156** was investigated following its appearance in a simulated brute
force attack scenario. WHOIS data reveals the IP is registered to Akamai Technologies
(Linode) in the United States. Further investigation confirmed this IP resolves to
**scanme.nmap.org** — a deliberately public test server maintained by the Nmap
project to allow security researchers and students to legally practice network
scanning techniques.

AbuseIPDB reports (20 total, 19% confidence) and VirusTotal flags (2/91) are
consistent with a public scanning target that receives high volumes of automated
security tool traffic — not genuine malicious activity. This IP should not be
blocked or treated as a threat.

---

## Investigation Methodology

- WHOIS lookup (Kali Linux terminal)
- Nmap port scan (Kali Linux terminal)
- VirusTotal (virustotal.com)
- AbuseIPDB (abuseipdb.com)

---

## Findings

### WHOIS Analysis
- **IP:** 45.33.32.156
- **Network Range:** 45.33.0.0 — 45.33.127.255
- **Organization:** Akamai Technologies, Inc. (Linode)
- **Network Type:** Direct Allocation — Cloud/Hosting Infrastructure
- **Owner Country:** United States
- **Owner City:** Cambridge, Massachusetts
- **Registration Date:** March 20, 2015
- **Last Updated:** September 18, 2023

### Nmap Analysis
- Nmap returned warning: *"giving up on port because retransmission cap hit (10)"*
- Packets sent but no replies received after 10 retries
- Host appears filtered or rate-limited — consistent with a public test server
  receiving high scan volumes

### VirusTotal Analysis
- **Detection Ratio:** 2/91 vendors flagged as malicious
- **Community Score:** +2 (low concern)
- **ASN:** AS63949 — Akamai Connected Cloud
- **Country:** United States
- **Registry:** ARIN
- **Assessment:** 89% clean — 2 flags consistent with automated scanner
  false positives on a high-traffic public IP

### AbuseIPDB Analysis
- **Abuse Confidence Score:** 19% (low)
- **Total Reports:** 20
- **Hostname:** scanme.nmap.org
- **Usage Type:** Data Center / Web Hosting / Transit
- **Location:** Fremont, California, US
- **Reported Activity Types:** Web application scanning, SSH scanning,
  bad web bot activity — all consistent with security researchers
  using this IP as an authorized test target

---

## Verdict

**Classification: LEGITIMATE PUBLIC TEST SERVER ✅**

IP 45.33.32.156 resolves to **scanme.nmap.org** — a server intentionally operated
by the Nmap Security Scanner project for authorized security testing. All abuse
reports and vendor flags are consistent with high volumes of legitimate security
tool traffic directed at this intentional scanning target.

**This IP is NOT malicious.** Any alerts involving this IP in a real environment
should be investigated for why internal systems are communicating with a public
test server — not for malicious behavior from this IP itself.

---

## Key SOC Lessons

- **Hostname resolution is critical** — always check what a suspicious IP
  actually resolves to before drawing conclusions
- **Context changes everything** — 20 abuse reports on a public test server
  means nothing; 20 reports on a residential IP is serious
- **Low abuse confidence (19%) + legitimate hostname = false positive**
- **Always verify across multiple sources** before attributing malicious intent
- **OSINT verification prevented a false accusation** — this is exactly why
  SOC analysts investigate before acting

---

## Recommendations

- No blocking required — this is a legitimate public resource
- If this IP appears in internal network logs, investigate **why** internal
  systems are communicating with a public scanner test server
- Use this IP for legal Nmap practice in your home lab

---

## IOCs

*None — this IP is a legitimate public test server.*

**Infrastructure for reference only:**
- **IP:** 45.33.32.156
- **Hostname:** scanme.nmap.org
- **ASN:** AS63949
- **Organization:** Akamai Technologies (Linode)
- **Purpose:** Authorized Nmap scanning practice target
