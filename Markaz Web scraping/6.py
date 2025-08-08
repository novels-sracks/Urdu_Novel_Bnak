import os
import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# --- Setup ---
folder_name = "product_images"
os.makedirs(folder_name, exist_ok=True)
all_data = []

# Start browser
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://www.shop.markaz.app/explore/supplier/605")
time.sleep(5)

# Loop through first 3 pages
for page in range(1, 2):
    print(f"\n--- Page {page} ---")
    time.sleep(3)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Find all product links
    products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/explore/product/']")
    product_links = list(set([p.get_attribute("href") for p in products if p.text.strip()]))

    for link in product_links:
        try:
            driver.get(link)

            # Wait for title to appear
            try:
                title_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))
                )
                title = title_element.text.strip()
            except TimeoutException:
                print(f"⚠️ Skipping - Title not found for: {link}")
                continue

            # Get price
            try:
                price = driver.find_element(By.XPATH, "//h1/following-sibling::p[1]").text.strip()
            except NoSuchElementException:
                price = "N/A"

            # Get description
            try:
                description = driver.find_element(
                    By.XPATH, "//div[contains(text(), 'Product Description')]/following-sibling::div"
                ).text.strip()
            except NoSuchElementException:
                description = "N/A"

            # Get product code from URL
            product_code = link.split("/")[-1]

            # Download product images
            image_elements = driver.find_elements(By.CSS_SELECTOR, "img[src*='cdn.markaz']")
            img_count = 1
            for img in image_elements:
                img_url = img.get_attribute("src")
                img_ext = img_url.split(".")[-1].split("?")[0]
                img_name = f"{product_code}_{img_count}.{img_ext}"
                img_path = os.path.join(folder_name, img_name)

                try:
                    response = requests.get(img_url)
                    with open(img_path, 'wb') as f:
                        f.write(response.content)
                    print(f"✅ Downloaded image: {img_name}")
                except Exception as e:
                    print(f"❌ Failed to download image: {img_url} | Error: {e}")
                img_count += 1

            # Append data to list
            all_data.append({
                "Title": title,
                "Price": price,
                "Description": description,
                "Product Code": product_code,
                "Product Link": link
            })

        except Exception as e:
            print(f"❌ Failed to extract product: {link} - {e}")
            continue

    # Click "Next" if not last page
    if page < 3:
        driver.get("https://www.shop.markaz.app/explore/supplier/605")
        try:
            next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Next']")))
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(5)
        except Exception as e:
            print("⚠️ Couldn't click Next button:", e)
            break

# Close browser
driver.quit()

# Save data to Excel
df = pd.DataFrame(all_data)
df.to_excel("markaz_products.xlsx", index=False)
print("\n✅ All product data saved to 'markaz_products.xlsx'")
