import os
import time
import re
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# === Utility to clean filename ===
def clean_filename(title):
    title = re.sub(r'[\\/*?:"<>|]', "", title)
    title = title.replace("\n", " ").strip()
    return title[:50]

# === Load Excel file with product links ===
df = pd.read_excel("markaz_products.xlsx")

# === Folder to save images ===
image_folder = ""
os.makedirs(image_folder, exist_ok=True)

# === Start Selenium WebDriver ===
driver = webdriver.Chrome()

# === List for product codes ===
product_codes = []

# === Process each product ===
for index, row in df.iterrows():
    product_title = str(row['Title'])
    product_link = row['Link']
    print(f"\n🔍 Processing: {product_title}")

    code = ""
    image_url = ""

    try:
        # Open product page
        driver.get(product_link)
        time.sleep(3)

        # --- Scrape product code ---
        try:
            code_element = driver.find_element(By.XPATH, "//span[contains(text(),'Product Code')]")
            full_text = code_element.text.strip()
            if "Product Code:" in full_text:
                code = full_text.split("Product Code:")[-1].strip()
                print(f"✅ Product Code: {code}")
        except Exception as e:
            print(f"⚠️ Product code not found: {e}")

        # --- Scrape product image ---
        try:
            image_element = driver.find_element(By.CSS_SELECTOR, "img")
            image_url = image_element.get_attribute("src")
            if image_url:
                filename = f"{clean_filename(product_title)}.jpg"
                filepath = os.path.join(image_folder, filename)

                response = requests.get(image_url)
                with open(filepath, "wb") as f:
                    f.write(response.content)
                print(f"🖼️ Image saved: {filename}")
        except Exception as e:
            print(f"⚠️ Image not saved: {e}")

    except Exception as e:
        print(f"❌ Error processing product: {e}")

    # Add product code to list
    product_codes.append(code)

# Add product code column to DataFrame
df["Product Code"] = product_codes

# Save final Excel file
df.to_excel("markaz_products_with_images_and_codes-51 to 73.xlsx", index=False)
print("\n📁 Data saved to markaz_products_with_images_and_codes.xlsx")

# Close browser
driver.quit()
print("✅ Scraping complete.")
