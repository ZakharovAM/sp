import pytest

from main import biggestPath

test_data = [
    ({"dir1": {}, "dir2": ["file1"], "dir3": {"dir4": ["file2"], "dir5": {"dir6": {"dir7": {}}}}}, "/dir3/dir5/dir6/dir7"),
    ({"dir1": ["file1", "file1"]}, "/"),
    ({"dir1": ["file1", "file2", "file2"]}, "/dir1/file1")
]


@pytest.mark.parametrize("inp,expected", test_data)
def test_expected(inp, expected):
    assert biggestPath(inp) == expected
