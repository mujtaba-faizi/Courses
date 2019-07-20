from PIL import Image
from PIL import ImageFilter
im1 = Image.open('F:\Pics & Videos\NUST Events 2017\CS-5A\_DSC6837(1).jpg').convert('LA')
im1.show()
im = Image.open('Mujtaba.jpg')
im2=im.filter(ImageFilter.SMOOTH).show()
im2=im.filter(ImageFilter.SHARPEN).show()
