import pandas as pd

# Excel file ka path
excel_file = r"E:\SUNB\Smart Urdu Novel Bank\add_new_novel.xlsx"  # Apni Excel file ka path daalein

# JSON file ka output path
json_file = r"E:\SUNB\Smart Urdu Novel Bank\add_new_novel.json"  # JSON file ka naam aur path

try:
    # Excel file ko read karein
    df = pd.read_excel(excel_file, engine='openpyxl')

    # DataFrame ko JSON mein convert karein (standard JSON format, not JSONL)
    df.to_json(json_file, orient='records', indent=4)  # Removed lines=True to create a single array

    print(f"Excel file successfully converted to JSON and saved as {json_file}")

except Exception as e:
    print(f"Error occurred: {e}")