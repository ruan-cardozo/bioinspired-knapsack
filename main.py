""" Main entry point for the Genetic Algorithm Knapsack Problem solver. """
import sys
from src.genetic_algorithm import genetic_algorithm
from src.io.io import (
    show_menu,
    get_user_choice,
    get_num_items,
    show_generation_info,
    show_solution,
    show_selected_items,
    get_manual_input
)
from src.utils.utils import generate_items

show_menu()

choice = get_user_choice()

if choice == '1':
    values, weights, capacity = get_manual_input()
else:
    num_items = get_num_items()
    values, weights, capacity = generate_items(num_items)
    show_generation_info(num_items, capacity)

solution, total_value = genetic_algorithm(values, weights, capacity)

if solution is None:
    print("❌ Nenhuma solução válida foi encontrada.")
    sys.exit(1)

show_solution(solution, weights, capacity, total_value)
show_selected_items(solution, values, weights)
