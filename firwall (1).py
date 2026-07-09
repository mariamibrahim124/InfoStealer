from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api/firewall/block', methods=['POST'])
def block_ip():
    data = request.json
    ip_to_block = data.get('ip', 'Unknown IP')
    attack_type = data.get('type', 'Unknown Attack')

    # هنا بنطبع الأكشن كأنه فايرول حقيقي بيشتغل
    print("-" * 50)
    print(f"🚨 [PredatorSec Active Response] 🚨")
    print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🛑 Action: BLOCK IP")
    print(f"🎯 Target IP: {ip_to_block}")
    print(f"⚔️ Attack Type: {attack_type}")
    print(f"✅ Status: Rule added to Local Firewall successfully.")
    print("-" * 50)

    # لو عايز تعمل Block بجد على لينكس شيل علامة الـ # من السطر اللي جاي
    # os.system(f"sudo iptables -A INPUT -s {ip_to_block} -j DROP")

    return jsonify({"status": "success", "message": f"IP {ip_to_block} blocked in PredatorSec Firewall"}), 200

if __name__ == '__main__':
    # السيرفر هيشتغل على بورت 5000
    app.run(host='0.0.0.0', port=5000)