import networkx as nx
from collections import Counter


class GraphIsoTester(object):
    """ TODO: docstring

    """

    def __init__(self, graph_g, graph_h):
        """
        Initialize class with instances
        G and H - networkx graphs,
        and the disjoint union of both

        :param graph_g: networkx graph
        :param graph_h: networkx graph
        :return: GraphIsoTester object
        """
        self.G = graph_g
        self.H = graph_h
        self.disjoint_union = nx.disjoint_union(self.G, self.H)

    def is_balanced(self):
        """ Validates if the degree of the nodes
         are equal in both graphs

        :return: boolean
        """
        degrees_g = Counter(self.G.degree().values())
        degrees_h = Counter(self.H.degree().values())
        if degrees_g == degrees_h:
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
        elif not self.is_balanced():
            return False

        return True

    def n_degree_hood(self, graph, node, degree=1):
        """
        Get the n-degree neighborhood of a node
        :param graph. networkx graph
        :param node: node of the graph
        :param degree: int: default value 1
        :return: list, containing the n-degree neighbors of node
        """
        shortest_paths = nx.single_source_dijkstra_path_length(
            graph, node
        )
        result = [node for node, path_length in shortest_paths.iteritems()
                  if path_length == degree]
        return result

    def one_step_color_refignment(self, colors):
        """TODO: docstring
        :param colors:
        :return:
        """
        # get initial colors of the disjoint union
        pass

    def color_refignment(self, X):
        """

        :param X: nx graph
        :return: graph X is colored such that
        no to neighbor nodes have the same color
        """
        # initial colors = degree of the nodes
        initial_colors = X.degree()
        # node and all its neighbors
        n_hood = {node: X.neighbors(node) for node in X.nodes()}
