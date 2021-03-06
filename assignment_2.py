'''
More advanced PD game model, using either:
    1. two-dimensional grid
    2. random network
to drive the interactions of players.
'''

# Required imports
import numpy
import networkx


class Grid2D(object):
    '''
    The Grid2D class represents a simple two-dimensional grid.
    '''

    # Dimensions of the grid
    num_rows = 0
    num_cols = 0

    def __init__(self, num_rows, num_cols):
        '''
        Constructor that initializes the grid based on a number of rows
        and columns.

        Your task is to create either:
            1. A list of lists
            2. A numpy.array
        '''
        pass

    def put(self, row, col, obj):
        '''
        The put method places an object in a given row/col.

        You should do this by assigning a value to your list-of-lists or
        numpy.array with the proper index.
        '''
        pass

    def get(self, row, col):
        '''
        The get method returns an object in a given row/col.

        You should do this by returning the value from your list-of-lists or
        numpy.array with the proper index.
        '''
        pass

    def get_neighbors(self, row, col):
        '''
        The get_neighbors method returns the list of objects/players
        in neighboring cells for the given row/column.

        For extra challenge, add an argument that allows either von Neumann
        or Moore neighborhoods.
        '''
        pass


class RandomNetwork(object):
    '''
    The RandomNetwork class represents a random network that defines
    PD player interactions.
    '''

    # Dimensions of the grid
    num_nodes = 0
    num_edges = 0

    def __init__(self, num_nodes, num_edges):
        '''
        Constructor that initializes the network based on a number of
        nodes and edges.

        Your task is to use networkx to create the graph.  Please see these
        pages:
            * http://networkx.github.io/documentation/latest/tutorial/index.html
            * http://networkx.github.io/documentation/latest/reference/generators.html
        '''
        pass

    def put(self, node_id, obj):
        '''
        The put method places an object in a given node_id.
        '''
        pass

    def get(self, row, col):
        '''
        The get method returns an object in a given node_id.
        '''
        pass

    def get_neighbors(self, node_id):
        '''
        The get_neighbors method returns the list of adjacent nodes for
        a given node_id.
        '''
        pass


class RandomPlayer(object):
    '''
    RandomPlayer class is a simple PD player who
    has a constant probability of defecting per game.

    Hint: use your answer to assignment_1!
    '''

    # Default probability of defection
    probability_defect = 0.5

    # Score
    score = 0.0

    # History
    history = []

    def __init__(self, probability_defect):
        '''
        Constructor for the player; takes a probability
        of defection as input.

        You will need to set the class variable from the argument.
        '''
        pass

    def move(self):
        '''
        The move method returns the player's move based on a
        random draw and their constant probability.

        You will need to:
            1. Draw a random variate from numpy.random.random()
            2. Transform the value into an action
        '''
        pass

    def record(self, outcome, score):
        '''
        The record method allows the player to update their score
        and history values if desired.
        '''
        pass
