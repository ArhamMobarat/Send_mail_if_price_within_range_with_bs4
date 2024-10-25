from bs4 import BeautifulSoup
import requests
import smtplib
import os
# IMPORTED os to access the environment variables
# Environment variables help keep confidentiality
PRODUCT_URL = os.environ["URL"]
APP_PASSWORD = os.environ["PASSWORD"]
MY_EMAIL_ID = os.environ["EMAIL"]
PRICE_LEVEL = 70.39

# give headers to mask the python bot so that it doesn't get blocked or access denied
header = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/547.46 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    "Accept-Language": "en-US,en;q=0.9,bn;q=0.8",
    }
#Get The Product Url
response= requests.get(url=PRODUCT_URL,headers=header)

soup = BeautifulSoup(response.text,"html.parser")
men_shaver = soup.select_one("span[class= 'a-offscreen']").getText()
men_shaver_price = float(men_shaver.strip("$"))
product_title = soup.select_one("span[class='a-size-large product-title-word-break']").getText().strip()

if PRICE_LEVEL>men_shaver_price:
    # Creating a smtp secure sockets layer and logging in:
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as connection:
        connection.login(MY_EMAIL_ID, APP_PASSWORD)
        # sending mail
        connection.sendmail(
            from_addr=MY_EMAIL_ID,
            to_addrs=MY_EMAIL_ID,
            msg=f"Subject:Price Went Down \n\n{product_title}\nPrice has gone down than {PRICE_LEVEL}\n"
                f"Current price is : ${men_shaver_price} "
        )
    print("email sent successfully")
else:
    print("It's Expensive 😒😒😊😊😊😊😊😊")
