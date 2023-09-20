import numpy as np
from heapdict import heapdict
import weighted_graph_tools as wgt  # See weighted_graph_tools.py in repository


# Using path_backtrack, similar to that used in assignment 3 on unweighted graphs
def path_backtrack(end_node,came_from):
    """ Construct path from start to end node based on previous traversal 
    
    # Arguments:
    end_node:       end node (unique identifier)
    came_from:      Dict from previous traversal
                    key = node, value = previous node

    # Returns:
    path:           List, starting with start_node and ending with end_node,
                    containing all nodes on the path taken from start to end

    # Notes:
    A previous version of this function had start_node as an input argument.
    This is not needed, and has been removed in this version.     
    """
    pass
    

def dijkstra_traverse(graph, start_node):
    """ Find shortest paths to all nodes using Dijkstra's algorithm
    
    # Arguments:
    graph:      Dictionary of dictionaries:
                Key (1. level): Name of node.
                Value (1. level): Dictionary with weighted edges from node
                Key (2. level): Name of neighbor
                Value (2. level): Weight of edge to neighbor
              
                Example: {'A':{'B':5,'C':7}}
                (edge A->B with weight 5, edge A->C with weight 7)
    start_node:    Name of start node
        
    # Returns:
    dist:       Dict with key = node and value = shortest distance to node from start. 
    came_from:  Dict containing the preceding node ("came_from") along the 
                shortest path to the node from start, for every node. 
                The dict includes the start node, came_from[start_node] == None.
    """
    pass


def dijkstra_search(graph, start_node, end_node):
    """ Find shortest path to single node using Dijkstra's algorithm with early stopping
    
    # Arguments:
    graph:      Dictionary of dictionaries:
                Key (1. level): Name of node.
                Value (1. level): Dictionary with weighted edges from node
                Key (2. level): Name of neighbor
                Value (2. level): Weight of edge to neighbor
              
                Example: {'A':{'B':5,'C':7}}
                (edge A->B with weight 5, edge A->C with weight 7)
    start_node: Name of start node
    end_node    Name of end node
        
    # Returns:
    dist:       Distance / cost from start node to end node (single value).
    came_from:  Dict containing the preceding node ("came_from") along the 
                shortest path to the node from start, for every node.
                The dict includes the start node, came_from[start_node] == None. 
    visited:    List containing nodes visited during search, ordered from first
                (start_node) to last (end_node).
    path:       ist containing every node along shortest path 
                from start to end node (including both).
    """
    pass


def distance_L1(pos1,pos2):
    """ Calculate L1 distance between two 2D positions 
    
    # Arguments:
    pos1:   (y,x) tuple describing position in 2D carteasian coordinates
    pos2:   Same as pos1

    # Returns:
    dist    L1 distance (also known as "taxicab" or "Manhattan" distance),
            (sum of absolute differences in coordinate values)
            See https://en.wikipedia.org/wiki/Taxicab_geometry 
    """
    pass


def greedy_search(graph, start_node, end_node):
    """ Find path from start to end node in graph using greedy search
    
    # Arguments:
    graph:      Dictionary of dictionaries:
                Key (1. level): Name of node.
                Value (1. level): Dictionary with weighted edges from node
                Key (2. level): Name of neighbor
                Value (2. level): Weight of edge to neighbor
              
                Example: {'A':{'B':5,'C':7}}
                (edge A->B with weight 5, edge A->C with weight 7)
    start_node: Name of start node
    end_node    Name of end node
        
    # Returns:
    dist:       Distance / cost from start node to end node (single value)
                along path followed (not necessarily shortest path).
    came_from:  Dict containing the preceding node ("came_from") along the 
                shortest path to the node from start, for every node.
                The dict includes the start node, came_from[start_node] == None. 
    visited:    List containing nodes visited during search, ordered from first
                (start_node) to last (end_node).
    path:       List containing every node along path followed 
                from start to end node (including both).
    """
    pass


def astar(graph,start_node,end_node):
    """ Find shortest path from start to end node using the A* algorithm
    
    # Input parameters:
    graph:          Dictionary of dictionaries:
                    Key (1. level): Name of node.
                    Value (1. level): Dictionary with weighted edges from node
                    Key (2. level): Name of neighbor
                    Value (2. level): Weight of edge to neighbor
                
                    Example: {'A':{'B':5,'C':7}}
                    (edge A->B with weight 5, edge A->C with weight 7)
    start_node:     Start node 
    end_node:       End node

    # Keyword arguments:
    end_node    If specified, the algorithm searches for a single end node and 
                stops traversing the graph when the node has been found.
                If None, the whole graph is traversed and shortest distances to 
                all nodes are calculated.
        
    # Returns:
    dist:       Distance / cost from start node to end node (single value).
    came_from:  Dict containing the preceding node ("came_from") along the 
                shortest path to the node from start, for every node.
                The dict includes the start node, came_from[start_node] == None. 
    visited:    List containing nodes visited during search, ordered from first
                (start_node) to last (end_node).
    path:       List containing every node along path followed 
                from start to end node (including both).
    """
    pass


def bellman_ford(graph, start_node):
    """ Find shortest paths to all nodes using Bellman-Ford
    
    # Arguments:
    graph:      Dictionary of dictionaries:
                Key (1. level): Name of node.
                Value (1. level): Dictionary with weighted edges from node
                Key (2. level): Name of neighbor
                Value (2. level): Weight of edge to neighbor
              
                Example: {'A':{'B':5,'C':7}}
                (edge A->B with weight 5, edge A->C with weight 7)
    start_node:    Name of start node
        
    # Returns:
    dist:       Dict with key = node and value = shortest distance to node from start. 
                If the graph contains a negative cycle, the function  returns None 
                (dist == None). 
    """
    pass