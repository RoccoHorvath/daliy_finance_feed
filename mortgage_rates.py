from bs4 import BeautifulSoup
import requests

# The function pulls a table from mortgagenewsdaily.com with today's mortgage rates
def get_mortgage_rates():
    html_text = requests.get('https://www.mortgagenewsdaily.com/mortgage-rates/mnd')
    soup = BeautifulSoup(html_text.text, 'lxml')
    mortgage_table = soup.find('table', class_='table table-hover mtg-rates')
    return mortgage_table
