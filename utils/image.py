from PIL import Image

from .files import ls

def scale(im, toWidth):
    wpercent = (toWidth / float(im.size[0]))
    toHeight = int((float(im.size[1]) * float(wpercent)))
    im = im.resize((toWidth, toHeight), Image.ANTIALIAS)
    return im

def autoCropImage(im):
    '''Trims an image by cropping away black edges'''
    def isBlack(x, y):
        try:
            rgb = im.getpixel((x, y))
        except IndexError:
            return False
        return max(rgb) <= 10

    width, height = im.size

    xMidpoint = width / 2
    yMidpoint = height / 2

    leftX = 0
    upperY = 0
    rightX = width - 1
    lowerY = height - 1

    for side in ['top', 'right', 'bottom', 'left']:
        if side == 'top':
            while isBlack(xMidpoint, upperY):
                upperY += 1

        if side == 'right':
            while isBlack(rightX, yMidpoint):
                rightX -= 1

        if side == 'bottom':
            while isBlack(xMidpoint, lowerY):
                lowerY -= 1

        if side == 'left':
            while isBlack(leftX, yMidpoint):
                leftX += 1

    cropped = im.crop(box=(leftX, upperY, rightX, lowerY))
    return cropped

def circleToSquare(im):
    '''Trims an image by cropping away black edges'''
    def isBlack(x, y):
        try:
            rgb = im.getpixel((x, y))
        except IndexError:
            return False
        return max(rgb) <= 10

    width, height = im.size

    quarterHeight = 0.30 * height

    topRight = width - 1
    bottomRight = width - 1
    bottomLeft = 0
    topLeft = 0

    for corner in ['topRight', 'bottomRight', 'bottomLeft', 'topLeft']:
        if corner == 'topRight':
            while isBlack(topRight, quarterHeight):
                topRight -= 1

        if corner == 'bottomRight':
            while isBlack(bottomRight, quarterHeight * 3):
                bottomRight -= 1

        if corner == 'bottomLeft':
            while isBlack(bottomLeft, quarterHeight * 3):
                bottomLeft += 1

        if corner == 'topLeft':
            while isBlack(topLeft, quarterHeight):
                topLeft += 1

    cropped = im.crop(
        box=(
            max(topLeft, bottomLeft),
            quarterHeight,
            min(topRight, bottomRight),
            quarterHeight * 3
        )
    )
    return cropped
