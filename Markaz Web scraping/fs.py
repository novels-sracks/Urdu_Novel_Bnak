from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import logging
import time

# Setup logging
logging.basicConfig(filename="scraper.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Initialize ChromeDriver
try:
    print("Initializing ChromeDriver...")
    service = Service(ChromeDriverManager().install())  # Auto-install ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Keep browser open
    driver = webdriver.Chrome(service=service, options=options)
    print("Navigating to supplier page...")
    driver.get("https://www.shop.markaz.app/explore/supplier/605")
    time.sleep(2)  # Wait for JavaScript to load
    wait = WebDriverWait(driver, 10)
    print("Page loaded successfully.")
except WebDriverException as e:
    logging.error(f"Failed to initialize ChromeDriver: {e}")
    print(f"Error: Failed to initialize ChromeDriver: {e}")
    exit(1)

# List to store scraped data
data = set()

# Function to scroll and load all products
def load_all_products():
    print("Scrolling to load products...")
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            wait.until(lambda d: d.execute_script("return document.body.scrollHeight") > last_height)
            last_height = driver.execute_script("return document.body.scrollHeight")
        except TimeoutException:
            print("No more content to load.")
            break

# Navigate to page 4
try:
    print("Navigating to page 4...")
    for i in range(3):
        print(f"Clicking 'Next' button (attempt {i+1}/3)...")
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next')]")))
        driver.execute_script("arguments[0].click();", next_button)
        wait.until(EC.staleness_of(next_button))
        print(f"Navigated to page {i+2}")
except TimeoutException as e:
    logging.warning(f"Failed to navigate to page 4: {e}")
    print(f"Warning: Could not navigate to page 4: {e}. Proceeding with current page.")

# Scrape pages 4 to 10
for page in range(4, 11):
    print(f"\n--- Scraping Page {page} ---")
    try:
        load_all_products()
        print("Extracting products...")
        products = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href*='/explore/product/']")))
        print(f"Found {len(products)} products on page {page}")
        for product in products:
            try:
                title = product.find_element(By.CSS_SELECTOR, ".product-title").text.strip()  # Replace with correct selector
                link = product.get_attribute("href")
                if title and link:
                    product_data = (title, link)
                    if product_data not in data:
                        data.add(product_data)
                        print(f"Title: {title}\nLink: {link}\n")
            except Exception as e:
                logging.warning(f"Error extracting product on page {page}: {e}")
                continue

        if page < 10:
            try:
                print(f"Attempting to navigate to page {page+1}...")
                next_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next')]")))
                driver.execute_script("arguments[0].click();", next_button)
                wait.until(EC.staleness_of(next_button))
            except TimeoutException as e:
                logging.info(f"No next button found on page {page}: {e}")
                print(f"No next button found on page {page}. Stopping.")
                break
    except Exception as e:
        logging.error(f"Error on page {page}: {e}")
        print(f"Error on page {page}: {e}")
        break

# Close driver
driver.quit()
print("Browser closed.")

# Save data to Excel
try:
    print("Saving data to Excel...")
    df = pd.DataFrame(list(data), columns=["Title", "Link"])
    df.to_excel("markaz_products.xlsx", index=False)
    print("✅ Data saved to markaz_products.xlsx")
except Exception as e:
    logging.error(f"Failed to save data to Excel: {e}")
    print(f"Error saving to Excel: {e}")