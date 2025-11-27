# Python Automations

This folder contains Python scripts for automating license plate annotation workflows.

## Scripts Included

1. **generate_char_state_txt.py**
   - Reads Excel/CSV files containing plate data
   - Filters correct rows and generates structured text output
   - Output format: `<main_folder>/<state>/<image_name>.jpg <plate_number> <state_code>`

2. **copy_images.py**
   - Copies referenced images from source to a centralized folder
   - Handles missing images gracefully
   - Prepares data for manual verification

3. **manual_verification.py**
   - Displays images for manual verification using OpenCV
   - Allows marking as VERIFIED, adding COMMENT, SKIP, or exiting
   - Saves results to a text file for downstream use

## Tools Used
- Python 3.x
- Pandas
- OpenCV
- OS / shutil modules

## Setup Instructions
1. Install dependencies:
   ```bash
   pip install pandas opencv-python
