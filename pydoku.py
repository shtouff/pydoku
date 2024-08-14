#!/usr/bin/env python3

import sys
from copy import deepcopy
from itertools import product
from typing import List, Tuple, Set

from math import ceil


class Pydoku(object):
    rows: List[List[int]]
    allwd_vals: Set[int] = {e for e in range(1, 10)}  # allowed values

    @classmethod
    def from_strings(cls, strings: List[str]):
        def c2v(c: str) -> int:
            assert len(c) == 1, "input is expected to be a single char"
            return 0 if c in " ." else int(c)

        return Pydoku([
            list(map(c2v, list(row))) for row in strings
        ])

    def __init__(self, rows: List[List[int]]):
        assert len(rows) == 9, "we expect 9 rows"
        assert all([len(row) == 9 for row in rows]), "we expect each row to be a list of 9 decimal digits"

        self.rows = rows

    def __str__(self) -> str:
        res = ""
        for start in 0, 3, 6:
            for row in self.rows[start: start + 3]:
                res += self.__row_as_str(row) + "\n"
            if start != 6:
                res += "------+-------+-------\n"
        return res

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, o):
        return str(self) == str(o)

    @staticmethod
    def __row_as_str(row: List[int]) -> str:
        res = ""
        for start in 0, 3, 6:
            for v in row[start: start + 3]:
                res += ("." if v == 0 else str(v)) + " "
            if start != 6:
                res += "| "
        return res

    def show_row(self, y):
        print(self.__row_as_str(self.rows[y - 1]) + "\n")

    def show_col(self, x):
        for start in 0, 3, 6:
            for row in self.rows[start: start + 3]:
                print(" " + ("." if row[x - 1] == 0 else str(row[x - 1])))
            print("" if start == 6 else "---")

    def show_sub(self, x, y):
        for row in self.rows[(y - 1) * 3: y * 3]:
            for v in row[(x - 1) * 3: x * 3]:
                print(("." if v == 0 else str(v)) + " ", end="")
            print("")
        print("")

    @staticmethod
    def __is_row_complete(row):
        return len(row) == 9 and 0 not in row

    def is_complete(self):
        return all([self.__is_row_complete(row) for row in self.rows])

    def misses_from_row(self, y) -> Set[int]:
        """
        return a set of missing values for this row
        """
        row = self.rows[y - 1]
        return self.allwd_vals - set(row)

    def misses_from_col(self, x) -> Set[int]:
        """
        return a set of missing values for this column
        """
        col = [row[x - 1] for row in self.rows]
        return self.allwd_vals - set(col)

    def misses_from_sub(self, x, y) -> Set[int]:
        """
        NB: the inputs x and y here are coords of the sub square, not its atomic elements:

            1,1 | 2,1 | 3,1
            ----+-----+----
            1,2 | 2,2 | 3,2
            ----+-----+----
            1,3 | 2,3 | 3,3


        return a set of missing values for this sub square
        """
        misses = self.allwd_vals
        for yy, xx in product(range((y - 1) * 3, y * 3), range((x - 1) * 3, x * 3)):
            if self.rows[yy][xx] != 0:
                misses = misses - {self.rows[yy][xx]}

        return misses

    def set_val(self, x: int, y: int, val: int):
        self.rows[y - 1][x - 1] = val

    def hypothesis(self) -> List[Tuple[Tuple[int, int], Set[int]]]:
        """
        return all hypothesis we can do on this grid, independently one from the other.
        it means some hypothesis can be mutually excluding !
        """
        hyps = []
        for y in range(1, 10):
            for x in range(1, 10):
                if self.rows[y - 1][x - 1] == 0:
                    y_misses = self.misses_from_row(y)
                    x_misses = self.misses_from_col(x)
                    xy_misses = self.misses_from_sub(ceil(x / 3.0), ceil(y / 3.0))

                    hyps.append(((x,y), y_misses.intersection(x_misses).intersection(xy_misses)))
        return hyps


class Solver(object):
    stack: List[Pydoku] = []

    def __init__(self, p: Pydoku):
        self.stack.append(p)

    def solve(self, debug: bool = False) -> List[Pydoku]:
        def backtrack():

            # try all hypothesis, recursively
            p = deepcopy(self.stack[-1])
            assert p == self.stack[-1]

            for (x, y), vals in p.hypothesis():
                for val in vals:
                    p.set_val(x, y, val)
                    self.stack.append(p)
                    if debug:
                        print(p)

                    if p.is_complete():
                        return self.stack

                    res = backtrack()  # inception !
                    if res is not None:
                        return res

                    self.stack.pop()
                    p.set_val(x, y, 0)
                return None  # no more hypothesis for those coords, dead-end detected

        return backtrack()


if __name__ == "__main__":
    p = Pydoku.from_strings(sys.argv[1:10])

    # p.show_row(7)
    # p.show_col(3)
    # p.show_sub(3, 2)

    s = Solver(p)
    s.solve(debug=True)
