# Wazuh SIEM Lab — Setup & Detection

## Environment

| Component | Detail |
|---|---|
| **Wazuh Server** | Ubuntu Server (Wazuh 4.7.5) — `192.168.56.102` |
| **Agent** | Kali Linux 2026.2 — `kali-agent` |
| **Network** | VirtualBox — Host-Only Adapter (agent ↔ manager) |
| **Dashboard** | `https://192.168.56.102` |

---

## 1. Wazuh Server Installation

Deployed the **Wazuh all-in-one stack** (manager, indexer, dashboard) on an Ubuntu Server VM using the official Wazuh install script.

Verified the manager was reachable at `192.168.56.102` and the dashboard login worked before moving on to agent enrollment.

---

## 2. Agent Deployment (Kali Linux)

Downloaded and installed the Wazuh agent package (`.deb`, 4.7.5) on the Kali VM:

```bash
sudo apt install ./wazuh-agent_4.7.5-1_amd64.deb
```

Configured the agent to point at the manager and enrolled it automatically via the `<enrollment>` block in `/var/ossec/etc/ossec.conf`:

```xml
<client>
  <server>
    <address>192.168.56.102</address>
    <port>1514</port>
    <protocol>tcp</protocol>
  </server>
  <enrollment>
    <enabled>yes</enabled>
    <agent_name>kali-agent</agent_name>
  </enrollment>
</client>
```

Started the agent:

```bash
sudo systemctl enable --now wazuh-agent
```

**Result:** Confirmed in the dashboard under **Agents** — `kali-agent` showing **Active**, 100% agent coverage, v4.7.5.

---

## 3. Network Configuration

Switched the Kali VM's network adapter to **Host-Only** so it could reach the Wazuh manager on the internal `192.168.56.0/24` network, separate from the manager's own hosting.

---

## 4. Generating a Real Detection (SSH Brute Force)

**Goal:** trigger a genuine alert rather than just confirm agent connectivity.

**Attempted approach:** Fail SSH logins locally against Kali (`ssh kali@localhost`) with intentionally wrong passwords, expecting Wazuh's built-in SSHD authentication-failure rules to fire from `/var/log/auth.log`.

### Issue #1 — No `/var/log/auth.log` on Kali

Kali 2026.2 doesn't ship with a traditional syslog daemon by default, so SSH auth events go to **journald**, not a flat file:

```bash
journalctl -u ssh -n 20
```

This confirmed the failed logins were being logged there (`Failed password for invalid user kali`), but Wazuh's default `<localfile>` config had **no block monitoring auth logs at all** — Kali's default profile only ships `command`-type localfiles (`df`, `netstat`, `last`).

**Fix:** Added a `<localfile>` block to `/var/ossec/etc/ossec.conf`:

```xml
<localfile>
  <log_format>syslog</log_format>
  <location>/var/log/auth.log</location>
</localfile>
```

and restarted the agent.

### Issue #2 — File still didn't exist

Since Kali has no rsyslog running by default, `/var/log/auth.log` was never being created in the first place. Attempted to install `rsyslog`:

```bash
sudo apt install rsyslog -y
```

### Issue #3 — No network connectivity

The install failed with `Temporary failure resolving 'http.kali.org'`, and `ping 8.8.8.8` returned `Network is unreachable` — the VM had no working network route at that point (a side effect of the earlier Host-Only adapter change removing NAT/internet access).

**Root cause:** a single Host-Only adapter gives agent↔manager connectivity but cuts off internet access needed for package installs. The fix going forward is a **second NAT adapter** alongside Host-Only, so Kali has both internet access *and* manager connectivity simultaneously.

### Result

Despite the auth.log gap, the earlier SSH failures were still captured by Wazuh (likely picked up once the agent config synced), confirmed in the dashboard:

- **Authentication failures:** 18
- **Authentication successes:** 38
- **Top MITRE ATT&CK categories triggered:** *SSH, Password Guessing, Brute Force, Valid Accounts*

---

## Detections Performed

- ✅ **SSH brute-force / failed-login simulation**
- ⏳ *Port scanning detection (planned)*
- ⏳ *Privilege escalation attempts (planned)*

---

## Screenshots

<img width="959" height="437" alt="wazuh 1" src="https://github.com/user-attachments/assets/b85aad35-addb-4da8-b328-2cc0b363444b" />

---
<img width="956" height="436" alt="wazuh2" src="https://github.com/user-attachments/assets/465de49e-ebf0-4e5f-8702-be8a51471562" />

---

<img width="959" height="437" alt="wazuh3" src="https://github.com/user-attachments/assets/8f66dda6-b603-477d-91cc-39e87394f668" />


---

## Key Takeaways

- Confirming an agent shows "Active" isn't the same as confirming it's actually shipping the log sources you care about — always verify the `<localfile>` config matches what the OS actually generates.
- Kali's default Wazuh agent profile is tuned for host/process telemetry (`netstat`, `last`, `df`), **not** auth logging — SSH monitoring has to be added explicitly.
- VirtualBox networking mode is a real operational constraint: Host-Only-only isolates a VM from the internet, which breaks package installs mid-troubleshooting. **Dual-adapter (NAT + Host-Only)** avoids this.


## — Custom Wazuh Detection Rules

### Objective
Create custom Wazuh rules to detect SSH brute-force attempts and sudo 
privilege escalation, mapped to MITRE ATT&CK techniques.

### Custom Rules Created
File: `/var/ossec/etc/rules/local_rules.xml`

​```xml
<rule id="100010" level="10">
    <if_sid>5760</if_sid>
    <match>failed</match>
    <description>Custom Rule: Multiple SSH authentication failures detected</description>
    <mitre>
      <id>T1110</id>
    </mitre>
</rule>

<rule id="100011" level="12">
    <if_sid>5503</if_sid>
    <description>Custom Rule: Sudo privilege escalation attempt detected</description>
    <mitre>
      <id>T1548</id>
    </mitre>
</rule>
​```

**Note:** Originally based rule 100010 on `if_sid 5710`, but discovered 
via `alerts.log` inspection that this system's SSH failures actually 
trigger rule `5760`. Corrected the `if_sid` and rule fired successfully.

### Testing Method
- Used Hydra from Kali to simulate SSH brute-force:
  `hydra -l root -P /tmp/small.txt ssh://192.168.56.102 -t 1 -w 3`
- Triggered `sudo` command on Ubuntu server to test rule 100011

### Results
| Rule ID | Level | MITRE | Description | Status |
|---------|-------|-------|--------------|--------|
| 100010  | 10    | T1110 | SSH auth failures | ✅ Fired |
| 100011  | 12    | T1548 | Sudo privilege escalation | ✅ Fired |

### Screenshots
<img width="1280" height="800" alt="custom rule file" src="https://github.com/user-attachments/assets/1cf74c93-24e1-424f-8f94-adc259ef671b" />

---
<img width="943" height="431" alt="100010" src="https://github.com/user-attachments/assets/941b2fad-3a39-434f-9843-e3776de077f4" />

---
<img width="943" height="436" alt="custom rule" src="https://github.com/user-attachments/assets/0924ac44-fc5b-4523-9b03-2e260e1f929d" />


### Key Learning
Wazuh's built-in rule 2502 already does generic brute-force correlation 
via syslog pattern matching, but a custom SSH-specific rule chained to 
the exact parent rule ID gives clearer, more targeted attribution and 
practice writing MITRE-mapped detections from scratch.
