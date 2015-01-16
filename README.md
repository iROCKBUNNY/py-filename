# myfile
A Python script to add/remove file name prefix/suffix

### `myfile.py`: core functions
1. myfile.**searchByExt(***rootpath*, *ext***)**  
Find files in `rootpath` with a certain file extentison of `ext`, obtain their file paths, and store those file paths into a `list`.

2. myfile.**modifyPrefix(***filelist*, *oldPrefix=''*, *newPrefix=''***)**  
For the files listed in `filelist`, change their file name prefix from `oldPrefix` to `newPrefix`. 

3. myfile.**modifySuffix(***filelist*, *oldSuffix=''*, *newSuffix=''***)**  
For the files listed in `filelist`, change their file name suffix from `oldSuffix` to `newSuffix`. 

### `myfile_sample_code.py`: sample code
    # -*- coding: uft-8 -*-
    
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
