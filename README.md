# EXIF Remover

Needed to remove EXIF data to use personal images on a website. This Python script will batch remove EXIF data from images in the current directory and saves the processed images to a new folder called `processed`. It will provide feedback for each image processed - I ran into an issue initially with WebP images and added this to debug.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone the repository or download the script.
2. Navigate to the directory containing the script.
3. Install the required dependencies using `pip`:

## Usage

1. Place the script in the directory containing the images you want to process.
2. Run the script:

    ```sh
    python remexif.py
    ```

The script will process all PNG, JPG, JPEG, and WebP images in the current directory, remove their EXIF data, and save the processed images to a new folder called `processed`. You can add other file types as needed - as long as they are supported by Pillow.

## Example

```sh
$ python remexif.py
Processing /path/to/your/image1.jpg
Successfully processed /path/to/your/image1.jpg
Processing /path/to/your/image2.png
Successfully processed /path/to/your/image2.png
Processing /path/to/your/image3.webp
Successfully processed /path/to/your/image3.webp
Skipped /path/to/your/document.txt: Unsupported file type
