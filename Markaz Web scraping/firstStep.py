
# #grok code
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException, WebDriverException
# import pandas as pd
# import logging

# # Setup logging
# logging.basicConfig(filename="scraper.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Initialize ChromeDriver
# try:
#     service = Service()  # Specify path to chromedriver if not in PATH
#     driver = webdriver.Chrome(service=service)
#     driver.get("https://www.shop.markaz.app/explore/supplier/605")
#     wait = WebDriverWait(driver, 10)
# except WebDriverException as e:
#     logging.error(f"Failed to initialize ChromeDriver: {e}")
#     exit(1)

# # List to store scraped data
# data = set()  # Use set to avoid duplicates

# # Function to scroll and load all products
# def load_all_products():
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#         try:
#             wait.until(lambda d: d.execute_script("return document.body.scrollHeight") > last_height)
#             last_height = driver.execute_script("return document.body.scrollHeight")
#         except TimeoutException:
#             break  # No more content to load

# # Navigate to page 4
# try:
#     for _ in range(3):  # Click "Next" 3 times to reach page 4
#         next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next')]")))
#         driver.execute_script("arguments[0].click();", next_button)
#         wait.until(EC.staleness_of(next_button))  # Wait for page to refresh
# except TimeoutException as e:
#     logging.error(f"Failed to navigate to page 4: {e}")
#     driver.quit()
#     exit(1)

# # Scrape pages 4 to 10
# for page in range(4, 11):
#     print(f"\n--- Page {page} ---")
#     try:
#         # Scroll to load all products
#         load_all_products()

#         # Get products
#         products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href*='/explore/product/']")))
#         for product in products:
#             try:
#                 # Adjust selector based on DOM (inspect the website)
#                 title = product.find_element(By.CSS_SELECTOR, "span, div, p").text.strip()
#                 link = product.get_attribute("href")
#                 if title and link:
#                     product_data = (title, link)
#                     if product_data not in data:
#                         data.add(product_data)
#                         print(f"Title: {title}\nLink: {link}\n")
#             except Exception as e:
#                 logging.warning(f"Error extracting product on page {page}: {e}")
#                 continue

#         # Navigate to next page if not on page 10
#         if page < 10:
#             try:
#                 next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next')]")))
#                 driver.execute_script("arguments[0].click();", next_button)
#                 wait.until(EC.staleness_of(next_button))  # Wait for page to refresh
#             except TimeoutException as e:
#                 logging.info(f"No next button found on page {page}: {e}")
#                 break
#     except Exception as e:
#         logging.error(f"Error on page {page}: {e}")
#         break

# # Close driver
# driver.quit()

# # Save data to Excel
# try:
#     df = pd.DataFrame(list(data), columns=["Title", "Link"])
#     df.to_excel("markaz_products.xlsx", index=False)
#     print("✅ Data saved to markaz_products.xlsx")
# except Exception as e:
#     logging.error(f"Failed to save data to Excel: {e}")

















    #chatgpt code 










from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import pandas as pd
import logging
import time

# --- Setup logging ---
logging.basicConfig(filename="scraper.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# --- Start Chrome browser ---
try:
    service = Service()  # Specify chromedriver path here if needed
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.shop.markaz.app/explore/supplier/605")
    wait = WebDriverWait(driver, 10)
except WebDriverException as e:
    logging.error(f"❌ ChromeDriver start error: {e}")
    exit(1)

# --- Collect data ---
data = set()  # Using set to avoid duplicates

# --- Scroll to bottom to load all products on the page ---
def scroll_to_load_all():
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)  # Wait for loading
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# --- Navigate to Page 4 ---
try:
    for i in range(3):  # Click Next 3 times
        next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Next')]")))
        driver.execute_script("arguments[0].click();", next_btn)
        wait.until(EC.staleness_of(next_btn))  # Wait for page reload
except TimeoutException as e:
    logging.error(f"❌ Could not reach page 4: {e}")
    driver.quit()
    exit(1)

# --- Scrape from Page 4 to 10 ---
for page in range(4, 11):
    print(f"\n🔄 Scraping Page {page}...")
    try:
        scroll_to_load_all()

        # Find all product links
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href*='/explore/product/']")))
        for product in products:
            try:
                title = product.text.strip()
                link = product.get_attribute("href")
                if title and link:
                    product_data = (title, link)
                    if product_data not in data:
                        data.add(product_data)
                        print(f"✅ Title: {title}\n🔗 Link: {link}\n")
            except Exception as e:
                logging.warning(f"⚠️ Error reading product on page {page}: {e}")
                continue

        # Go to next page if page < 10
        if page < 10:
            try:
                next_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Next')]")))
                driver.execute_script("arguments[0].click();", next_btn)
                wait.until(EC.staleness_of(next_btn))
            except TimeoutException as e:
                logging.warning(f"⚠️ No Next button on page {page}: {e}")
                break

    except Exception as e:
        logging.error(f"❌ Error on page {page}: {e}")
        break

# --- Close browser ---
driver.quit()

# --- Save to Excel ---
try:
    df = pd.DataFrame(list(data), columns=["Title", "Link"])
    df.to_excel("markaz_products.xlsx", index=False)
    print("✅ Data saved successfully to markaz_products.xlsx")
except Exception as e:
    logging.error(f"❌ Failed to save Excel: {e}")
