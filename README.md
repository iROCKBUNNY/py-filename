# py-filename
A Python script to add/remove file name prefix/suffix

### Core functions: `filename.py`
1. filename.**searchByExt(***rootpath*, *ext***)**
Find files in `rootpath` with a certain file extentison of `ext`, obtain their file paths, store those file paths into a `list`, and return it.

2. filename.**modifyPrefix(***filelist*, *oldPrefix=''*, *newPrefix=''***)**
For the files listed in `filelist`, change their file name prefix from `oldPrefix` to `newPrefix`.

3. filename.**modifySuffix(***filelist*, *oldSuffix=''*, *newSuffix=''***)**
For the files listed in `filelist`, change their file name suffix from `oldSuffix` to `newSuffix`.

### Sample code: `filename_sample_code.py`
```
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
```

### Further reading
1. [Python和正则表达式：给PDF文件批量添加前缀或后缀](http://research.irockbunny.com/post/100749403437/python-pdf)
