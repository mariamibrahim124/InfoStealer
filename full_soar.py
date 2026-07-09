import requests
import json
import smtplib
import time
import urllib3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta, timezone

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ================= الإعدادات (تأكد من صحتها) =================
ELASTIC_URL = "https://localhost:9200/.internal.alerts-security.alerts-*/_search"
ELASTIC_AUTH = ('elastic', '')

VT_API_KEY = ""
SMTP_SENDER = ""
SMTP_PASS = ""
RECEIVER_EMAIL = ""
# ==========================================================

def send_alert_email(ip, score):
    msg = MIMEMultipart()
    msg['From'] = SMTP_SENDER
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = f"🚨 [PredatorSec] Malicious IP: {ip}"

    body = f"Alert! Malicious IP detected: {ip}\nVT Threat Score: {score}\nTime: {datetime.now()}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SMTP_SENDER, SMTP_PASS)
        server.sendmail(SMTP_SENDER, RECEIVER_EMAIL, msg.as_string())
        server.quit()
        print(f"✅ Alert email sent for IP: {ip}")
    except Exception as e:
        print(f"❌ Email error: {e}")

def check_vt_reputation(ip):
    url = f"https://www.virustotal.com/api/v3/ip_addresses/{ip}"
    headers = {"x-apikey": VT_API_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        malicious_score = data['data']['attributes']['last_analysis_stats']['malicious']
        return malicious_score
    return 0

def monitor_siem():
    print("PredatorSec Pipeline is Running... 🛡️")
    while True:
        now = datetime.now(timezone.utc)
        five_mins_ago = now - timedelta(minutes=5)

        query = {"query": {"bool": {"must": [{"match": {"event.kind": "signal"}}],
                 "filter": [{"range": {"@timestamp": {"gte": five_mins_ago.strftime("%Y-%m-%dT%H:%M:%S.000Z")}}}]}}}

        try:
            res = requests.get(ELASTIC_URL, json=query, verify=False, auth=ELASTIC_AUTH)
            alerts = res.json()['hits']['total']['value']

            if alerts > 0:
                for hit in res.json()['hits']['hits']:
                    # استخراج الـ IP المتغير ديناميكياً
                    ip = hit['_source'].get('source', {}).get('ip', 'Unknown')
                    if ip != 'Unknown':
                        print(f"🔍 Checking IP: {ip}")
                        score = check_vt_reputation(ip)
                        if score > 0: # لو الـ IP خطير
                            send_alert_email(ip, score)
            else:
                print(f"[{datetime.now()}] No new alerts.")

        except Exception as e:
            print(f"Error: {e}")

        time.sleep(60) # ابحث كل دقيقة

if __name__ == "__main__":
    monitor_siem()
