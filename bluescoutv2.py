import requests
import mysql.connector
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.CYAN + "[*] BlueScout CTI Bot Initializing (API Mode)...")

try:
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD_HERE", 
        database="bluescout_db"
    )
    cursor = db.cursor()
    print(Fore.GREEN + "[+] Database connection established!")
except Exception as e:
    print(Fore.RED + f"[-] Database error: {e}")
    exit()

# NIST NVD API URL for 'RCE' vulnerabilities
api_url = "https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=RCE&resultsPerPage=10"
print(Fore.YELLOW + f"[*] Fetching data from: {api_url}\n")

try:
    headers = {'User-Agent': 'BlueScout-CTI-Bot/1.0'}
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        veri = response.json()
        zafiyetler = veri.get('vulnerabilities', [])
        kayit_sayisi = 0
        
        for z in zafiyetler:
            cve_kodu = z['cve']['id']
            aciklamalar = z['cve']['descriptions']
            aciklama = next((item['value'] for item in aciklamalar if item['lang'] == 'en'), "No description.")
            
            tehdit_turu = "CRITICAL RCE"
            kaynak_link = f"https://nvd.nist.gov/vuln/detail/{cve_kodu}"
            
            print(Fore.RED + Style.BRIGHT + f"[!] SOC ALERT: {cve_kodu} Detected!")
            print(Fore.WHITE + f"    Detail: {aciklama[:100]}...")
            
            sql = "INSERT INTO cti_logs (tehdit_turu, baslik, aciklama, kaynak_url) VALUES (%s, %s, %s, %s)"
            degerler = (tehdit_turu, cve_kodu, aciklama, kaynak_link)
            
            try:
                cursor.execute(sql, degerler)
                db.commit()
                kayit_sayisi += 1
            except mysql.connector.Error:
                pass
                
        print(Fore.CYAN + f"\n[*] Scan complete. {kayit_sayisi} critical RCE vulnerabilities logged to database.")
    else:
        print(Fore.RED + f"[-] API request failed. HTTP Status: {response.status_code}")

except Exception as e:
    print(Fore.RED + f"[-] An error occurred: {e}")

finally:
    cursor.close()
    db.close()
