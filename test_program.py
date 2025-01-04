from program import *


def test_sorted():
    sorted_result = sortedList()
    print(f"Sorted list: {sorted_result}")
    assert sorted_result == [1, 2, 3, 4, 5]


def test_reverse():
    reverse_result = reverseList()
    print(f"Reversed list: {reverse_result}")
    assert reverse_result == [5, 4, 3, 2, 1]
