from PIL import Image

from os import listdir, makedirs
from os.path import join as joinPaths


def ls(path, fullpath=True):
    '''List all visible files'''
    def nameOrPath(name):
        if fullpath:
            return joinPaths(path, name)
        else:
            return name

    return [nameOrPath(name) for name in listdir(path) if not name.startswith('.')]


def scale(sourcePath, targetPath, toWidth):
    im = Image.open(sourcePath)
    wpercent = (toWidth / float(im.size[0]))
    toHeight = int((float(im.size[1]) * float(wpercent)))
    im = im.resize((toWidth, toHeight), Image.ANTIALIAS)
    im.save(targetPath, quality=100)


def autoCropImage(imagePath, targetPath):
    '''Trims an image by cropping away black edges'''
    def isBlack(x, y):
        try:
            rgb = im.getpixel((x, y))
        except IndexError:
            return False
        return max(rgb) <= 10

    im = Image.open(imagePath).convert('RGB')

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
    cropped.save(targetPath)



def circleToSquare(imagePath, targetPath):
    '''Trims an image by cropping away black edges'''
    def isBlack(x, y):
        try:
            rgb = im.getpixel((x, y))
        except IndexError:
            return False
        return max(rgb) <= 10

    im = Image.open(imagePath).convert('RGB')

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
    cropped.save(targetPath, quality=100)


def centerCrop(sourcePath, targetPath, length):
    im = Image.open(sourcePath)
    im.thumbnail((length, length))
    im.save(targetPath, 'jpeg', quality=100)

for classPath in ls('./data/subset/'):
    for imagePath in ls(classPath):
        print('> ' + imagePath)
        autoCropImage(imagePath, imagePath)
        circleToSquare(imagePath, imagePath)
        scale(imagePath, imagePath, 512)
