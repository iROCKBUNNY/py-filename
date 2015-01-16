# -*- coding: utf-8 -*-


import myfile


if __name__ == '__main__':
    rootpath = '~/Documents' # change this to a proper directory path
    ext = 'pdf' # change it to whatever file extension you need
    oldPrefix = '' # left empty when adding new prefix
    newPrefix = 'prefix-' # left empty when removing old prefix
    oldSuffix = '' # left empty when adding new suffix
    newSuffix = '-suffix' # left empty when removing old suffix

    results = myfile.searchByExt(rootpath, ext)
    myfile.modifyPrefix(results, oldPrefix, newPrefix)
    myfile.modifySuffix(results, oldSuffix, newSuffix)
