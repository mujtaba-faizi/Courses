
from PIL import Image
import requests
import numpy as np
from io import BytesIO
import skimage.color as sc
import matplotlib.pyplot as plt

def hist_im(im, bins = 256):
    """ Display histogram of flattened image"""

    fig = plt.figure(figsize=(8, 6))
    fig.clf()
    ax = fig.gca()
    ax.hist(im.flatten(), bins = bins)
    return 'Done'


def cdf_im(im, bins=256):
    """Display cumulative distirbution of flattened image"""
    import matplotlib.pyplot as plt
    import numpy as np

    y, x = np.histogram(im.flatten(), bins=bins)
    y = y.cumsum()

    fig = plt.figure(figsize=(8, 6))
    fig.clf()
    ax = fig.gca()
    ax.plot(x[:256], y)
    return 'Done'

url = "https://github.com/MicrosoftLearning/Applied-Machine-Learning/raw/master/Labs/Faces/Steve.jpg"   # to get image from a website

response = requests.get(url)
steve = np.array(Image.open(BytesIO(response.content)))
steve = sc.rgb2gray(steve)

hist_im(steve)
cdf_im(steve)