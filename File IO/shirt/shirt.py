import os
import sys
from PIL import Image, ImageOps


def main():
    valid_arguments()
    overlay(sys.argv[1], sys.argv[2])


def valid_arguments():
    """check for valid command line arguments"""
    formats = [".jpg", ".jpeg", ".png"]

    if len(sys.argv) < 3:
        sys.exit("Too few command line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command line arguments")

    # use os.path.splitext to get file extensions
    input_ext = os.path.splitext(sys.argv[1])[1]
    output_ext = os.path.splitext(sys.argv[2])[1]


    if input_ext.lower() != output_ext.lower():
        sys.exit("Input and output have different extensions")
    elif input_ext.lower() not in formats or output_ext.lower() not in formats:
        sys.exit("Invalid format")


def overlay(before, after):
    """crops muppet image, overlays shirt onto muppet, then save result to new image file"""
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Source image does not exist")

    try:
        before = Image.open(before)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    cropped = ImageOps.fit(before, shirt.size)
    cropped.paste(shirt, shirt)
    cropped.save(after)


if __name__ == "__main__":
    main()
