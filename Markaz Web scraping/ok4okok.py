# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import pandas as pd

# # Start Chrome
# driver = webdriver.Chrome()
# driver.get("https://www.shop.markaz.app/explore/supplier/605")
# wait = WebDriverWait(driver, 10)
# time.sleep(5)

# # List to store scraped data
# data = []

# # First reach page 4 manually by clicking "Next" 3 times
# for i in range(1, 4):
#     try:
#         next_button = wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//a[text()='Next']")
#         ))
#         driver.execute_script("arguments[0].click();", next_button)
#         print(f"Reached Page {i+1}")
#         time.sleep(5)
#     except Exception as e:
#         print("Couldn't reach Page 4:", e)
#         driver.quit()
#         exit()

# # Now scrape from Page 4 to Page 10
# for page in range(4, 11):  
#     print(f"\n--- Scraping Page {page} ---")
#     time.sleep(3)

#     # Scroll to bottom to load products
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

#     # Get products
#     products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/explore/product/']")
#     for product in products:
#         title = product.text.strip()
#         link = product.get_attribute("href")
#         if title:
#             print(f"Title: {title}\nLink: {link}\n")
#             data.append({"Title": title, "Link": link})

#     if page < 10:
#         try:
#             next_button = wait.until(EC.element_to_be_clickable(
#                 (By.XPATH, "//a[text()='Next']")
#             ))
#             driver.execute_script("arguments[0].click();", next_button)
#             time.sleep(5)
#         except Exception as e:
#             print("Couldn't click Next:", e)
#             break

# # Close browser
# driver.quit()

# # Save data to Excel
# df = pd.DataFrame(data)
# df.to_excel("markaz_products_page4_to_10.xlsx", index=False)
# print("✅ Data saved to markaz_products_page4_to_10.xlsx")






# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import pandas as pd

# # Start Chrome
# driver = webdriver.Chrome()
# driver.get("https://www.shop.markaz.app/explore/supplier/605")
# wait = WebDriverWait(driver, 10)
# time.sleep(5)

# # List to store scraped data
# data = []

# # Reach page 11 manually by clicking "Next" 10 times
# for i in range(1, 11):
#     try:
#         next_button = wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//a[text()='Next']")
#         ))
#         driver.execute_script("arguments[0].click();", next_button)
#         print(f"Reached Page {i+1}")
#         time.sleep(5)
#     except Exception as e:
#         print("Couldn't reach Page 11:", e)
#         driver.quit()
#         exit()

# # Now scrape from Page 11 to Page 30
# for page in range(11, 31):  
#     print(f"\n--- Scraping Page {page} ---")
#     time.sleep(3)

#     # Scroll to bottom to load products
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

#     # Get products
#     products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/explore/product/']")
#     for product in products:
#         title = product.text.strip()
#         link = product.get_attribute("href")
#         if title:
#             print(f"Title: {title}\nLink: {link}\n")
#             data.append({"Title": title, "Link": link})

#     if page < 30:
#         try:
#             next_button = wait.until(EC.element_to_be_clickable(
#                 (By.XPATH, "//a[text()='Next']")
#             ))
#             driver.execute_script("arguments[0].click();", next_button)
#             time.sleep(5)
#         except Exception as e:
#             print("Couldn't click Next:", e)
#             break

# # Close browser
# driver.quit()

# # Save data to Excel
# df = pd.DataFrame(data)
# df.to_excel("markaz_products_page11_to_30.xlsx", index=False)
# print("✅ Data saved to markaz_products_page11_to_30.xlsx")











# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import pandas as pd

# # Start Chrome
# driver = webdriver.Chrome()
# driver.get("https://www.shop.markaz.app/explore/supplier/605")
# wait = WebDriverWait(driver, 10)
# time.sleep(5)

# # List to store scraped data
# data = []

# # Reach page 31 manually by clicking "Next" 30 times
# for i in range(1, 31):
#     try:
#         next_button = wait.until(EC.element_to_be_clickable(
#             (By.XPATH, "//a[text()='Next']")
#         ))
#         driver.execute_script("arguments[0].click();", next_button)
#         print(f"Reached Page {i+1}")
#         time.sleep(5)
#     except Exception as e:
#         print("Couldn't reach Page 31:", e)
#         driver.quit()
#         exit()

# # Now scrape from Page 31 to Page 50
# for page in range(31, 51):  
#     print(f"\n--- Scraping Page {page} ---")
#     time.sleep(3)

#     # Scroll to bottom to load products
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(3)

#     # Get products
#     products = driver.find_elements(By.CSS_SELECTOR, "a[href*='/explore/product/']")
#     for product in products:
#         title = product.text.strip()
#         link = product.get_attribute("href")
#         if title:
#             print(f"Title: {title}\nLink: {link}\n")
#             data.append({"Title": title, "Link": link})

#     if page < 50:
#         try:
#             next_button = wait.until(EC.element_to_be_clickable(
#                 (By.XPATH, "//a[text()='Next']")
#             ))
#             driver.execute_script("arguments[0].click();", next_button)
#             time.sleep(5)
#         except Exception as e:
#             print("Couldn't click Next:", e)
#             break

# # Close browser
# driver.quit()

# # Save data to Excel
# df = pd.DataFrame(data)
# df.to_excel("markaz_products_page31_to_50.xlsx", index=False)
# print("✅ Data saved to markaz_products_page31_to_50.xlsx")







from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Start Chrome
driver = webdriver.Chrome()
driver.get("https://www.shop.markaz.app/explore/supplier/605")
wait = WebDriverWait(driver, 10)
time.sleep(5)

# List to store scraped data
data = []

# Reach page 51 manually by clicking "Next" 50 times
for i in range(1, 51):
    try:
        next_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//a[text()='Next']")
        ))
        driver.execute_script("arguments[0].click();", next_button)
        print(f"Reached Page {i+1}")
        time.sleep(5)
    except Exception as e:
        print("❌ Couldn't reach Page 51:", e)
        driver.quit()
        exit()

# Now scrape from Page 51 to Page 73
for page in range(51, 74):  
    print(f"\n--- Scraping Page {page} ---")
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
            data.append({"Title": title, "Link": link})

    if page < 73:
        try:
            next_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[text()='Next']")
            ))
            driver.execute_script("arguments[0].click();", next_button)
            time.sleep(5)
        except Exception as e:
            print("❌ Couldn't click Next on page", page, ":", e)
            break

# Close browser
driver.quit()

# Save data to Excel
df = pd.DataFrame(data)
df.to_excel("markaz_products_page51_to_73.xlsx", index=False)
print("✅ Data saved to markaz_products_page51_to_73.xlsx")
