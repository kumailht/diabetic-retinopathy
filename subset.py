'''
    Working on an entire dataset may not be optimal. This script helps you pare
    it down to just what you need.

    - Limit number of images per class
    - Set dimension minimums
    - Crop images to same aspect ratio
    - Scale images to standardize sizing
'''

from os import listdir, makedirs
from PIL import Image
from os.path import join as joinPaths
from shutil import copyfile

def mkdir(path):
    if not pathExists(path):
        makedirs(path)


def ls(path, fullpath=True):
    '''List all visible files'''
    def nameOrPath(name):
        if fullpath:
            return joinPaths(path, name)
        else:
            return name

    return [nameOrPath(name) for name in listdir(path) if not name.startswith('.')]

def minDimension(minWidth, minHeight):
    def check(path):
        with Image.open(path) as img:
            width, height = img.size
            if width > minWidth and height > minHeight:
                return True
        return False
    return check


def move(targetRoot):
    def moveFile(sourcePath):
        className, imageName = sourcePath.split('/')[3:]
        targetPath = joinPaths(targetRoot, className, imageName)
        try:
            copyfile(sourcePath, targetPath)
        except (FileNotFoundError):
            makedirs(joinPaths(targetRoot, className))
            copyfile(sourcePath, targetPath)
    return moveFile


# Find all classes
# ['/0', '/1', ...]
classNames = ls('./data/classified/')

# Get the image paths in each class folder
# [['/a.jpg', '/b.jpg'], ['/a.jpg', '/b.jpg']]
imagesByClass = map(ls, classNames)

# Keep only images with the minimum dimensions
# [['/0/b.jpg'], ['/1/b.jpg']]
minDimensions = map(lambda c: list(filter(minDimension(1000, 500), c)), imagesByClass)

limit100 = map(lambda l: l[:99], minDimensions)

# [['0/b.jpg'], ['1/b.jpg']]
moveToSubset = move('./data/subset/')

for classOfImages in limit100:
    for image in classOfImages:
        print('> ' + image)
        moveToSubset(image)
