# Tile Analyzer - Color Selection and Image Processing with OpenCV

## Overview

This Python script allows users to interactively select colors in images, preview the selected colors on a white background, and save the processed results. It utilizes OpenCV for image processing and mouse event handling, making it ideal for color analysis tasks where specific colors need to be highlighted or removed. The script processes all images in a specified folder, allowing users to move between images, select up to two colors, and save the results.

## Key Features

- **Interactive Color Selection**: Select up to two colors by clicking on the image.
- **Real-Time Preview**: Instantly see the preview of the selected colors on a white background.
- **Multiple Image Processing**: Navigate through a folder of images, process them one by one.
- **Error Handling**: Ensures that no actions are performed until the first color is selected.
- **Save Processed Images**: Save the processed images in a subfolder called `processed_images`.
- **Navigation Controls**: Move between images using the keyboard (next, previous, or skip).
- **Customizable Folder Path**: Easily update the folder path to point to your image folder.

## Requirements

- **Python 3.x**
- **OpenCV** (`opencv-python` package)
- **NumPy** (`numpy` package)

### Installation

To install the required dependencies, run the following command:

```bash
pip install opencv-python numpy
```
### Script Breakdown

- Folder Setup

    - Images Folder: The script processes all images in the specified folder (folder_path). You should place the images you wish to process in this folder.
    - Processed Folder: The processed images will be saved in a subfolder named processed_images inside the original folder.

- Color Selection

    - First Color: Click on any pixel of the image to select the first color.
    - Second Color: After selecting the first color, click on another pixel to select the second color.
    - Reset: If both colors are selected, clicking on a third pixel will reset the color selection.
    - Color Tolerance: The script uses a tolerance of 20 in BGR space to include colors similar to the ones selected.

###Real-Time Preview

Once the colors are selected, the script displays a preview where the selected colors are highlighted on a white background:

    - Black (0, 0, 0) for the first selected color.
    - Gray (169, 169, 169) for the second selected color.

### Image Navigation

    - Next Image: Press the n key to move to the next image.
    - Previous Image: Press the b key to go back to the previous image.
    - Skip Image: Press the ESC key to skip the current image and move to the next one.

### Saving Processed Images

Once you've selected the colors and previewed the result, you can save the processed image by pressing the p key. The processed image will be saved in the processed_images folder under a unique name for each version of the same image.

### Exiting the Program

- To quit the program, press the q key.

### How to Use the Script

  - Update the Folder Path: Change the folder_path variable to the directory where your images are stored. For example:

```
folder_path = '/path/to/your/images/'
```

Run the Script: Execute the Python script by running the following command:
```
    python3 tile_analyser.py
```
  - Select Colors: Click on the image to select the colors:
  - First Color: Click on any pixel in the image to select the first color.
  - Second Color: After selecting the first color, click on another pixel to select the second color.
  - Reset: Click on a third pixel to reset the color selection.
  - Preview the Result: As you select colors, the preview window will update in real-time to show how the selected colors appear on a white background.
  - Process the Image: Once both colors are selected, you can press the p key to save the processed image.
  - Navigate Between Images:
        Next Image: Press the n key to move to the next image in the folder.
        Previous Image: Press the b key to go to the previous image.
        Skip Image: Press the ESC key to skip the current image.
  -Exit the Program: Press the q key to exit the script.

### Example Usage

```
$ python tile_analyser.py
```

### Controls During Execution

  - n: Move to the next image.
  - b: Move to the previous image.
  - ESC: Skip to the next image.
  - p: Save the processed image.
  - q: Quit the program.

### Folder Structure

The folder should have the following structure:
```
/path/to/images/
    ├── image1.jpg
    ├── image2.jpg
    ├── ...
    └── processed_images/
        └── image1/
            ├── processed_image_1.jpg
            └── processed_image_2.jpg
```
  - Original Images: All images in the specified folder will be processed.
  - Processed Images: Processed images will be saved in a processed_images subfolder, under a subfolder named after the original image file (without the extension).

### Error Handling

  - The script ensures that both colors are selected before performing any processing.
  - If no first color is selected, it will not process the image and print an error message.
  - If there are issues with loading an image, an error message will be shown.

### Customization

  - Tolerance: The color selection tolerance is set to 20 (in BGR space). You can adjust this value to make the color matching more or less sensitive.

      For example:

      tolerance = 30  # Increase or decrease the tolerance value.

   - Folder Path: Make sure to set the folder_path variable to the correct path where your images are located.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

