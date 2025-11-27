import pandas as pd
import os

input_file = r"E:\platesmart\plates_with_images_AZ.xlsx"
output_file = "char_state_AZ.txt"
main_folder = "Engineteamerror"
state_name = "AZ"

plate_dict = [
    'NM', 'UT', 'IL', 'MA', 'MN', 'AR', 'CO', 'DC', 'HI', 'NE', 'PA', 'NJ', 'OH', 'CT',
    'KY', 'VA', 'VT', 'WV', 'NY', 'TX', 'OK', 'AZ', 'RI', 'SD', 'NC', 'KS', 'TN', 'MI',
    'NV', 'LA', 'FL', 'WI', 'IA', 'WA', 'MD', 'CA', 'AL', 'ME', 'SC', 'MO', 'DE', 'GA',
    'OR', 'NH', 'AK', 'MS', 'ND', 'paper', 'ON', 'QC'
]

state_code = plate_dict.index(state_name)

# Load Excel / CSV
if input_file.endswith(".xlsx"):
    df = pd.read_excel(input_file)
else:
    df = pd.read_csv(input_file)

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Filter rows where "which is right" == "Plate Recognizer"
if "which is right" not in df.columns:
    raise Exception("❌ ERROR: 'which is right' column not found")

filtered_df = df[df["which is right"].str.strip().str.lower() == "plate recognizer".lower()]

# Determine plate number column
possible_plate_cols = ["csv_plate_number", "plate recognizer", "plate_recognizer"]
plate_col = None
for col in df.columns:
    col_clean = col.replace(" ", "")
    for name in possible_plate_cols:
        if col_clean == name.replace(" ", ""):
            plate_col = col
            break
    if plate_col:
        break
if not plate_col:
    raise Exception("❌ ERROR: Could not find a plate number column")

# Determine image column
possible_image_cols = ["image_name", "image", "filename"]
image_col = None
for col in df.columns:
    if col in possible_image_cols:
        image_col = col
        break
if not image_col:
    raise Exception("❌ ERROR: Could not find an image column")

# Generate output
lines = []
for _, row in filtered_df.iterrows():
    image_name = str(row[image_col]).strip()
    plate_number = str(row[plate_col]).strip().replace("'", "").upper()
    file_path = f"{main_folder}/{state_name}/{image_name}.jpg"
    lines.append(f"{file_path} {plate_number} {state_code}")

# Write output
with open(output_file, "w") as f:
    for line in lines:
        f.write(line + "\n")

print(f"✅ {len(lines)} records written to {output_file}")
