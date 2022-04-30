import math
import operator
from functools import reduce

from PIL import Image, ImageChops


def rms_diff(im1, im2):
    """
        Calculate the root-mean-square difference between two images
    """

    im1 = Image.open(im1)
    im2 = Image.open(im2)

    try:
        h = ImageChops.difference(im1, im2).histogram()
    except ValueError:
        return 100

    # calculate rms
    return math.sqrt(reduce(operator.add,
                            map(lambda x, i: x * (i ** 2), h, range(256))
                            ) / (float(im1.size[0]) * im1.size[1]))
