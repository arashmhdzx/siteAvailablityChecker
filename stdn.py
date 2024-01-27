import time
import requests
from datetime import datetime
import os


def check_website(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except requests.ConnectionError:
        pass
    return False

def play_alert_sound():
    file = "ACDC-thunderstruck.mp3"
    print('playing sound using native player')
    os.system(file)

def main():
    # website_url = "https://google.com"  
    website_url = "https://stdn.iau.ir/Student/captchaProcess"  

    sleep_interval = 10  

    while True:
        if check_website(website_url):
            print(f"{datetime.now()} - Website is accessible now!")
            play_alert_sound()
            break
        else:
            print(f"{datetime.now()} - Website is still inaccessible.")
            time.sleep(sleep_interval)

if __name__ == "__main__":
    main()
