from __future__ import annotations

from typing import Tuple, Any, Dict

import pytest

from sudouest import sudokus as so_sudokus
from euler import sudokus as eu_sudokus
from pydoku import Pydoku


def get_sudoku_by_type(source: str, name: str, cls: type[Pydoku]) -> Tuple[Pydoku, Pydoku]:
    if source == "sudouest":
        docstrings = so_sudokus[name]
    elif source == "euler":
        docstrings = eu_sudokus[name]
    else:
        raise ValueError(f"unknown source: {source}")
    return cls.from_docstring(docstrings[0]), cls.from_docstring(docstrings[1])


@pytest.fixture()
def get_sudoku():
    def __f(source, name) -> Tuple[Pydoku, Pydoku]:
        return get_sudoku_by_type(source, name, Pydoku)
    return __f


@pytest.fixture(params=so_sudokus.keys())
def sudouest(get_sudoku, request):
    return get_sudoku("sudouest", request.param)


@pytest.fixture(params=eu_sudokus.keys())
def euler(get_sudoku, request):
    return get_sudoku("euler", request.param)


def __flatten(d: Dict[str, Dict[str, Any]]):
    """
    Flatten a dict of dicts to a list a combined keys
    """
    keys = []
    for k1 in d.keys():
        for k2 in d[k1].keys():
            keys.append(":".join([k1, k2]))

    return keys


@pytest.fixture(params=__flatten(dict(sudouest=so_sudokus, euler=eu_sudokus)))
def sudokus(get_sudoku, request):
    return get_sudoku(*request.param.split(":"))
