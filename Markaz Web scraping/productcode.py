import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Load the Excel file
df = pd.read_excel("markaz_products.xlsx")

# Start Chrome browser
driver = webdriver.Chrome()

# List to store product codes
product_codes = []

# Loop through each row
for index, row in df.iterrows():
    title = str(row['Title'])
    link = row['Link']
    print(f"🔍 Processing: {title}")

    try:
        driver.get(link)
        time.sleep(3)  # Let the page load

        # Find the span containing product code
        code_element = driver.find_element(By.XPATH, "//span[contains(text(),'Product Code')]")
        full_text = code_element.text.strip()  # e.g., "• Product Code: MZ605200157KIBKSE"

        # Extract only the code part
        if "Product Code:" in full_text:
            code = full_text.split("Product Code:")[-1].strip()
        else:
            code = ""

        product_codes.append(code)
        print(f"✅ Code found: {code}")

    except Exception as e:
        print(f"❌ Error: {e}")
        product_codes.append("")

# Close browser
driver.quit()

# Add product codes to DataFrame
df["Product Code"] = product_codes

# Save to new Excel file
df.to_excel("markaz_products_with_codes.xlsx", index=False)
print("📁 Saved as markaz_products_with_codes.xlsx")
