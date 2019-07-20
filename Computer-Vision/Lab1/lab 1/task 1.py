from PIL import Image
import requests

#reading an image from the internet
url="http://ichef.bbci.co.uk/onesport/cps/480/mcs/media/images/57210000/jpg/_57210683_57210682.jpg"
im = Image.open(requests.get(url, stream=True).raw)
im.show()
outfile = "cricket.jpg"
im.save(outfile)

#reading an image from a file
a = Image.open('4.PNG')
print(a.format, a.size, a.mode)
a.show()



