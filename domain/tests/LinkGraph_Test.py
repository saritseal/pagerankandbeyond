from domain import LinkGraphs as G
from domain import Node as N
import unittest
import uuid
import logging 

class LinkGraph_Test(unittest.TestCase):

    def test_linkgraph(self):
        graph = G.LinkGraph()

        for i in range(1000000):
            nodeFr = N.Node(str(uuid.uuid1()), {"x": 33})
            nodeTo = N.Node(str(uuid.uuid1()), {"x": 44})

            graph.add_node(nodeFr)
            graph.add_node(nodeTo)

            graph.add_edges(str(uuid.uuid1()), nodeFr, nodeTo)

            # graph.get_allNodes()
            if i % 1000 == 0 :
                logging.info("finished {}".format(i))

        nodes, edges = graph.getStats()
        logging.info( "graph has nodes {} edges {}".format(nodes, edges))    