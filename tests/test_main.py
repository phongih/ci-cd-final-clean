from app import main


def test_add():
    assert main.add(2, 3) == 5


def test_subtract():
    assert main.subtract(5, 3) == 2
