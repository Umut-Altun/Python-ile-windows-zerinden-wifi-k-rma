import subprocess
import re

# WiFi profillerini alma
komut_cıktısı = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, encoding="utf-8", errors='ignore')

if komut_cıktısı.returncode == 0:
    # print("Kayıtlı WiFi profilleri alındı.")
    komut_cıktısı = komut_cıktısı.stdout

    # Profil adlarını bulma
    profil_adları = re.findall(r"All User Profile\s+:\s+(.*)", komut_cıktısı)
    
    if profil_adları:
        # print("Kayıtlı WiFi profilleri bulundu.")
        wifi_listesi = []

        for ad in profil_adları:
            wifi_profil = {}
            # WiFi profili bilgilerini alma
            profil_bilgisi = subprocess.run(["netsh", "wlan", "show", "profile", ad], capture_output=True, encoding="utf-8", errors='ignore')
            if profil_bilgisi.returncode == 0:
                # print(f"{ad} için WiFi profil bilgileri alındı.")
                profil_bilgisi = profil_bilgisi.stdout

                if re.search("Güvenlik anahtarı\s+:\s+Yok", profil_bilgisi):
                    continue
                else:
                    wifi_profil["ssid"] = ad
                    # WiFi şifresini alma
                    profil_bilgisi_şifre = subprocess.run(["netsh", "wlan", "show", "profile", ad, "key=clear"], capture_output=True, encoding="utf-8", errors='ignore').stdout
                    şifre = re.search(r"Key Content\s+:\s+(.*)", profil_bilgisi_şifre)
                    if şifre:
                        wifi_profil["şifre"] = şifre.group(1)
                    else:
                        wifi_profil["şifre"] = None
                                    
                    wifi_listesi.append(wifi_profil) 
            else:
                print(f"{ad} için WiFi profil bilgileri alınamadı.")
                
        # print("WiFi ağları listesi oluşturuldu.")
        for wifi in wifi_listesi:
            print(wifi)
    else:
        print("Kayıtlı WiFi profili bulunamadı.")
else:
    print("Komut çıktısı alınamadı.")
