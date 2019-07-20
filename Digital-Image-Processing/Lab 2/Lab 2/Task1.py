from PIL import Image

im = Image.open('JIJIJIJJ.png')
print(im.format, im.size, im.mode)
im.show()
f='Mujtaba'
outfile = f + ".jpg"
im.save(outfile)
