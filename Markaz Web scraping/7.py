import os
import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
driver = webdriver.Chrome()
driver.get("https://www.shop.markaz.app/explore/supplier/605")
wait = WebDriverWait(driver, 10)
time.sleep(5)

# Folder for images
os.makedirs("images", exist_ok=True)

data = []

# Loop through first 3 pages
for page in range(1, 2):
    print(f"\n--- Page {page} ---")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Find all product links
    product_links = driver.find_elements(By.CSS_SELECTOR, "a[href*='/explore/product/']")
    links_seen = set()
    
    for link_element in product_links:
        link = link_element.get_attribute("href")
        if not link or link in links_seen:
            continue
        links_seen.add(link)

        driver.execute_script("window.open(arguments[0]);", link)
        driver.switch_to.window(driver.window_handles[-1])

        try:
            time.sleep(4)
            title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))).text.strip()
            
            try:
                price = driver.find_element(By.XPATH, "//h2[contains(text(),'Rs')]").text.strip()
            except:
                price = "N/A"

            try:
                description = driver.find_element(By.XPATH, "//div[contains(@class,'text-gray-600')]").text.strip()
            except:
                description = "N/A"

            try:
                product_code = link.split('/')[-1]
            except:
                product_code = "Unknown"

            # Download image
            try:
                img = driver.find_element(By.CSS_SELECTOR, "img[src*='product']")
                img_url = img.get_attribute("src")
                img_data = requests.get(img_url).content
                with open(f"images/{product_code}.jpg", 'wb') as f:
                    f.write(img_data)
            except Exception as e:
                print("Image not found:", e)

            print(f"Title: {title}\nPrice: {price}\nCode: {product_code}\n")
            data.append({
                "Title": title,
                "Price": price,
                "Description": description,
                "Product Code": product_code,
                "Link": link
            })

        except Exception as e:
            print("Error extracting product:", e)

        driver.close()
        driver.switch_to.window(driver.window_handles[0])

    if page < 3:
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Next']")))
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(5)
        except Exception as e:
            print("Couldn't click Next:", e)
            break

driver.quit()

# Save to Excel
df = pd.DataFrame(data)
df.to_excel("markaz_products.xlsx", index=False)
print("\n✅ Data saved to markaz_products.xlsx")
