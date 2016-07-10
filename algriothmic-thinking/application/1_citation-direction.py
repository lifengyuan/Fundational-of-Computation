"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

# general imports, this version is general python. For the Codeskulptor, it only support simpleplot lib.
import urllib2
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mtick


# Set timeout for CodeSkulptor if necessary
#import simpleplot
#import math
#import codeskulptor
#codeskulptor.set_timeout(20)

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

###################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

#citation_graph = load_graph(CITATION_URL)

def normalized_in_degree(diagraph):
    normalized = in_degree_distribution(diagraph)
    length = 0
    for each in normalized:
        length +=normalized[each]
    for each in normalized:
        normalized[each] /= float(length)
    return normalized

def out_degree_average(diagraph):
    total = 0
    for each in diagraph:
        total += len(diagraph[each])
    return total / len(diagraph)
    
def plot_normalized_log(diagraph):
    normalized = in_degree_distribution(diagraph)
    
    x = normalized.keys()
    y = normalized.values()
    fig, ax = plt.subplots()
    ax.loglog(x, y, basex = np.e, basey = np.e, linestyle='None', 
            marker='x', markeredgecolor='red')
    plt.xlabel("Log of in degrees, base e")
    plt.ylabel("Log of fraction of in degrees, base e")
    plt.title("Distribution of citations on a log scale")

    def ticks(y, pos):
        return r'$e^{:.0f}$'.format(np.log(y))

    ax.xaxis.set_major_formatter(mtick.FuncFormatter(ticks))
    ax.yaxis.set_major_formatter(mtick.FuncFormatter(ticks))
    plt.show()