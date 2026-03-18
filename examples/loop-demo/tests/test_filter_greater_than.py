from filter import filter_greater_than


def test_filters_numbers_greater_than_limit():
    result = filter_greater_than([12, 45, 7, 23, 56, 89, 3, 67], 20)
    assert result == [45, 23, 56, 89, 67]


def test_returns_empty_list_when_no_numbers_exceed_limit():
    result = filter_greater_than([1, 2, 3], 10)
    assert result == []


def test_returns_all_numbers_when_all_exceed_limit():
    result = filter_greater_than([50, 60, 70], 10)
    assert result == [50, 60, 70]


def test_does_not_include_number_equal_to_limit():
    result = filter_greater_than([10, 20, 30], 20)
    assert result == [30]


def test_empty_input_list():
    result = filter_greater_than([], 5)
    assert result == []


def test_does_not_modify_original_list():
    original = [5, 25, 15]
    filter_greater_than(original, 10)
    assert original == [5, 25, 15]
