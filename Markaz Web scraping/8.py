import os
import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup
options = webdriver.ChromeOptions()
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 15)

driver.get("https://www.shop.markaz.app/explore/supplier/605")
time.sleep(5)

os.makedirs("images", exist_ok=True)
all_data = []

# Loop through first 3 pages
for page in range(1, 4):
    print(f"\n🔄 Page {page}")
    time.sleep(3)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/explore/product/']")
    links = list({a.get_attribute("href") for a in products if "/explore/product/" in a.get_attribute("href")})

    for link in links:
        try:
            driver.get(link)
            time.sleep(3)

            title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))).text.strip()
            print(f"📦 {title}")

            try:
                price = driver.find_element(By.XPATH, "//h2[contains(text(),'Rs')]").text.strip()
            except:
                price = "N/A"

            try:
                description = driver.find_element(By.XPATH, "//div[contains(@class,'text-gray-600')]").text.strip()
            except:
                description = "N/A"

            product_code = link.split('/')[-1]

            # Download main image
            try:
                img = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[src*='product']")))
                img_url = img.get_attribute("src")
                img_data = requests.get(img_url).content
                with open(f"images/{product_code}.jpg", 'wb') as f:
                    f.write(img_data)
                print(f"📷 Image saved: {product_code}.jpg")
            except:
                print("❌ Image not found")

            all_data.append({
                "Title": title,
                "Price": price,
                "Description": description,
                "Product Code": product_code,
                "Link": link
            })

        except Exception as e:
            print("❌ Error extracting product:", e)
            continue

    if page < 3:
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Next']")))
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(5)
        except:
            print("🚫 Couldn't click 'Next' button.")
            break

driver.quit()

# Save to Excel
df = pd.DataFrame(all_data)
df.to_excel("markaz_products.xlsx", index=False)
print("\n✅ Excel file saved: markaz_products.xlsx")
