import re
from urllib.parse import urlparse
import ipaddress

input_message = input("Enter the message to analyze: ")

def analyze_message(message):
    detected_keywords = []
    message=message.lower()

    suspicious_keywords = [
        "urgent",
        "account suspended",
        "verify your account",
        "password",
        "you have won"
    ]

    for keyword in suspicious_keywords:
        if keyword in message:
            detected_keywords.append(keyword)

    if detected_keywords:
        return "This message may be a phishing attempt.", detected_keywords

    return "No suspicious keywords found", detected_keywords

result, detected = analyze_message(input_message)

score = len(detected)
if score == 0 or score == 1:
    level = "Low"
elif score == 2 or score == 3:
    level = "Medium"
else:   
    level = "High"



def url_exactor(message):
    urls = re.findall(r'https?://[^\s]+', message)

    shortenedurls = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "is.gd"]

    for url in urls:
        if url.startswith("http://"):
            print(f"Warning:{url} URL uses insecure HTTP")

        try:
            ipaddress.ip_address(urlparse(url).hostname)
            print(f"Warning:{url} is an IP address")

        except ValueError:
            pass

        if urlparse(url).hostname in shortenedurls:
            print(f"Warning:{url} is a shortened URL")
    
    if urls:
        return "Urls found", urls
    else:
        return "No urls found", urls



url_result, url_list = url_exactor(input_message)





print(url_result, "Urls:", (", ".join(url_list)))
print()
print(result, "\nDetected keywords:", (", ".join(detected)))
print("\nRisk level: ", level)