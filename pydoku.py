import sys
from copy import copy, deepcopy
from functools import lru_cache
from itertools import product
from typing import List, Tuple, Set

from math import ceil


class Pydoku(object):
    rows: List[List[int]]
    vals: Set[int]

    @classmethod
    def from_strings(cls, strings: List[str]):
        if len(strings) != 9:
            raise ValueError(f"input should contain 9 strings of 9 numbers, space or . meaning no value")

        rows = []
        for s in strings:
            if len(s) != 9:
                raise ValueError(f"{s} doesnt have 9 values")
            row = []
            for char in s:
                if char in " .":
                    row.append(0)
                else:
                    row.append(int(char))
            rows.append(row)
        return Pydoku(rows)

    def __init__(self, rows: List[List[int]]):
        self.rows = rows
        self.vals = {e for e in range(1, 10)}  # possible values

    def __str__(self) -> str:
        res = ""
        for start in 0, 3, 6:
            for row in self.rows[start: start + 3]:
                res += self._row_str(row) + "\n"
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
    def _row_str(row: List[int]) -> str:
        res = ""
        for start in 0, 3, 6:
            for n in row[start: start + 3]:
                if n == 0:
                    res += ". "
                else:
                    res += f"{n} "
            if start != 6:
                res += "| "
        return res

    def show_row(self, y):
        print(self._row_str(self.rows[y - 1]))
        print("")

    def show_col(self, x):
        for start in 0, 3, 6:
            for row in self.rows[start: start + 3]:
                if row[x - 1] == 0:
                    print(".")
                else:
                    print(row[x - 1])
            if start != 6:
                print("--")
            else:
                print("")

    def show_sub(self, x, y):
        for row in self.rows[(y - 1) * 3: y * 3]:
            for val in row[(x - 1) * 3: x * 3]:
                if val == 0:
                    print(". ", end="")
                else:
                    print(f"{val} ", end="")
            print("")
        print("")

    @staticmethod
    def is_row_complete(row):
        return len(row) == 9 and 0 not in row

    def is_complete(self):
        return all([self.is_row_complete(row) for row in self.rows])

    def is_valid(self):
        return all([
            *[self.is_row_valid(y) for y in range(1, 10)],
            *[self.is_col_valid(x) for x in range(1, 10)],
            *[self.is_sub_valid(x, y) for x, y in product(range(1, 4), repeat=2)]
        ])

    @lru_cache(maxsize=1_000_000)
    def miss_from_row(self, y) -> Tuple[Set[int], List[Tuple[int, int]]]:
        """
        return 2 lists:
        - the list of missing values
        - the list of coords (x, y), index 1, for those values
        """
        row = self.rows[y - 1]
        misses = self.vals - set(row)
        coords = []

        for xx, val in enumerate(row):
            if val == 0:
                coords.append((xx + 1, y))

        return misses, coords

    @lru_cache(maxsize=1_000_000)
    def miss_from_col(self, x) -> Tuple[Set[int], List[Tuple[int, int]]]:
        """
        return 2 lists:
        - the list of missing values
        - the list of coords (x, y), index 1, for those values
        """
        col = [row[x - 1] for row in self.rows]
        misses = self.vals - set(col)
        coords = []

        for yy, val in enumerate(col):
            if val == 0:
                coords.append((x, yy + 1))

        return misses, coords

    @lru_cache(maxsize=1_000_000)
    def miss_from_sub(self, x, y):
        """
        NB: the inputs x and y here are coords of the sub square, not its atomic elements:

            1,1 | 2,1 | 3,1
            ----+-----+----
            1,2 | 2,2 | 3,2
            ----+-----+----
            1,3 | 2,3 | 3,3


        return 2 lists:
        - the list of missing values
        - the list of coords (x, y), index 1, for those values. x and y are classical coords of elements.

        """
        coords = []
        misses = self.vals
        for yy, xx in product(range((y - 1) * 3, y * 3), range((x - 1) * 3, x * 3)):
            if self.rows[yy][xx] == 0:
                coords.append((xx + 1, yy + 1))
            else:
                misses = misses - {self.rows[yy][xx]}

        return misses, coords

    def is_row_valid(self, y):
        # return len(list(self.miss_from_row(y))) == 0
        return len(self.miss_from_row(y)[0]) == 0

    def is_col_valid(self, x):
        # return len(list(self.miss_from_col(x))) == 0
        return len(self.miss_from_col(x)[0]) == 0

    def is_sub_valid(self, x, y):
        return len(list(self.miss_from_sub(x, y))) == 0

    def set_val(self, x, y, val: int):
        self.rows[y - 1][x - 1] = val

    def hypothesis(self) -> List[Tuple[Tuple[int, int], Set[int]]]:
        """
        return all hypothesis we can do on this grid, independently
        """
        hyps = []
        for y in range(1, 10):
            for x in range(1, 10):
                if self.rows[y - 1][x - 1] == 0:
                    ymiss, _ = self.miss_from_row(y)
                    xmiss, _ = self.miss_from_col(x)
                    smiss, _ = self.miss_from_sub(ceil(x/3.0), ceil(y/3.0))

                    hyps.append(((x,y), ymiss.intersection(xmiss).intersection(smiss)))
        return hyps


class Solver(object):
    stack: List[Pydoku] = []

    def __init__(self, p: Pydoku):
        self.stack.append(p)

    def solve(self) -> List[Pydoku]:
        def backtrack():
            # 1st, optimize as much as possible with card-1 hypothesis: non-recursive part
            # while True:
            #     p = deepcopy(self.stack[-1])
            #     assert p == self.stack[-1]
            #     for (x, y), vals in p.hypothesis():
            #         if len(vals) == 1:
            #             if x == 8 and y in [7, 8]:
            #                 breakpoint()
            #             p.set_val(x, y, list(vals)[0])
            #     if p != self.stack[-1]: # was mutated, stack it !
            #         self.stack.append(p)
            #     elif p.is_complete():
            #         return self.stack
            #     else:
            #         break

            # print(p)

            # try other hypothesis, recursively
            for (x, y), vals in p.hypothesis():
                for val in vals:
                    # if x == 8 and y in [7, 8]:
                    #     breakpoint()
                    p.set_val(x, y, val)
                    # if all([
                    #     p.is_row_valid(y),
                    #     p.is_col_valid(x),
                    #     p.is_sub_valid(ceil(x / 3.0), ceil(y / 3.0)),
                    # ]):
                    self.stack.append(p)
                    if p.is_complete():
                        return self.stack
                    res = backtrack()
                    if res is not None:
                        return res
                    self.stack.pop()
                    p.set_val(x, y, 0)
                return None  # no more hypothesis for those coords

        return backtrack()


if __name__ == "__main__":
    p = Pydoku.from_strings(sys.argv[1:10])
    s = Solver(p)
    # print(s.solve()[-1])
    for idp, p in enumerate(s.solve()):
        print(f"## {idp} ##")
        print(p)
