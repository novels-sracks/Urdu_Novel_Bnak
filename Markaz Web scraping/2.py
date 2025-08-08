import requests
import time

base_url = "https://api.markaz.app/productsv2/v4/supplier/1"
params = {
    "countryCode": "PK",
    "platform": "dropshipping_web"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

def scrape_products():
    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        # Adjust based on API response structure
        products = data.get("products", [])  # Example key, check actual response
        for product in products:
            title = product.get("title", "N/A")
            price = product.get("price", "N/A")
            print(f"Title: {title}, Price: {price}")
    else:
        print(f"Failed to retrieve data: {response.status_code} - {response.text}")

# Run for a single page (adjust for pagination if needed)
scrape_products()