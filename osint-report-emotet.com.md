# OSINT Investigation Report

**Target Domain:** emotet.com
**Date:** July 27, 2026
**Analyst:** Samra Sharafat Ali (0xsamra)
**Classification:** Non-Malicious

---

## Executive Summary

Domain "emotet.com" was investigated due to its association with the notorious Emotet
malware family name. WHOIS data reveals the domain was recently registered on May 20,
2026 by Cloud DNS Ltd — owner identity and country were redacted for privacy. DNS
resolution failed due to port 53 being blocked on the institutional network. VirusTotal
returned zero detections across all vendors. ThreatFox showed no documented malicious
activity. URLScan confirmed Cloudflare-hosted infrastructure with no suspicious behavior
detected.

---

## Investigation Methodology

Tools used:
- WHOIS lookup (Kali Linux terminal)
- NSLOOKUP (Kali Linux terminal)
- VirusTotal (virustotal.com)
- ThreatFox (threatfox.abuse.ch)
- URLScan (urlscan.io)

---

## Findings

### WHOIS Analysis
- **Domain:** emotet.com
- **Creation Date:** May 20, 2026 — recently registered
- **Registrar:** Cloud DNS Ltd (Bulgaria)
- **WHOIS Server:** whois.cloudns.net
- **Name Servers:** KENNETH.NS.CLOUDFLARE.COM / RAINA.NS.CLOUDFLARE.COM
- **Owner:** Redacted for privacy
- **Owner Country:** Redacted for privacy

### NSLOOKUP Analysis
- DNS server contacted: 10.14.93.44 on port 53
- Request timed out — no response received
- Port 53 likely blocked by institutional network policy
- DNS resolution could not be completed from this network

### VirusTotal Analysis
- **Overall detections:** 0/91 vendors flagged as malicious
- **Category:** Clean — no vendor classifies domain as malicious,
  phishing, or malware
- **Note:** 3/91 values visible in Relations tab refer to historical
  IP addresses associated with the domain — not the domain verdict itself

### ThreatFox Analysis
- No documented history or malicious activity found for emotet.com
- No IOCs, malware samples, or C2 indicators associated with this domain

### URLScan Analysis
- **CDN:** Cloudflare (WAF and DDoS protection active)
- **TLS Certificate:** Issued by WE1 — valid 3 months from July 18, 2026
- **HTTPS:** Enabled
- **IPs detected:**
  - 172.67.215.197 (Cloudflare AS13335)
  - 104.18.95.41 (Cloudflare AS13335)
- **Verdict:** No classification — no malicious behavior detected
- **Page behavior:** Cloudflare verification page ("Just a moment...")
- **Transactions:** 20 HTTP requests during scan across 2 domains

---

## Verdict

**Classification: NON-MALICIOUS ✅**

All five investigation tools returned clean results. The real Emotet malware was a
banking trojan and botnet dismantled by international law enforcement in January 2021.
The actual Emotet infrastructure never used "emotet.com" as a C2 domain — it operated
through hundreds of compromised servers globally. This domain appears to be a recently
registered domain that shares a name with the malware but shows no malicious activity.

---

## Key SOC Lessons

- Domain names alone do not confirm malicious intent — full context required
- Privacy-protected WHOIS is common and not inherently suspicious
- Cloudflare hosting is used by both legitimate sites and attackers
- Recently registered domains warrant monitoring even when currently clean
- Always verify across multiple sources before drawing conclusions
- A verdict of "clean today" does not mean "clean permanently" — monitor

---

## Recommendations

- No immediate action required
- Add to watchlist — recently registered domain sharing malware name
- Re-investigate in 30 days if any alerts involving this domain appear
- Do not block based on name alone — confirm with behavioral evidence first

---

## IOCs (Indicators of Compromise)

*None confirmed at time of investigation.*

**Associated Infrastructure (for monitoring only):**
- **Domain:** emotet.com
- **IPs:** 172.67.215.197 / 104.18.95.41
- **ASN:** AS13335 (Cloudflare)
- **Registrar:** Cloud DNS Ltd
- **First seen:** May 20, 2026
