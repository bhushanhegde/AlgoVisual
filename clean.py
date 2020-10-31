#this is just for removing the pyc files that are created during the execution of scripts.

import os
#path here
PATH='/home/solver/PycharmProjects/python/Algorithms_Visualization1/'
files=os.listdir(PATH)
for file in files:
    if file.endswith('.pyc'):
        #print(file)
        os.remove(file)
