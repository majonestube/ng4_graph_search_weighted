import weighted_graph_search_solution as wgs
import weighted_graph_tools as wgt
import pytest

##############################
#  FIXTURES ("test objects")
##############################
@pytest.fixture
def directed_graph():
    """ Small directed test graph """
    return {'A':{'B':5,'C':1},
            'B':{'C':2,'D':3},
            'C':{'B':3,'E':12},
            'D':{'C':3,'E':2,'F':6},
            'E':{'F':1},
            'F':{}}

@pytest.fixture
def directed_graph_with_neg_weights():
    """ Directed graph with negative weights, without negative cycle """
    return {"A": {"B": -1, "C": 4},
            "B": {"C": 3, "D": 2, "E": 2},
            "C": {"A": 4, "B": 3, "D": 5},
            "D": {"B": 1, "C": 5},
            "E": {"B": 2, "D": -3}}

@pytest.fixture
def directed_graph_with_neg_cycle():
    """ Directed graph with negative cycle """
    return {"A": {"B": 5},
            "B": {"C": 1, "D": 2},
            "C": {"E": 1},
            "D": {"F": 2},
            "E": {"D": -1},
            "F": {"E": -3}}

###########
#  TESTS   
###########
def test_path_backtrack(): # 2p
   """ Simple backtrack test """
   came_from = {'A':None,'B':'A','C':'A','D':'C'}
   assert wgs.path_backtrack('B',came_from) == ['A','B']
   assert wgs.path_backtrack('D',came_from) == ['A','C','D']
   assert wgs.path_backtrack('A',came_from) == ['A']


def test_dijkstra_traverse_1(directed_graph): # 2p
    """ Traverse simple directed graph
    Same test graph as used in description of Dijkstra's algorithm in video
    """
    dist, came_from = wgs.dijkstra_traverse(directed_graph,start_node='A')
    assert dist == {'A':0,'B':4,'C':1,'D':7,'E':9,'F':10}
    assert came_from == {'A':None,'B':'C','C':'A','D':'B','E':'D','F':'E'}


def test_dijkstra_traverse_2(): # 1p
    """ Traverse 3x3 maze with wall in middle
    Forces only two possible paths to a node
    """
    maze_text = wgt.read_maze_text('mazes/maze_3x3_weighted.txt')
    graph = wgt.maze_text_to_graph(maze_text)
    dist, came_from = wgs.dijkstra_traverse(graph,start_node=(1,1))
    assert dist == {(1, 1): 0, (1, 2): 5, (1, 3): 12, (2, 1): 2, 
                    (2, 3): 17, (3, 1): 3, (3, 2): 6, (3, 3): 8}
    assert came_from == {(1, 1): None, (2, 1): (1, 1), (1, 2): (1, 1), 
                         (3, 1): (2, 1), (3, 2): (3, 1), (1, 3): (1, 2), 
                         (3, 3): (3, 2), (2, 3): (3, 3)}


def test_djikstra_traverse_3(): # 2p
    """ Traverse 5x5 weighted maze with some walls in the middle
    More complex maze with more "open space" than the 3x3 maze tested above
    """
    maze_text = wgt.read_maze_text('mazes/maze_5x5_weighted.txt')
    graph = wgt.maze_text_to_graph(maze_text)
    dist, came_from = wgs.dijkstra_traverse(graph,start_node=(1,1))
    assert dist[(4,1)] == 14
    assert dist[(4,2)] == 11
    assert dist[(3,5)] == 20
    assert dist[(4,5)] == 24
    assert wgs.path_backtrack(end_node=(4,1),came_from=came_from) == [
        (1, 1), (2, 1), (3, 1), (4, 1)] 
    assert wgs.path_backtrack(end_node=(4,2),came_from=came_from) == [
        (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (4, 2)] 
    assert wgs.path_backtrack(end_node=(3,5),came_from=came_from) == [
        (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5)] 
    assert wgs.path_backtrack(end_node=(4,5),came_from=came_from) == [
        (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2), (4, 2), 
        (5, 2), (5, 3), (5, 4), (5, 5), (4, 5)] 
    

def test_dijkstra_search_1(directed_graph): # 2p
    """ Perform search with early stopping in simple directed graph """
    dist, _, visited, path = wgs.dijkstra_search(directed_graph,start_node='A',end_node='D')
    assert dist == 7
    assert visited == ['A','C','B','D']
    assert path == ['A','C','B','D']


def test_dijkstra_search_2(): # 2p
    """ Search with early stopping in 5x5 weighted maze """
    maze_text = wgt.read_maze_text('mazes/maze_5x5_weighted.txt')
    graph = wgt.maze_text_to_graph(maze_text)
    dist, came_from, visited, path = wgs.dijkstra_search(graph,start_node=(1,1),end_node=(3,2))
    assert dist == 10
    assert len(came_from) == 15
    assert len(visited) == 10
    assert path == [(1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (3, 2)] 


def test_distance_L1(): # 2p
    """ Test L1 ("Manhattan") distance for a few integer points in 2D space"""
    assert wgs.distance_L1((0,0),(0,0)) == 0
    assert wgs.distance_L1((1,0),(0,0)) == 1
    assert wgs.distance_L1((0,1),(0,0)) == 1
    assert wgs.distance_L1((1,1),(0,0)) == 2
    assert wgs.distance_L1((0,0),(1,1)) == 2
    assert wgs.distance_L1((-1,1),(1,-1)) == 4
    assert wgs.distance_L1((7,4),(1,2)) == 8
    assert wgs.distance_L1((-5,4),(2,-7)) == 18


def test_greedy_search_1(): # 2p
    """ Test greedy search in open maze with all edge weights equal"""
    maze_text = wgt.read_maze_text('mazes/maze_10x10_uniform_cost.txt')
    graph = wgt.maze_text_to_graph(maze_text)
    dist, _, visited, path = wgs.greedy_search(graph,start_node=(5,5),end_node=(8,8))
    assert dist == 6
    assert len(visited) == 7
    assert len(path) == 7
    assert path[0] == (5,5)
    assert path[-1] == (8,8)


def test_greedy_search_2(): # 2p
    """ Test greedy search in maze with high-cost corner wall """
    maze_text = wgt.read_maze_text('mazes/maze_10x10_corner.txt')
    graph = wgt.maze_text_to_graph(maze_text)
    dist, _, visited, path = wgs.greedy_search(graph,start_node=(5,5),end_node=(10,10))
    assert dist == 18           # Distance when going straight through high-cost wall
    assert len(visited) == 11   # Distance when going the smallest number of edges
    assert len(path) == 11 
    assert path[0] == (5,5)
    assert path[-1] == (10,10)


def test_astar_1(): # 2p
    """ Test A* in simple 3x3 maze with center wall """
    maze_text = wgt.read_maze_text('mazes/maze_3x3_weighted.txt')
    graph = wgt.maze_text_to_graph(maze_text)
    dist, came_from, visited, path = wgs.astar(graph,start_node=(1,1),end_node=(2,3))
    assert dist == 17
    assert came_from == {(1, 1): None, (2, 1): (1, 1), (1, 2): (1, 1), (3, 1): (2, 1), 
                         (3, 2): (3, 1), (1, 3): (1, 2), (3, 3): (3, 2), (2, 3): (3, 3)}
    assert path == [(1,1),(2,1),(3,1),(3,2),(3,3),(2,3)]
    assert visited == [(1,1),(2,1),(3,1),(1,2),(3,2),(3,3),(1,3),(2,3)] 


def test_astar_2(): # 2p
    """ Test A* in maze with high-cost corner wall """
    maze_text = wgt.read_maze_text('mazes/maze_10x10_corner.txt')
    graph = wgt.maze_text_to_graph(maze_text)
    dist, came_from, visited, path = wgs.astar(graph,start_node=(5,5),end_node=(10,10))
    assert dist == 12
    assert len(came_from) == 44
    assert len(visited) == 25
    assert len(path) == 13
    assert path[0] == (5,5)
    assert path[-1] == (10,10)


def test_astar_3(): # 1p
    """ Test A* in 10x10 maze with many different weights """
    maze_text = wgt.read_maze_text('mazes/maze_10x10_weighted.txt')
    graph = wgt.maze_text_to_graph(maze_text)
    dist, _, _, _ = wgs.astar(graph,start_node=(1,1),end_node=(7,1))
    assert dist == 28
    dist, _, _, _ = wgs.astar(graph,start_node=(1,1),end_node=(5,8))
    assert dist == 21
    dist, _, _, _ = wgs.astar(graph,start_node=(1,1),end_node=(10,10))
    assert dist == 43


def test_bellman_ford_1(directed_graph): # 1p
    """ Test Bellman-Ford on directed graph with only positive weights """
    dist = wgs.bellman_ford(directed_graph,'A')
    assert dist == {'A':0,'B':4,'C':1,'D':7,'E':9,'F':10}


def test_bellman_ford_2(directed_graph_with_neg_weights): # 2p
    """ Test Bellman-Ford on directed graph with negative weigths """
    dist = wgs.bellman_ford(directed_graph_with_neg_weights,'A')
    assert dist == {'A':0,'B':-1,'C':2,'D':-2,'E':1}


def test_bellman_ford_3(directed_graph_with_neg_cycle): # 2p
    """ Test Bellman-ford on directed graph with negative cycle """
    dist = wgs.bellman_ford(directed_graph_with_neg_cycle,'A')
    assert dist is None