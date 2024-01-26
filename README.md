# Image Resizing Script

This Python script is designed to efficiently resize images located in subfolders of a specified directory. It recursively processes each image, reducing its size by 55% while maintaining transparency, and preserves the original directory structure in the output folder.

## Features

- **Recursive Processing:** Automatically goes through all subfolders in a specified directory.
- **Maintains Transparency:** Preserves the transparency of PNG, GIF, and other formats with alpha channels.
- **Preserves Directory Structure:** Keeps the same folder hierarchy in the output directory as found in the input directory.
- **Support for Common Formats:** Processes .png, .jpg, .jpeg, and .gif files.

## Prerequisites

To use this script, you need Python installed on your system along with the Pillow library, which is used for image processing.

You can install Pillow using pip:
```bash
pip install Pillow
```

## Usage

1. **Download the Script:** Clone or download this repository to your local machine.

2. **Specify Paths:** Open the script in a text editor and set the `input_folder` and `output_folder` variables to your desired input and output paths respectively.

   Example:
   ```python
   input_folder = r'REPLACE'
   output_folder = r'REPLACE'
   ```

3. **Run the Script:** Execute the script in your Python environment. The script will process all images in each subfolder of the specified input directory and save the resized images in the output directory, mirroring the original folder structure.

   ```bash
   python path/to/script.py
   ```

4. **Check Output:** After the script has finished running, check your output directory for the resized images.

