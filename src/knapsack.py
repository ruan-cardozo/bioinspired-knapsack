import numpy as np
from src.config import NUMPY_RANDOM_GENERATOR

FITNESS_INVALID = 0

def fitness(individual, values, weights, capacity):
    total_weight = np.dot(individual, weights)
    if total_weight > capacity:
        return FITNESS_INVALID
    return np.dot(individual, values)

def generate_individual(n):
    return NUMPY_RANDOM_GENERATOR.integers(2, size=n)

def generate_population(pop_size, n):
    return [generate_individual(n) for _ in range(pop_size)]
