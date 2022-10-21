#Copilot still can't do ascii art, it has to evolve to do that.
#This is what you get if you try to do an ascii art with copilot in 21/10/2022 (first test with copilot with images)

#converts a given image to an array of romaji chars
#useful for making ascii art
#requires the copilot module

from copilot import * #pip install copilot
from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw


fileInput = "./pythonComponentes/memeYaoMing.jpg"
fileOutput = "./pythonComponentes/memeYaoMingConverted.jpg"

#load image
img = Image.open(fileInput)
#convert to greyscale
img = img.convert("L")
#invert
img = ImageOps.invert(img)
#resize
img = img.resize((500,500),Image.NEAREST)
#convert to array
arr = img.load()
#make a new image
img2 = Image.new("RGB",(500,500),(255,255,255))
#load array
arr2 = img2.load()
#loop through pixels
for x in range(500):
    for y in range(500):
        #get pixel
        px = arr[x,y]
        #set pixel to black if it's black
        if px < 127:
            arr2[x,y] = (0,0,0)
#save image
img2.save(fileOutput)
