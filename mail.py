import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta, timezone
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ================= 1. إعدادات ElasticSearch =================
ELASTIC_URL = "http://localhost:9200/.internal.alerts-security.alerts-*/_search"
ELASTIC_AUTH = ('elastic', '') #password elastic

# ================= 2. إعدادات Shuffle SOAR =================
# حط اللينك اللي نسخته من Shuffle هنا
SHUFFLE_WEBHOOK = "http://localhost:3001/api/v1/hooks/webhook_223d73c2-e6b0-40de-bda4-847b5f60d04e"

# ================= 3. إعدادات الإيميل =======================
SENDER_EMAIL = ""
SENDER_PASSWORD = "" #app password
RECEIVER_EMAIL = ""
# ========================================================

seen_alerts = set()
def send_soc_email(target_ip, alert_name):
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = RECEIVER_EMAIL
    message['Subject'] = f"🚨 [PredatorSec] Threat Detected: {target_ip}"

    body = f"""\
    🚨 PredatorSec SOC Automated Alert 🚨

    A suspicious activity has been detected by your Elastic SIEM.

    🔴 Alert Name: {alert_name}
🌐 Target IP: {target_ip}
    🕒 Detection Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    Action Required: Please check Elastic SIEM and Shuffle for full incident context.
    -----------------------------------------
    Automated by PredatorSec Engine.
    """

    message.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        server.quit()
        print(f"[{datetime.now()}] ✅ Email Alert for IP {target_ip} sent successfully!")
    except Exception as e:
        print(f"❌ Error sending email: {e}")
def check_elastic_and_alert():
    now = datetime.now(timezone.utc)
    lookback_time = now - timedelta(minutes=2)
    time_format = "%Y-%m-%dT%H:%M:%S.000Z"

    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"event.kind": "signal"}}
                ],
                "filter": [
                    {"range": {"@timestamp": {"gte": lookback_time.strftime(time_format)}}}
                ]
            }
        }
    }

    try:
        response = requests.get(ELASTIC_URL, json=query, verify=False, auth=ELASTIC_AUTH)
        response.raise_for_status()
        data = response.json()
        total_hits = data['hits']['total']['value']

        if total_hits > 0:
		for hit in data['hits']['hits']:
                	alert_id = hit['_id']

                if alert_id not in seen_alerts:
                    alert_data = hit['_source']

                    source_ip = alert_data.get('source', {}).get('ip', 'Unknown IP')
                    alert_name = alert_data.get('kibana.alert.rule.name', 'Failed Login Alert')

                    print(f"[{datetime.now()}] ⚠️ New Alert Detected ({alert_name})!")

                    # 1. إرسال الداتا لـ Shuffle عشان ينفذ الـ Workflow بتاعه
                    try:
                        requests.post(SHUFFLE_WEBHOOK, json=alert_data)
                        print(f"[{datetime.now()}] 🔄 Alert data sent to Shuffle Webhook.")
                    except Exception as e:
                        print(f"❌ Error sending to Shuffle: {e}")
	                    # 2. إرسال الإيميل
                    send_soc_email(source_ip, alert_name)

                    seen_alerts.add(alert_id)
        else:
            pass

    	except Exception as e:
        	print(f"❌ Error checking Elastic: {e}")

if __name__ == "__main__":
    print("🚀 PredatorSec Service is running... Monitoring Elastic SIEM Alerts.")
    while True:
        check_elastic_and_alert()
        time.sleep(60)
