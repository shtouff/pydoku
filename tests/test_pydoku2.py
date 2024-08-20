import pytest

from pydoku2 import Solver


def test_pydoku_is_immutable(get_sudoku2):
    easy1, _ = get_sudoku2("sudouest", "easy1")

    with pytest.raises(TypeError):
        easy1[0] = [1, 2]

    with pytest.raises(TypeError):
        easy1[0][0] = 1



def test_solver(sudokus2):
    problem, solution = sudokus2
    res = Solver(problem).solve()
    assert res == solution
