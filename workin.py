import cv2
import numpy as np


def inpaint_colored_image(image, start_point, end_point):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Extract the marked area
    marked_area = gray_image[start_point[1]:end_point[1], start_point[0]:end_point[0]]

    # Iterate from the bottom to the top of the marked area
    for y in range(end_point[1] - 1, start_point[1], -1):
        for x in range(start_point[0], end_point[0]):
            below_pixel = marked_area[y - start_point[1], x - start_point[0]]
            boundary_pixel = marked_area[-1, x - start_point[0]]

            # Linear interpolation between boundary color and color below
            fill_color = np.round(np.linspace(boundary_pixel, below_pixel, 1)).astype(int)

            # Update the pixel value in the original grayscale image
            gray_image[y, x] = fill_color[0]

    # Create a mask to identify the marked region
    mask = np.zeros_like(image, dtype=np.uint8)
    cv2.rectangle(mask, start_point, end_point, (255, 255, 255), thickness=cv2.FILLED)

    # Inpaint the marked region using the Navier-Stokes equation
    inpainted_result = cv2.inpaint(image, mask[:, :, 0], inpaintRadius=3, flags=cv2.INPAINT_TELEA)

    return inpainted_result

# Load a color image
image_path = r'path of the image'  # Replace with the path to your image
image = cv2.imread(image_path)

# Create a named window and set the callback function for marking the area
cv2.namedWindow("Mark Area")
start_point = None
end_point = None
top_left_clicked = False

def draw_rectangle(event, x, y, flags, param):
    global start_point, end_point, top_left_clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        if top_left_clicked:
            # If already clicked, reset the points
            start_point = None
            end_point = None
            top_left_clicked = False

        # Mark the starting point
        start_point = (x, y)
        top_left_clicked = True

    elif event == cv2.EVENT_LBUTTONUP:
        # Mark the ending point
        end_point = (x, y)
        top_left_clicked = False

# Set the callback function for marking the area
cv2.setMouseCallback("Mark Area", draw_rectangle)

# Display the color image for marking the area
while True:
    clone = image.copy()

    if start_point and end_point:
        cv2.rectangle(clone, start_point, end_point, (255, 255, 255), 2)

    cv2.imshow("Mark Area", clone)

    # Break the loop if 'Esc' key is pressed
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()

# Check if a valid area is marked
if start_point and end_point:
    # Perform inpainting on the color image with linear interpolation
    inpainted_result = inpaint_colored_image(image.copy(), start_point, end_point)

    # Display the inpainted color image
    cv2.imshow("Inpainted Image", inpainted_result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No valid area marked.")
