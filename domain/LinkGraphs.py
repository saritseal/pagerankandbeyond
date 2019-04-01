import networkx as nx
import cuckoopy as c
import logging

class LinkGraph(object):

    def __init__(self):
        self.graph = nx.MultiDiGraph()
        self.filter = c.CuckooFilter(1000000, 1000)

    
    def add_node(self, node):
        if self.filter.contains(node.getIdentity()) == True:
            logging.info("ignoring node already in graph {}".format(node.getIdentity()))
        else:
            self.graph.add_node(node)
            self.filter.insert(node.getIdentity())


    def add_edges(self, edgeId, nodeFrom, nodeTo):
        self.graph.add_edge(nodeFrom, nodeTo, edgeId)
        
    def get_allNodes(self):
        adjacency = {}
        for n, p in self.graph.adjacency_iter():
            nodeList = (ln.getIdentity() for ln in p)
            adjacency[n.getIdentity()] = list(nodeList)
        return adjacency 

    def getStats(self):
        return self.graph.number_of_nodes(), self.graph.number_of_edges()    