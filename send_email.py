import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from datetime import date
from mortgage_rates import get_mortgage_rates
from market_indices import get_market_data
from conf import perform_get_market_data, perform_get_mortgage_data
from HTML import create_stock_table

# Get today's date and format it as Month Day, Year
# pulling environment variables and assigning them to python variables
today = date.today()
formatted_day = today.strftime("%B %d, %Y")
sender_email_address = os.getenv('sender_email_address')
email_password = os.getenv('email_password')
receiver_email_address = os.getenv('receiver_email_address')
stock_data , mortgage_data = "" , ""

# If today's date is a Monday - Friday it sends an email using gmail with market and mortgage data. 
if today.weekday() in [0,1,2,3,4]:
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Daily Dose of Data for {formatted_day}"
    msg['From'] = sender_email_address
    msg['To'] = receiver_email_address

# the below if statemnets check whether the varibles on the conf.py file are true
# adds html code to html variable and attaches to msg
    if perform_get_market_data:
        stock_data = get_market_data()
        market_table = create_stock_table(stock_data)
    
    if perform_get_mortgage_data:
        mortgage_data = get_mortgage_rates()

    html = market_table + str(mortgage_data)
    msg.attach(MIMEText(html, 'html'))

#sign into gmail and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email_address, email_password)
        smtp.sendmail(sender_email_address, receiver_email_address, msg.as_string())
        smtp.quit()
