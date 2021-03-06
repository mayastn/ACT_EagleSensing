#Function to run sen2cor (old and new format) with file control for unfinished L2A folders

import os
from itertools import starmap
import parmap
import fire
import shutil


## RUN SEN2COR---------------------------------------------------------


# 1. ONE BY ONE PROCESSING

def sen2_single (res, prod): # resolution should be 10, 20, 60, or all
    res = str(res)
    if res == 'all':
        os.system("L2A_Process" + " " + prod)
    else:
        os.system("L2A_Process --resolution=" + res + " " + str(prod))

# 2. BATCH PROCESSING

def sen2_batch (res, dir): # Creates a list of arguments based on number of files to run
    os.chdir(dir)
    datafiles = os.listdir(dir)
    slist = []

    for files in datafiles: # checks for L1C folders
        checker1 = "L1C"
        if files[7:10] == checker1 or files[16:19] == checker1:
            slist.append((res, files))
        checker2 = "L2A" # checks for unfinished L2A folders an deletes it
        if files[7:10] == checker2 or files[16:19] == checker2:
            each_folder_dir = str(os.listdir(dir)) + '/' + str(files)
            for subf in each_folder_dir:
                if len(subf) <= 8:
                    shutil.rmtree(files, ignore_errors=True) #resolving the bug that shows error after deleting files

    if not os.path.isdir(dir):
        raise ValueError('working_directory: '+ dir + ' does not exist or is inaccesible. Your current working directory is '+os.getcwd()+'.')



    parmap.starmap(sen2_single, slist) #goes for optimal processing setup since GIPP parallelizing is set to AUTO
    dir_L1C = dir
    return dir_L1C


if __name__ == '__main__':
    fire.Fire(sen2_batch)

