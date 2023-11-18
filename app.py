from email.mime import image
from colorthief import ColorThief

def generate_palette(image_path, num_colors=12):
    color_thief = ColorThief(image_path)
    palette = color_thief.get_palette(color_count=num_colors)

    return palette
Image = "image"
def print_palette(palette):
    print("Color Palette:")
    for color in palette:
        print(f"RGB: {color}, HEX: #{color[0]:02X}{color[1]:02X}{color[2]:02X}")

def visualize_palette(palette):
    width = 50
    height = 50 * len(palette)
    palette_image = Image.new('RGB', (width, height))

    for i, color in enumerate(palette):
        row = Image.new('RGB', (width, 50), color)
        palette_image.paste(row, (0, i * 50))

    palette_image.show()

if __name__ == "__main__":
    # Replace 'your_image.jpg' with the path to your image file
    image_path = 'your_image.jpg'

    palette = generate_palette(image_path)
    print_palette(palette)
    visualize_palette(palette)
