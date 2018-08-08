def inc(x):
    return x + 1


# def test_failing():
#    assert inc(3) == 5


def test_ok():
    assert inc(3) == 4


# following list is not black-compatible
my_list = [
    1,
    2,
    3,
]
