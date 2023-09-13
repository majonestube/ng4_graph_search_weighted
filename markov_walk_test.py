import pytest
from markov_walk_solution import State, simulate_temperature

###########
#  TESTS   
###########
def test_state_transition(): # 2p
   """ Simple state transition test """

   state_1 = State("A")
   state_2 = State("B")

   state_1.add_neighbor(state_2, 1.0)
   state_2.add_neighbor(state_1, 1.0)

    # should go from state 1 -> state 2
   next_state = state_1.get_next_state()

   assert next_state == state_2


def test_two_state_transition(): # 1p
    """ Simple two-state transition test """

    state_1 = State("A")
    state_2 = State("B")

    state_1.add_neighbor(state_2, 1.0)
    state_2.add_neighbor(state_1, 1.0)

    # should go from state 1 -> state 2 -> state 1
    next_state = state_1.get_next_state()
    next_state = next_state.get_next_state()

    assert next_state == state_1


def test_multiple_transitions(): # 1p
    """ Multiple state transitions test """

    state_1 = State("A")
    state_2 = State("B")
    state_3 = State("C")
    state_4 = State("D")
    state_5 = State("E")

    state_1.add_neighbor(state_2, 1.0)
    state_2.add_neighbor(state_3, 1.0)
    state_3.add_neighbor(state_4, 1.0)
    state_4.add_neighbor(state_5, 1.0)

    # should go from state 1 -> ... -> state 5
    current_state = state_1
    for _ in range(4):
        next_state = current_state.get_next_state()
        current_state = next_state

    assert current_state == state_5


def test_simulate_temperature(): # 3p
    """ Run simulation and check that probabilities are within reasonable range """
    prob = simulate_temperature(1000,10)
    assert prob['Cold'] == pytest.approx(20.0,abs=7.0)
    assert prob['Normal'] == pytest.approx(50.0,abs=10.0)
    assert prob['Hot'] == pytest.approx(5.0,abs=5.0)
    assert prob['Overheating'] == pytest.approx(25.0,abs=10.0)


def test_simulate_temperature_final_state(): # 2p
    """ Run simulation for many transitions - converges towards overheating """
    prob = simulate_temperature(1000,200)
    assert prob['Overheating'] > 99.0