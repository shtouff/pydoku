import pytest

from pydoku import Pydoku


@pytest.fixture
def p763():
    return Pydoku.from_strings([
        "7 3  4 21",
        " 8916   5",
        "   32 76 ",
        "8 4    1 ",
        "19    4 7",
        "3 7 1685 ",
        "9  53 2  ",
        "  8  219 ",
        " 327   84",
    ])
