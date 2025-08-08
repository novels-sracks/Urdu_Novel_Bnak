# from PIL import Image, ImageDraw, ImageFont
# from fpdf import FPDF
# import os

# # ✅ Step 1: Set the folder path where your images are
# folder_path = r"E:\My-Workstation\product_images"  # ← اپنی فولڈر کا راستہ دیں
# output_pdf = "product_catalog.pdf"

# # ✅ Step 2: Initialize PDF
# pdf = FPDF()
# pdf.set_auto_page_break(auto=True, margin=15)

# # ✅ Step 3: Process each image in the folder
# for filename in os.listdir(folder_path):
#     if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
#         image_path = os.path.join(folder_path, filename)

#         # Extract Title and Price from filename
#         name_without_ext = os.path.splitext(filename)[0]
#         parts = name_without_ext.split(' ', 2)  # e.g. ['Rs.', '1,194.00', 'Urdu Novel Name']
#         if len(parts) >= 3:
#             price = parts[0] + ' ' + parts[1]
#             title = parts[2]
#         else:
#             price = ""
#             title = name_without_ext

#         # ✅ Step 4: Add a new page and write content
#         pdf.add_page()

#         # Add image
#         pdf.image(image_path, x=10, y=30, w=pdf.w - 20)

#         # Add Title and Price
#         pdf.set_font("Arial", size=14)
#         pdf.set_y(10)
#         pdf.cell(0, 10, title, ln=True)
#         pdf.set_font("Arial", size=12)
#         pdf.cell(0, 10, price, ln=True)

# # ✅ Step 5: Save the PDF
# pdf.output(output_pdf)
# print("PDF created successfully:", output_pdf)






from PIL import Image
from fpdf import FPDF
import os

# ✅ Step 1: Folder ka path jahan images hain
folder_path = r"E:\My-Workstation\product_images" # ← apna folder ka path yahan likhein
output_pdf = "products_catalog.pdf"

# ✅ Step 2: PDF object banayein
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)

# ✅ Step 3: Special characters ko clean karne wala function
def clean_text(text):
    return text.replace("–", "-").encode('latin-1', 'ignore').decode('latin-1')

# ✅ Step 4: Har image ko process karein
for filename in os.listdir(folder_path):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(folder_path, filename)

        # ✅ Filename se Title aur Price nikaalein
        name_without_ext = os.path.splitext(filename)[0]
        parts = name_without_ext.split(' ', 2)  # e.g. ['Rs.', '1,194.00', 'Urdu Novel Name']
        if len(parts) >= 3:
            price = parts[0] + ' ' + parts[1]
            title = parts[2]
        else:
            price = ""
            title = name_without_ext

        # ✅ Naya page add karein
        pdf.add_page()

        # ✅ Font set karein
        pdf.set_font("Arial", size=14)
        pdf.set_y(10)

        # ✅ Title likhein
        pdf.cell(0, 10, clean_text(title), ln=True)

        # ✅ Price likhein
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, clean_text(price), ln=True)

        # ✅ Image add karein
        pdf.image(image_path, x=10, y=30, w=pdf.w - 20)

# ✅ Step 5: PDF save karein
pdf.output(output_pdf)
print("✅ PDF ban gaya:", output_pdf)
