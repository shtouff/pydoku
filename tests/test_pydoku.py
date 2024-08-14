from textwrap import dedent

from pydoku import Solver


def test_misses_from_row(easy1):
    assert easy1.misses_from_row(2) == {2, 3, 4, 7}


def test_misses_from_col(easy1):
    assert easy1.misses_from_col(7) == {3, 5, 6, 9}


def test_misses_from_sub(easy1):
    assert easy1.misses_from_sub(3, 1) == {3, 4, 8, 9}


def test_show_row(easy1, capsys):
    easy1.show_row(2)
    captured = capsys.readouterr()
    assert captured.out == dedent(
        """\
        . 8 9 | 1 6 . | . . 5 
        
        """
    )


def test_show_col(easy1, capsys):
    easy1.show_col(7)
    captured = capsys.readouterr()
    assert captured.out == dedent(
        """\
         .
         .
         7
        ---
         .
         4
         8
        ---
         2
         1
         .
        
        """
    )


def test_str(easy1):
    assert str(easy1) == dedent(
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


def test_show_sub(easy1, capsys):
    easy1.show_sub(3, 1)
    captured = capsys.readouterr()
    assert captured.out == dedent(
        """\
        . 2 1 
        . . 5 
        7 6 . 
    
        """
    )


def test_solver(sudoku):
    problem, solution = sudoku
    stack = Solver(problem).solve()
    assert stack[-1] == solution
