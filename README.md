
# Watermarking Image Tool

This Python tool allows users to add a watermark to multiple images in a specified folder. It provides functionality to either upload an existing watermark or create a new one. The watermark is applied to the images in the selected folder and saved to the output folder.

## Features

- Create a custom watermark with user-defined text and size.
- Add a watermark to multiple images in a folder.
- Specify input and output folders.
- Supports multiple image formats: `.png`, `.jpg`, `.jpeg`.
- Interactive command-line interface for easy use.

## Requirements

To run this project, you need Python 3 and the following Python libraries:

- Pillow (for image processing)
- tqdm (for displaying a progress bar)

You can install these dependencies using pip:

```bash
pip install pillow tqdm
```

## Setup Instructions

1. Clone the repository or download the project files.
2. Ensure you have Python 3 installed on your machine.
3. Install the required dependencies:
   
   ```bash
   pip install pillow tqdm
   ```

4. Run the script using the command below:

   ```bash
   python watermark_tool.py
   ```

5. Follow the prompts in the terminal to:
   - Specify the input folder containing the images.
   - Specify the output folder for saving watermarked images.
   - Create or provide an existing watermark image.
   - Add the watermark to your images.

## Customization Guide

If you're not familiar with coding, you can easily adjust the watermark's **font**, **size**, **position**, **padding**, and other measurements by modifying specific lines in the code. Here’s how you can customize these settings:

### 1. **Font**
You can change the font of the watermark text by modifying **line 24** in the `watermark_tool.py` file. Update the `font_path` variable to the path of the font you want to use.

**Line to Modify:**
```python
font_path = "/System/Library/Fonts/Supplemental/Copperplate.ttc"
```

Make sure the font path points to a valid font file on your system (you can find system fonts or use custom ones). If `arial.ttf` does not work, you can use any `.ttf` or `.ttc` font file.

### 2. **Font Size**
You can change the size of the watermark text by modifying **line 28**. Update the `size` parameter to your desired font size.

**Line to Modify:**
```python
font = ImageFont.truetype(font_path, size=200)
```

You can adjust `size=200` to any number to increase or decrease the font size.

### 3. **Position of the Watermark**
The position of the watermark on the image can be adjusted by modifying **line 52**. You can change the `(50, 50)` tuple to control where the watermark appears on the image.

**Line to Modify:**
```python
draw.text((50, 50), "©" + text, font=font, fill=(255, 255, 255, 128))
```

The tuple `(50, 50)` specifies the coordinates where the watermark is placed. Increase or decrease the values to move the watermark around the image. For example, `(100, 100)` would shift the watermark further to the right and down.

### 4. **Padding for the Watermark**
The padding between the watermark and the edges of the image is defined in **line 74**. You can modify the `padding` value to adjust how far the watermark is placed from the edges of the image.

**Line to Modify:**
```python
position = (image_width - watermark_width - padding, image_height - watermark_height - padding)
```

To change the padding, simply adjust the `padding` value (currently set to `10`). Increasing the padding value will move the watermark further away from the edges.

### 5. **Adjusting Watermark Transparency**
If you want to adjust the transparency of the watermark, modify the `fill` parameter in **line 52**.

**Line to Modify:**
```python
draw.text((50, 50), "©" + text, font=font, fill=(255, 255, 255, 128))
```

In the `fill=(255, 255, 255, 128)` tuple:
- The first three values `(255, 255, 255)` control the RGB color of the watermark (white in this case).
- The last value `128` controls the transparency. You can set this value from `0` (fully transparent) to `255` (fully opaque).

### 6. **Watermark Image Size**
The size of the watermark image is created based on user input during the watermark creation process. You can adjust the width (`w`) and height (`h`) when creating the watermark.

**Line to Modify (in the `create_watermark` function):**
```python
w = int(input("Enter the width of the watermark: "))
h = int(input("Enter the height of the watermark: "))
```

### Example Adjustments

- To change the font to a custom one, update the `font_path`.
- To change the watermark's font size, modify the `size` parameter.
- To move the watermark further to the left, change the `(50, 50)` position to something like `(10, 50)`.
- To add more space around the watermark, increase the `padding` value.

