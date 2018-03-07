
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
classifiedPath = './data/subset/'
validationPath = './data/validation/'
trainingPath = './data/training/'
testPath = './data/test/'

def mkdir(path):
	if not pathExists(path):
		makedirs(path)

def ls(path):
	'''List all visible files'''
	return [f for f in listdir(path) if not f.startswith('.')]

def moveTo(targetFolder, className, files):
	'''Copy all files to the validation set'''

	for fileName in files:
		sourcePath   = '{}{}/{}'.format(classifiedPath, className, fileName)
		targetPath   = '{}{}/{}'.format(targetFolder, className, fileName)

		try:
			copyfile(sourcePath, targetPath)
		except (FileNotFoundError):
			copyfile(sourcePath, targetPath)

def splitIntoValidationTrainingTest():
	# Make validation and training directories
	mkdir(validationPath)
	mkdir(trainingPath)
	mkdir(testPath)

	# List all classes (which are the folders in the classified directory)
	classFolders = ls(classifiedPath)

	for className in classFolders:
	    # List all images in this class
		images = ls(classifiedPath + className)

	    # Split images
		l = len(images)
		s1, s2, s3 = int(l * 0.6), int(l * 0.2), int(l * 0.2)
		train, validate, test = images[0:s1], images[s1:s1 + s2], images[s1 + s2:]

		mkdir('{}{}/'.format(validationPath, className))
		mkdir('{}{}/'.format(trainingPath, className))
		mkdir('{}{}/'.format(testPath, className))

		moveTo(trainingPath, className, train)
		moveTo(validationPath, className, validate)
		moveTo(testPath, className, test)
