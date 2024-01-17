from PIL import Image
import os

# Directory path containing the PNG files
directory = 'qrs'

# Create a list to store the image frames
images = []

# Keep track of the previous image size
prev_size = None

# Create a blank image with a white background
blank_img = Image.new('RGB', (300, 300), (255, 255, 255))

# Iterate over the PNG files in the directory
for filename in sorted(os.listdir(directory)):
    if filename.endswith('.png'):
        # Open the image
        img = Image.open(os.path.join(directory, filename))

        # Convert the image to RGB mode
        img = img.convert('RGB')

        # Resize the image to a consistent size (e.g., 300x300)
        img = img.resize((300, 300))

        # Check if the current image is smaller than the previous one
        if prev_size is not None and img.size < prev_size:
            # Add the blank image
            images.append(blank_img)

        # Add the current image to the list
        images.append(img)

        # Update the previous image size
        prev_size = img.size

# Save the animated GIF
try:
    images[0].save('animated.gif', save_all=True, append_images=images[1:], duration=1000, loop=0)
except AttributeError as e:
    print("Error occurred with image:", images[0])
    raise e
