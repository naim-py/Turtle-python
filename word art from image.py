from PIL import Image
Image.open("naim.jpg")
import pywhatkit as py
py.image_to_ascii_art('naim.jpg','MyArt')
read_file= open('MyArt.txt','r')
print(read_file.read())


