import os
from PIL import Image

def resize_image(input_path, output_path, scale_factor=0.50):
    """Resize the image at the input path and save it to the output path."""
    with Image.open(input_path) as img:
        print(f"Resizing image: {input_path}")
        # Ensure transparency is preserved if the image has an alpha channel
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            img = img.convert("RGBA")
        new_size = tuple([int(dim * scale_factor) for dim in img.size])
        # Use Image.Resampling.LANCZOS for high-quality downsampling
        resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
        resized_img.save(output_path)
        print(f"Saved SWAG resized image to: {output_path}")

def process_folder(input_folder, output_folder):
    """Resize images in all subfolders of the input folder."""
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                input_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_path, input_folder)
                output_path = os.path.join(output_folder, relative_path)

                # Create the output directory if it doesn't exist
                os.makedirs(os.path.dirname(output_path), exist_ok=True)

                resize_image(input_path, output_path)
            else:
                print(f"Skipping non-image file: {file}")

# Define the input and output folders
input_folder = r'REPLACE'  # Your specified input directory
output_folder = r'REPLACE'  # Your specified output directory

print(f"Starting processing of folder: {input_folder}")
process_folder(input_folder, output_folder)
print("HELL YEAH MY BOI.")
