import networkx as nx

class LinkGraph(object):

    def __init__(self):
        self.graph = nx.MultiDiGraph()
        
    
    def add_node(self, node):
        self.graph.add_node(node)

    def add_edges(self, edgeId, nodeFrom, nodeTo):
        self.graph.add_edge(nodeFrom, nodeTo, edgeId)
        
    def get_allNodes(self):
        adjacency = {}
        for n, p in self.graph.adjacency_iter():
            nodeList = (ln.getIdentity() for ln in p)
            adjacency[n.getIdentity()] = list(nodeList)
        return adjacency 