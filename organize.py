
'''

Classifies files in a folder into multiple folders

'''

import csv
from os import listdir, makedirs
from os.path import isfile, join
from shutil import copyfile

rootPath = './data/train/'
classMapCSVPath = './data/train.csv'

def getClassMap(path):
	classMap = {}

	with open(path, 'r') as classMapCSV:
		classMapCSV = csv.reader(classMapCSV, delimiter=',', quotechar='|')
		for row in classMapCSV:
			classMap[row[0]] = row[1]

	return classMap


def moveFile(fileName, className):
	sourcePath   = './data/train/{}'.format(fileName)
	targetPath   = './data/classified/{}/{}'.format(className, fileName)
	targetFolder = './data/classified/{}/'.format(className)

	print('-> {}'.format(fileName))

	try:
		copyfile(sourcePath, targetPath)
	except (FileNotFoundError):
		makedirs(targetFolder)
		copyfile(sourcePath, targetPath)


def sortFiles(classMap):
	for name in listdir(rootPath):
		try:

			target = classMap[name.split('.')[0]]
		except KeyError:
			target = 'unknown'

		moveFile(name, target)


classMap = getClassMap(classMapCSVPath)
print(classMap)
print(len(classMap))

sortFiles(classMap)
