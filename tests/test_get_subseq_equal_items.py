import pytest
from task import get_subseq_equal_items

test_data = (
    ("aabc", [["a", "a"], ["b"], ["c"]]),
    ("aabcс", [["a", "a"], ["b"], ["c"], ["с"]]),
    ("1111221133444", [["1", "1", "1", "1"], ["2", "2"], ["1", "1"], ["3", "3"], ["4", "4", "4"]]),
)


@pytest.mark.parametrize("inp,expected", test_data)
def test_get_subseq_equal_items(inp, expected):
    assert get_subseq_equal_items(inp) == expected
