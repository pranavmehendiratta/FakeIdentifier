from PIL import Image
import pytesseract
import argparse
import cv2
import os
import sys

def main(argv):
    print("Inside main")
    #print(type(argv))
    #print(' '.join(argv)) 

    if len(argv) < 2:
	print('image should be paramter')
	sys.exit(1)

    # Extract the text from the drivers license
    extractText(argv[1])

def checkIfAddressIsValid(addr):
    # addr will be a dictionary
    print("Inside checkIfAddressIsValid")

def extractText(imagePath):
    # Use tesseract to extract the text from the image
    print("Inside extract text using tesseract");
    
    # Load image
    print("Image path: " + imagePath)

    # Convert the image to text
    image = Image.open(imagePath)
    text = pytesseract.image_to_string(image)
    print(text);

if __name__ == '__main__':
    main(sys.argv)
