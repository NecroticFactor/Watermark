from PIL import Image, ImageDraw, ImageFont
import os
import sys
from tqdm import tqdm

def validate_path(source_path, check_is_dir=False):
    if check_is_dir:
        if os.path.exists(source_path) and os.path.isdir(source_path):
            return True
        else:
            print("Directory doesn't exist")
            return False
    else:
        if os.path.exists(source_path) and os.path.isfile(source_path):
            return True
        else:
            print("File doesn't exist")
            return False

# Create watermark if user doesn't have one
def create_watermark():
    while True:
        try:
            w = int(input("Enter the width of the watermark: "))
        except ValueError:
            print("Invalid width unit. Please enter an integer.")
            continue
        try:
            h = int(input("Enter the height of the watermark: "))
        except ValueError:
            print("Invalid height unit. Please enter an integer.")
            continue

        image = Image.new("RGBA", (w, h), (0, 0, 0, 0))  # Fully transparent image
        draw = ImageDraw.Draw(image)

        font_path = "/System/Library/Fonts/Supplemental/Copperplate.ttc"

        try:
            # Change prefered font and it's size, if .ttc then specify index
            font = ImageFont.truetype(font_path, size=80, index=0)
        except IOError:
             font = ImageFont.load_default()

        text = input("Enter the copyright text: ")

         # fill -> Semi-transparent white text (ADJUST TO ALTER OPACITY)
         # Adjust co-ordinates to position watermark during creation
        draw.text((50, 50), "©" + text, font=font, fill=(255, 255, 255, 180))

        while True:
            save_path = input("Enter the path to store the watermark: ")
            if validate_path(save_path, check_is_dir=True):
                try:
                    watermark_path = os.path.join(save_path, "watermark.png")
                    image.save(watermark_path)
                    print(f"Watermark saved at {watermark_path}")
                    return watermark_path
                except Exception as e:
                    print(f"Error saving the image: {e}")
                    break
            else:
                print("Invalid directory, please try again.")
        break


def process_image_with_watermark(input_image_path, output_image_path, watermark_path, padding):
    # Load the original image and the watermark
    image = Image.open(input_image_path).convert("RGBA")
    watermark = Image.open(watermark_path).convert("RGBA")

    # Get dimensions of both the image and the watermark
    image_width, image_height = image.size
    watermark_width, watermark_height = watermark.size

    # Calculate the position for the watermark (bottom-right corner with padding)
    position = (image_width - watermark_width - padding, image_height - watermark_height - padding)

    # Create a transparent image for combining
    transparent = Image.new("RGBA", image.size)
    transparent.paste(image, (0, 0))
    transparent.paste(watermark, position, mask=watermark)

    # Convert back to RGB if necessary and save the image
    output_image = transparent.convert("RGB")
    output_image.save(output_image_path)


def add_watermark(input_folder, output_folder, watermark_path, padding=10):
    images = [f.lower() for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    print (len(images))

    # Initialize the progress bar
    with tqdm(total=len(images), desc="Adding watermark", unit="image") as pbar:
        for image in images:
            input_image_path = os.path.join(input_folder, image)
            output_image_path = os.path.join(output_folder, image)

            # Apply the watermark using the processing function
            process_image_with_watermark(input_image_path, output_image_path, watermark_path, padding)

            pbar.update(1)



def have_watermark():
    while True:
        choice = input("Do you have a watermark? Enter 'n' to create one, or 'y' to proceed: ").lower().strip()
        if choice == 'n':
            return create_watermark()
        elif choice == 'y':
            return True
        else:
            print("Invalid response. Please enter 'y' or 'n'.")



def entry():
    while True:
        input_folder = input("Enter the path to the images: ").strip()
        if validate_path(input_folder, check_is_dir=True):
            break

    while True:
        output_folder = input("Enter the output path for the images: ").strip()
        if os.path.exists(output_folder):
            break
        else:
            print(f"Output folder '{output_folder}' does not exist. Creating it now.")
            os.makedirs(output_folder)

    if not have_watermark():
        print("No watermark created or provided. Exiting.")
        return

    while True:
        watermark_path = input("Enter the path to the watermark: ").strip()
        if validate_path(watermark_path, check_is_dir=False):
            break
        else:
            print("Invalid watermark path. Please try again.")

    print("Watermark process will begin.")
    add_watermark(input_folder, output_folder, watermark_path, padding=80) # -> Adjust Padding here
    print("Watermark added, please check output directory.")



def main():
    try:
        entry()
    except EOFError:
        sys.exit("\nExiting application...")

if __name__ == "__main__":
    main()