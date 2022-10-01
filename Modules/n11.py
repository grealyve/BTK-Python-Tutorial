import requests
from bs4 import BeautifulSoup

url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"
html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.find_all("li", {"class":"column"}, limit=10)

counter = 1

for li in list:

    # name = li.find("div", {"class":"columnContent"}).find("div", {"class":"pro"}).find("h3", {"class":"productName"}).text.strip()
    # price = li.find("div", {"class":"proDetail"}).find("p", {"class":"view-instant-price"}).text

    name = li.div.a.h3.text.strip()
    oldPrice = li.find("div", {"class":"proDetail"}).find_all("span")[0].text.strip().strip("TL")
    newPrice = li.find("div", {"class":"proDetail"}).find_all("span")[1].text.strip().strip().strip("TL")

    print(f"{counter}-Model: {name.ljust(50)} | Fiyatı: {oldPrice} yerine sadece {newPrice}")

    counter += 1



