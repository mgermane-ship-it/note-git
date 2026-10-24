"""Complete solutions for the Lessons 01–06 exam-preparation workshop."""


def shipping_fee(weight, express=False):
    pass


def passing_students(results, threshold=10):
    pass


def summarize_inventory(deliveries):
    pass


def read_score():
    while True:
        pass




def number_sign(n):
    pass


def count_above(values, limit):
    pass


def cheapest_product(prices):
    # The exercise assumes a nonempty dictionary and a unique minimum.
    pass


def average(values):
    # The exercise assumes a nonempty list.
    pass


def shared_interests(first, second):
    pass

def run_tests():
    assert shipping_fee(1.5) == 3
    assert shipping_fee(2) == 3
    assert shipping_fee(3, express=True) == 10
    try:
        shipping_fee(0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for zero weight")

    results = [("Maya", 14), ("Leo", 8), ("Nina", 10), ("Omar", 17)]
    assert passing_students(results) == ["Maya", "Nina", "Omar"]
    assert passing_students(results, 15) == ["Omar"]
    assert passing_students([]) == []

    deliveries = [("apple", 2), ("pear", 1), ("apple", 4), ("pear", 2)]
    totals, large = summarize_inventory(deliveries)
    assert totals == {"apple": 6, "pear": 3}
    assert large == {"apple"}
    assert summarize_inventory([]) == ({}, set())

    # Test interactive input without requiring manual typing.
    from unittest.mock import patch
    from io import StringIO
    with patch("builtins.input", side_effect=["hello", "25", "16"]):
        with patch("sys.stdout", new_callable=StringIO) as output:
            assert read_score() == 16
            assert output.getvalue().splitlines() == [
                "Invalid integer", "Out of range"
            ]
    assert number_sign(5) == "positive"
    assert number_sign(-2) == "negative"
    assert number_sign(0) == "zero"
    assert count_above([3, 8, 1, 9], 5) == 2
    assert count_above([], 5) == 0
    assert cheapest_product({"pen": 2, "book": 8, "eraser": 1}) == "eraser"
    assert average([2, 4, 6]) == 4
    assert average([10]) == 10
    assert shared_interests({"music", "sport"}, {"sport", "art"}) == {"sport"}
    assert shared_interests(set(), {"art"}) == set()
    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
