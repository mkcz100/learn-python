import pytest
from common.util import build_path
from data.numpy_manager import NumpyManger


def test_load_data():
    npm = NumpyManger()

    data = npm.load_file(build_path('assets/sample1.csv'))
    num_rows, num_cols = data.shape

    assert 4 == num_cols
    assert 21 == num_rows
