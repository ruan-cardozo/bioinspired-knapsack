import numpy as np
from src.knapsack import (
    fitness,
    generate_individual,
    generate_population
)

class TestFitness:
    def test_fitness(self):
        values = [10, 20, 30]
        weights = [1, 2, 3]
        capacity = 5

        # Takes items 0 and 2
        individual = [1, 0, 1]
        assert fitness(individual, values, weights, capacity) == 40

        # Takes items 0 and 1
        individual = [1, 1, 0]
        assert fitness(individual, values, weights, capacity) == 30

        # Takes no items
        individual = [0, 0, 0]
        assert fitness(individual, values, weights, capacity) == 0

        # Takes all items (exceeds capacity)
        individual = [1, 1, 1]
        assert fitness(individual, values, weights, capacity) == 0

class TestGenerateIndividual:
    def test_generate_individual_multiple_runs(self):
        n = 10
        for _ in range(20):
            individual = generate_individual(n)
            assert len(individual) == n
            assert all(gene in [0, 1] for gene in individual)

    def test_generate_individual_zero_length(self):
        n = 0
        individual = generate_individual(n)
        assert len(individual) == 0
        assert isinstance(individual, np.ndarray)

    def test_generate_individual_type(self):
        n = 4
        individual = generate_individual(n)
        assert isinstance(individual, np.ndarray)

class TestGeneratePopulation:
    def test_generate_population_size(self):
        pop_size = 5
        n = 10
        population = generate_population(pop_size, n)
        assert len(population) == pop_size
        for individual in population:
            assert len(individual) == n
            assert all(gene in [0, 1] for gene in individual)

    def test_generate_population_zero_size(self):
        pop_size = 0
        n = 10
        population = generate_population(pop_size, n)
        assert len(population) == 0

    def test_generate_population_type(self):
        pop_size = 3
        n = 4
        population = generate_population(pop_size, n)
        assert isinstance(population, list)
        for individual in population:
            assert isinstance(individual, np.ndarray)
