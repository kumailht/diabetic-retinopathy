from os import listdir, makedirs
from os.path import join as joinPaths
from os.path import exists as pathExists

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
