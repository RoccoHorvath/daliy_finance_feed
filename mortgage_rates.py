from bs4 import BeautifulSoup
import requests
from datetime import date

# The function scrapes mortgagenewsdaily.com Monday - Thursday to obtain today's mortgage rates
def get_mortgage_rates():
    today = date.today()
    if today.weekday() in [0,1,2,3]:
        html_text = requests.get('https://www.mortgagenewsdaily.com/mortgage-rates/mnd')

        soup = BeautifulSoup(html_text.text, 'lxml')
        table = soup.find('table', class_='table table-hover mtg-rates')
        mortgage_data = ""
        for product in table.find_all('tbody'):
            rows = product.find_all('tr')
            for row in rows:
                product_name = row.find('th').text.strip()
                current_rate = row.find('td').text.strip()
                daily_change = row.find('td', class_ = 'text-center change').text.strip()
                mortgage_data = mortgage_data + f"{product_name}: {current_rate} | Daily change: {daily_change}\n"
        return mortgage_data

    else:
        mortgage_data = "No mortgage data today"
        return mortgage_data