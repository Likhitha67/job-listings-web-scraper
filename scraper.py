import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

url = "https://books.toscrape.com/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error while accessing the website:", e)
    exit()

soup = BeautifulSoup(response.text, "html.parser")

print("Page Title:", soup.title.text)

books = soup.find_all("article", class_="product_pod")

print("Number of books found:", len(books))

data = []

for book in books:
    title_tag = book.h3.a
    price_tag = book.find("p", class_="price_color")

    title = title_tag.get("title", "N/A")
    link = urljoin(url, title_tag.get("href", ""))
    price = price_tag.get_text(strip=True).replace("Â£", "£") if price_tag else "N/A"

    data.append({
        "title": title,
        "link": link,
        "price": price
    })

df = pd.DataFrame(data)

print(df)
df.to_csv("books.csv", index=False)

print("Data saved successfully to books.csv")