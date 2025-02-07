import cv2
import numpy as np
import os

# Global variables to store the selected colors
selected_color_1 = None
selected_color_2 = None
color_count = 0  # Variable to keep track of color selection
image_files = []  # List to hold all image paths in the folder
current_image_index = 0  # Index to keep track of the current image being processed
image = None  # Current image being processed
preview_image = None  # Image for the preview window

# Folder containing the images to process
folder_path = '/home/intellection/Intellection/local/python_tests/tile_analyser_openCV/in/Handmade/'  # Update with your folder path

# Mouse callback function to select colors
def select_color(event, x, y, flags, param):
    global selected_color_1, selected_color_2, color_count, image, preview_image

    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the color of the clicked pixel (in BGR format)
        selected_color = image[y, x]
        print(f"Selected color: {selected_color}")

        if color_count == 0:
            # First color selection
            selected_color_1 = selected_color
            color_count = 1
            print("First color selected. Click to select the second color or press 'Esc' to finish.")
        
        elif color_count == 1:
            # Second color selection
            selected_color_2 = selected_color
            color_count = 2
            print("Second color selected.")
        
        elif color_count == 2:
            # If both colors are selected, clicking the third time resets the selection
            selected_color_1 = None
            selected_color_2 = None
            color_count = 0
            print("Color selection reset.")
        
        # Preview the result in real-time
        preview_result()

# Process the image to display selected colors on a white background
def process_image():
    global selected_color_1, selected_color_2, image, current_image_index

    # Ensure that color 1 has been selected before proceeding
    if selected_color_1 is None:
        print("Error: No first color selected!")
        return None

    # Create a white background (same size as the original image)
    white_background = np.ones_like(image) * 255

    # Create masks for both selected colors (with a tolerance of 20)
    lower_bound_1 = np.array([max(c - 20, 0) for c in selected_color_1])  # Tolerance for first color
    upper_bound_1 = np.array([min(c + 20, 255) for c in selected_color_1])

    mask_1 = cv2.inRange(image, lower_bound_1, upper_bound_1)

    # If second color is selected, create a mask for the second color
    if selected_color_2 is not None:
        lower_bound_2 = np.array([max(c - 20, 0) for c in selected_color_2])  # Tolerance for second color
        upper_bound_2 = np.array([min(c + 20, 255) for c in selected_color_2])
        mask_2 = cv2.inRange(image, lower_bound_2, upper_bound_2)

        # Create the final output image
        result_image = white_background.copy()
        result_image[mask_1 > 0] = [0, 0, 0]  # Set first color (black)
        result_image[mask_2 > 0] = [169, 169, 169]  # Set second color (gray)
    else:
        # If no second color selected, just use the first color (black)
        result_image = white_background.copy()
        result_image[mask_1 > 0] = [0, 0, 0]  # Set first color (black)

    # Convert the image to grayscale for the output
    gray_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2GRAY)

    return gray_image

# Real-time preview of the result
def preview_result():
    global selected_color_1, selected_color_2, image, preview_image

    # Ensure that color 1 has been selected before proceeding
    if selected_color_1 is None:
        preview_image = np.ones_like(image) * 255  # Reset preview to white
        cv2.imshow('Preview', preview_image)
        return

    # Create a white background (same size as the original image)
    white_background = np.ones_like(image) * 255

    # Create masks for both selected colors (with a tolerance of 20)
    lower_bound_1 = np.array([max(c - 20, 0) for c in selected_color_1])  # Tolerance for first color
    upper_bound_1 = np.array([min(c + 20, 255) for c in selected_color_1])

    mask_1 = cv2.inRange(image, lower_bound_1, upper_bound_1)

    # If second color is selected, create a mask for the second color
    if selected_color_2 is not None:
        lower_bound_2 = np.array([max(c - 20, 0) for c in selected_color_2])  # Tolerance for second color
        upper_bound_2 = np.array([min(c + 20, 255) for c in selected_color_2])
        mask_2 = cv2.inRange(image, lower_bound_2, upper_bound_2)

        # Create the preview image
        preview_image = white_background.copy()
        preview_image[mask_1 > 0] = [0, 0, 0]  # Set first color (black)
        preview_image[mask_2 > 0] = [169, 169, 169]  # Set second color (gray)
    else:
        # If no second color selected, just use the first color (black)
        preview_image = white_background.copy()
        preview_image[mask_1 > 0] = [0, 0, 0]  # Set first color (black)

    # Convert preview image to grayscale for display
    preview_gray = cv2.cvtColor(preview_image, cv2.COLOR_BGR2GRAY)

    # Display the preview image
    cv2.imshow('Preview', preview_gray)

# Load the next image from the folder
def load_next_image():
    global selected_color_1, selected_color_2, color_count, image, preview_image

    if current_image_index < len(image_files):
        image_path = image_files[current_image_index]
        image = cv2.imread(image_path)

        if image is None:
            print(f"Error: Unable to load image {image_path}")
            return

        selected_color_1 = None
        selected_color_2 = None
        color_count = 0

        # Initialize preview as soon as the image is loaded
        preview_result()

        # Display the image
        cv2.imshow('Original Image', image)

        # Set the mouse callback function for selecting colors
        cv2.setMouseCallback('Original Image', select_color)

# Load the previous image from the folder
def load_previous_image():
    global current_image_index  # Declare the global variable
    if current_image_index > 0:
        current_image_index -= 1
        load_next_image()

# Process the image and save it
def save_image():
    global selected_color_1, selected_color_2, image, current_image_index

    # Process the image to get the final result
    processed_image = process_image()

    if processed_image is None:
        print("Error: Cannot save image, no first color selected!")
        return

    # Save the processed image in a subfolder named "processed_images"
    image_filename = os.path.basename(image_files[current_image_index])
    processed_folder = os.path.join(folder_path, 'processed_images', os.path.splitext(image_filename)[0])

    if not os.path.exists(processed_folder):
        os.makedirs(processed_folder)

    # Generate a unique filename for each export of the same image
    existing_files = os.listdir(processed_folder)
    num_existing_files = len([f for f in existing_files if f.startswith('processed_image')])

    output_path = os.path.join(processed_folder, f'processed_image_{num_existing_files + 1}.jpg')
    cv2.imwrite(output_path, processed_image)
    print(f"Processed image saved as '{output_path}'.")

# Load images from the folder
def load_images_from_folder():
    global image_files
    image_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    if len(image_files) == 0:
        print(f"No images found in folder: {folder_path}")
    else:
        load_next_image()

# Start processing images in the folder
load_images_from_folder()

# Wait for user to press a key to skip the current image or process
while current_image_index < len(image_files):
    key = cv2.waitKey(0) & 0xFF
    
    if key == 27:  # ESC key to skip
        print("Skipping to next image...")
        current_image_index += 1
        if current_image_index < len(image_files):
            load_next_image()
        else:
            break
    elif key == ord('n'):  # 'N' key to move to the next image
        print("Moving to next image...")
        current_image_index += 1
        if current_image_index < len(image_files):
            load_next_image()
        else:
            break
    elif key == ord('b'):  # 'B' key to move to the previous image
        print("Moving to previous image...")
        load_previous_image()
    elif key == ord('p'):  # 'P' key to save image and move to the next
        save_image()
    elif key == ord('q'):  # 'Q' key to quit the program gracefully
        print("Exiting program...")
        break

cv2.destroyAllWindows()

