from os import walk
import os

def generate_path(dir):
    collection = []
    
    for (dirpath, dirnames, filenames) in walk(dir):
        for f in filenames:
            collection.append(os.path.join(dirpath, f))
    return collection
