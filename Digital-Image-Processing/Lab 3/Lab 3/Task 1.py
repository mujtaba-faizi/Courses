from PIL import Image

def binarize_image(path,threshold):
    """Binarize an image."""
    img = Image.open(path)
    img = img.convert('L')  # convert image to greyscale
    img = img.point(lambda i: 0 if i < threshold else 255)  # if pixel intensity is less than threshold, change it to else 255
    img.show()

binarize_image("B1.png",145)
binarize_image("B2.jpg",150)
binarize_image("B3.jpg",200)