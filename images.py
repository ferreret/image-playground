from ctypes import resize
from PIL import Image, ImageFilter

img = Image.open('./images/pikachu.jpg')

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save("./images/smooth_pikachu.jpg", "png")

gray_scale_image = img.convert('L')
gray_scale_image.save("./images/gray_pikachu.jpg", "png")

crooked = filtered_img.rotate(90)

resize = filtered_img.resize((300, 300))

resize.show()
