from domain import LinkGraphs as G
from domain import Node as N
import unittest
import uuid

class LinkGraph_Test(unittest.TestCase):

    def test_linkgraph(self):
        graph = G.LinkGraph()

        nodeFr = N.Node(str(uuid.uuid1()), {"x": 33})
        nodeTo = N.Node(str(uuid.uuid1()), {"x": 44})

        graph.add_node(nodeFr)
        graph.add_node(nodeTo)

        graph.add_edges(str(uuid.uuid1()), nodeFr, nodeTo)

        print(graph.get_allNodes())