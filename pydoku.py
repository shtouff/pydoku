#!/usr/bin/env python3
from __future__ import annotations

import os
from itertools import chain, product
from textwrap import dedent
import time
from typing import List, Tuple, Optional, Dict, Union


rc_start = lambda b: ((b // 3) * 3, (b % 3) * 3)
block_num = lambda r, c: (r // 3) * 3 + c // 3


class Pydoku(object):
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
    def from_docstring(cls, src: str) -> Pydoku:
        return cls.from_strings(src.split("\n")[0:9])

    @classmethod
    def from_strings(cls, strings: List[str]) -> Pydoku:
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

    def is_valid(self, digit: int, row: int, col: int) -> bool:
        """
        Check whether a specific number can be used for specific dimensions
        """
        r_start, c_start = map(lambda n: 3 * (n // 3), (row, col))
        return not (
            digit in self[row][0:9] or
            digit in [self[i][col] for i in range(9)] or
            digit in [
                self[i][j] for j in range(c_start, c_start + 3) for i in range(r_start, r_start + 3)
            ]
        )


class Solver(object):
    __p: __MutablePydoku = None

    class _DebugRow(list):
        __p: Pydoku = None

        def __init__(self, p: Pydoku, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__p = p

        def __setitem__(self, key, value):
            super().__setitem__(key, value)
            print(self.__p.pretty())
            time.sleep(0.02)

    Row = Union[List, _DebugRow]

    class __MutablePydoku(Pydoku):
        __mutable_rows: List[Solver.Row[int]] = None

        def __init__(self, p: Pydoku):
            if os.environ.get("DEBUG", "0").lower() in ["1", "true", "yes"]:
                rows = [Solver._DebugRow(self, row) for row in p]
            else:
                rows = [list(row) for row in p]

            super().__init__(rows)
            self.__mutable_rows = rows

        def __getitem__(self, item):
            return self.__mutable_rows[item]

        def allowed_values(self, row, col) -> List[int]:
            return [digit for digit in range(1, 10) if self.is_valid(digit, row, col)]

    def __init__(self, p: Pydoku):
        """
        Initialize a solver bound on a given sudoku object.

        NB: the given object will never be mutated.
        """

        self.__p = Solver.__MutablePydoku(p)

    def cache_allowed_values(self) -> Dict[Tuple[int, int], List[int]]:
        return {
            (row, col): self.__p.allowed_values(row, col)
            for row in range(9)
            for col in range(9)
            if self.__p[row][col] == 0
        }

    # def update_cache(self, cache, rows, cols, blocks):
    def update_cache(self, cache, updated):
        """
        Update the cache smartly. Compute every candidate, then dedup the list before actual update
        """
        # 1st, remove from cache positions that were updated.
        for row, col in updated:
            if (row, col) in cache:
                del cache[row, col]


        # 2nd, compute rows, cols and blocks that need a cache update
        rows = set([row for row, _ in updated])
        cols = set([col for _, col in updated])
        blocks = set([block_num(row, col) for row, col in updated])

        # 3rd, update the cache
        to_update = []

        ## Update candidate positions with rows, cols and blocks
        to_update.extend(product(rows, range(9)))
        to_update.extend(product(range(9), cols))

        for block in blocks:
            r_start, c_start = rc_start(block)
            to_update.extend(product(range(r_start, r_start + 3), range(c_start, c_start + 3)))

        ## actual update on dedup'ed list
        for row, col in set(to_update):
            if self.__p[row][col] == 0:
                cache[row, col] = self.__p.allowed_values(row, col)

    def update_with_unique_solutions(self, cache) -> List[Tuple[int, int]]:
        """
        Making use of the available information on the board, try to update the board where there is only one solution
        """
        digit_counts_in_row = [{} for _ in range(9)]
        digit_counts_in_col = [{} for _ in range(9)]
        digit_counts_in_block = [{} for _ in range(9)]

        # Iterate through the columns of a row and count appearance of numbers
        # within the cache
        for row in range(9):
            allwd_vals = list(chain(*[cache.get((row, col), []) for col in range(9)]))
            for digit in set(allwd_vals):
                digit_counts_in_row[row][digit] = allwd_vals.count(digit)

        # Iterate through the rows of a column and count appearance of numbers
        # within the cache
        for col in range(9):
            allwd_vals = list(chain(*[cache.get((row, col), []) for row in range(9)]))
            for digit in set(allwd_vals):
                digit_counts_in_col[col][digit] = allwd_vals.count(digit)

        # Iterate through the 9 different blocks of the board and count
        # appearance of numbers within the cache
        for block in range(9):
            r_start, c_start = rc_start(block)
            allwd_vals = list(chain(*[
                cache.get((row, col), []) for col in range(c_start, c_start + 3) for row in
                range(r_start, r_start + 3)
            ]))
            for digit in set(allwd_vals):
                digit_counts_in_block[block][digit] = allwd_vals.count(digit)

        # now check if there are some values in the cache for which their occurrence is
        # unique in their row, or in their column, or in their block.
        # Also, handle obvious cases where values in cache is unique.
        #
        # In both cases, update the board and notify caller.
        updated = []

        for (row, col), values in cache.items():
            if len(values) == 1:
                self.__p[row][col] = values[0]
                updated.append((row, col))
                continue
            block = block_num(row, col)
            for value in values:
                if digit_counts_in_row[row][value] == 1 or digit_counts_in_col[col][value] == 1 or \
                        digit_counts_in_block[block][value] == 1:
                    self.__p[row][col] = value
                    updated.append((row, col))

        return updated

    def solve(self):
        def __backtrack() -> bool:
            blank = self.__p.find_empty()
            if not blank:
                return True
            else:
                row, col = blank

            for i in cache[(row, col)]:
                if self.__p.is_valid(i, row, col):
                    # try with difit i
                    self.__p[row][col] = i

                    # if success, stop recursion
                    if __backtrack():
                        return True

                    # otherwise, rollback then give a chance to the next digit
                    self.__p[row][col] = 0
            return False

        cache = self.cache_allowed_values()
        while True:
            updated = self.update_with_unique_solutions(cache)
            if not updated:
                break
            self.update_cache(cache, updated)

        if __backtrack():
            return self.__p
        else:
            raise RuntimeError("could not solve this sudoku")


if __name__ == "__main__":
    p = Pydoku.from_docstring(dedent("""\
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
    print(p.pretty())
    print(Solver(p).solve().pretty())
