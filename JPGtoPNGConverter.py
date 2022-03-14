from PIL import Image
import os
import sys

if len(sys.argv) != 3:
    print("Usage: python JPGtoPNGConverter.py <input_dir> <output_dir>")
    sys.exit()

input_dir = sys.argv[1]
output_dir = sys.argv[2]

# Check if input_dir exists
if not os.path.exists(input_dir):
    print("Input directory does not exist.")
    sys.exit()

# If output_dir does not exist, create it
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# loop through all files in input_dir
for filename in os.listdir(input_dir):
    # ignore directories
    if os.path.isdir(filename):
        continue

    # convert JPG to PNG
    if filename.endswith(".jpg"):
        jpg_filepath = os.path.join(input_dir, filename)
        png_filename = filename.replace(".jpg", ".png")
        png_filepath = os.path.join(output_dir, png_filename)
        try:
            Image.open(jpg_filepath).save(png_filepath, "png")
        except IOError:
            print("Cannot convert", jpg_filepath)

