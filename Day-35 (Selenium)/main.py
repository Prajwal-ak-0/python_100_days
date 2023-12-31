# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# url = 'https://www.amazon.in/s?k=msi&i=software&s=date-desc-rank&crid=ITF9V46IKCNT&qid=1700489416&sprefix=msi%2Csoftware%2C202&ref=sr_st_date-desc-rank&ds=v1%3Awyd9zuNL57ENlKNzgDtIrgSdyfFX0NjlXvY3KcJ9vHQ'
# driver.get(url)
#
# # Wait for the page to load (you might need to adjust the wait time)
# driver.implicitly_wait(10)
#
# # Find all the laptop elements using the specified class
# laptops = driver.find_elements(By.CLASS_NAME, 'a-carousel-card')
#
# print(laptops)
#
# # Loop through each laptop and extract the name and price
# for laptop in laptops:
#     name_element = laptop.find_element(By.CLASS_NAME, 'a-truncate-full')
#     price_element = laptop.find_element(By.CLASS_NAME, 'a-offscreen')
#
#     name = name_element.text
#     price = price_element.text
#
#     print(f"Name: {name}\nPrice: {price}\n{'='*30}")
#
# driver.close()
#
#
# import requests
# from bs4 import BeautifulSoup
#
# url = "https://www.moneycontrol.com/"
# response = requests.get(url)
#
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # Extract data for Nifty
#     nifty_table = soup.find('div', {'id': 'in_tgNifty'}).find('table', {'class': 'rhsglTbl'})
#     print("Top Gainers - Nifty:")
#     print("-" * 50)
#     for row in nifty_table.find('tbody').find_all('tr'):
#         company = row.find('td').find('a').text.strip()
#         price = row.find_all('td')[1].text.strip()
#         change = row.find_all('td')[2].text.strip()
#         percent_gain = row.find_all('td')[3].text.strip()
#
#         print(f"Company: {company}")
#         print(f"Price: {price}")
#         print(f"Change: {change}")
#         print(f"% Gain: {percent_gain}")
#         print("-" * 50)
#
#     # Extract data for Sensex
#     sensex_table = soup.find('div', {'id': 'in_tgSensex'}).find('table', {'class': 'rhsglTbl'})
#     print("Top Gainers - Sensex:")
#     print("-" * 50)
#     for row in sensex_table.find('tbody').find_all('tr'):
#         company = row.find('td').find('a').text.strip()
#         price = row.find_all('td')[1].text.strip()
#         change = row.find_all('td')[2].text.strip()
#         percent_gain = row.find_all('td')[3].text.strip()
#
#         print(f"Company: {company}")
#         print(f"Price: {price}")
#         print(f"Change: {change}")
#         print(f"% Gain: {percent_gain}")
#         print("-" * 50)
# else:
#     print(f"Failed to fetch data. Status code: {response.status_code}")
import pandas
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
#
# url = "https://www.python.org/"
#
# driver.get(url)
#
# # Find the element using the class name
# about_link = driver.find_element(By.CLASS_NAME, 'shrubbery')
#
# print(about_link.text)
# list_items = about_link.find_elements(By.TAG_NAME, 'li')
#
# # Iterate through each list item and extract the event name
# for item in list_items:
#     event_name = item.find_element(By.TAG_NAME, 'a').text
#     print("Event Name:", event_name)
#
# # Close the WebDriver
# driver.quit()

# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
# url = "https://www.5paisa.com/ipo/ipo-gmp"
# driver.get(url)
#
# # Find the table element
# table = driver.find_element(By.CLASS_NAME, "table.subs-stat-tabletable.subs-stat-table")
#
# # Extract header texts
# headers = table.find_elements(By.TAG_NAME, "th")
# header_texts = [header.text for header in headers]
#
# # Extract data from the table
# data_rows = []
# rows = table.find_elements(By.XPATH, "//tbody/tr")
# for row in rows:
#     cells = row.find_elements(By.TAG_NAME, "td")
#     row_data = [cell.text for cell in cells]
#     data_rows.append(row_data)
#
# # Create a DataFrame using pandas
# df = pd.DataFrame(data_rows, columns=header_texts)
#
# # Replace the rupee symbol in relevant columns
# df["IPO Price Range"] = df["IPO Price Range"].str.replace("₹", "Rs. ")
# df["IPO GMP"] = df["IPO GMP"].str.replace("₹", "Rs. ")
#
# # Save DataFrame to a CSV file
# df.to_csv("ipo.csv", index=False)

# info = pandas.read_csv("ipo.csv")
# print(info)


# driver.quit()


from twilio.rest import Client
import pandas as pd

# Twilio credentials
account_sid = 'AC125ef8a4d23928f3ba8272dd134e7820'
auth_token = '6ce89e2f0c701732cc6fc6ec23e9e1f7'
twilio_client = Client(account_sid, auth_token)

# Read the CSV file
df = pd.read_csv("nift.csv")

# Extract relevant information
message_body = "NIFTY 50 Information:\n\n" + df.to_string(index=False)

# Twilio message details
from_number = '+12512410520'
to_number = '+918310260149'

# Send the entire message in one go
message = twilio_client.messages.create(
    body=message_body,
    from_=from_number,
    to=to_number
)

print("Message SID:", message.sid)






# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# url = "https://www.wikipedia.org/"
#
# driver.get(url)
#
# # Find the element using the class name
# search_field = driver.find_element(By.ID, "searchInput")
#
# # Enter the search keyword and submit
# search_field.send_keys("FIFA World Cup")
# search_field.submit()
#
# # Find the element using the class name
# # the div has this class name : mw-content-ltr mw-parser-output, I want you extract all the <p> tags from this div
# search_results = driver.find_element(By.CLASS_NAME, "mw-content-ltr.mw-parser-output")
#
# # Extract all the paragraphs
# results = search_results.find_elements(By.TAG_NAME, "p")
#
# # Print the text from all the paragraphs
# for result in results:
#     print(result.text)
#
# # Close the WebDriver
#
# driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Assuming you have a WebDriver set up (e.g., ChromeDriver)
# driver = webdriver.Chrome()
#
# # Your HTML snippet
# html_snippet = '<div class="u-lineHeightBase postItem"><a href="https://towardsdatascience.com/musicgen-reimagined-metas-under-the-radar-advances-in-ai-music-36c1adfd13b7?source=collection_home---4------0-----------------------" data-action="open-post" data-action-value="https://towardsdatascience.com/musicgen-reimagined-metas-under-the-radar-advances-in-ai-music-36c1adfd13b7?source=collection_home---4------0-----------------------" class="u-block u-xs-height170 u-width600 u-height272  u-backgroundSizeCover u-backgroundOriginBorderBox u-backgroundColorGrayLight u-borderLighter" style="background-image: url(&quot;https://cdn-images-1.medium.com/max/600/1*4m-yjG8mUfJSzpSc7FSO8g.png&quot;); background-position: 50% 50% !important;"><span class="u-textScreenReader">MusicGen Reimagined: Meta’s Under-the-Radar Advances in AI Music</span></a></div>'
#
# # Parse the HTML snippet
# driver.get("data:text/html;charset=utf-8,{html}".format(html=html_snippet))
#
# # Find the image element and extract the image link
# image_element = driver.find_element(By.CSS_SELECTOR, 'div.u-lineHeightBase a.u-block')
# image_link = image_element.value_of_css_property('background-image')
# image_link = image_link.replace('url("', '').replace('")', '')
#
# print("Image Link:", image_link)
#
# # Close the WebDriver
# driver.quit()





# import time
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # Set up the WebDriver (assuming you have ChromeDriver installed)
# driver = webdriver.Chrome()
#
# # Open the URL
# url = "https://www.5paisa.com/share-market-today"
# driver.get(url)
#
# # Function to extract data
# def extract_data():
#     data = []
#     company_info_list = driver.find_elements(By.CSS_SELECTOR, 'div.stock__scraldata div.expand')
#     for company_info in company_info_list:
#         company_name = company_info.find_element(By.XPATH, 'ul/li[1]/a').text
#         market_price = company_info.find_element(By.XPATH, 'ul/li[2]').text
#         market_cap = company_info.find_element(By.XPATH, 'ul/li[3]').text
#         week_high = company_info.find_element(By.XPATH, 'ul/li[4]').text
#
#         data.append({
#             "Company Name": company_name,
#             "Market Price": market_price,
#             "Market Cap": market_cap,
#             "52 Week High": week_high
#         })
#     return data
#
# # Click on the "Load More" button twice
# for _ in range(2):
#     load_more_button = driver.find_element(By.XPATH, '//*[@id="load"]')
#     driver.execute_script("arguments[0].click();", load_more_button)
#     time.sleep(2)  # Wait for the content to load
#
# # Extract data after clicking twice
# final_data = extract_data()
#
# # Create a DataFrame from the scraped data
# df = pd.DataFrame(final_data)
#
# # Save the DataFrame to a CSV file
# df.to_csv("nift.csv", index=False)
#
# # Close the WebDriver
# driver.quit()
