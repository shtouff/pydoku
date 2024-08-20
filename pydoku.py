#!/usr/bin/env python3

from __future__ import annotations

import sys
from copy import deepcopy
from functools import lru_cache
from itertools import product
from typing import List, Tuple, Set

from math import ceil


class Pydoku(object):
    rows: List[List[int]]
    allwd_vals: Set[int] = {e for e in range(1, 10)}  # allowed values

    @staticmethod
    def __char2digit(char: str) -> int:
        assert len(char) == 1, "input is expected to be a single char"
        return 0 if char in " ." else int(char)

    @classmethod
    def from_docstring(cls, src: str) -> Pydoku:
        return cls.from_strings(src.split("\n")[0:9])

    @classmethod
    def from_strings(cls, strings: List[str]) -> Pydoku:
        return cls([
            list(map(cls.__char2digit, list(row))) for row in strings
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

    def __hash__(self):
        return hash(str(self))

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

        # for yy, xx in product(range((y - 1) * 3, y * 3), range((x - 1) * 3, x * 3)):
        #     if self.rows[yy][xx] != 0:
        #         misses = misses - {self.rows[yy][xx]}
        for yy in range((y - 1) * 3, y * 3):
            for xx in range((x - 1) * 3, x * 3):
                if self.rows[yy][xx] != 0:
                    misses = misses - {self.rows[yy][xx]}

        return misses

    def set_val(self, x: int, y: int, val: int):
        self.rows[y - 1][x - 1] = val

    # @lru_cache()
    def hypothesis(self) -> List[Tuple[Tuple[int, int], List[int]]]:
        """
        return all hypothesis we can do on this grid, independently one from the other.
        it means some hypothesis can be mutually excluding !
        """
        hyps = []

        # dcount = 0
        # for x, y in product(range(1, 5), range(1, 10)):
        #     if self.rows[y - 1][x - 1] == 0:
        #         dcount += 1
        # for y in range(1, 6):
        #     if self.rows[y - 1][4] == 0:
        #         dcount += 1
        #
        # rcount = 0
        # for y, x in product(range(1, 5), range(1, 10)):
        #     if self.rows[y - 1][x - 1] == 0:
        #         rcount += 1
        # for x in range(1, 6):
        #     if self.rows[4][x - 1] == 0:
        #         rcount += 1
        #
        # if dcount > rcount:
        #     for x, y in product(range(1, 10), range(1, 10)):
        #         if self.rows[y - 1][x - 1] == 0:
        #             y_misses = self.misses_from_row(y)
        #             x_misses = self.misses_from_col(x)
        #             xy_misses = self.misses_from_sub(ceil(x / 3.0), ceil(y / 3.0))
        #
        #             hyps.append(((x, y), y_misses.intersection(x_misses).intersection(xy_misses)))
        # else:
        #     for y, x in product(range(1, 10), range(1, 10)):
        #         if self.rows[y - 1][x - 1] == 0:
        #             y_misses = self.misses_from_row(y)
        #             x_misses = self.misses_from_col(x)
        #             xy_misses = self.misses_from_sub(ceil(x / 3.0), ceil(y / 3.0))
        #
        #             hyps.append(((x, y), y_misses.intersection(x_misses).intersection(xy_misses)))

        # for y in range(1, 10):
        #     for x in range(1, 10):
        #         if self.rows[y - 1][x - 1] == 0:
        #             y_misses = self.misses_from_row(y)
        #             x_misses = self.misses_from_col(x)
        #             xy_misses = self.misses_from_sub(ceil(x / 3.0), ceil(y / 3.0))
        #
        #             hyps.append(((x, y), y_misses.intersection(x_misses).intersection(xy_misses)))
        for y, x in product(range(1, 10), range(1, 10)):
            if self.rows[y - 1][x - 1] == 0:
                y_misses = self.misses_from_row(y)
                x_misses = self.misses_from_col(x)
                xy_misses = self.misses_from_sub(ceil(x / 3.0), ceil(y / 3.0))

                hyps.append(((x, y), list(y_misses.intersection(x_misses).intersection(xy_misses))))


        # sort hypothesis by increasing frequency of appareance of values
        hyps_by_coords = {}
        for (x, y), vals in hyps:
            hyps_by_coords[x, y] = vals

        for (x, y), vals in hyps:
            freqs = [0] * 9

            # scan row
            for xx in range(1, 10):
                for val in hyps_by_coords.get((xx, y), []):
                    freqs[val - 1] += 1

            # scan col
            for yy in range(1, 10):
                for val in hyps_by_coords.get((x, yy), []):
                    freqs[val - 1] += 1

            # scan sub square
            xstart = (ceil(x / 3.0) - 1) * 3 + 1
            ystart = (ceil(y / 3.0) - 1) * 3 + 1
            for yy in range(ystart, ystart + 3):
                for xx in range(xstart, xstart + 3):
                    for val in hyps_by_coords.get((xx, yy), []):
                        freqs[val - 1] += 1

            # re-order this vals given frequencies
            vals.sort(key=lambda e: freqs[e - 1])

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
    p = Pydoku.from_strings([
        ".35....4.",
        "6....4...",
        "1..7..92.",
        "...6..7.5",
        "...2.....",
        ".4..89...",
        ".5....8.4",
        ".......69",
        "...965.7.",
    ])
    s = Solver(p)
    s.solve(debug=True)


    # p = Pydoku.from_strings([
    #     ".38...42.",
    #     ".9....3..",
    #     "...1.8...",
    #     "..1.....4",
    #     ".8.7.4.5.",
    #     "..4...69.",
    #     "..9.7.1..",
    #     "...31....",
    #     "7..46.5..",
    # ])
    # s = Solver(p)
    # s.solve(debug=True)


    # p = Pydoku.from_strings(sys.argv[1:10])
    #
    # p.show_row(7)
    # p.show_col(3)
    # p.show_sub(3, 2)
    #
    # s = Solver(p)
    # s.solve(debug=True)
