from pydoku import Pydoku, Solver


def test_solver1():
    p = Pydoku.from_strings([
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

    stack = Solver(p).solve()
    assert stack[-1] == Pydoku.from_strings([
        "763854921",
        "289167345",
        "415329768",
        "854973612",
        "196285437",
        "327416859",
        "941538276",
        "578642193",
        "632791584",
    ])


def test_solver2():
    p = Pydoku.from_strings([
        "87...15.3",
        "....8..26",
        "6..52....",
        ".918....4",
        "4.....215",
        "5.36.4.97",
        "9....6371",
        "1..73895.",
        "23.1.....",
    ])

    stack = Solver(p).solve()
    assert stack[-1] == Pydoku.from_strings([
        "872961543",
        "359487126",
        "614523789",
        "791852634",
        "468379215",
        "523614897",
        "985246371",
        "146738952",
        "237195468",
    ])


def test_solver3():
    # moyen difficile
    p = Pydoku.from_strings([
        ".38...42.",
        ".9....3..",
        "...1.8...",
        "..1.....4",
        ".8.7.4.5.",
        "..4...69.",
        "..9.7.1..",
        "...31....",
        "7..46.5..",
    ])

    stack = Solver(p).solve()
    print(stack[-1])
    # assert stack[-1] == Pydoku.from_strings([
    # ])
