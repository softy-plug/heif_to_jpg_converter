import os
from PIL import Image

# Prompt user for folders
heif_folder = input('Enter the folder with heif images: ')
jpg_folder = input('Enter folder to save converted jpg images: ')

# Check if folders exists, else create them
if not os.path.exists(jpg_folder):
    os.makedirs(jpg_folder)

# Loop through all files in the heif folder
for file_name in os.listdir(heif_folder):
    if file_name.endswith('.heif'):
        # Open heif image and convert to RGB
        heif_image = Image.open(os.path.join(heif_folder, file_name))
        heif_image = heif_image.convert('RGB')

        # Create new jpg file name
        jpg_file_name = os.path.splitext(file_name)[0] + '.jpg'
        jpg_file_path = os.path.join(jpg_folder, jpg_file_name)

        # Save jpg image with maximum quality
        jpg_image = heif_image.save(jpg_file_path, 'JPEG', quality=100)

print('All heif images in {} converted to jpg and saved in {}.'.format(heif_folder, jpg_folder))

#softy_plug