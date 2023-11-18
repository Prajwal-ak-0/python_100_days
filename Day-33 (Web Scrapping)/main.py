import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.cricbuzz.com/cricket-scores/75413/eng-vs-nz-1st-match-icc-cricket-world-cup-2023")

soup = BeautifulSoup(response.text, "html.parser")

div_with_classes = soup.find('div', class_='cb-col cb-col-100 cb-min-tm cb-text-gray')

print(div_with_classes.string)
