from filter import quick_sort


def test_sorts_unsorted_list():
    result = quick_sort([3, 1, 4, 1, 5, 9, 2, 6])
    assert result == [1, 1, 2, 3, 4, 5, 6, 9]


def test_already_sorted_list():
    result = quick_sort([1, 2, 3, 4])
    assert result == [1, 2, 3, 4]


def test_reverse_sorted_list():
    result = quick_sort([5, 4, 3, 2, 1])
    assert result == [1, 2, 3, 4, 5]


def test_single_element():
    result = quick_sort([42])
    assert result == [42]


def test_empty_list():
    result = quick_sort([])
    assert result == []


def test_list_with_duplicates():
    result = quick_sort([3, 3, 1, 1, 2, 2])
    assert result == [1, 1, 2, 2, 3, 3]


def test_does_not_modify_original_list():
    original = [3, 1, 2]
    quick_sort(original)
    assert original == [3, 1, 2]
