import networkx as nx
from collections import Counter


class GraphIsoTester(object):
    """ TODO: docstring

    """

    def __init__(self, graph_g, graph_h):
        """
        TODO: docstring

        :param graph_g:
        :param graph_h:
        :return:
        """
        self.G = graph_g
        self.H = graph_h
        self.disjoint_union = nx.disjoint_union(self.G, self.H)

    def is_balanced(self):
        """ Validates if the degree of the edges
         are equal in both graphs

        :return: boolean
        """
        labels_g = Counter(self.G.degree().values())
        labels_h = Counter(self.H.degree().values())
        if labels_g == labels_h:
            return True
        else:
            return False

    def initial_test(self):
        """
        Validate if number of edges, nodes
        and degrees of the nodes are equal

        :return: boolean
        """
        if self.G.number_of_nodes() != self.H.number_of_nodes():
            return False
        elif self.G.number_of_edges() != self.H.number_of_edges():
            return False
        elif self.is_balanced() is False:
            return False
        return True

