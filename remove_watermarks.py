# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw

project_path = r'c:\Users\Victu\OneDrive\Desktop\Ai関連\hp_development\projects\hp\Usen関連\USEN-NET'
images_path = os.path.join(project_path, 'images')

# Get all jpg files
jpg_files = [f for f in os.listdir(images_path) if f.lower().endswith('.jpg')]
jpg_files.sort()

print(f"Processing {len(jpg_files)} images...")

for i, jpg_file in enumerate(jpg_files):
    file_path = os.path.join(images_path, jpg_file)
    img = Image.open(file_path)
    draw = ImageDraw.Draw(img)

    width, height = img.size

    # Remove top right logo (USEN NETWORKS / U-NEXT HOLDINGS)
    top_right_box = (int(width * 0.72), 0, width, 90)
    draw.rectangle(top_right_box, fill='black')

    # Remove bottom right page number
    page_num_box = (int(width * 0.95), height - 60, width, height)
    draw.rectangle(page_num_box, fill='white')

    # Save
    img.save(file_path, quality=95)
    print(f"Processed {i+1}/{len(jpg_files)}: {jpg_file}")

print("\nDone! All watermarks removed.")
