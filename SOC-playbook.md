# SOC Analyst Playbook — 0xsamra

## Overview
This playbook documents standard operating procedures
for common security incidents encountered in a SOC
environment. Based on real investigation experience
from home lab practice.

---

## Playbook #1 — SSH Brute Force Response

### Detection
- Wazuh Rule: 5710 (Multiple auth failures)
- Threshold: 5+ failures in 60 seconds
- MITRE: T1110 — Brute Force

### Investigation Steps
1. Identify source IP from SIEM alert
2. Check IP reputation (AbuseIPDB, VirusTotal)
3. Review authentication logs for pattern
4. Check if any login succeeded after failures
5. Identify targeted account/service

### Containment
1. Block source IP at firewall
2. If login succeeded — disable compromised account
3. Force password reset on targeted account
4. Enable account lockout policy

### Escalation Criteria
- Escalate to L2 if: successful login detected
- Escalate to IR if: lateral movement observed

---

## Playbook #2 — Phishing Email Response

### Detection
- User reports suspicious email
- Email security gateway alert
- SIEM detects credential submission

### Investigation Steps
1. Collect original email with full headers
2. Extract: sender, Reply-To, URLs, attachments
3. Check URLs on VirusTotal and URLScan
4. Check sender domain reputation
5. Determine if user clicked link or submitted credentials

### Containment
1. Block phishing URL at web proxy/firewall
2. Remove email from all mailboxes
3. If credentials submitted — force password reset
4. Revoke active sessions

### Escalation Criteria
- Escalate to L2 if: credentials were submitted
- Escalate to IR if: account compromise confirmed

---

## Playbook #3 — Ransomware Detection

### Detection
- Mass file modifications (hundreds/second)
- Known ransomware extensions (.locked, .encrypted)
- C2 beaconing from endpoint
- Wazuh integrity monitoring alerts

### Investigation Steps
1. Identify affected host immediately
2. Determine ransomware family if possible
3. Check network for lateral spread
4. Identify patient zero

### Containment
1. IMMEDIATELY isolate affected host from network
2. Block C2 IP/domain at firewall
3. Preserve forensic image before remediation
4. Notify management and legal

### Escalation Criteria
- ALWAYS escalate to IR immediately
- This is a critical incident — no L1 solo handling

---

## Playbook #4 — Unauthorized Account Creation

### Detection
- Windows Event ID 4720 (account created)
- Linux: /etc/passwd modification
- Wazuh integrity monitoring alert
- After-hours timing

### Investigation Steps
1. Identify who created the account
2. Check change management for authorization
3. Review what the account did after creation
4. Check for privilege escalation

### Containment
1. Disable unauthorized account immediately
2. Review all actions taken by that account
3. Check for persistence mechanisms

### Escalation Criteria
- Escalate to L2 if: account has admin rights
- Escalate to IR if: evidence of data access
