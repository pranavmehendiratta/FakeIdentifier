# FakeIdentifier

## Team
Joseluis Garcia  
Pranav Mehendiratta  
Shubham Aggarwal  
Utkarsh Jain  

## Summary
Fake-IDentifier is an application with the sole objective of making the process of identifying fake from genuine IDs convenient. This app could potentially be used in-person at places such as bars, clubs, cinemas, dispensaries, chemists in addition to verify age-controlled purchases online.  
  
The application uses text and face Recognition, SIFT feature matching, image normalization to detect inconsistencies 
with the provided ID. It has the capability to look for microscoping differences  and inconsistencies when compared with the copy of a genuine ID from the dataset.  

## Motivation
Our idea stems from a survey which showed that college students are prone to alcohol related dangers and college bars 
across the country face the problem of identifying underage minors trying to sneak into bars. It is very easy for a kid to acquire a fake ID by either crafting one on their own or buying them online. Even if the stores try to enforce these age restricted rules, people can spoof the system by using fake IDs that are difficult to verify.

Access to alcohol isn't the only problem. Rising e-cigarette popularity in high schools recently is a source of concern for the FDA, as these vape sticks can be found virtually everwhere for anyone above the age of 18 (21 in some states). We wanted to curb this problem, to help authorities on college campuses. Recent surveys have found this problem to be rampant and having a tool to sniff out fake IDs would be helpful for bars. Businesses have an incentive to not serve to minors too as they can lose their liquor license. Our fake ID detector would be able to assist both bouncers at the doors and university officials.  
  
Anyone with proficiency in design skills is capable of spoofing a genuine ID by forging fake details on it. Intricate designers 
can spoof an ID to resemble every pixel on a genuine ID. Such a problem could be significantly reduced, if not completely solved, by a platform that is trained to ‘sniff out’ fake identities by the use of simple concepts of Computer Vision.  
   
![](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/web.png =250x250)
   
   
## Approach
There are multiple ways by which we can solve the problem at hand, but it boils down to being able to read the text
and the photo separately from the ID. There is currently no software or library package on the internet that is 
specifically designed to combat counterfeit US drivers licenses. We have come up with our own solution using text recognition, 
image recognition, SIFT, address verification, and template matching to create a multi-step verfication system to calculate the confidence about the authenticity of an ID.

Here is an overview of the approach :-  
* Using image recognition in order to recognize the type of Id being provided. If the ID is unable to be recognized, we ask the user to manually input the type of ID they are providing.
* Use image recognition to see any disparities by comparing against a dataset of genuine IDs. We look for inconsistencies like spacing, font, color and the aspect ratio of the photo on the ID.
* Use text recognition to see any inconsistencies with the formatting of the identities. Look for inconsistencies like font-size, font-color and general regional formats (DD/MM/YYYY in case of European/Indian IDs or MM/DD/YYYY in case of American/Canadian ID). Can also add spelling and grammar checking, if need be.
* Using image recognition to see whether the photo present on the ID matches the photo of the person presenting the ID. For this, we would ask the user of the app to take a close-up of the person in question.
* Using text recognition to check whether the signature(if present on the ID) matches the signature provided by the person in question.    
Finally, we aggregate all these features to feed data to a decision system based on that will decide whether the document in question is genuine, or not

## Implementation
**TODO: @Pranav (Use the slide-show audio transcript you used here)** 

## Current State of the art
Although our team was unable to find anything similar to what we are trying to do, the closest match was the hardware made by Fraud Fighter (https://www.fraudfighter.com/company). They use ultraviolet equipment to see if the ID in question has minute details found only on genuine documents on it. The equipment then decrypts the data and checks the legibility of these documents. They have other handheld devices to verify the barcodes, counterfeit currency detection, and other security equipment. While this machine has a high success rate, it comes with a high price, restricting its accessibility. Our application, however, would be free on mobile. Its success rate would essentially depend on our model parameters and depend on the various level of checks to identify any kind of discrepancy. It also assumes the picture taken during entry would be well lit enough for a face match.
Even though our application would have various false positives, we believe that with time, we could reinforce our model to be able to weed out some of these false positives. 


## Results
#### Text Recognition Results:  
Text recognition results can be seen in the output.json file below. The input for validating the address is (city, state, zip\_code) and the smarty streets API returns whether that is a valid mailable address.
#### Background Removal Results:  
Below we first have the input image and its corresponding background removed image. New background color is white.
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/input/emma.jpg "Emma Watson" =250x250)  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/emma_masked.jpg "Emma Watson with Masked Background")  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/Images/woman.jpg "Random Woman")  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/Images/woman_masked.jpg "Woman with Masked Background")  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/input/rakesh.jpg "Random Man")
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/rakesh_masked.jpg "Man with Masked Background")  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/input/mia.jpg "Mia Kunis")  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/mia_masked.jpg "Mia Kunis with Masked Background")  
#### State Detection Results:  
Here we input a valid wisconsin drivers license and output a new image with a red box around the valid state template matching.
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/input/driver1.jpg "Valid state ID" =250x250)  
![alt text](https://github.com/pranavmehendiratta/FakeIdentifier/blob/master/output/driver1.jpg "Valid state ID" =250x250)  
#### Facial Recognition Results:  
#### Structure Similary Index Test Results:  
#### Example final JSON: 
```json
{	
   "MailableCity": true, 
    "City": "Madison", 
    "State": "Wisconsin"
    "FacialMatch": true,
    "StateMatch": true
}
```
## Problems
**TODO: (Talk about quality of results here)**
* The biggest problem we faced was to procure the dataset. We were not able to find good "fake" IDs or bad valid IDs. Therefore, we were not able to test the accuracy of our projet correctly. To resolve this problem we manually created a small set of fake IDs to test against.
* Another problem is with text recgonition. Optical text recgonition works well when the resolution of the image is high otherwise similar looking characters are sometimes not correctly identified.

## Slides
https://drive.google.com/file/d/11D_uPDwuzzh7fYszADgHioz0ASGKJ15G/view?fbclid=IwAR3V4FctFCtrQOHagRxswpPXldnQ_RUofi40uPDi29QEl-Cce6T2SNg6LQk
