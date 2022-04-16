import smtplib
import os
from datetime import date
from mortgage_rates import get_mortgage_rates
from market_indices import get_market_data

# Get today's date and format it as Month Day, Year
# pulling environment variables and assigning them to python variables
today = date.today()
formatted_day = today.strftime("%B %d, %Y")
sender_email_address = os.getenv('sender_email_address')
email_password = os.getenv('email_password')
receiver_email_address = os.getenv('receiver_email_address')

# If today's date is a Monday - Friday it sends an email using gmail with market and mortgage data. 
if today.weekday() in [0,1,2,3,4]:
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(sender_email_address, email_password)

        subject = f"Daily Dose of Data for {formatted_day}"
        body = f'Market Data:\n{get_market_data()}\nMortgage Data:\n{get_mortgage_rates()}'

        email = f'Subject: {subject}\n\n{body}'
        smtp.sendmail(sender_email_address, receiver_email_address, email)