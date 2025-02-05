import os
import random
from PIL import Image, ImageOps
 
def compress_images(input_folder, quality=30):
    # Validate input folder
    if not os.path.isdir(input_folder):
        print(f"❌ Invalid folder path: {input_folder}")
        return

    # Set the output folder to the parent directory of the input folder
    parent_dir, folder_name = os.path.split(os.path.abspath(input_folder))
    output_folder = os.path.join(parent_dir, f"compressed-{folder_name}")
    os.makedirs(output_folder, exist_ok=True)
    
    # if output folder is not empty, add random number to the folder name
    if os.listdir(output_folder):
        output_folder = os.path.join(parent_dir, f"compressed-{folder_name}-{random.randint(1, 100)}")
        os.makedirs(output_folder, exist_ok=True)
        
    # Valid image extensions to compress
    valid_extensions = ('.jpg', '.jpeg', '.png', '.webp')

    # Get the list of image files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(valid_extensions)]
 
    if not image_files:
        print(f"❌ No image files found in the folder: {input_folder} Supported image formats: JPG, PNG, WebP.")
        return

    print(f"📂 {len(image_files)} images are being compressed...")

    for file_name in image_files:
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, file_name)

        try:
            with Image.open(input_path) as img:
                # Apply EXIF rotation if necessary
                img = ImageOps.exif_transpose(img)

                # Save the image with the same format if it's PNG
                if img.format == "PNG":
                    img.save(output_path, optimize=True)
                else:
                    img.save(output_path, quality=quality)

                # Keep the original file's metadata
                os.utime(output_path, (os.path.getatime(input_path), os.path.getmtime(input_path)))

                print(f"✅ {file_name} → compressed")
        except Exception as e:
            print(f"❌ Error occurred while processing {file_name}: {e}")

    print(f"\n🎉 Compressed images are saved in: {output_folder}")

if __name__ == "__main__":
    folder_path = input("📂 Enter the absolute path of the image folder to compress: ").strip()
    compress_images(folder_path)
