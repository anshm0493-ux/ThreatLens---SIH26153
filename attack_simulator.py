import time
import random

LOG_FILE = "logs.txt"

# Fake attacker IPs
ips = ["203.0.113.45", "198.51.100.23", "192.0.2.78"]

print("Attack Simulator Started... Injecting fake attacks every 3 sec")
print("Keep your dashboard running in other terminal: python app.py")

count = 0
while True:
    ip = random.choice(ips)
    count += 1
    attack_type = random.choice(["Brute Force", "DDoS", "SQLi"])
    
    if attack_type == "Brute Force":
        log = f"2026-09-09 20:01:{count:02d} - {ip} - Failed login for admin - 401\n"
    elif attack_type == "DDoS":
        log = f"2026-09-09 20:01:{count:02d} - {ip} - GET /api/data - 429 - Rate Limit Exceeded\n"
    else:
        log = f"2026-09-09 20:01:{count:02d} - {ip} - GET /login?payload=' OR 1=1-- - 403\n"

    with open(LOG_FILE, "a") as f:
        f.write(log)
    
    print(f"Injected: {log.strip()}")
    time.sleep(3)