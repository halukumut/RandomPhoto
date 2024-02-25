import os
import random
from PIL import Image

path=("C:/Users/haluk/OneDrive/Photos") #ABSOLUTE PATH

files = os.listdir(path)
random_image = random.choice(files)
image_path = os.path.join(path,random_image)
img = Image.open(image_path)
img.show()
