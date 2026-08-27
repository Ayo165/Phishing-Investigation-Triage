# Phishing Investigation & Triage

## 📝 Objective
This project demonstrates the workflow of a SOC Analyst investigating suspicious emails. The goal was to analyze real-world phishing samples, manually extract Indicators of Compromise (IOCs), and write a lightweight Python script to automate the enrichment and threat-scoring of those artifacts.

## 🛠️ Tools & Technologies Used
*   **Scripting:** Python (Requests, JSON, Regex)
*   **Email Analysis:** EML file parsing, Header analysis
*   **OSINT & Threat Intel:** VirusTotal API, AbuseIPDB
*   **Data Sources:** Public phishing datasets

## 🗺️ Investigation Workflow

### 1. Manual Email & Header Analysis
The investigation started by safely opening public phishing email samples (EML files) in an isolated environment. The email headers were analyzed to trace the true sender's origin, bypassing spoofed "From" addresses by examining `Received` and `Return-Path` fields, and checking SPF/DKIM/DMARC authentication results.

### 2. IOC Extraction
Once the origin was traced, malicious artifacts were carefully extracted from the email body and attachments. These Indicators of Compromise (IOCs) included:
*   Suspicious URLs and embedded hyperlinks.
*   Attacker IP addresses.
*   File hashes (SHA256) of malicious attachments.

### 3. Python Automation for Threat Enrichment
To speed up the triage process, a Python script was developed to automate the analysis of the extracted IOCs. 
*   Used standard Python libraries (like `re` for regular expressions) to parse out IPs and domains from text blocks.
*   Integrated the **VirusTotal API** to automatically submit the extracted domains and hashes, retrieving their community threat scores and malicious flagging status.
*   Outputted the results in a clean format to immediately determine if the email was a known threat.

### 4. Triage Reporting
Based on the manual analysis and Python-enriched data, a final triage report was generated. The report detailed the attack vector, the severity of the phishing attempt, and actionable remediation steps for the engineering team.

## 💡 Conclusion
This project bridged the gap between manual SOC analysis and security automation. By understanding how to read raw email headers and extracting IOCs, I can accurately identify sophisticated phishing attempts. Furthermore, building a Python tool to interact with threat intelligence APIs demonstrates the ability to scale up investigations and reduce incident response time.
