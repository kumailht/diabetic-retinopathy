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
from .files import ls, mkdir

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

def createSubset(classifiedPath, subsetPath, imageCondition, limit=100):
    # Find all classes
    # ['/0', '/1', ...]
    classNames = ls(classifiedPath)

    # Get the image paths in each class folder
    # [['/a.jpg', '/b.jpg'], ['/a.jpg', '/b.jpg']]
    imagesByClass = map(ls, classNames)

    moveToSubset = move(subsetPath)

    for _class in imagesByClass:

        count = 0
        for image in _class:
            print('> ' + image)

            if imageCondition(image):
                moveToSubset(image)
                count += 1

            if count == (limit - 1):
                break
