import os
import sys
import ipaddress
import requests

ABUSE_KEY = os.environ.get("ABUSEIPDB_KEY")
VT_KEY = os.environ.get("VT_KEY")


def check_abuseipdb(ip):
    print("\n=== AbuseIPDB Results ===")
    if not ABUSE_KEY:
        print("Missing ABUSEIPDB_KEY environment variable")
        return
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {"Accept": "application/json", "Key": ABUSE_KEY}
    params = {"ipAddress": ip, "maxAgeInDays": 90}
    try:
        r = requests.get(url, headers=headers, params=params, timeout=10)
        r.raise_for_status()
        d = r.json()["data"]
        print(f"IP: {d['ipAddress']}")
        print(f"Abuse Score: {d['abuseConfidenceScore']}%")
        print(f"Total Reports: {d['totalReports']}")
        print(f"Country: {d.get('countryCode', 'Unknown')}")
        print(f"ISP: {d.get('isp', 'Unknown')}")
        print(f"Usage Type: {d.get('usageType', 'Unknown')}")
    except Exception as e:
        print(f"AbuseIPDB error: {e}")


def check_virustotal(ip):
    print("\n=== VirusTotal Results ===")
    if not VT_KEY:
        print("Missing VT_KEY environment variable")
        return
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": VT_KEY}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        r.raise_for_status()
        attrs = r.json()["data"]["attributes"]
        stats = attrs["last_analysis_stats"]
        total = sum(stats.values())
        print(f"Malicious: {stats['malicious']}/{total} vendors")
        print(f"Suspicious: {stats['suspicious']}")
        print(f"Harmless: {stats['harmless']}")
        print(f"Undetected: {stats['undetected']}")
        print(f"Country: {attrs.get('country', 'Unknown')}")
        print(f"ASN: {attrs.get('asn', 'Unknown')}")
    except Exception as e:
        print(f"VirusTotal error: {e}")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ip-checker.py <IP_ADDRESS>")
        sys.exit(1)

    ip = sys.argv[1]
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        print(f"'{ip}' is not a valid IP address")
        sys.exit(1)

    print(f"\n🔍 Investigating IP: {ip}")
    print("=" * 40)
    check_abuseipdb(ip)
    check_virustotal(ip)
    print("\n✅ Investigation complete!")


if __name__ == "__main__":
    main()
