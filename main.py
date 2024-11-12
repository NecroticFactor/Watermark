from PIL import Image, ImageDraw, ImageFont
import os
import sys


# Get the image path through sys argv
def get_path():
    if len(sys.argv) < 2:
        print("Please add source directory")
        sys.exit(1) 
    elif len(sys.argv) > 2:
        print("Too many arguments")
        sys.exit(1)
    else:
        return sys.argv[1]


# Check if image path exists
def validate_path(source_path):
    if os.path.exists(source_path) and os.path.isdir(source_path):
        return True
    else:
        print("Directory doesn't exist")
        sys.exit(1)  


# Retrieve the image width
def get_image_width(path):
    image_width = []
    files = os.listdir(path)
    
    if not files:
        print("No files found in the directory.")
        sys.exit(1)

    for filename in files:
        filename = filename.lower()
        if filename and filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img_path = os.path.join(path, filename)
            try:
                with Image.open(img_path) as img:
                    width = img.width
                    image_width.append(width)
            except IOError:
                print(f"Error opening {filename}, skipping...")

    return image_width


# Retrive the watermark width
def get_watermark_width(w_path=None):
    if w_path is None:
        while True:
            w_path = input("Enter the path containing the watermark: ")
            if validate_path(w_path):  # Check if the path is valid
                break  # Exit loop once the path is validated
            else:
                print("Invalid path, please try again.")

    for filename in os.listdir(w_path):
        print(w_path)
        if filename.endswith('.png'):
            watermark_path = os.path.join(w_path, filename)
            print(watermark_path)
            try:
                with Image.open(watermark_path) as img:
                    width = img.width
                    print(width)
                    return width
            except IOError:
                print(f"Error opening {filename}, skipping...")

    print("No valid watermark image found in the directory.")
    return None  # Return None if no valid watermark image is found



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
        
        # Create a new image with transparent background (RGBA mode)
        image = Image.new("RGBA", (w, h), (0, 0, 0, 0))  # (0, 0, 0, 0) is fully transparent

        # Create a drawing context
        draw = ImageDraw.Draw(image)

        # Add some text to the image
        # Load a better font if available, or use default
        try:
            font = ImageFont.truetype("arial.ttf", size=30)  # You can adjust the font size
        except IOError:
            font = ImageFont.load_default()  # Fallback to default font if TTF is not available

        text = input("Enter the copyright text: ")
        draw.text((50, 50), text + "©", font=font, fill=(255, 255, 255, 128))  # Semi-transparent white text

        # Loop until a valid path is provided
        while True:
            save_path = input("Enter the path to store the watermark: ")
            if validate_path(save_path):
                # Save the image as a PNG (preserves transparency)
                try:
                    watermark_path = os.path.join(save_path, "watermark.png")
                    image.save(watermark_path)
                    print(f"Watermark saved at {watermark_path}")
                    get_watermark_width(save_path)
                except Exception as e:
                    print(f"Error saving the image: {e}")
                    break  
            else:
                print("Invalid path, please try again.")
        break



# Check if user has a watermark
def get_watermark():
    while True:
        choice = input("Do you have a watermark? If not, enter 'n' to create or else 'y': ").lower().strip()
        if choice == 'y':
           return get_watermark_width()
            
        elif choice == 'n':
            return create_watermark()           
        else:
            print("Invalid response")
    



# Entry point of application
def entry():
    # Get the source path
    source_path = get_path()

    # Validate source path
    if not validate_path(source_path):
        return  # Exit if the source path is not valid

    # Get the image width for the source images
    image_width = get_image_width(source_path)

    # Get the watermark width
    watermark_width = get_watermark()

    # Proceed with further processing, such as applying the watermark
    print(f"Image width: {image_width}")
    print(f"Watermark width: {watermark_width}")




def main():
    try:
        entry()
    except EOFError:
        sys.exit("\nExiting application...")
        

if __name__ == "__main__":
    main()