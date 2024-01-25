import cv2
import numpy as np

def print_boundary_conditions(image):
    rows, cols = image.shape[:2]

    # Left boundary
    left_boundary = image[:, 0]
    print(f'Left Boundary Coordinates and Values:')
    for i in range(rows):
        print(f'({i}, 0): {left_boundary[i]}')

    # Right boundary
    right_boundary = image[:, -1]
    print(f'\nRight Boundary Coordinates and Values:')
    for i in range(rows):
        print(f'({i}, {cols - 1}): {right_boundary[i]}')

    # Top boundary
    top_boundary = image[0, :]
    print(f'\nTop Boundary Coordinates and Values:')
    for j in range(cols):
        print(f'(0, {j}): {top_boundary[j]}')

    # Bottom boundary
    bottom_boundary = image[-1, :]
    print(f'\nBottom Boundary Coordinates and Values:')
    for j in range(cols):
        print(f'({rows - 1}, {j}): {bottom_boundary[j]}')

# Load an image
image_path = r'path of the image'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Increase pixel values by 10
increased_image = np.clip(image + 30, 0, 255)

# Decrease pixel values by 10
decreased_image = np.clip(image - 30, 0, 255)

# Display the original, increased, and decreased images
cv2.imshow('Original Image', image)
cv2.imshow('Increased Image', increased_image.astype(np.uint8))
cv2.imshow('Decreased Image', decreased_image.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

# Print boundary conditions for the original image
print_boundary_conditions(image)
