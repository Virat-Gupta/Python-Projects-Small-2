from bs4 import BeautifulSoup

import requests
import smtplib

import os
from dotenv import load_dotenv
load_dotenv()

URL = r"https://www.amazon.com/dp/B075CYMYK6"
EMAIL_PROVIDER_SMTP_ADDRESS=os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
MY_EMAIL=os.environ["MY_EMAIL"]
MY_EMAIL_PASSWORD=os.environ["MY_EMAIL_PASSWORD"]
TO_EMAIL = os.environ["TO_EMAIL"]

header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
    "Accept-Language" : "en-US,en;q=0.9,en-IN;q=0.8"
}

response = requests.get(URL, headers=header)
amazon_web_scrap = response.text

soup = BeautifulSoup(amazon_web_scrap, "html.parser")

price = float(soup.find(class_="a-price-whole").text + soup.find(class_="a-price-fraction").text)
print(price)

if price < 100:
    with smtplib.SMTP(EMAIL_PROVIDER_SMTP_ADDRESS) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_EMAIL_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=f"Subject:Price Drop Alert (Amazon)\n\nThe amaon Item {URL} is available for {price}")