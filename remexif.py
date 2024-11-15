from PIL import Image
import os

def remove_exif(image_path, output_path):
    try:
        image = Image.open(image_path)
        data = list(image.getdata())
        image_without_exif = Image.new(image.mode, image.size)
        image_without_exif.putdata(data)
        image_without_exif.save(output_path, format=image.format)
        print(f"Successfully processed {image_path}")
    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def batch_remove_exif():
    input_folder = os.getcwd()
    output_folder = os.path.join(input_folder, 'processed')
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            print(f"Processing {file_path}")
            output_path = os.path.join(output_folder, filename)
            remove_exif(file_path, output_path)
        else:
            print(f"Skipped {filename}: Unsupported file type")

if __name__ == "__main__":
    batch_remove_exif()