#TODO: add some tests for the helper functions and hamiltonian functions

from qlass.helper_functions import *

def test_compute_energy():
    # test case 1
    pauli_bin = (0, 0, 0)
    res = {(0, 0, 0): 0.5, (0, 0, 1): 0.3, (0, 1, 0): 0.1, (1, 0, 0): 0.1}
    assert compute_energy(pauli_bin, res) == 0.5

    # test case 2
    pauli_bin = (0, 0, 1)
    res = {(0, 0, 0): 0.5, (0, 0, 1): 0.3, (0, 1, 0): 0.1, (1, 0, 0): 0.1}
    assert compute_energy(pauli_bin, res) == 0.3

    # test case 3
    pauli_bin = (0, 1, 0)
    res = {(0, 0, 0): 0.5, (0, 0, 1): 0.3, (0, 1, 0): 0.1, (1, 0, 0): 0.1}
    assert compute_energy(pauli_bin, res) == 0.1

    # test case 4
    pauli_bin = (1, 0, 0)
    res = {(0, 0, 0): 0.5, (0, 0, 1): 0.3, (0, 1, 0): 0.1, (1, 0, 0): 0.1}
    assert compute_energy(pauli_bin, res) == 0.1

def test_get_probabilities():
    # test case 1
    samples = [(0, 0, 0), (0, 0, 1), (0, 0, 0), (0, 1, 0), (0, 0, 1)]
    assert get_probabilities(samples) == {(0, 0, 0): 0.4, (0, 0, 1): 0.4, (0, 1, 0): 0.2}

    # test case 2
    samples = [(0, 0, 0), (0, 0, 1), (0, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0)]
    assert get_probabilities(samples) == {(0, 0, 0): 0.5, (0, 0, 1): 0.3333333333333333, (0, 1, 0): 0.16666666666666666}

    # test case 3
    samples = [(0, 0, 0), (0, 0, 1), (0, 0, 0), (0, 1, 0), (0, 0, 1), (0, 0, 0), (0, 0, 0)]
    assert get_probabilities(samples) == {(0, 0, 0): 0.5714285714285714, (0, 0, 1): 0.2857142857142857, (0, 1, 0): 0.14285714285714285}

def test_qubit_state_marginal():
    # test case 1
    prob_dist = {(0, 0, 0): 0.4, (0, 0, 1): 0.4, (0, 1, 0): 0.2}
    assert qubit_state_marginal(prob_dist) == {(0, 0): 0.6, (0, 1): 0.4}

    # test case 2
    prob_dist = {(0, 0, 0): 0.5, (0, 0, 1): 0.3333333333333333, (0, 1, 0): 0.16666666666666666}
    assert qubit_state_marginal(prob_dist) == {(0, 0): 0.6666666666666666, (0, 1): 0.3333333333333333}

    # test case 3
    prob_dist = {(0, 0, 0): 0.5714285714285714, (0, 0, 1): 0.2857142857142857, (0, 1, 0): 0.14285714285714285}
    assert qubit_state_marginal(prob_dist) == {(0, 0): 0.8571428571428571, (0, 1): 0.14285714285714285}

def test_is_qubit_state():
    # test case 1
    state = (0, 0, 0)
    assert is_qubit_state(state) == (0, 0)

    # test case 2
    state = (0, 0, 1)
    assert is_qubit_state(state) == (0, 1)

    # test case 3
    state = (0, 1, 0)
    assert is_qubit_state(state) == (0, 0)

    # test case 4
    state = (1, 0, 0)
    assert is_qubit_state(state) == (0, 1)

    # test case 5
    state = (0, 1, 1)
    assert is_qubit_state(state) == False

    # test case 6
    state = (1, 0, 1)
    assert is_qubit_state(state) == False

    # test case 7
    state = (1, 1, 0)
    assert is_qubit_state(state) == False

    # test case 8
    state = (1, 1, 1)
    assert is_qubit_state(state) == False