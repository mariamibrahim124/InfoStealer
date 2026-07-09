import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_soc_email(target_ip, threat_score):
    # ================= الإعدادات =================
    sender_email = "" # الإيميل اللي هتبعت منه
    sender_password = ""
    receiver_email = "" # الإيميل اللي هيستقبل (ممكن تخليهم هما الاتنين واحد للتجربة)
    # ============================================

    # تجهيز محتوى الرسالة
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = f"🚨 [PredatorSec Alert] Malicious IP Detected: {target_ip}"

    # شكل الإيميل من جوه
    body = f"""\
    🚨 PredatorSec SOC Automated Alert 🚨

    A suspicious activity has been detected and verified by your pipeline.

    🌐 Target IP: {target_ip}
    💀 VirusTotal Threat Score: {threat_score}
    🕒 Detection Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    Action Required: Please check Elastic SIEM and Shuffle SOAR for full incident context.
    -----------------------------------------
    Automated by PredatorSec Engine.
    """

    message.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        # الاتصال بسيرفرات جوجل
        print("Connecting to Gmail SMTP server...")
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() # تشفير الاتصال
        server.login(sender_email, sender_password)

        # إرسال الرسالة
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print(f"[{datetime.now()}] ✅ Email Alert sent successfully to {receiver_email}!")

    except Exception as e:
        print(f"❌ Error sending email: {e}")

# للتجربة المباشرة (Test)
if __name__ == "__main__":
    test_ip = "8.8.8.8"
    test_score = "5"
    send_soc_email(test_ip, test_score)
