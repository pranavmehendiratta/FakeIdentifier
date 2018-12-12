# FakeIdentifier

## Team
Joseluis Garcia  
Pranav Mehendiratta  
Shubham Aggarwal  
Utkarsh Jain  

## Summary
Fake-IDentifier is an application with a sole objective of making the process of identifying fake from genuine IDs convenient.   
This app could potentially be used in-person at places such as bars, clubs, cinemas, dispensaries, chemists in addition to  
any age-controlled online platforms.  
  
The application uses Text Recognition, Image Recognition, SIFT Age Determination, Image Normalization to detect inconsistencies 
within the same ID, and inconsistencies when compared with the copy of a genuine ID from the dataset.  

## Motivation
Our idea stems from a survey which showed that teenagers have started showing signs of alcohol addiction and college bars 
across the country face the problem of identifying underage minors trying to sneak into bars. The major source of 
their supply is liquor stores, bars, and even supermarkets. Even after strict enforcement of rules, cunning teenagers find 
a way to get around them. One such way is forging a ‘very-legible’ fake identity document, which a human eye might not be 
able to distinguish. 
  
The power of a fake identity document isn’t limited to the purchase of alcohol. While teenagers use fake identity documents to 
get access to restricted commodities like alcohol, drugs, nicotine products and access to age-restricted places/website, 
others use fake identities to commit illegal activities like fraud, scams or even physical harm.

The main problem of under-age drinking that we are trying to address is viewed seriously by authorities on several college campuses. 
To prevent access of liquor to underage students is a matter of safety as well as law. Recent surveys have found this problem to 
be rampant and having a tool to sniff out fake IDs would be helpful for bars. Businesses have an incentive to not 
serve to minors too as that can get you a felony charge. Our fake ID detector would be able to assist both bouncers 
at the doors and university officials.  
  
Anyone with proficiency in design skills is capable of spoofing a genuine ID by forging fake details on it. Intricate designers 
can spoof an ID to resemble every pixel on a genuine ID. Such a problem could be significantly reduced, if not completely solved,
by a platform that is trained to ‘sniff out’ fake identities by the use of simple concepts of Computer Vision:  
A) Pattern recognition  
B) Image recognition  
C) Text recognition  
D) SIFT  
E) Age determination  

## Approach
There are multiple ways by which we can solve the problem at hand, but it boils down to being able to read the text
and the photo separately from the ID. There is currently no software or library package on the internet that is 
specifically designed to combat counterfeit documents. We have come up with our own solution using text recognition, 
image recognition, SIFT, age determination, address verification, and image normalization through homography. 
Here is an overview of the approach :-  
* Using image recognition in order to recognize the type of Id being provided. If the ID is unable to be recognized, we ask the user to manually input the type of ID they are providing.
* Use image recognition to see any disparities by comparing against a dataset of genuine IDs. We look for inconsistencies like spacing, font, color and the aspect ratio of the photo on the ID.
* Use text recognition to see any inconsistencies with the formatting of the identities. Look for inconsistencies like font-size, font-color and general regional formats (DD/MM/YYYY in case of European/Indian IDs or MM/DD/YYYY in case of American/Canadian ID). Can also add spelling and grammar checking, if need be.
* Using image recognition to see whether the photo present on the ID matches the photo of the person presenting the ID. For this, we would ask the user of the app to take a close-up of the person in question.
* Using text recognition to check whether the signature(if present on the ID) matches the signature provided by the person in question.  
  
Finally, we aggregate all these features to feed data to a decision system based on that will decide whether the document in question is genuine, or not

## Implementation

## Current State of the art
Although our team was unable to find anything similar to what we are trying to do, the closest match was the hardware made by Fraud Fighter (https://www.fraudfighter.com/company). They use ultraviolet equipment to see if the ID in question has minute details found only on genuine documents on it. The equipment then decrypts the data and checks the legibility of these documents. They have other handheld devices to verify the barcodes, counterfeit currency detection, and other security equipment. While this machine has a high success rate, it comes with a high price, restricting its accessibility. Our application, however, would be free on mobile. Its success rate would essentially depend on our model parameters and depend on the various level of checks to identify any kind of discrepancy. It also assumes the picture taken during entry would be well lit enough for a face match.
Even though our application would have various false positives, we believe that with time, we could reinforce our model to be able to weed out some of these false positives. 


## Results
**TODO: PRANAV (Insert screenshots)

## Problems
**TODO: PRANAV (Talk about quality of results here)

## Slides
https://drive.google.com/file/d/11D_uPDwuzzh7fYszADgHioz0ASGKJ15G/view?fbclid=IwAR3V4FctFCtrQOHagRxswpPXldnQ_RUofi40uPDi29QEl-Cce6T2SNg6LQk
