import requests
import json
from datetime import datetime, timedelta, timezone
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# ================= الإعدادات =================
ELASTIC_URL = "https://localhost:9200/.internal.alerts-security.alerts-*/_search"
SHUFFLE_WEBHOOK = ""
ELASTIC_AUTH = ('elastic', '')
# ============================================

def check_and_send():
    now = datetime.now(timezone.utc)
    five_mins_ago = now - timedelta(minutes=5)
    time_format = "%Y-%m-%dT%H:%M:%S.000Z"

    # الـ Query دي بتجيب أي Alert حقيقي طلع من الـ Detection Engine
    query = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"event.kind": "signal"}}
                ],
                "filter": [
                    {"range": {"@timestamp": {"gte": five_mins_ago.strftime(time_format)}}}
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
            print(f"[{datetime.now()}] Found {total_hits} SIEM Alerts. Sending to Shuffle...")
            for hit in data['hits']['hits']:
                alert_data = hit['_source']
                alert_data['es_id'] = hit['_id']
                # بنبعت الـ Alert كامل بكل تفاصيله لشافل
                requests.post(SHUFFLE_WEBHOOK, json=alert_data)
        else:
            print(f"[{datetime.now()}] No new SIEM alerts found.")
    except Exception as e:
        print(f"Error: {e}")

if name == "main":
    print("Service is running... Monitoring SIEM Alerts.")
    while True:
        check_and_send()
        time.sleep(60)