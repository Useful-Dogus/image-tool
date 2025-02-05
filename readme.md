# Image Tool

## Image Compressor

### Usage

1. Install required packages:

   ```sh
   pip install -r requirements.txt
   ```

2. Run the script

   ```sh
   python compress_image.py
   ```

3. Follow the instructions to enter the path, and the script will compress images in the specified folder.

4. Check the compressed images in the output folder (`compressed-<folder_name>`).

### Features

- Supports JPG, PNG, and WEBP formats.
- Automatically adjusts image orientation using EXIF data.
- Optimizes images for reduced file size while preserving quality.

### Requirements

- Python 3.x
- Pillow (for image processing)
