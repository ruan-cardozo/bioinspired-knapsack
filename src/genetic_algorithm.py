import numpy as np
from src.knapsack import fitness, generate_population
from src.config import NUMPY_RANDOM_GENERATOR

CROSSOVER_MIN_POINT = 1
DEFAULT_POP_SIZE = 50
DEFAULT_GENERATIONS = 100
DEFAULT_MUTATION_RATE = 0.05
NUM_PARENTS = 2
FITNESS_INVALID = 0

def selection(population, values, weights, capacity):
    scores = [fitness(ind, values, weights, capacity) for ind in population]
    total = np.sum(scores)
    if total == 0:
        probabilities = [1 / len(scores)] * len(scores)
    else:
        probabilities = scores / total
    selected = NUMPY_RANDOM_GENERATOR.choice(len(population), size=NUM_PARENTS, replace=False, p=probabilities)
    return population[selected[0]], population[selected[1]]

def crossover(parent1, parent2):
    point = NUMPY_RANDOM_GENERATOR.integers(CROSSOVER_MIN_POINT, len(parent1) - 1)
    child1 = np.concatenate([parent1[:point], parent2[point:]])
    child2 = np.concatenate([parent2[:point], parent1[point:]])
    return child1, child2

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if NUMPY_RANDOM_GENERATOR.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm(values, weights, capacity, pop_size=DEFAULT_POP_SIZE, generations=DEFAULT_GENERATIONS, mutation_rate=DEFAULT_MUTATION_RATE):
    population = generate_population(pop_size, len(values))
    best_solution = None
    best_fitness = 0

    for _ in range(generations):
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = selection(population, values, weights, capacity)
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1, mutation_rate))
            new_population.append(mutate(child2, mutation_rate))
        population = new_population

        for individual in population:
            score = fitness(individual, values, weights, capacity)
            if score > best_fitness:
                best_fitness = score
                best_solution = individual.copy()

    if best_solution is None:
        return None, FITNESS_INVALID
    return best_solution, best_fitness
