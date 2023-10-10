import requests
from requests.structures import CaseInsensitiveDict
import time

count = 1

while(True):
    # Şimdiki zaman, saat, dakika
    current_time = time.localtime()
    hour = current_time.tm_hour
    minute = current_time.tm_min
    # Zaman dilimlerini belirle
    if(hour == 22 and minute == 1):
        break
    while(hour == 22 and minute == 0):
        # Token ve CRNleri yaz
        url = "https://kepler-beta.itu.edu.tr/api/ders-kayit/v21"
        token = ""
        headers = CaseInsensitiveDict()
        headers["Accept"] = "application/json"
        headers["Authorization"] = f"Bearer {token}"
        headers["Content-Type"] = "application/json"

        data = {
            "ECRN": [
                "",
                ""
            ],
            "SCRN": []
        }
        resp = requests.post(url, headers=headers, json=data)
        print(resp.status_code)
        time.sleep(5)
        print(f'İstek {count} gönderildi.')
