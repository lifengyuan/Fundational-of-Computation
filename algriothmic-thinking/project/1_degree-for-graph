"""
Week1: Degree distributions for graphs
"""

#Define three constants to the three directed graphs 
#http://storage.googleapis.com/codeskulptor-alg/alg_example_graph0.jpg
EX_GRAPH0 = {
    0 : set([1,2]),
    1 : set(),
    2 : set(),
}

#http://storage.googleapis.com/codeskulptor-alg/alg_example_graph1.jpg
EX_GRAPH1 = {
    0 : set([1,4,5]),
    1 : set([2,6]),
    2 : set([3]),
    3 : set([0]),
    4 : set([1]),
    5 : set([2]),
    6 : set(),
}

#http://storage.googleapis.com/codeskulptor-alg/alg_example_graph2.jpg
EX_GRAPH2 = {
    0 : set([1,4,5]),
    1 : set([2,6]),
    2 : set([3,7]),
    3 : set([7]),
    4 : set([1]),
    5 : set([2]),
    6 : set(),
    7 : set([3]),
    8 : set([1,2]),
    9 : set([0,3,4,5,6,7])
}

def make_complete_graph(num_nodes):
    """
    Takes the number of nodes num_nodes and 
    returns the specified number of nodes. 
    """
    graph = dict()
    nodes = set([i for i in xrange(num_nodes)])
    for index in xrange(num_nodes):
        adj_lst = set(nodes)
        adj_lst.remove(index)
        graph[index] = adj_lst
    return graph

def compute_in_degrees(digraph):
    """
    Takes a directed graph digraph and computes the 
    in-degrees and return a dictionary with the 
    same set of keys (nodes) 
    """
    in_degrees = dict()
    for each in digraph:
        degree = 0
        for each1 in digraph:
            if(each in digraph[each1]):
                degree += 1
        in_degrees[each] = degree
    return in_degrees

def in_degree_distribution(digraph):
    """
    Takes a directed graph digraph and computes the 
    unnormalized distribution of the in-degrees of the graph. 
    The function should return a dictionary whose keys 
    correspond to in-degrees of nodes in the grap
    """
    in_degrees = compute_in_degrees(digraph)
    degree_dist = dict()
    for each in in_degrees:
        if degree_dist.get(in_degrees[each]) is None:
            degree_dist[in_degrees[each]] = 1
        else:
            degree_dist[in_degrees[each]] += 1
    return degree_dist
    
# http://www.codeskulptor.org/#user41_Wx3ItgxJet_4.py 
#All pass though the test, score 100/100