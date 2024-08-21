from textwrap import dedent

import pytest

from pydoku import Solver


def test_pydoku_is_immutable(get_sudoku):
    easy1, _ = get_sudoku("sudouest", "easy1")

    with pytest.raises(TypeError):
        easy1[0] = [1, 2]

    with pytest.raises(TypeError):
        easy1[0][0] = 1


def test_str(get_sudoku):
    easy1, _ = get_sudoku("sudouest", "easy1")

    assert str(easy1) == dedent(
        """\
        703004021
        089160005
        000320760
        804000010
        190000407
        307016850
        900530200
        008002190
        032700084
        """
    )


def test_pretty(get_sudoku):
    easy1, _ = get_sudoku("sudouest", "easy1")

    assert str(easy1.pretty()) == dedent(
        """\
        7 . 3 | . . 4 | . 2 1 
        . 8 9 | 1 6 . | . . 5 
        . . . | 3 2 . | 7 6 . 
        ------+-------+-------
        8 . 4 | . . . | . 1 . 
        1 9 . | . . . | 4 . 7 
        3 . 7 | . 1 6 | 8 5 . 
        ------+-------+-------
        9 . . | 5 3 . | 2 . . 
        . . 8 | . . 2 | 1 9 . 
        . 3 2 | 7 . . | . 8 4 
        """
    )


def test_solver(sudokus):
    problem, solution = sudokus
    res = Solver(problem).solve()
    assert res == solution
