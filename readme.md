<div align="center">

# 🛡️ PredatorSec
## InfoStealer Detection & Response

Integrated SIEM & SOAR Project using **Elastic Security**, **Shuffle SOAR**, and **Python**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Elastic](https://img.shields.io/badge/Elastic-Security-005571?style=for-the-badge&logo=elastic&logoColor=white)
![Shuffle](https://img.shields.io/badge/Shuffle-SOAR-orange?style=for-the-badge)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-red?style=for-the-badge)
![VirusTotal](https://img.shields.io/badge/VirusTotal-API-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

</div>

---

# 📖 Overview

PredatorSec is an integrated SOC project designed to detect **Information Stealer malware** using **Elastic Security (SIEM)** and automate incident response through **Shuffle SOAR**.

The project combines detection engineering, threat intelligence enrichment, and automation to reduce analyst workload and improve incident response efficiency.

---

# 👥 Team Members

- Eslam
- Omar Khaled Mohamed Kamal Abdo
- Gamal Mohamed Yassin Mahmoud
- Mariam Hossam Eldin Hussien
- Fatma Elzahraa Mohamed Elsayed
- Mariam Ibrahim ayad Abdel Sayed

---

# 📂 Repository Structure

## Detection Rules

| Detection Rule | File |
|----------------|------|
| Initial Access | [Initial_Access.ndjson](./Initial_Access.ndjson) |
| Execution | [Execution.ndjson](./Execution.ndjson) |
| Credential Access | [Credential_Access.ndjson](./Credential_Access.ndjson) |
| Persistence | [Persistence.ndjson](./Persistence.ndjson) |
| Exfiltration & Command and Control | [Exfiltration_C2.ndjson](./Exfiltration_C2.ndjson) |
| Complete Detection Rules | [PredatorSec_All_250.ndjson](./PredatorSec_All_250.ndjson) |

---

## Automation Components

| Component | File |
|-----------|------|
| Elastic → Shuffle Integration | [elasticlinker.py](./elasticlinker.py) |
| SOAR Automation | [full_soar.py](./full_soar.py) |
| Email Notification Service | [mail.py](./mail.py) |
| Firewall Automation | [firwall.py](./firwall.py) |

---

# 🛠 Technology Stack

| Category | Technologies |
|----------|--------------|
| SIEM | Elastic Security, Kibana, Elasticsearch |
| SOAR | Shuffle |
| Programming | Python |
| Threat Intelligence | VirusTotal API |
| Detection | KQL |
| Framework | MITRE ATT&CK |

---

# 🎯 Detection Coverage

- Initial Access
- Execution
- Credential Access
- Persistence
- Command & Control (C2)
- Exfiltration

---

# 🔄 Project Workflow

```text
Information Stealer
        │
        ▼
 Endpoint Logs
        │
        ▼
 Filebeat
        │
        ▼
 Elasticsearch
        │
        ▼
 Elastic Detection Rules
        │
        ▼
 Kibana Alerts
        │
        ▼
 Python Integration
        │
        ▼
 Shuffle SOAR
        │
        ▼
 VirusTotal Enrichment
        │
        ▼
 Automated Email Alert
```

---

# 📸 Project Preview

> Screenshots can be added after uploading them to the repository.

```text
images/
├── elastic-alert.png
├── python-script.png
├── shuffle-workflow.png
└── dashboard.png
```

Example:

```md
<p align="center">
<img src="images/elastic-alert.png" width="900">
</p>

<p align="center">
<img src="images/shuffle-workflow.png" width="900">
</p>
```

---

# 📄 Documentation

The complete implementation details, architecture, methodology, testing process, and project report are available in the accompanying documentation.

---

# 📌 Notes

Default Elastic indices:

```text
logs-*
winlogbeat-*
logs-endpoint.events.*
```

Detection rules can be customized before importing into Elastic Security.


---

<div align="center">

### PredatorSec • InfoStealer Detection & Response

Integrated SIEM • Detection Engineering • SOAR Automation

</div>
