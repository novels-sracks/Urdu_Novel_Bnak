# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time

# # Launch Chrome browser
# driver = webdriver.Chrome()

# # Open the supplier page
# driver.get("https://www.shop.markaz.app/explore/supplier/605")
# time.sleep(5)  # Let the page load

# # Scroll to load more products
# for i in range(5):  # Adjust as needed
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

# # Find product cards (adjust CSS selector as per actual site)
# products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/explore/product/']")

# # Extract info
# for product in products:
#     link = product.get_attribute("href")
#     title = product.text.strip()
#     if title:
#         print(f"Title: {title}\nLink: {link}\n")

# driver.quit()






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.action_chains import ActionChains
# import time

# # Setup Chrome driver
# driver = webdriver.Chrome()

# # Go to supplier page
# driver.get("https://www.shop.markaz.app/explore/supplier/605")
# time.sleep(5)

# # Loop through first 3 pages
# for page in range(1, 4):
#     print(f"\n--- Page {page} ---")
#     time.sleep(3)

#     # Scroll to bottom to trigger product load
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

#     # Extract products
#     products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/explore/product/']")
#     for product in products:
#         title = product.text.strip()
#         link = product.get_attribute("href")
#         if title:
#             print(f"Title: {title}\nLink: {link}\n")

#     # Click "Next" for next page, except after page 3
#     if page < 3:
#         try:
#             next_button = driver.find_element(By.XPATH, "//button[contains(text(),'Next')]")
#             driver.execute_script("arguments[0].click();", next_button)
#         except Exception as e:
#             print("Couldn't click Next:", e)
#             break

# driver.quit()







from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Start Chrome
driver = webdriver.Chrome()
driver.get("https://www.shop.markaz.app/explore/supplier/605")
wait = WebDriverWait(driver, 10)
time.sleep(5)

# Loop through first 3 pages
for page in range(1,2):
    print(f"\n--- Page {page} ---")
    time.sleep(3)

    # Scroll to bottom to load products
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

    # Get products
    products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/explore/product/']")
    for product in products:
        title = product.text.strip()
        link = product.get_attribute("href")
        if title:
            print(f"Title: {title}\nLink: {link}\n")

    # Click Next (only for page 1 and 2)
    if page < 3:
        try:
            # Wait for and click the "Next" <a> tag
            next_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[text()='Next']")
            ))
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(5)
        except Exception as e:
            print("Couldn't click Next:", e)
            break

driver.quit()
