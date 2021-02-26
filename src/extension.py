# rename extension of files
import os

def rename_file(filepath, ext):
    name_grp = os.path.splitext(filepath)
    
    # process .textfile only
    if name_grp[-1] != '.textfile':
        return False
    
    new_name_with_ext = name_grp[0] + ext
    os.rename(filepath, new_name_with_ext)
    return True
