import os
from os import listdir
from os.path import isfile, join
import pandas as pd

# def getlistofallfiles(directory):
#     listoffiles = os.listdir(directory)
#     allfiles = list()
#     for x in listoffiles:
#         if os.path.isdir(join(directory,x)):
#             allfiles = allfiles+getlistofallfiles(join(directory,x))
#         else:
#             allfiles.append(join(directory,x))
#     return allfiles

# try:
#     path = 'C:/'            
#     files = getlistofallfiles(path)
#     file_size = []
#     for file in files:
#         file_size.append(os.path.getsize(file))
# except PermissionError:
#     pass

def main():
    files = []
    file_size = []
    for (dirpath, dirnames, filenames) in os.walk('C:/'):
        for dir in dirnames:
            path = os.path.join(dirpath, dir)
            read_write = os.access(path, os.W_OK) and os.access(path, os.R_OK)
            # W_OK write True and R_OK read True
            if read_write:
                files.append(path)
                file_size.append(os.path.getsize(path))
            else:
                continue
    data = pd.DataFrame({'Files':files,'Size':file_size})
    data = data.sort_values(by=['Size'], ascending=0)
    print(data)

if __name__ == "__main__":
    main()