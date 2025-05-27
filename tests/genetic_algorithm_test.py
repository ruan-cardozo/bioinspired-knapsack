import numpy as np
from src.genetic_algorithm import (
    selection,
    crossover,
    mutate,
    genetic_algorithm
)

class TestSelection:
    def test_selection(self):
        population = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 1, 0]
        ]
        values = [10, 20, 30]
        weights = [1, 2, 3]
        capacity = 5

        selected = selection(population, values, weights, capacity)
        assert len(selected) == 2
        assert all(isinstance(individual, list) for individual in selected)

    def test_selection_zero_fitness(self):
        population = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        values = [10, 20, 30]
        weights = [1, 2, 3]
        capacity = 5

        selected = selection(population, values, weights, capacity)
        assert len(selected) == 2
        assert all(isinstance(individual, list) for individual in selected)

class TestCrossover:
    def test_crossover(self):
        parent1 = [1, 0, 1, 0]
        parent2 = [0, 1, 0, 1]
        child1, child2 = crossover(parent1, parent2)

        assert len(child1) == len(parent1)
        assert len(child2) == len(parent2)
        assert set(child1) == set(child2) == {0, 1}

class TestMutate:
    def test_mutate(self):
        individual = [1, 0, 1, 0]
        mutation_rate = 0.5
        mutated = mutate(individual.copy(), mutation_rate)

        assert len(mutated) == len(individual)
        assert any(gene != original for gene, original in zip(mutated, individual)) or mutated == individual

    def test_mutate_no_change(self):
        individual = [1, 0, 1, 0]
        mutation_rate = 0.0
        mutated = mutate(individual.copy(), mutation_rate)

        assert mutated == individual

class TestGeneticAlgorithm:
    def test_genetic_algorithm(self):
        values = [10, 20, 30]
        weights = [1, 2, 3]
        capacity = 5
        best_solution, best_fitness = genetic_algorithm(values, weights, capacity)

        assert best_solution is not None
        assert isinstance(best_solution, np.ndarray)
        assert all(gene in [0, 1] for gene in best_solution)
        assert best_fitness >= 0

    def test_genetic_algorithm_no_solution(self):
        values = [10, 20, 30]
        weights = [1, 2, 3]
        capacity = 0
        best_solution, _ = genetic_algorithm(values, weights, capacity)
        assert best_solution is None
