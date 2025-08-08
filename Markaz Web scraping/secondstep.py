import os
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException
import logging
import re
import random

# Setup logging
logging.basicConfig(filename="product_code_scraper.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize ChromeDriver with headless mode
try:
    service = Service()  # Specify path to chromedriver if not in PATH
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(service=service, options=options)
except WebDriverException as e:
    logging.error(f"Failed to initialize ChromeDriver: {e}")
    exit(1)

# Load the Excel file
try:
    df = pd.read_excel("markaz_products.xlsx")
except FileNotFoundError:
    logging.error("markaz_products.xlsx not found")
    driver.quit()
    exit(1)

# List to store product codes
product_codes = []

# Loop through each row
for index, row in df.iterrows():
    title = str(row['Title'])
    link = row['Link']
    print(f"🔍 Processing: {title}")

    try:
        driver.get(link)
        # Wait for product code element to load
        code_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'Product Code')]"))
        )
        full_text = code_element.text.strip()
        
        # Extract code using regex for robustness
        match = re.search(r"Product Code:?\s*(\w+)", full_text)
        code = match.group(1) if match else ""
        
        if code:
            print(f"✅ Code found: {code}")
        else:
            print(f"⚠️ No valid code found for {title}")
        product_codes.append(code)

    except TimeoutException:
        logging.warning(f"Timeout: Product code element not found for {link}")
        print(f"❌ Timeout: Product code not found for {title}")
        product_codes.append("")
    except NoSuchElementException:
        logging.warning(f"Element not found for {link}")
        print(f"❌ Element not found for {title}")
        product_codes.append("")
    except Exception as e:
        logging.error(f"Error processing {link}: {e}")
        print(f"❌ Error: {e}")
        product_codes.append("")
    
    # Random delay to avoid rate limiting
    time.sleep(random.uniform(0.5, 1.5))

# Close browser
driver.quit()

# Add product codes to DataFrame
df["Product Code"] = product_codes

# Save to new Excel file
try:
    df.to_excel("markaz_products_with_codes.xlsx", index=False)
    print("📁 Saved as markaz_products_with_codes.xlsx")
except Exception as e:
    logging.error(f"Failed to save Excel file: {e}")
    print(f"❌ Error saving Excel: {e}")