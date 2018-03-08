from PIL import Image

from utils.classify import getClassMap, sortFiles
from utils.subset import createSubset

from utils.files import ls
from utils.split import splitIntoValidationTrainingTest
from utils.image import autoCropImage, circleToSquare, scale

def imageCondition(imagePath):
    '''
        Should you accept this image into the dataset?
    '''
    im = Image.open(imagePath).convert('RGB')

    im = autoCropImage(im)
    im = circleToSquare(im)

    width, height = im.size
    minWidth, minHeight = (800, 800)

    # The ratio should be within 10% of being a square
    isSquarish = lambda w, h: (w/h) < 1.1 and (w/h) > 0.9
    isLargeEnough = lambda w, h: w > minWidth and h > minHeight

    # Check for minimum dimension & aspect ratio
    try:
        if isSquarish(width, height) and isLargeEnough(width, height):
            return True
    except ZeroDivisionError:
        return False

    return False


# Classify: train/images -> classified/class/images
print('# Organizing images by class')
# classMap = getClassMap('./data/train.csv')
# sortFiles(classMap, './data/train/')

# Create a subset
print('# Picking a subset')
createSubset('./data/classified/', './data/subset/', imageCondition, limit=700)

# Transform images
for classPath in ls('./data/subset/'):
    for imagePath in ls(classPath):
        print('> ' + imagePath)

        im = Image.open(imagePath).convert('RGB')

        im = autoCropImage(im)
        # im = circleToSquare(im)
        im = scale(im, 512)

        im.save(imagePath, quality=100)

# Split the subset that has been transformed into valid/train/test
# with ratio 60/20/20
splitIntoValidationTrainingTest()
