# BlueScout - Cyber Threat Intelligence (CTI) Bot 🛡️

🌍 **Choose Language / Dil Seçimi:**
* [🇬🇧 English](#english)
* [🇹🇷 Türkçe](#türkçe)

---

## English

**BlueScout** is a Python-based automated Threat Intelligence bot designed for Security Operations Center (SOC) environments. It interacts with the official NIST National Vulnerability Database (NVD) API to hunt for high-risk vulnerabilities (such as Remote Code Execution - RCE) and directly logs the findings into a MariaDB/MySQL database for further analysis and SIEM integration.

### Features
* **API Integration:** Pulls clean JSON data directly from NIST NVD without relying on unstable HTML scraping.
* **Automated Logging:** Seamlessly connects to MariaDB/MySQL to store vulnerability logs.
* **Targeted Threat Hunting:** Filters specifically for critical vulnerabilities like RCE.
* **Terminal Alerts:** Color-coded CLI outputs for immediate SOC alerts.

### Prerequisites
* Python 3.x
* MariaDB / MySQL Server
* Required Python Libraries: `requests`, `mysql-connector-python`, `colorama`

### Setup & Database Configuration

1. **Install dependencies:**
   ```bash
   pip install requests mysql-connector-python colorama
   ```

2. **Create the database and table:**
   ```sql
   CREATE DATABASE bluescout_db;
   USE bluescout_db;
   CREATE TABLE cti_logs (
       id INT AUTO_INCREMENT PRIMARY KEY,
       tehdit_turu VARCHAR(50),
       baslik VARCHAR(255),
       aciklama TEXT,
       kaynak_url VARCHAR(255),
       kesif_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

3. **Configure the script:**
   Update the `password` field in `bluescout.py` with your database credentials.

### Usage
```bash
python3 bluescout.py
```

### Disclaimer
This tool is developed for educational and defensive security (Blue Team) purposes using publicly available APIs.

---

## Türkçe

**BlueScout**, Güvenlik Operasyon Merkezleri (SOC) için tasarlanmış Python tabanlı otomatik bir Siber Tehdit İstihbarat botudur. Resmi NIST Ulusal Zafiyet Veritabanı (NVD) API'si ile haberleşerek yüksek riskli zafiyetleri (örneğin RCE) avlar ve daha ileri analizler veya SIEM entegrasyonu için bulguları doğrudan MariaDB/MySQL veritabanına kaydeder.

### Özellikler
* **API Entegrasyonu:** Kararsız HTML kazıma yöntemleri yerine doğrudan NIST NVD'den temiz JSON verisi çeker.
* **Otomatik Loglama:** Zafiyet loglarını depolamak için MariaDB/MySQL ile sorunsuz bağlantı kurar.
* **Hedefli Tehdit Avcılığı:** Özellikle RCE gibi kritik zafiyetleri filtreler.
* **Terminal Alarmları:** Anlık SOC alarmları için renklendirilmiş terminal çıktıları.

### Gereksinimler
* Python 3.x
* MariaDB / MySQL Sunucusu
* Gerekli Python Kütüphaneleri: `requests`, `mysql-connector-python`, `colorama`

### Kurulum ve Veritabanı Yapılandırması

1. **Kütüphaneleri kurun:**
   ```bash
   pip install requests mysql-connector-python colorama
   ```

2. **Veritabanı ve tabloyu oluşturun:**
   ```sql
   CREATE DATABASE bluescout_db;
   USE bluescout_db;
   CREATE TABLE cti_logs (
       id INT AUTO_INCREMENT PRIMARY KEY,
       tehdit_turu VARCHAR(50),
       baslik VARCHAR(255),
       aciklama TEXT,
       kaynak_url VARCHAR(255),
       kesif_tarihi TIMESTAMP DEFAULT CURRENT_TIMESTAMP
   );
   ```

3. **Script'i yapılandırın:**
   `bluescout.py` dosyası içindeki `password` kısmını kendi veritabanı şifrenizle güncelleyin.

### Kullanım
```bash
python3 bluescout.py
```

### Yasal Uyarı
Bu araç, halka açık API'ler kullanılarak eğitim ve defansif güvenlik (Mavi Takım) amacıyla geliştirilmiştir.

---
**Developer / Geliştirici:** Güven Zenci
