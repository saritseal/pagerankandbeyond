from domain import Node as N
import unittest

import uuid
from test_helper.Helper import * 

class Node_Test(unittest.TestCase):

    def test_createNode(self):
        id = uuid.uuid1()
        node = N.Node( id, {"x": 20, "type": "data"})
        print(id, node.getIdentity())
        self.assertEqual(id, node.getIdentity())
        print(node.to_string())

    

if __name__ == "__main__":
    unittest.main()