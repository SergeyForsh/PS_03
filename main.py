from bs4 import BeautifulSoup
import requests
url = "http://quotes.toscrape.com/"
response = requests.get(url)
# print(response.content)
html = response.text
soup = BeautifulSoup(html, "html.parser")
links = soup.find_all("a")
for link in links:
    print(link.get('href'))

