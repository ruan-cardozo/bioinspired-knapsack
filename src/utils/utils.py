import random

CAPACITY_RATIO = 0.6

def generate_items(num_items, value_range=(1, 100), weight_range=(1, 50)):
    values = [random.randint(*value_range) for _ in range(num_items)]
    weights = [random.randint(*weight_range) for _ in range(num_items)]
    capacity = int(sum(weights) * CAPACITY_RATIO)
    return values, weights, capacity
