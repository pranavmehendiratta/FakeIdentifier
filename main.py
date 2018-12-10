# Tesseract imports
from PIL import Image
import pytesseract
import argparse
import cv2
import numpy as np

# SmartySteets imports
from smartystreets_python_sdk import StaticCredentials, exceptions, ClientBuilder
from smartystreets_python_sdk.us_zipcode import Lookup

# General imports
import sys
import os
import re
import json
from pprint import pprint

def main(argv):
    print("Inside main")
    #print(type(argv))
    #print(' '.join(argv))

    if len(argv) < 3:
        print("Usage: python main.py <license.jpg> <image.jpg>")
        sys.exit(1)

    # Read smarty streets api keys
    with open('config.json') as f:
        config = json.load(f)

    # Extract the text from the drivers license
    match = extractText(argv[1])

    if match is not None:
        result = checkIfAddressIsValid(match, config)
        if result is not None:
            print("result in main: " + str(result));
        else:
            print("result is None")
    else:
        print("Cannot find address in the parsed image. Skipping lookup")
    
    removeBackground(argv[2])

def checkIfAddressIsValid(addr, config):
    """
    This function uses the extract city, state, zipcode and smartystreets
    API to validate that combination
    """
    # addr will be a dictionary
    print("Inside checkIfAddressIsValid")

    # Credentials for using the smartystreets API
    smartystreets = config['smartystreets']
    credentials = StaticCredentials(smartystreets['auth_id'], smartystreets['auth_token'])

    #print(type(addr.groups()))
    #print(addr.groups(1)[1])

    regularExp = '(.*),(\s*.*)(\s\d\d\d\d\d)'
    match = re.search(regularExp, addr.groups(1)[1])

    if match is None:
        print ("cannot find city, state and zip code in checkIfAddressIsValid")
        return False

    #print("city: " + str(match.groups(0)[0]))
    #print("state: " + str(match.groups(0)[1]))
    #print("zip: " + str(match.groups(0)[2]))

    client = ClientBuilder(credentials).build_us_zipcode_api_client()
    lookup = Lookup()

    lookup.city = str(match.groups(0)[0])
    lookup.state = str(match.groups(0)[1])
    lookup.zipcode = str(match.groups(0)[2])

    print("-------- All output below is smartystreets' ----------")

    try:
        client.send_lookup(lookup)
    except exceptions.SmartyException as err:
        print(err)
        return False

    result = lookup.result
    zipcodes = result.zipcodes
    cities = result.cities

    for city in cities:
        print("\nCity: " + city.city)
        print("State: " + city.state)
        print("Mailable City: {}".format(city.mailable_city))
	data = {
	    "City": city.city,
	    "State": city.state,
	    "MailableCity": city.mailable_city
	}
	
	
	#"{ City:" + city.city + "," + "State: " + city.state + "," + "Mailable_city: {}".format(city.mailable_city) + "}"
	with open('output.json', 'w') as outfile:
	    json.dump(data, outfile)

    # TODO: Need to convert abbreviation to full state
    #if str(match.groups(0)[0]).lower() != city.city.lower():
    #    print("city is not correct")
    #    return False
    #if str(match.groups(0)[1]).lower() != city.state.lower():
    #    print("state is not correct")
    #    return False

    for zipcode in zipcodes:
    # TODO: Check this one the city and state are matching
    #if str(match.groups(0)[1]) != zipcode.zipcode:
    #    print("zip code is not correct")
    #    return False
        print("\nZIP Code: " + zipcode.zipcode)
        print("Latitude: {}".format(zipcode.latitude))
        print("Longitude: {}".format(zipcode.longitude))

    return True

"""
References: 
"""
def removeBackground(filePath):
    """
    This function takes the file path provided and removes the background
    by changing it to the color of white.
    """

    # Constants
    cBlur = 21
    #Canny Thresholds
    primaryThresh = 10
    secondaryThresh = 50
    dilateMask = 10
    erodeMask = 10
    backgroundColor = (1.0,1.0,1.0) # In BGR format

    # Read the Image
    img = cv2.imread(filePath)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Canny Edge Detection
    edges = cv2.Canny(gray, primaryThresh, secondaryThresh)
    edges = cv2.dilate(edges, None)
    edges = cv2.erode(edges, None)

    # Sort the area, find Countours.
    contour_info = []
    _, contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    for c in contours:
        contour_info.append((
            c,
            cv2.isContourConvex(c),
            cv2.contourArea(c),
        ))
    contour_info = sorted(contour_info, key=lambda c: c[2], reverse=True)
    max_contour = contour_info[0]

    #-- Create empty mask, draw filled polygon on it corresponding to largest contour ----
    # Mask is black, polygon is white
    mask = np.zeros(edges.shape)
    cv2.fillConvexPoly(mask, max_contour[0], (255))

    #Smooth mask, then blur it
    mask = cv2.dilate(mask, None, iterations=dilateMask)
    mask = cv2.erode(mask, None, iterations=erodeMask)
    mask = cv2.GaussianBlur(mask, (cBlur, cBlur), 0)
    mask_stack = np.dstack([mask]*3)    # Create 3-channel alpha mask

    #Blend masked img into backgroundColor background
    mask_stack  = mask_stack.astype('float32') / 255.0          # Use float matrices,
    img = img.astype('float32') / 255.0                 #  for easy blending

    masked = (mask_stack * img) + ((1-mask_stack) * backgroundColor) # Blend
    masked = (masked * 255).astype('uint8')                     # Convert back to 8-bit

    #cv2.imshow('img', masked)
    cv2.waitKey()
    cv2.imwrite(filePath[:len(filePath) - 4] + "_masked.jpg", masked)           # Save

def extractText(imagePath):
    """
    This function takes the image path provided as a command line argument
    and extracts text from the image. Then, we use a regular expression to
    extract the city, state, and zipcode.
    """

    # Use tesseract to extract the text from the image
    print("Inside extract text using tesseract");

    # Load image
    print("Image path: " + imagePath)

    # Convert the image to text
    image = Image.open(imagePath)
    text = pytesseract.image_to_string(image)

    # Regular expression to find the address
    regularExp = '(.*\s*)(.*,\s.*\s\d\d\d\d\d)'
    match = re.search(regularExp, text)

    print(text)
    #print("match: ")

    if match is not None:
        #print(type(match.groups()))
        #print(' '.join(match.groups()))
        #print("match.groups(1): " + str(match.groups(1)))
        return match
    else:
        return None

if __name__ == '__main__':
    main(sys.argv)
