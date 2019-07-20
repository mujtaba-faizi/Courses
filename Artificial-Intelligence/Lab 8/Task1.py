from PIL import Image
im = Image.open('F:\Pics & Videos\NUST Events 2017\CS-5A\_DSC6837(1).jpg').convert('LA')
rot=im.rotate(45)
rot.show()

