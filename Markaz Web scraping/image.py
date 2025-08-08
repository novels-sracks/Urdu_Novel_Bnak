# import os
# import time
# import pandas as pd
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By

# # Load Excel file
# df = pd.read_excel("markaz_products.xlsx")

# # Create folder for images
# image_folder = "product_images"
# os.makedirs(image_folder, exist_ok=True)

# # Start Selenium
# driver = webdriver.Chrome()

# # Loop through product links
# for index, row in df.iterrows():
#     product_title = row['Title']
#     product_link = row['Link']
#     print(f"Processing: {product_title}")

#     try:
#         driver.get(product_link)
#         time.sleep(3)  # Wait for page to load

#         # Find image (you may adjust the selector if it changes)
#         image_element = driver.find_element(By.CSS_SELECTOR, "img")
#         image_url = image_element.get_attribute("src")

#         if image_url:
#             # Create valid filename
#             filename = f"{product_title[:50].strip().replace('/', '-')}.jpg"
#             filepath = os.path.join(image_folder, filename)

#             # Download and save the image
#             response = requests.get(image_url)
#             with open(filepath, "wb") as f:
#                 f.write(response.content)

#             print(f"✅ Saved: {filename}")

#     except Exception as e:
#         print(f"❌ Error processing {product_link}: {e}")

# # Close browser
# driver.quit()
# print("✅ All images downloaded.")

import os
import time
import re
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

# === Utility to clean filename ===
def clean_filename(title):
    # Remove illegal characters and limit length
    title = re.sub(r'[\\/*?:"<>|]', "", title)  # Remove invalid characters
    title = title.replace("\n", " ").strip()    # Replace newline with space
    return title[:50]

# === Load Excel with product links ===
df = pd.read_excel("markaz_products-ok.xlsx")

# === Folder to save images ===
image_folder = "product_images_of_markaz"
os.makedirs(image_folder, exist_ok=True)

# === Start Selenium ===
driver = webdriver.Chrome()

# === Process each product ===
for index, row in df.iterrows():
    product_title = str(row['Title'])
    product_link = row['Link']
    print(f"Processing: {product_title}")

    try:
        driver.get(product_link)
        time.sleep(3)  # Wait for page to load

        # Find product image (modify selector if needed)
        image_element = driver.find_element(By.CSS_SELECTOR, "img")
        image_url = image_element.get_attribute("src")

        if image_url:
            # Clean and create filename
            filename = f"{clean_filename(product_title)}.jpg"
            filepath = os.path.join(image_folder, filename)

            # Download and save image
            response = requests.get(image_url)
            with open(filepath, "wb") as f:
                f.write(response.content)

            print(f"✅ Saved: {filename}")

    except Exception as e:
        print(f"❌ Error processing {product_link}: {e}")

# === Close browser ===
driver.quit()
print("✅ All done.")
