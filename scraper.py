import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin

# Store all scraped data
data = []

# Scrape pages 1 to 50
for page in range(1, 51):

    # Create URL
    if page == 1:
        url = "https://books.toscrape.com/"
    else:
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"

    print(f"Scraping page {page}...")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Error scraping page {page}: {e}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

   

    # Find all books
    books = soup.select("article.product_pod")

    # Extract each book
    for book in books:

        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip()
        availability = book.select_one(".availability").text.strip()
        rating = book.p["class"][1]
        book_url = urljoin(url, book.h3.a["href"])

        data.append({ 
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Availability": availability,
        "URL": book_url
   })
# Create DataFrame
df = pd.DataFrame(data)

# Clean price
df["Price"] = df["Price"].str.replace(
    r"[^\d.]", "", regex=True
).astype(float)

# Convert rating to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating"] = df["Rating"].map(rating_map)

# Display dataset information
print("\nTotal books scraped:", len(df))

print("\nFirst 5 records:")
print(df.head())

# Save dataset
df.to_csv("books_dataset.csv", index=False)

print("\nDataset saved successfully!")