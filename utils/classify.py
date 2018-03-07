
'''
	Move training samples into their respective class folders
	train/images -> classified/class/images
'''

import csv
from os import listdir, makedirs
from os.path import isfile, join
from shutil import copyfile

def getClassMap(csvPath):
	classMap = {}

	with open(csvPath, 'r') as classMapCSV:
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


def sortFiles(classMap, rootPath):
	for name in listdir(rootPath):
		try:
			target = classMap[name.split('.')[0]]
		except KeyError:
			target = 'unknown'

		moveFile(name, target)
