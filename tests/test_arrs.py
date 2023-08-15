import pytest
from utils import arrs

# Фикстура для создания пустого списка перед каждым тестом
@pytest.fixture
def empty_list():
    return []

# Фикстура для создания списка перед каждым тестом
@pytest.fixture
def sample_list():
    return [1, 2, 3, 4, 5]

def test_get_existing_index(sample_list):
    assert arrs.get(sample_list, 1, "test") == 2

def test_get_non_existing_index_with_default(sample_list):
    assert arrs.get(sample_list, 10, "test") == "test"

def test_get_negative_index_with_default(sample_list):
    assert arrs.get(sample_list, -1, "test") == "test"

def test_get_empty_list(empty_list):
    assert arrs.get(empty_list, 0, "test") == "test"

def test_my_slice_default(sample_list):
    assert arrs.my_slice(sample_list) == [1, 2, 3, 4, 5]

def test_my_slice_with_start(sample_list):
    assert arrs.my_slice(sample_list, 2) == [3, 4, 5]

def test_my_slice_with_end(sample_list):
    assert arrs.my_slice(sample_list, None, 3) == [1, 2, 3]

def test_my_slice_with_negative_start(sample_list):
    assert arrs.my_slice(sample_list, -2) == [4, 5]

def test_my_slice_with_negative_end(sample_list):
    assert arrs.my_slice(sample_list, None, -2) == [1, 2, 3]

def test_my_slice_with_negative_start_and_end(sample_list):
    assert arrs.my_slice(sample_list, -3, -1) == [3, 4]

def test_my_slice_empty_list(empty_list):
    assert arrs.my_slice(empty_list, 1, 3) == []

