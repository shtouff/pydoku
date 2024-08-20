from __future__ import annotations

from textwrap import dedent
from typing import List, Tuple, Optional


class Pydoku2(object):
    """
    An  immutable object representing a sudoku grid.
    """
    __rows: Tuple[Tuple[int, ...], ...] = None

    def __init__(self, rows: List[List[int]]):
        assert len(rows) == 9, "we expect 9 rows"
        assert all([len(row) == 9 for row in rows]), "we expect each row to be a list of 9 decimal digits"
        self.__rows = tuple([tuple(row) for row in rows])

    @staticmethod
    def __char2digit(char: str) -> int:
        assert len(char) == 1, "input is expected to be a single char"
        return 0 if char in " ." else int(char)

    @classmethod
    def from_docstring(cls, src: str) -> Pydoku2:
        return cls.from_strings(src.split("\n")[0:9])

    @classmethod
    def from_strings(cls, strings: List[str]) -> Pydoku2:
        return cls([
            list(map(cls.__char2digit, list(row))) for row in strings
        ])

    @staticmethod
    def __row_as_str(row: List[int]) -> str:
        res = ""
        for start in 0, 3, 6:
            for v in row[start: start + 3]:
                res += ("." if v == 0 else str(v)) + " "
            if start != 6:
                res += "| "
        return res

    def pretty(self) -> str:
        res = ""
        for start in 0, 3, 6:
            for row in self[start: start + 3]:
                res += self.__row_as_str(row) + "\n"
            if start != 6:
                res += "------+-------+-------\n"
        return res

    def __str__(self) -> str:
        res = ""
        for row in self:
            res += "".join(map(str, row)) + "\n"
        return res

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, o):
        return str(self) == str(o)

    def __hash__(self):
        return hash(str(self))

    def __getitem__(self, item):
        return self.__rows[item]

    def find_empty(self) -> Optional[Tuple[int, int]]:
        """
        Find next empty space in Sudoku board and return dimensions
        """
        for row in range(9):
            for col in range(9):
                if self[row][col] == 0 :
                    return row, col
        return None

    def is_valid(self, num, pos) -> bool:
        """
        Check whether a specific number can be used for specific dimensions
        """
        row, col = pos
        # Check if all row elements include this number
        for j in range(9):
            if self[row][j] == num:
                return False

        # Check if all column elements include this number
        for i in range(9):
            if self[i][col] == num:
                return False

        # Check if the number is already included in the block
        r_start, c_start = map(lambda n: 3 * (n // 3), (row, col))

        for i in range(r_start, r_start + 3):
            for j in range(c_start, c_start + 3):
                if self[i][j] == num:
                    return False

        return True

class Solver(object):
    __p: __MutablePydoku = None

    class __MutablePydoku(Pydoku2):
        __mutable_rows: List[List[int]] = None

        def __init__(self, p: Pydoku2):
            rows = [list(row) for row in p]
            super().__init__(rows)
            self.__mutable_rows = rows

        def __getitem__(self, item):
            return self.__mutable_rows[item]

    def __init__(self, p: Pydoku2):
        """
        Initialize a solver bound on a given sudoku object.

        NB: the given object will never be mutated.
        """

        self.__p = Solver.__MutablePydoku(p)

    # Solve Sudoku using backtracking
    def solve(self) -> Pydoku2:

        def __backtrack(p: Solver.__MutablePydoku):
            blank = p.find_empty()
            if not blank:
                return True
            else:
                row, col = blank

            for i in range(1,10):
                if p.is_valid(i, (row, col)):
                    # try with digit i
                    p[row][col] = i

                    # if success, stop recursion
                    if __backtrack(p):
                        return True

                    # otherwise, rollback then give a chance to the next digit
                    p[row][col] = 0

            # no digit worked, it's a dead-end
            return False

        if __backtrack(self.__p):
            return self.__p
        else:
            raise RuntimeError("could not solve this sudoku")

if __name__ == "__main__":
    p = Pydoku2.from_docstring(dedent("""\
        .35....4.
        6....4...
        1..7..92.
        ...6..7.5
        ...2.....
        .4..89...
        .5....8.4
        .......69
        ...965.7.
    """))

    print(Solver(p).solve().pretty())
