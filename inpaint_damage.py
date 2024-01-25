import cv2 
import numpy as np
import matplotlib.pyplot as plt

def detect_damage(image):
    # Convert the image to grayscale for simplicity
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary mask of damaged regions
    _, binary_mask = cv2.threshold(grayscale_image, 200, 1, cv2.THRESH_BINARY_INV)

    # Invert the colors of the binary mask (color inversion)
    inverted_mask = 1 - binary_mask

    return inverted_mask

def inpaint_image(image, mask):
    # Convert the mask to an 8-bit 1-channel image
    mask = (mask * 255).astype(np.uint8)

    # Inpaint the damaged region using the Navier-Stokes equation
    inpainted_result = cv2.inpaint(image, mask, 25, cv2.INPAINT_TELEA)

    return inpainted_result

# Load the colored image
image = cv2.imread(r'path of the image ')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB for Matplotlib

# Detect damage in the image
damage_mask = detect_damage(image)

# Inpaint the damaged region
inpainted_result = inpaint_image(image, damage_mask)

# Display the results
plt.figure(figsize=(13, 5))
plt.subplot(131)
plt.imshow(image)
plt.title('Original Image')

plt.subplot(132)
plt.imshow(damage_mask, cmap='gray')
plt.title('auto generated Mask')

plt.subplot(133)
plt.imshow(inpainted_result)
plt.title('Inpainted Result')

plt.show()

