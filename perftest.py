# -*- coding:utf-8 -*-

import dictree
import time
import argparse
from functools import wraps

def func_timer(func):
    @wraps(func)
    def function_timer(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        t1 = time.time()
        print("Total tiem runing {} :{} seconds".format(func.func_name, t1-t0))
        return result
    return function_timer

@func_timer
def test_save(tnode):
    tnode.save()

@func_timer
def test_insert(tnode, filename):
    with open(filename, "r") as f:
        for line in f:
            tnode.insert(line.strip())
    return tnode

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("filename",
        help="filename like:passwd1.txt", type=str)
    option = parser.parse_args()

    filename = option.filename
    print("test password file:{}".format(filename))
    tnode = dictree.TNode()
    print("test class TNcode insert function ......")
    tnode = test_insert(tnode, filename)
    print("\ntest class TNode save function ......")
    test_save(tnode)
