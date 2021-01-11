# 1
import cv2

img = cv2.imread('094455_6.jpg')

# print("Image Properties")
# print("- Number of Pixels: " + str(img.size))
# print("- Shape/Dimensions: " + str(img.shape))

# 2
# blue, green, red = cv2.split(img) # Split the image into its channels
# img_gs = cv2.imread('094455_6.jpg', cv2.IMREAD_GRAYSCALE) # Convert image to grayscale

# cv2.imshow("Red", red) # Display the red channel in the image
# cv2.imshow("Green", green) # Display the red channel in the image
# cv2.imshow("Blue", blue) # Display the red channel in the image
# cv2.imshow("Img_gs", img_gs) # Display the grayscale version of image

# cv2.waitKey(0)

# #closing all open windows
# cv2.destroyAllWindows()
# 3

# cap = cv2.VideoCapture(0)
# while True:
# 	success,img = cap.read()
# 	cv2.imshow("Video", img)
# 	if cv2.waitKey(1) & 0xFF == ord('q'):
# 		break
import numpy as np

kernel = np.ones((5,5), np.uint8)

img_cvt = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_cvt, (11, 11), 0)
img_canny = cv2.Canny(img_cvt, 100, 100)
img_dia = cv2.dilate(img_canny, kernel, iterations = 5)
img_eroded = cv2.erode(img_dia, kernel, iterations = 5)

cv2.imshow("Gray Image", img_cvt)
cv2.imshow("Blur Image", img_blur)
cv2.imshow("Canny Image", img_canny)
cv2.imshow("Dialation Image", img_dia)
cv2.imshow("Erode Image", img_eroded)
cv2.waitKey(0)
cv2.destroyAllWindows()