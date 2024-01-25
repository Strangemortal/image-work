import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image from file
image_path = 'path of image' 
original_image = cv2.imread(image_path)

# Convert the image to grayscale
gray_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to the grayscale image
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 30)

# Apply Laplacian operator for edge detection
laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)

# Convert the Laplacian result to uint8 (8-bit) image
laplacian = np.uint8(np.absolute(laplacian))

# Display the original, grayscale, blurred, and edges images
plt.figure(figsize=(12, 4))

plt.subplot(141), plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)), plt.title('Original')
plt.subplot(142), plt.imshow(gray_image, cmap='gray'), plt.title('Grayscale')
plt.subplot(143), plt.imshow(blurred_image, cmap='gray'), plt.title('Blurred')
plt.subplot(144), plt.imshow(laplacian, cmap='gray'), plt.title('Laplacian Edge Detection')

plt.show()
