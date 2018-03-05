
'''

- Given a folder of organized classes [unknown, classA, classB, ...]
- Create a validation and training set
- Split the data by a ratio, eg: 70/30

'''

from os import listdir, makedirs
from os.path import exists as pathExists
from shutil import copyfile
from PIL import Image

# Folders which make up classes, contain the images
classifiedPath = './data/classified/'
validationPath = './data/validation/'
trainingPath = './data/training/'

def mkdir(path):
	if not pathExists(path):
		makedirs(path)


def ls(path):
	'''List all visible files'''
	return [f for f in listdir(path) if not f.startswith('.')]


def toValidation(className, files):
	'''Copy all files to the validation set'''

	for fileName in files:
		sourcePath   = '{}{}/{}'.format(classifiedPath, className, fileName)
		targetPath   = '{}{}/{}'.format(validationPath, className, fileName)

		try:
			copyfile(sourcePath, targetPath)
		except (FileNotFoundError):
			copyfile(sourcePath, targetPath)
	return l1, l2


def toTraining(className, files):
	'''Copy all files to the validation set'''

	for fileName in files:
		sourcePath   = '{}{}/{}'.format(classifiedPath, className, fileName)
		targetPath   = '{}{}/{}'.format(trainingPath, className, fileName)

		try:
			copyfile(sourcePath, targetPath)
		except (FileNotFoundError):
			copyfile(sourcePath, targetPath)


def mirrorImage(sourcePath, targetPath):
    '''Flip or mirror the image'''
    image_obj = Image.open(sourcePath)
    rotated_image = image_obj.transpose(Image.FLIP_LEFT_RIGHT)
    rotated_image.save(targetPath)


def splitLists(l):
	'''Split lists by a 1:2 ratio'''
	if len(l) == 1:
		return [l[0]], [l[0]]

	if len(l) == 2:
		return [l[0]], [l[1]]

	splitIndice = len(l) // 3

	l1 = l[0:splitIndice]
	l2 = l[splitIndice:]

	return l1, l2


# Make validation and training directories
mkdir(validationPath)
mkdir(trainingPath)

# List all classes (which are the folders in the classified directory)
classFolders = ls(classifiedPath)

for className in classFolders:
	print(className)

    # List all images in this class
	images = ls(classifiedPath + className)

    # Split images by a 1:2 ratio
	l1, l2 = splitLists(images)

	mkdir('{}{}/'.format(validationPath, className))
	mkdir('{}{}/'.format(trainingPath, className))

	toValidation(className, l1)
	toTraining(className, l2)

	if (l1[0] == l2[0]):
		path = '{}{}/{}'.format(validationPath, className, l1[0])
		mirrorImage(path, path)
