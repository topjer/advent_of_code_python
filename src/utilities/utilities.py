from pathlib import Path
import time

def timing_val(func):
    def wrapper(*arg, **kw):
        t1 = time.time()
        res = func(*arg, **kw)
        t2 = time.time()
        print(f"Runtime of function: {(t2 - t1)}")
        return res
    return wrapper

def load_file(file_path: Path):
    with open(file_path) as file:
        content = file.readlines()
    return content

def load_file_single(file_path: Path):
    with open(file_path) as file:
        content = file.read()
    return content
