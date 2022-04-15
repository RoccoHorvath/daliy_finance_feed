from bs4 import BeautifulSoup
import requests
import smtplib
import os
from datetime import date

today = date.today()
today = today.strftime("%B %d, %Y")
html_text = requests.get('https://www.mortgagenewsdaily.com/mortgage-rates/mnd')

soup = BeautifulSoup(html_text.text, 'lxml')
table = soup.find('table', class_='table table-hover mtg-rates')
msg = ""
for product in table.find_all('tbody'):
    rows = product.find_all('tr')
    for row in rows:
        product_name = row.find('th').text.strip()
        current_rate = row.find('td').text.strip()
        daily_change = row.find('td', class_ = 'text-center change').text.strip()
        msg = msg + f"\n{product_name}: {current_rate} | Daily change: {daily_change}"

sender_email_address = os.getenv('sender_email_address')
email_password = os.getenv('email_password')
receiver_email_address = os.getenv('receiver_email_address')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(sender_email_address, email_password)

    subject = f"Mortgage Rates for {today}"
    body = msg

    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(sender_email_address, receiver_email_address, msg)