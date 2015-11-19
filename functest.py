# -*- coding:utf-8 -*-

import unittest
from dictTree import TNode

class DTestCase(unittest.TestCase):
    """
    """
    def test_accept(self):
        self.assertTrue(TNode().acceptable("admin"), msg="test acceptable function fail")

    def test_insert(self):
        self.assertTrue(TNode().insert("admin"), msg="test insert function fail")

    def test_search(self):
        tnode = TNode()
        tnode.insert("admin")
        self.assertGreater(tnode.search("admin"), 0, msg="test search function fail")

if __name__ == "__main__":
    unittest.main()
