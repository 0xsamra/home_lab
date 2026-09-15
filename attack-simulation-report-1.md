# Attack Simulation Report — Full Chain

**Date:** September 15, 2026
**Analyst:** Samra (0xsamra)
**Environment:** Home Lab (VirtualBox — Kali Linux attacker, Wazuh manager/target)

## Lab Topology Note
This lab consists of two VMs: a Kali Linux attacker and a Wazuh manager (192.168.56.102), which also served as the SSH target for this exercise. As a result, all alerts are attributed to agent `000` (wazuh-server), the manager's own self-monitoring agent, rather than a separate victim agent. A three-tier lab (attacker → dedicated victim → manager) is planned as a future improvement — see Conclusion.

## Attack Stages

### 1. Reconnaissance — Nmap Scan

Performed service/version detection and OS fingerprinting against the target.

### 2. Brute Force — Hydra SSH Attack

Ran a dictionary-based brute-force attack against SSH (port 22) using 4 parallel threads.

## Wazuh Detections

### Reconnaissance (Nmap)
No alerts fired for the Nmap scan. Wazuh operates as a host-based intrusion detection system (HIDS) and does not inspect raw network traffic by default. Detecting port scans would require a network IDS (e.g., Suricata or Zeek) integrated with Wazuh, or firewall logging (ufw/iptables) configured to feed the log collector. This is documented as a visibility gap rather than a failed test.

### Brute Force (Hydra)
Multiple alerts fired, escalating in severity as the attack progressed:

| Rule ID | Level | Description |
|---------|-------|-------------|
| 2501 | 5 | User authentication failure |
| 2502 | 10 | User missed the password more than one time |
| 5758 | 8 | Maximum authentication attempts exceeded |
| 100010 | 10 | Custom Rule: Multiple SSH authentication failures detected |

---

<img width="944" height="388" alt="Day 17 stage 2" src="https://github.com/user-attachments/assets/7276ddb3-c82c-475e-a6a4-fbd90211fb59" />

---

<img width="938" height="350" alt="Day 17 stage 2(2)" src="https://github.com/user-attachments/assets/c144daaa-5db2-4549-b832-118d9e1977d2" />


---

- **Total events (15 min window):** 188
- **Authentication failures:** 99
- **Level 12+ alerts:** 11
- Alert volume spiked sharply between 23:20–23:22, matching the Hydra run window exactly.
- A pre-existing custom correlation rule (100010) also fired, indicating brute-force-specific detection logic beyond Wazuh's default ruleset was already in place.

## MITRE ATT&CK Mapping
- Reconnaissance → **T1595** (Active Scanning) — attempted, not detected
- Brute Force → **T1110** (Brute Force) — detected, tactic: Credential Access

## Conclusion
This exercise confirmed that Wazuh's default configuration provides strong detection for credential-based attacks (SSH brute force) but has no visibility into network reconnaissance without additional tooling. The escalating severity levels (5 → 10 → 8 → 10) show Wazuh correlating repeated failures rather than logging them as flat, isolated events, which is useful for prioritizing real incidents over noise.

**Planned improvements:**
- Add a dedicated victim VM with its own Wazuh agent, separate from the manager, to more accurately reflect a real network topology
- Integrate Suricata or firewall logging to close the reconnaissance detection gap
