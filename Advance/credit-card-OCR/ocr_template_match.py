# USAGE
# python ocr_template_match.py --image images/credit_card_01.png --reference ocr_a_reference.png

# import the necessary packages
# you will need to install OpenCV and imutils if you don't already have
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

# now that we're installed and imported packages, we can parse our command line arguments
## construct the argument parser and parse the arguments
### we establish an argument parser, add two arguments, and parse them, storing as the variable, args
#### --reference: This image contains the digits 0-9 in the OCR-A font, thereby allowing us
#### to perform template matching later in the pipeline.
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-r", "--reference", required=True, help="path to reference OCR-A image")
args = vars(ap.parse_args())

# next let's define credit card types:
## define a dictionary that maps the first digit of a credit card
## number to a credit card type
### credit card types, such as American Express, Visa, etx., can be identified by
### https://money.howstuffworks.com/personal-finance/debt-management/credit-card1.htm
#### we define a dictionary, FIRST_NUMBER, which maps the first digit to the corresponding credit card type.
FIRST_NUMBER = {
    "3": "American Express",
    "4": "Visa",
    "5": "MasterCard",
    "6": "Discover Card"
}
# let's start our image processing pipeline by loading the reference OCR-A image:
## load the reference OCR-A image from disk, convert it to grayscale,
## and threshold it, such that digits appear as *white* on a *black* background
## and invert it, such that the digits appear as *white* on a *black*
ref = cv2.imread(args["reference"]) # we load the reference OCR-A image
ref = cv2.cvtColor(ref, cv2.COLOR_BGR2GRAY) #convert it to grayscale
ref = cv2.threshold(ref, 10, 255, cv2.THRESH_BINARY_INV)[1] # threshoding + inverting it

# now let's locate contours on our OCR-A font image:
## find contours in the OCR-A image(i.e,. the outlines of the digits)
## sort them from left to right, and initialize a dictionary to map digit name to the ROI
refCnts = cv2.findContours(ref.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # we find the contours present in the ref image.
## due to how OpenCV 2.4 and OpenCV 3
## https://www.pyimagesearch.com/2015/08/10/checking-your-opencv-version-using-python/
refCnts = refCnts[0] if imutils.is_cv2() else refCnts[1] # we check the version and make an appropriate change to refCnts

## we sort the contours from left-to-right as well as initialize a dictionary, digits, which maps the digit name to the region of interest
refCnts = contours.sort_contours(refCnts, method="left-to-right")[0]
digits = {}

# at this point, we should loop through the contours, extract, and associate ROIs with their corresponding digits:
## loop over the OCR-A reference contours

### we loop through the reference image contours.
### n the loop, i  holds the digit name/number and c  holds the contour.
for (i, c) in enumerate(refCnts):

    ### We compute a bounding box around each contour, c , (Line 46) storing the (x, y)-coordinates and width/height of the rectangle.
    # compute the bounding box for the digit, extract it, and resize it to a fixed resize
    (x, y, w, h) = cv2.boundingRect(c)

    ### we extract the roi  from ref  (the reference image) using the bounding rectangle parameters. This ROI contains the digit.
    roi = ref[y:y + h, x:x + w]
    ### We resize each ROI to a fixed size of 57×88 pixels.
    ### We need to ensure every digit is resized to a fixed size in order to apply template matching for digit recognition later in this tutorial.
    roi = cv2.resize(roi, (57, 88))

    # update the digits dictionary, mapping the digit name to the ROI
    ### We associate each digit 0-9 (the dictionary keys) to each roi  image (the dictionary values)
    digits[i] = roi


# at this point, we are done extracting the digits from our reference image and asscociating them with their corresponding digit name.
# Our next goal is to isolate the 16-digit credit card number in the input --image .
# We need to find and isolate the numbers before we can initiate template matching to identify each of the digits.
# These image processing steps are quite interesting and insightful,
# especially if you have never developed an image processing pipeline before,
# so be sure to pay close attention.

# Let’s continue by initializing a couple structuring kernels:
## initialize a rectangular (wider than it is tall) and square structuring kernel
## You can think of a kernel as a small matrix which we slide across the image to do (convolution) operations such as blurring, sharpening, edge detection, or other image processing operations.
### we construct two such kernels — one rectangular and one square. We will use the rectangular one for a Top-hat morphological operator and the square one for a closing operation.
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 3))
sqKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Now let’s prepare the image we are going to OCR:
# load the input image, resize it, and convert it to grayscale
image = cv2.imread(args["image"]) # we load our command line argument image  which holds the photo of the credit card.
image = imutils.resize(image, width=300) # we resize it to width=300 , maintaining the aspect ratio
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #followed by converting it to grayscale

# Now that our image is grayscaled and the size is consistent, let’s perform a morphological operation:
## apply a tophat (whitehat) morphological operator to find light
## regions against a dark background (i.e., the credit card numbers)
### Using our rectKernel and our gray  image, we perform a Top-hat morphological operation, storing the result as tophat
### The Top-hat operation reveals light regions against a dark background (i.e. the credit card numbers)
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)

# Given our tophat  image, let’s compute the gradient along the x-direction:
## compute the Scharr gradient of the tophat image, then scale
## the rest back into the range [0, 255]
gradX = cv2.Sobel(tophat, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=-1) # The next step in our effort to isolate the digits is to compute a Scharr gradient of the tophat  image in the x-direction.
### We complete this computation, storing the result as gradX .
gradX = np.absolute(gradX)
### After computing the absolute value of each element in the gradX  array, we take some steps to scale the values into the range [0-255] (as the image is currently a floating point data type).
### To do this we compute the minVal  and maxVal  of gradX  (Line 111) followed by our scaling equation shown on Line 112 (i.e., min/max normalization).
(minVal, maxVal) = (np.min(gradX), np.max(gradX))
gradX = (255 * ((gradX - minVal) / (maxVal - minVal)))
### The last step is to convert gradX  to a uint8  which has a range of [0-255]
gradX = gradX.astype("uint8")


# Let’s continue to improve our credit card digit finding algorithm:
## apply a closing operation using the rectangular kernel to help
## cloes gaps in between credit card number digits, then apply
## Otsu's thresholding method to binarize the image
gradX = cv2.morphologyEx(gradX, cv2.MORPH_CLOSE, rectKernel)
thresh = cv2.threshold(gradX, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

## apply a second closing operation to the binary image, again
## to help close gaps between credit card number regions
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, sqKernel)

### To close the gaps, we do a closing operation on Line 121.
### Notice that we use our rectKernel  again. Subsequently we perform an Otsu and binary threshold of the gradX  image (Lines 122),
### followed by another closing operation (Line 126).


# Next let’s find the contours and initialize the list of digit grouping locations.
## find contours in the thresholded image, then initialize the
## list of digit locations
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]
locs = []

# Now let’s loop through the contours while filtering based on the aspect ratio of each, allowing us to prune the digit group locations from other, irrelevant areas of the credit card:
## loop over the contours
for (i, c) in enumerate(cnts):
	### compute the bounding box of the contour, then use the
	### bounding box coordinates to derive the aspect ratio
	(x, y, w, h) = cv2.boundingRect(c)
	ar = w / float(h)

	### since credit cards used a fixed size fonts with 4 groups
	### of 4 digits, we can prune potential contours based on the
	### aspect ratio
	if ar > 2.5 and ar < 4.0:
		### contours can further be pruned on minimum/maximum width
		### and height
		if (w > 40 and w < 55) and (h > 10 and h < 20):
			### append the bounding box region of the digits group
			### to our locations list
			locs.append((x, y, w, h))


# Next, we’ll sort the groupings from left to right and initialize a list for the credit card digits:
## sort the digit locations from left-to-right, then initialize the
## list of classified digits
locs = sorted(locs, key=lambda x:x[0])
output = []

# Now that we know where each group of four digits is, let’s loop through the four sorted groupings and determine the digits therein.
# This loop is rather long and is broken down into three code blocks — here is the first block:
## loop over the 4 groupings of 4 digits
for (i, (gX, gY, gW, gH)) in enumerate(locs):
	### initialize the list of group digits
	groupOutput = []

	### extract the group ROI of 4 digits from the grayscale image,
	### then apply thresholding to segment the digits from the
	### background of the credit card
	group = gray[gY - 5:gY + gH + 5, gX - 5:gX + gW + 5]
	group = cv2.threshold(group, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	### detect the contours of each individual digit in the group,
	### then sort the digit contours from left to right
	digitCnts = cv2.findContours(group.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	digitCnts = digitCnts[0] if imutils.is_cv2() else digitCnts[1]
	digitCnts = contours.sort_contours(digitCnts, method="left-to-right")[0]

    # Let’s continue the loop with a nested loop to do the template matching and similarity score extraction:
	# loop over the digit contours
	for c in digitCnts:
		# compute the bounding box of the individual digit, extract
		# the digit, and resize it to have the same fixed size as
		# the reference OCR-A images
		(x, y, w, h) = cv2.boundingRect(c)
		roi = group[y:y + h, x:x + w]
		roi = cv2.resize(roi, (57, 88))

		# initialize a list of template matching scores
		scores = []

		# loop over the reference digit name and digit ROI
		for (digit, digitROI) in digits.items():
			# apply correlation-based template matching, take the
			# score, and update the scores list
			result = cv2.matchTemplate(roi, digitROI,
				cv2.TM_CCOEFF)
			(_, score, _, _) = cv2.minMaxLoc(result)
			scores.append(score)

		# the classification for the digit ROI will be the reference
		# digit name with the *largest* template matching score
		groupOutput.append(str(np.argmax(scores)))

        # Now, let’s loop (third nested loop) through each reference digit and perform template matching. This is where the heavy lifting is done for this script.

        # Finally, let’s draw a rectangle around each group and view the credit card number on the image in red text:
	# draw the digit classifications around the group
	cv2.rectangle(image, (gX - 5, gY - 5),
		(gX + gW + 5, gY + gH + 5), (0, 0, 255), 2)
	cv2.putText(image, "".join(groupOutput), (gX, gY - 15),
		cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 2)

	# update the output digits list
	output.extend(groupOutput)
    # The last step is to append the digits to the output list. The Pythonic way to do this is to use the extend  function which appends each element of the iterable object (a list in this case) to the end of the list.

# To see how well the script performs, let’s output the results to the terminal and display our image on the screen.
# display the output credit card information to the screen
print("Credit Card Type: {}".format(FIRST_NUMBER[output[0]]))
print("Credit Card #: {}".format("".join(output)))
cv2.imshow("Image", image)
cv2.waitKey(0)
