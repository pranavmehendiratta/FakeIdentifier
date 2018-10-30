# Tesseract imports
from PIL import Image
import pytesseract
import argparse
import cv2

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

    if len(argv) < 2:
	print('image should be paramter')
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

    print(type(addr.groups()))
    print(addr.groups(1)[1])

    regularExp = '(.*),(\s*.*)(\s\d\d\d\d\d)'
    match = re.search(regularExp, addr.groups(1)[1])

    if match is None:
	print "cannot find city, state and zip code in checkIfAddressIsValid"
	return False

    print("city: " + str(match.groups(0)[0]))
    print("state: " + str(match.groups(0)[1]))
    print("zip: " + str(match.groups(0)[2]))

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

    for zipcode in zipcodes:
	print("\nZIP Code: " + zipcode.zipcode)
	print("Latitude: {}".format(zipcode.latitude))
	print("Longitude: {}".format(zipcode.longitude))

    return True


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
    print("match: ")

    if match is not None:
	print(type(match.groups()))
	print(' '.join(match.groups())) 
	print("match.groups(1): " + str(match.groups(1)))
	return match
    else:
	return None

if __name__ == '__main__':
    main(sys.argv)
