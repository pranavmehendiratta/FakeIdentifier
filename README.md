# FakeIdentifier

## Team
Joseluis Garcia  
Pranav Mehendiratta  
Shubham Aggarwal  
Utkarsh Jain  

## Summary
Fake-IDentifier is an application with the sole objective of making the process of identifying fake from genuine IDs convenient. This app could potentially be used in-person at places such as bars, clubs, cinemas, dispensaries, chemists in addition to verifying online age-controlled purchases.  
  
The application uses text and face recognition, SIFT feature matching, and image normalization techniques o detect inconsistencies with the provided ID. It has the capability to look for microscoping differences by storing a dataset of known genuine IDs scraped from DMV archives.

## Motivation
Our idea stems from a survey which showed that college students are prone to alcohol related dangers. Moreover, college bars 
across the country face the problem of identifying underage minors trying to sneak into bars. It is very easy for a kid to acquire a fake ID by either crafting one on their own or buying them online. Even if the stores try to enforce these age restricted rules, people can spoof the system by using fake IDs that are difficult to verify.

Access to alcohol isn't the only problem. Rising e-cigarette popularity in high schools recently is a source of concern for the FDA, as these vape sticks can be found virtually everywhere for anyone above the age of 18 (21 in some states). We wanted to prevent these products from reaching minors. Recent surveys have found this problem to be rampant and having a tool to sniff out fake IDs would be helpful for bars. Businesses have an incentive to not serve to minors too as they can lose their liquor license. Our fake ID detector would be able to assist both bouncers at the doors and university officials.  
  
Anyone with proficiency in design skills is capable of spoofing a genuine ID by forging fake details on it. Skilled designers can spoof an ID to resemble every pixel on a genuine ID. Such a problem could be significantly reduced, if not completely solved, by a platform that is trained to ‘sniff out’ fake identities by the use of simple concepts of Computer Vision.  
   
![](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/web.png)
   
## Approach
There are multiple ways by which we can solve the problem at hand, but it boils down to being able to read the text
and the photo separately from the ID. There is currently no software or library package on the internet that is 
specifically designed to combat counterfeit US drivers licenses. We have come up with our own solution using text recognition, 
image recognition, SIFT, address verification, and template matching to create a multi-step verfication system to calculate the confidence about the authenticity of an ID.

Here is an overview of the approach :-  
* Using image recognition in order to recognize the type of Id being provided. If the ID is unable to be recognized, we ask the user to manually input the type of ID they are providing.
* Use image recognition to see any disparities by comparing against a dataset of genuine IDs. We look for inconsistencies like spacing, font, color and the aspect ratio of the photo on the ID.
* Use text recognition to see any inconsistencies with the formatting of the identities. Look for inconsistencies like font-size, font-color and general regional formats (DD/MM/YYYY in case of European/Indian IDs or MM/DD/YYYY in case of American/Canadian ID). Can also add spelling and grammar checking, if need be.
* Using image recognition to see whether the photo present on the ID matches the photo of the person presenting the ID. For this, we ask the user of the app to take a close-up of the person in question.

Finally, we aggregate all these features to feed data to a decision system based on that will decide whether the document in question is genuine, or not.

## Implementation

* Text Recognition

We used optical character recognition for this step. We send the drivers license as the input and then output all the text on that drivers license. Then we use regular expressions to extract the city, state, and zip code. We send this as input to smarty streets API which tells us whether this address is valid or not. The motivation behind this step was that if a person is using a fake ID they will  most probably not have a correct address. Hence, we want to verify that part of the ID presented.

* Background replacement

For this step we use canny edge detection to identify the boundaries of the person in the photo. Once the edges are identified we replace the background with white color. Different values of thresholds can be used so that out algorithm works on images with different backgrounds. The motivation behind this step was to ensure that the background does not have any other person/objects in it which yields incorrect facial recognition results.

* Facial Recognition

Using pre trained models based on dlib C++ library, our system can detect faces both from live feed from the smartphone camera or by taking a picture of the person presenting the ID. A lot of times people borrow IDs from their friends or siblings that look very much like them. By fine tuning the tolerance parameter, we can detect accurately between people who look very similar. Beards, glasses or even face fat does not fool the implementation.

* State matching

To match the ID with its corresponding state,  we implemented template matching, which is a technique for finding areas of an image that are similar to a provided set of templates. We first scrapped each state’s logos found on their respective driver’s license image from the internet (mainly from https://www.aceable.com/blog/all-51-driver-license-designs-ranked-worst-to-best/ ). By collecting the interest points like pixel intensity, color and focus of the provided logos of all 48 drriver license headers, we compare them to the ones present in the ID. After segmenting the image, the segments are matched with our database using cv2.matchTemplate( ) function, where each pixel denotes how much does the neighborhood of that pixel match with template. 
Then we applied cv2.minMaxLoc() on the result to obtained the max_val for each template and stored it dictionary with its corresponding state name. Finally, we take the max value from every template to obtain the best matching template (the state). 

* SSM Index

Even if the ID passed our three tests, the ID is processed by a microscopic algorithm to detect fine prints and microscopic patterns found only in genuine IDs. These patterns are hard to reproduce with a scanner, but a human eye can miss these tiny details under dim bar lighting conditions. Wang *et al* proposed the Structure Similarity Index in 2004.

We use OpenCV’s support to calculate the SSM index. SSM index is the average value of three attributes for each pixel - luminance, contrast and structure. By taking the difference of SSM indexes (converted to 8-bit grayscale) for two images, we are able to distinguish areas where the ID differs from the known dataset. We then draw a rectangle around this detected contour to convey any differences detected by our system.

Using this method, we were able to easily determine if the ID was identical to our dataset of known IDs or had differences due to slight image manipulations or purposeful tampering.

**Therefore, our evaluation uses a multi step procedure to detect fake IDs. This system can act as a second choice by establishments to verify if the ID is genuine if they have doubts about it. Using our multi step procedure, our design can be made as a mobile app. Through this app, the bouncer can quickly verify the ID without needing actual scanners.**

## Current State of the art
Although our team was unable to find anything similar to what we are trying to do, the closest match was the hardware made by Fraud Fighter (https://www.fraudfighter.com/company). They use ultraviolet equipment to see if the ID in question has minute details found only on genuine documents on it. The equipment then decrypts the data and checks the legibility of these documents. They have other handheld devices to verify the barcodes, counterfeit currency detection, and other security equipment. While this machine has a high success rate, it comes with a high price, restricting its accessibility. Our application, however, would be free on mobile. Its success rate would essentially depend on our model parameters and depend on the various level of checks to identify any kind of discrepancy. It also assumes the picture taken during entry would be well lit enough for a face match.
Even though our application would have various false positives, we believe that with time, we could reinforce our model to be able to weed out some of these false positives. 


## Results
#### Text Recognition Results:  
Text recognition results can be seen in the output.json file below. The input for validating the address is (city, state, zip\_code) and the smarty streets API returns whether that is a valid mailable address.
#### Background Removal Results:  
Below we first have the input image and its corresponding background removed image. New background color is white.

Example 1

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/input/emma.jpg "Emma Watson")  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/emma_masked.jpg "Emma Watson with Masked Background")  

Example 2

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/input/rakesh.jpg "Random Man")
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/rakesh_masked.jpg "Man with Masked Background")  

Example 3

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/input/mia.jpg "Mia Kunis")  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/mia_masked.jpg "Mia Kunis with Masked Background")  

Example 4

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/input/image1.jpg "Person")  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/image1.jpg "Person with Masked Background")  

## State Detection Results:  
Here we input a valid wisconsin drivers license and output a new image with a red box around the valid state template matching.

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/input/driver1.jpg "Valid state ID")  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/driver1.png "State matchig result on a valid state ID")  
## Facial Recognition Results:  

Facial recognition will output a new image with box around the face on the ID and mention the name of the person it matched with otherwise it will say "unknown".

Example 1

Inputs

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/image1.jpg "Person with Masked Background")  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/input/driver1.jpg "Valid state ID")  

Output

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/faceMatch.png "Valid state ID")  

Example 2

Inputs

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/mia_masked.jpg "Mia Kunis with Masked Background")  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/input/driver2.jpg "Valid state ID")  

Outputs

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/incorrectFaceMatch.png "Valid state ID")  

NOTE: Here we can see that the facial recognition correctly identifies that the person in the input image is not on the drivers license.

## Structure Similary Index Test Results:  

The first image has been modified to have a black box on the top right. This represents a fake ID presented at the bar by a naive freshman. 

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/driver3e.jpg "Valid state ID")  

The difference image is represented in [0,1] range. 

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/SSM2.png "Valid state ID")  

Our system detects that the image is different in the top roght than the dataset, and draws a rectangle around it. This represents that the ID is fake. 

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/SSM4.png "Valid state ID")  

SSM image for the genuine ID.

![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/SSM3.png "Valid state ID")  

## Example final JSON: 
```json
{	
   "MailableCity": true, 
    "City": "Madison", 
    "State": "Wisconsin"
    "FacialMatch": true,
    "StateMatch": "Wisconsin"
}
```
## Problems
* The biggest problem we faced was to procure the dataset. We were not able to find good "fake" IDs or bad valid IDs. Therefore, we were not able to test the accuracy of our projet correctly. To resolve this problem we manually created a small set of fake IDs to test against.

* Another problem is with text recgonition. Optical text recgonition works well when the resolution of the image is high otherwise similar looking characters are sometimes not correctly identified.

* For background replacement we encountered several problems. The primary issue was to make our background algorithm work efficiently with all kinds of images with different contrast in the background. Ultimately, we decided that we need to run this program at night, therefore, adjusted the threshold such that we can get a fair result from this step for facial recognition.

* For most states the program detects the correct name and position but fails the rest of the times. In order to make it more accurate we need a bigger data set of templates but unfortunately with the short time span it did not give us enough time to improve it.

* Finding the right method to detect differences was important. Also, a lot of IDs have color gradients that are intensity neutral at some spots in the ID. Because of this, the above approach is not able to detect differences through SSM for some states like Michigan or Pennsylvania. 

## Slides
https://drive.google.com/file/d/11D_uPDwuzzh7fYszADgHioz0ASGKJ15G/view?fbclid=IwAR3V4FctFCtrQOHagRxswpPXldnQ_RUofi40uPDi29QEl-Cce6T2SNg6LQk

##References
Z.Wang, Conrad Bovik et al. Image Quality Assessment: From Error Visibility to Structural Similarity
https://pythonspot.com/object-detection-with-templates/
