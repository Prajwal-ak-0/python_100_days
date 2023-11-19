import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.moneycontrol.com/stocksmarketsindia/")
soup = BeautifulSoup(response.text, "html.parser")

div_with_classes = soup.find('div', class_='tbl_redtxt')

if div_with_classes:
    print(div_with_classes.string)
else:
    print("Div with class 'tbl_redtxt' not found.")
