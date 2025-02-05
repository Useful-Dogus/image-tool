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

## Generate Image Sequence Generator

### Usage

1. Install required packages:

   ```sh
   pip install -r requirements.txt
   ```

2. Run the script

   ```sh
   python generate_sequence_video.py
   ```

3. Follow the instructions to enter the folder path containing images, output video file name, and desired frame duration in milliseconds. The script will create a video sequence from the images in the folder.

4. Check the generated video in the same folder as the input images.

### Features

- Supports JPG, PNG, and JPEG formats.
- Resizes and centers images to fit a 1280x720 resolution while preserving aspect ratio, adding black borders as necessary.
- Automatically adjusts image orientation using EXIF data.
- Creates a video where each image is shown for a specified duration.
- Supports output video in MP4 format with H.264 or MJPEG encoding.

### Requirements

- Python 3.x
- OpenCV (for video processing)
- Pillow (for image processing)
- Numpy (for array manipulation)
