# Watermark Application

## Description
This script allows users to apply a watermark to an image. The watermark image should be in PNG format and can be placed at various positions on the base image. The script uses the `cv2` and `numpy` libraries.

## How to Use
1. **Installation**:
   - Install Python if you haven't already. You can download it from [python.org](https://www.python.org/downloads/).
   - Install required libraries by running:
     ```
     pip install opencv-python numpy
     ```

2. **Running the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script `mark.py`.
   - Run the script using the command:
     ```
     python mark.py
     ```

3. **Using the Script**:
   - You need to provide the paths for the input image, the watermark image, and the output image. You also need to specify the position of the watermark on the image. The position can be 'center', 'bottom_right', 'top_left', 'top_right', or 'bottom_left'.
   - For example, you can run the script as follows:
     ```
     apply_watermark('path to your input image', 'path to your watermark image (png only)', 'output.jpg', 'bottom_right')
     ```

4. **Note**:
   - The watermark image must have an alpha channel (4 channels).
   - If the watermark image is larger than the base image, it will be scaled down to 5% of its original size.
   - If an invalid position argument is provided, a ValueError will be raised.