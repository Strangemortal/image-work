import tkinter as tk
from tkinter import filedialog
import cv2 as cv
from PIL import Image, ImageTk 

def inpaint_image():
    img_path = filedialog.askopenfilename(title="Select Image",
             filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    mask_path = filedialog.askopenfilename(title="Select Mask",
             filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

    if img_path and mask_path:
        img = cv.imread(img_path)
        mask = cv.imread(mask_path, cv.IMREAD_GRAYSCALE)

        if img is None or mask is None or img.shape[:2] != mask.shape:
            result_label.config(text="Error: Invalid images or dimensions")
        else:
            dst = cv.inpaint(img, mask, 2, cv.INPAINT_TELEA)
            display_image(dst)

def display_image(image):
    # Resize the image for display
    scale_factor = 2
    height, width = image.shape[:2]
    new_height, new_width = int(height * scale_factor), int(width * scale_factor)
    resized_image = cv.resize(image, (new_width, new_height))

    # Convert to RGB and create a PhotoImage
    resized_image = cv.cvtColor(resized_image, cv.COLOR_BGR2RGB)
    resized_image = Image.fromarray(resized_image)
    photo = ImageTk.PhotoImage(image=resized_image)

    # Update the label with the resized image
    result_label.config(image=photo)
    result_label.image = photo

# Create the main window
app = tk.Tk()
app.title("Image Inpainting App")

# Create a button to trigger inpainting
inpaint_button = tk.Button(app, text="Inpaint Image",command=inpaint_image)
inpaint_button.pack(pady=10)

# Create a label to display the inpainted image
result_label = tk.Label(app)
result_label.pack()

# Start the main loop
app.mainloop()

