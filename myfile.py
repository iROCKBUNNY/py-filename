import os
import re


def searchByExt(rootpath, ext):
    print '----- File List -----'
    results = []
    for root, dirs, files in os.walk(rootpath):
        for filename in files:
            if re.search(r'.*\.%s' % ext, filename):
                result = os.path.join(root, filename)
                results.append(result)
                print 'Find: %s' % result
    print '-- End of File List--'
    return results


def modifyPrefix(filelist, oldPrefix='', newPrefix=''):
    # add prefix
    if oldPrefix == '' and newPrefix != '':
        action = 'Add'

    # remove prefix
    if oldPrefix != '' and newPrefix == '':
        action = 'Remove'

    # change prefix
    if oldPrefix != '' and newPrefix != '':
        action = 'Change'

    # stay unchanged
    if oldPrefix == newPrefix:
        print 'The prefix stay unchanged.'
        return

    for oldFile in filelist:
        if os.path.exists(oldFile):
            if os.path.isfile(oldFile):
                dirname, filename = os.path.split(oldFile)
                if filename[:len(oldPrefix)] == oldPrefix:
                    newFilename = newPrefix + filename[len(oldPrefix):]
                    newFile = os.path.join(dirname, newFilename)
                    os.rename(oldFile, newFile)
                    if os.path.exists(newFile):
                        print '%s prefix: %s -> %s. Succeed' % (action, filename, newFilename)
                    else:
                        print '%s prefix: %s -> %s. Fail' % (action, filename, newFilename)
                else:
                    print 'Warning: Invalid old prefix for file: %s (The requested prefix to be %sd is "%s"). Skip' % (filename, action.lower(), oldPrefix)
                    continue
            else:
                print 'Warning: %s is not a valid file. Skip' % oldFile
        else:
            print 'Warning: %s does not exist. Skip' % oldFile


def modifySuffix(filelist, oldSuffix='', newSuffix=''):
    # add suffix
    if oldSuffix == '' and newSuffix != '':
        action = 'Add'

    # remove suffix
    if oldSuffix != '' and newSuffix == '':
        action = 'Remove'

    # change suffix
    if oldSuffix != '' and newSuffix != '':
        action = 'Change'

    # stay unchanged
    if oldSuffix == newSuffix:
        print 'The suffix stay unchanged.'
        return

    for oldFile in filelist:
        if os.path.exists(oldFile):
            if os.path.isfile(oldFile):
                dirname, fullfilename = os.path.split(oldFile)
                filename, ext = os.path.splitext(fullfilename)
                if filename[len(filename)-len(oldSuffix):] == oldSuffix:
                    newFilename = filename[:len(filename)-len(oldSuffix)] + newSuffix + ext
                    newFile = os.path.join(dirname, newFilename)
                    os.rename(oldFile, newFile)
                    if os.path.exists(newFile):
                        print '%s suffix: %s -> %s. Succeed' % (action, fullfilename, newFilename)
                    else:
                        print '%s suffix: %s -> %s. Fail' % (action, fullfilename, newFilename)
                else:
                    print 'Warning: Invalid old suffix for file: %s (The requested suffix to be %sd is "%s"). Skip' % (fullfilename, action.lower(), oldSuffix)
                    continue
            else:
                print 'Warning: %s is not a valid file. Skip' % oldFile
        else:
            print 'Warning: %s does not exist. Skip' % oldFile
