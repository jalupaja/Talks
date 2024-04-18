# https://www.tutorialspoint.com/python_pillow/python_pillow_creating_a_watermark.htm

#Import required Image library
from PIL import Image, ImageDraw, ImageFont

#Create an Image Object from an Image
im = Image.open('images/OTH.jpg')
width, height = im.size

draw = ImageDraw.Draw(im)
text = "sample watermark"

font = ImageFont.truetype('arial.ttf', 36)
textwidth, textheight = draw.textsize(text, font)

# calculate the x,y coordinates of the text
margin = 10
x = width - textwidth - margin
y = height - textheight - margin

# draw watermark in the bottom right corner
draw.text((x, y), text, font=font)
im.show()

#Save watermarked image
im.save('watermarked_images/website.png')
