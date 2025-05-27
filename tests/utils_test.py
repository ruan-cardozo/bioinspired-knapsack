from src.utils.utils import generate_items

def test_generate_items():
    num_items = 10
    values, weights, capacity = generate_items(num_items)

    assert len(values) == num_items
    assert len(weights) == num_items
    assert isinstance(capacity, int)
    assert capacity > 0

    for value in values:
        assert isinstance(value, int)
        assert value > 0

    for weight in weights:
        assert isinstance(weight, int)
        assert weight > 0
    assert capacity <= sum(weights) * 0.6
    assert capacity >= min(weights)
