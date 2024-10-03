#!/usr/bin/python3

import os,pathlib

def get_dir_size(qwe):
    total=0
    try:
        for entry in os.scandir(qwe):
            if entry.is_file():
                total+=entry.stat().st_size
            elif entry.is_dir():
                try:
                    total+=get_dir_size(entry.path)
                except FileNotFoundError:
                    pass
    except NotADirectoryError:
        return os.path.getsize(qwe)
    except PermissionError:
        return 0
    return total

for j in sorted([(get_dir_size(i), i) for i in os.listdir(pathlib.Path().resolve())], reverse=True):
    print(j)