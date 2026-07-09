<div align="center">

# 🛡️ InfoStealer
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

- Eslam Ahmed Mohamed Abdel Hafez
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
| Initial Access | [Initial_Access.ndjson](./PredatorSec_Elastic_Rules_Renamed_All_Sections/Initial_Access.ndjson) |
| Execution | [Execution.ndjson](./PredatorSec_Elastic_Rules_Renamed_All_Sections/Execution.ndjson) |
| Credential Access | [Credential_Access.ndjson](./PredatorSec_Elastic_Rules_Renamed_All_Sections/Credential_Access.ndjson) |
| Persistence | [Persistence.ndjson](./PredatorSec_Elastic_Rules_Renamed_All_Sections/Persistence.ndjson) |
| Exfiltration & Command and Control | [Exfiltration_C2.ndjson](./PredatorSec_Elastic_Rules_Renamed_All_Sections/Exfiltration_C2.ndjson) |
| Complete Detection Rules | [PredatorSec_All_250.ndjson](./PredatorSec_Elastic_Rules_Renamed_All_Sections/PredatorSec_All_250.ndjson) |

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

# 📚 Project Documents

The following documents provide additional details about the project design, implementation, and presentation.

| Document | Link |
|----------|------|
| Project Report | [InfoStealer_Project_Report.pdf](./InfoStealer_Project_Report.pdf) |
| Project Presentation | [InfoStealer_Presentation.pptx](./InfoStealer_Presentation.pptx) |

---

<div align="center">

###  • InfoStealer Detection & Response

Integrated SIEM • Detection Engineering • SOAR Automation

</div>
