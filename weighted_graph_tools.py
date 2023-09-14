import numpy as np
import matplotlib.pyplot as plt

def read_maze_text(maze_file_path):
    """ Read text file defining a maze 
    
    # Arguments:
    maze_file_path      String or pathlib.Path with text file path

    # Returns:
    maze_text           List with each text line, newline characters removed
    """
    with open(maze_file_path) as file:
        lines = []
        for line in file:
            lines.append(line.rstrip())
    return lines

def maze_text_to_graph(maze_text):
    """ Parse maze text and return graph as dict
    
    # Arguments:
    maze_text   List of maze text lines.
                Walls in the maze are indicated with '#' symbols.
                A wall of '#'s surrounding the maze is assumed.
                Non-blocked nodes have integers in the range [1-9],
                representing the cost of moving to that node.
                This means that all edges going to a node with integer 
                x have a "cost" equal to x. 
                The maze is assumed to be rectangular (each text 
                line is assumed to be equally long).

    graph:      A nested dict containing nodes and edges in the graph.
                The keys in the 1st-level dict are nodes represented as 
                2-element tuples (y,x) indicating node position.
                Position follows standard matrix / image indexing,
                with upper left corner being origo, x axis pointing 
                from left to right, and y axis pointing from top to bottom.
                The values in the 1st-level dict are the 2nd-level dicts.
                The key in each 2nd-level dict is the (y,x) tuple identifying 
                a neighbor node, and the corresponding value is the cost
                of the edge from the node (1st level) to the neighbor node 
                (2nd level) 

    # Example:
    maze:       ######
                #23#9#
                #5178#
                ######
    maze_text = ['#######','#23#9#','#5178#','#####']
    graph = maze_text_to_graph(maze_text)
    graph:  (1, 1): {(2, 1): 5, (1, 2): 3}
            (1, 2): {(2, 2): 1, (1, 1): 2}
            (1, 4): {(2, 4): 8}
            (2, 1): {(1, 1): 2, (2, 2): 1}
            (2, 2): {(1, 2): 3, (2, 1): 5, (2, 3): 7}
            (2, 3): {(2, 2): 1, (2, 4): 8}
            (2, 4): {(1, 4): 9, (2, 3): 7}
    """
    graph = {}
    for i,line in enumerate(maze_text):
        for j,char in enumerate(line):
            if char != '#':                                                 # If maze tile is not blocked
                graph[(i,j)] = {}                                           # Add tile (node) to graph dict
                if maze_text[i-1][j] != '#':                                # If valid node to the north
                    graph[(i,j)][(i-1,j)] = int(maze_text[i-1][j])     # Add northern edge (with weight)
                if maze_text[i+1][j] != '#':                                # If valid node to the south
                    graph[(i,j)][(i+1,j)] = int(maze_text[i+1][j])     # Add southern edge (with weight)
                if maze_text[i][j-1] != '#':                                # If valid node to the west
                    graph[(i,j)][(i,j-1)] = int(maze_text[i][j-1])     # Add western edge (with weight)
                if maze_text[i][j+1] != '#':                                # If valid node to the east
                    graph[(i,j)][(i,j+1)] = int(maze_text[i][j+1])     # Add eastern edge (with weight)
    return graph


def maze_text_to_matrix(maze_text):
    """ Convert maze text into 2D matrix 
    
    # Arguments:
    maze_text   List of maze text lines. See maze_text_to_graph()

    # Returns:
    grid        NumPy 2D matrix with values equal to the node costs
                [1-9] in the maze text.
                Walls (# symbols) are encoded as -5 to separate the 
                values clearly from the node costs.

    # Notes:
    For easy visualization of a maze, plot the 2D matrix as an image.
    Example:
        grid = maze_text_to_matrix(['#######','#23#9#','#5178#','#####'])
        import matplotlib.pyplot
        matplotlib.pyplot.imshow(grid)  # Show as image
    """
    n_rows = len(maze_text)
    n_cols = len(maze_text[0])
    grid = np.zeros((n_rows,n_cols),dtype=int)
    for i,line in enumerate(maze_text):
        for j,char in enumerate(line):
            if char == '#':
                grid[i,j] = -5
            else:
                grid[i,j] = int(char)
    return grid

def visualize_weighted_maze(grid):
    """ Show maze with numbers indicating weights """
    plt.imshow(grid)
    for row_ind in range(grid.shape[0]):
        for col_ind in range(grid.shape[1]):
            if grid[row_ind,col_ind] > 0:
                plt.text(col_ind,row_ind,str(grid[row_ind,col_ind]),
                    horizontalalignment='center',verticalalignment='center')  


def plot_came_from(came_from):
    """ Plot came_from in maze using arrows """
    for (to_node),(from_node) in came_from.items():
        if from_node is not None:
            (y0,x0) = from_node
            (y,x) = to_node
            dy,dx = y-y0, x-x0
            plt.arrow(x=x0,y=y0,dx=0.8*dx,dy=0.8*dy,head_width=0.1)

def plot_path(path):
    """ Plot path (list of maze node coordinates) using arrows """
    for i in range(len(path)-1):
        y0,x0 = path[i]
        y,x = path[i+1]
        dy,dx = y-y0, x-x0
        plt.arrow(x=x0+0.2*dx,y=y0+0.2*dy,dx=0.55*dx,dy=0.55*dy,head_width=0.1)


def plot_node_circles(nodes, circle_size=400, edgecolors='black',linestyle='-'):
    """ Plot circles in nodes (maze tiles)

    Input arguments:
    nodes:      Iterable containing tile coordinates pairs (y,x)

    Keyword arguments (see matplotlib.pyplot.Circle for details):
    circle_size:    Size of circle 
    edgecolors:     Color of circle edge (circumference)
    linestyle:      E.g. dashed ('--') or regular ('-', default)
    """
    x = [xi for (_,xi) in nodes]
    y = [yi for (yi,_) in nodes]
    plt.scatter(x, y, s=circle_size, facecolors='none', edgecolors=edgecolors,
                linestyle=linestyle)
