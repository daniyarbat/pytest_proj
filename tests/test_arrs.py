from utils import arrs

def test_get_existing_index():
    assert arrs.get([1, 2, 3], 1, "test") == 2

def test_get_non_existing_index_with_default():
    assert arrs.get([1, 2, 3], 10, "test") == "test"

def test_get_negative_index_with_default():
    assert arrs.get([1, 2, 3], -1, "test") == "test"

def test_get_empty_list():
    assert arrs.get([], 0, "test") == "test"

def test_my_slice_default():
    assert arrs.my_slice([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_my_slice_with_start():
    assert arrs.my_slice([1, 2, 3, 4, 5], 2) == [3, 4, 5]

def test_my_slice_with_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], None, 3) == [1, 2, 3]

def test_my_slice_with_negative_start():
    assert arrs.my_slice([1, 2, 3, 4, 5], -2) == [4, 5]

def test_my_slice_with_negative_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], None, -2) == [1, 2, 3]

def test_my_slice_with_negative_start_and_end():
    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]

def test_my_slice_empty_list():
    assert arrs.my_slice([], 1, 3) == []
