import cv2
import os

# --- Configuration ---
txt_file = r"E:\platesmart\char_state_AZ.txt"
images_folder = r"E:\platesmart\extractedAZ"
output_file = "manual_verification_resultsAZ.txt"

# --- Read lines from text file ---
with open(txt_file, 'r') as f:
    lines = [line.strip() for line in f if line.strip()]

results = []

print("Keyboard Controls:")
print("✅ [Enter] → Verified")
print("✏️ [X] → Add comment (saved in output)")
print("🚫 [S] → Skip")
print("❌ [Esc] → Exit early\n")

for line in lines:
    parts = line.split()

    # Expected format: <filepath> <plate> <state_code>
    if len(parts) < 3:
        print(f"⚠️ Skipping malformed line: {line}")
        continue

    file_path = parts[0]      # Engineteamerror/CA/image.jpg
    plate_number = parts[1]
    state_code = parts[2]

    # Extract only filename (without .jpg)
    image_filename = os.path.basename(file_path)
    image_name = image_filename.replace(".jpg", "")

    # Build local image path
    image_path = os.path.join(images_folder, image_filename)

    if not os.path.exists(image_path):
        print(f"⚠️ Missing image in folder: {image_path}")
        continue

    img = cv2.imread(image_path)
    if img is None:
        print(f"⚠️ Unable to open: {image_path}")
        continue

    # Display overlay text on image
    overlay_text = f"{image_name} | Plate: {plate_number}"
    cv2.putText(img, overlay_text, (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 0), 2)

    cv2.imshow("Manual Verification", img)

    key = cv2.waitKey(0) & 0xFF  # Wait for user action

    if key == 13:  # ENTER → VERIFIED
        result = f"{image_name} | Plate: {plate_number} | VERIFIED"
        print(f"✅ {image_name} marked VERIFIED")

    elif key in [ord('x'), ord('X')]:  # X → COMMENT
        comment = input(f"Enter comment for {image_name}: ").strip()
        result = f"{image_name} | Plate: {plate_number} | COMMENT: {comment}"
        print(f"✏️ Comment saved for {image_name}")

    elif key in [ord('s'), ord('S')]:  # SKIP
        print(f"🚫 {image_name} skipped")
        cv2.destroyAllWindows()
        continue

    elif key == 27:  # ESC → Early exit
        print("❌ Exiting verification early...")
        cv2.destroyAllWindows()
        break

    else:
        result = f"{image_name} | Plate: {plate_number} | UNKNOWN_ACTION"

    results.append(result)
    cv2.destroyAllWindows()

# --- Save results ---
with open(output_file, 'w') as f:
    for r in results:
        f.write(r + "\n")

print(f"\n✅ Verification complete! Results saved to {output_file}")
