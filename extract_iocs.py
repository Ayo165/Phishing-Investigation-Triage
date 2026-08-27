import re
import sys
import os

def extract_iocs(file_path):
    
    if not os.path.exists(file_path):
        print(f"[ERROR] The file {file_path} was not found. Please double check the path.")
        return

    print(f"--- Scanning {file_path} for IOCs ---")
    
  
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    url_pattern = re.compile(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+')

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            
            ips = ip_pattern.findall(content)
            urls = url_pattern.findall(content)

            
            unique_ips = set(ips)
            unique_urls = set(urls)

            print("\n[+] Extracted IP Addresses:")
            if unique_ips:
                for ip in unique_ips:
                    print(f"    - {ip}")
            else:
                print("    None found.")

            print("\n[+] Extracted URLs:")
            if unique_urls:
                for url in unique_urls:
                    print(f"    - {url}")
            else:
                print("    None found.")

    except Exception as e:
        print(f"[ERROR] Could not read the file accurately: {e}")

if __name__ == "__main__":
    
    print("Starting IOC Extraction Tool...")
    
    sample_file = "suspicious_email.txt" 
    
 
    if not os.path.exists(sample_file):
        with open(sample_file, 'w') as f:
            f.write("Received from 192.168.1.50. Please click http://malicious-login-update.com to verify your account. Sender IP: 10.0.0.5")
            
    extract_iocs(sample_file)
