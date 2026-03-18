from filter import sort_naive


def test_sorts_unsorted_list():
    result = sort_naive([3, 1, 4, 1, 5, 9, 2, 6])
    assert result == [1, 1, 2, 3, 4, 5, 6, 9]


def test_already_sorted_list():
    result = sort_naive([1, 2, 3, 4])
    assert result == [1, 2, 3, 4]


def test_reverse_sorted_list():
    result = sort_naive([5, 4, 3, 2, 1])
    assert result == [1, 2, 3, 4, 5]


def test_single_element():
    result = sort_naive([42])
    assert result == [42]


def test_empty_list():
    result = sort_naive([])
    assert result == []


def test_list_with_duplicates():
    result = sort_naive([3, 3, 1, 1, 2, 2])
    assert result == [1, 1, 2, 2, 3, 3]


def test_does_not_modify_original_list():
    original = [3, 1, 2]
    sort_naive(original)
    assert original == [3, 1, 2]
