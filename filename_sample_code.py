# -*- coding: utf-8 -*-

import filename


def main():
    rootpath = '~/Documents' # change this to a proper directory path
    ext = 'pdf' # change it to whatever file extension you need
    oldPrefix = '' # left empty when adding new prefix
    newPrefix = 'prefix-' # left empty when removing old prefix
    oldSuffix = '' # left empty when adding new suffix
    newSuffix = '-suffix' # left empty when removing old suffix

    results = filename.searchByExt(rootpath, ext)
    filename.modifyPrefix(results, oldPrefix, newPrefix)
    filename.modifySuffix(results, oldSuffix, newSuffix)


if __name__ == '__main__':
    main()