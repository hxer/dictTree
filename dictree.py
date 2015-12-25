#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""字典树
[+] 从不同的密码文件中获取密码
[+] 存入字典树中，并保存密码出现的次数属性
[!] 只存入[0~9, a-z, A-Z, _,]组成的密码

#by hxer， 2015.11.17
#version python2.7
"""

"""FIXME
[+] cpickle replace pickle, get shorter time in running TNode().save function
"""

"""TODO
[+]pickle文件保存数据结构，文件大
"""

import cPickle  #quicker than pickle
import os.path
import argparse

def genDTABLE():
    """
    generate the table that only include "a-z,A-Z,0-9,_"
    """
    dtable = []
    for i in range(26):
        dtable.append(chr(ord('a')+i))
        dtable.append(chr(ord('A')+i))
    for i in range(10):
        dtable.append(str(i))
    dtable.append('_')
    return dtable

DTABLE = genDTABLE()

class Node(object):
    """
    tree node, abstract class
    """
    def __init__(self):
        self.tag = False
        self.cnt = 0
        self.child = dict()


class TNode(Node):
    """
    """

    """not need now ===
    def __init__(self):
        Node.__init__(self)
    """

    def insert(self, passwd):
        """
        param:
            passwd: string
        return
            False: passws can't be accepted
            True: insert success
        """
        if not self.acceptable(passwd):
            return False

        node = self
        for c in passwd:
            if c not in node.child.keys():
                node.child[c] = Node()
            node = node.child[c]
            node.tag = True
        node.cnt += 1
        return True

    def search(self, passwd):
        """
        param:
            passwd: string
        return:
            cnt: the counts of passwd recorder
        """
        if not self.acceptable(passwd):
            return 0
        node = self
        for c in passwd:
            if c in node.child.keys() and node.child[c].tag:
                node = node.child[c]
            else:
                return 0
        return node.cnt

    def acceptable(self, string):
        """
        """
        if len(string)>15:
            return False
        for c in string:
            if c not in DTABLE:
                return False
        return True

    def save(self, pfile=''):
        """
        """
        if not pfile:
            pfile = os.path.join("output", "passwd.pkl")
        with open(pfile, 'wb') as f:
            cPickle.dump(self, f)


if __name__ == "__main__":
    """use example
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("filename",
        help="filename like:passwd1.txt", type=str)
    option = parser.parse_args()
    #print(DTABLE)
    filename = option.filename
    tnode = TNode()
    """
    with open("passwd.pkl", "rb") as f:
        tnode = cpickle.load(f)
    """
    with open(filename, "r") as f:
        num = 0
        for line in f:
            tnode.insert(line.strip())
            num +=1
            if not num%500:
                print(line.strip())
    print("begin to save......")
    tnode.save()
    print("admin", tnode.search("admin"))

