import os
import shutil

# Paths for California
txt_file = "E:\platesmart\char_state_AZ.txt"
source_folder = r"E:\platesimages\AZ"
destination_folder = r"E:\platesmart\extractedAZ"

os.makedirs(destination_folder, exist_ok=True)


with open(txt_file, 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]

copied = 0
missing = 0

for line in lines:
    parts = line.split()
    if len(parts) < 1:
        continue

    # Full path example: Engineteamerror/CA/image.jpg
    full_path = parts[0]

    # Extract just the image filename
    image_name = os.path.basename(full_path).strip()

    # Ensure extension
    if not image_name.lower().endswith(".jpg"):
        image_name += ".jpg"

    # Build complete source/destination path
    src_path = os.path.join(source_folder, image_name)
    dst_path = os.path.join(destination_folder, image_name)

    # Normalize paths (Windows safe)
    src_path = os.path.normpath(src_path)
    dst_path = os.path.normpath(dst_path)

    # Copy if exists
    if os.path.exists(src_path):
        shutil.copy2(src_path, dst_path)
        copied += 1
    else:
        print(f"⚠️ Missing image in source: {image_name}")
        missing += 1

print(f"\n✅ Done! {copied} images copied to '{destination_folder}'")
if missing > 0:
    print(f"⚠️ {missing} images were missing in source folder.")
