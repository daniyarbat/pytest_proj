from utils import arrs

def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2  # Ожидаемое значение изменено на 2
    assert arrs.get([], 0, "test") == "test"

def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]  # Ожидаемый срез не меняется
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]  # Ожидаемый срез не меняется

