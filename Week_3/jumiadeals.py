# Jumia Deals Scraper (Beginner Friendly)
# This script goes to the Jumia Flash Sales page
# and collects product details like Name, Brand, Price, Discount, Reviews, and Rating.
# Finally, it saves the results into a CSV file.

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.jumia.co.ke/flash-sales/"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("Page loaded successfully!")
else:
    print("Error:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("article", class_="prd")


all_products = []

for item in products:
    # Product name
    name = item.get("data-name")
    if not name:
        name = None
    
    # Brand name
    brand = item.get("data-brand")
    if not brand:
        brand = None
    
    # Price
    price_tag = item.find("div", class_="prc")
    price = price_tag.text.strip() if price_tag else None
    
    # Discount (if any)
    discount_tag = item.find("div", class_="bdg _dsct")
    discount = discount_tag.text.strip() if discount_tag else "0%"
    
    # Reviews (if available)
    reviews_tag = item.find("div", class_="rev")
    reviews = reviews_tag.text.strip() if reviews_tag else "0"
    
    # Rating (stars)
    rating_tag = item.find("div", class_="stars")
    rating = rating_tag.text.strip() if rating_tag else None
    
    # Save product info into our list
    all_products.append({
        "Product Name": name,
        "Brand": brand,
        "Price (Ksh)": price,
        "Discount": discount,
        "Reviews": reviews,
        "Rating": rating
    })

# Step 9: Turn the list into a DataFrame
df = pd.DataFrame(all_products)

# Step 10: Save everything into a CSV file
df.to_csv("jumia_deals.csv", index=False, encoding="utf-8")

print("Done! All products have been saved into jumia_deals.csv")

