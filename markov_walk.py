import random as rnd

# 1 - Finish add_neighbor and get_next_state in the State-class 
# based on the supplied docstrings
# 2 - Use the functions you created to model the Markov Chain given
# in markov_state.png

class State:
    """
    Class representing a state in a Markov chain.
    Each state has a set of neighbors in the form of
    a dictionary. Keys point to the neighboring 
    state(s) and values represent transition probability
    """

    def __init__(self, name):
        self.name = name
        self._neighbors = {}

    def add_neighbor(self, neighbor, probability):
        """Adds a new neighbor to the state
        # Arguments:
        neighbor:         a pointer to a neighboring instance of State
        probability:      the probability of going to the neighbor
        """
        pass

    def get_next_state(self):
        """Returns a new state based on neigbor probability       
        # Returns:
        next_state: A new random state based on probability
        """
        pass


def simulate_temperature(n_simulations,n_transitions):
    """ Monte Carlo simulation of temperature state ("Cold", "Normal", "Hot", "Overheating")
    
    Assignment: Create a state transition graph based on the graph shown in
    file markov_state.png. The graph is defined as part of this function.
    The initial state is always "Cold". Run Monte Carlo simulations
    according to the input arguments.

    # Input arguments:
    n_simulations:  Number of Monte Carlo simulations to run 
    n_transitions:  Number of state transitions 

    # Output 
    prob:   A dictionary listing probabilities as percentages
            keys:    State names ("Cold", "Normal", "Hot", "Overheating")
            values:  Probabilities in %

    # Notes:
    - The probabilities will change each time the function is run. 
    However, with a large number of simulations, the probabilities should be 
    relatively stable.
    """
    pass