import os
import logging
import shutil


def walk_dir(dir_path, ext=None):
    result = []
    for r, d, f in os.walk(dir_path):
        for file in f:
            if ext is not None and file.endswith(ext):
                result.append(os.path.join(r, file))
            elif ext is None:
                result.append(os.path.join(r, file))

    return result


def empty_dir(folder_path):
    shutil.rmtree(folder_path)
    os.makedirs(folder_path)
