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

    def add_colour_label(self, graph):
        """
        Add label 'colour' to graphs nodes and makes initial coloring.
        Initial colour equals the degree of the node
        :param graph: networkx Graph object
        :return: graph: networkx graph with labels 'colour',
                the next colour to use
                and a list, containing all initial colours
        """
        # TODO: check if graph is empty and if so return message
        degrees = graph.degree()
        initial_colours = list(set(degrees.values()))
        for one_node in graph.nodes():
            graph.node[one_node]['colour'] = degrees[one_node]
        return graph, max(degrees.values()) + 1, initial_colours

    def group_by_colour(self, graph, initial_colours):
        """
        Group all nodes with the same colour.

        :param graph: networkx grap hwith colour labels
        :param initial_colours: list with the initial colours
        :return: {
                    colour_1: [list og nodes with colour_1]
                    colour_2_ [list of nodes with colour_2]
                    }
        """
        result = {}
        for colour in initial_colours:
            result[colour] = []
            for one_node in graph.nodes():
                if graph.node[one_node]['colour'] == colour:
                    result[colour].append(one_node)
        return result

    def one_step_colour_refinement(self,
                                   graph,
                                   initial_colours,
                                   next_colour):
        """
        Two nodes x and y get different colours
        if there is some colour c such that
        x and y have different number of neighbours of colour c
        :param: graph:
        :param: initial_colours
        :param next_colour:
        :return: networkx graph with new 'colour' label after one iterartion
        """
        colour_groups = self.group_by_colour(graph=graph,
                                             initial_colours=initial_colours)
        
        return graph

    def colour_refinement(self, graph):
        """

        :param graph: networkx graph
        :return: graph: is colored such that
        no two neighbor nodes have the same color
        """
        graph, next_colour, initial_colours = self.add_colour_label(graph=graph)
        new_graph = self.one_step_colour_refinement(
            graph=graph,
            initial_colours=initial_colours,
            next_colour=next_colour
        )
        # n_hood = {node: X.neighbors(node) for node in X.nodes()}
