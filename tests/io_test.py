from unittest import mock
import numpy as np

import src.io.io as io

INVALID_INPUT_MESSAGE = "Entrada inválida"

class TestShowMenu:
    def test_show_menu_prints_correctly(self, capsys):
        io.show_menu()
        captured = capsys.readouterr()
        assert "Problema da Mochila 0/1 com Algoritmo Genético" in captured.out
        assert "1 - Inserir dados manualmente" in captured.out
        assert "2 - Gerar dados automaticamente" in captured.out

class TestGetUserChoice:
    @mock.patch("builtins.input", side_effect=["3", "2"])
    def test_invalid_then_valid_choice(self, capsys):
        result = io.get_user_choice()
        captured = capsys.readouterr()
        assert "Opção inválida" in captured.out
        assert result == "2"

    @mock.patch("builtins.input", side_effect=["1"])
    def test_valid_choice_first_try(self):
        assert io.get_user_choice() == "1"

class TestGetNumItems:
    @mock.patch("builtins.input", side_effect=["-1", "abc", "5"])
    def test_invalid_then_valid_num_items(self, capsys):
        result = io.get_num_items()
        captured = capsys.readouterr()
        assert "Digite um número inteiro positivo" in captured.out
        assert result == 5

    @mock.patch("builtins.input", side_effect=["10"])
    def test_valid_num_items(self):
        assert io.get_num_items() == 10

class TestShowGenerationInfo:
    def test_show_generation_info_prints(self, capsys):
        io.show_generation_info(10, 50)
        captured = capsys.readouterr()
        assert "10 itens gerados automaticamente" in captured.out
        assert "Capacidade da mochila: 50" in captured.out

class TestShowSolution:
    def test_show_solution_prints(self, capsys):
        solution = np.array([1, 0, 1])
        weights = [2, 3, 5]
        capacity = 10
        total_value = 42
        io.show_solution(solution, weights, capacity, total_value)
        captured = capsys.readouterr()
        assert "Melhor solução encontrada" in captured.out
        assert "Itens selecionados" in captured.out
        assert "Peso total da mochila" in captured.out
        assert "Valor total obtido" in captured.out

    def test_show_solution_zero_capacity(self, capsys):
        solution = np.array([1, 1])
        weights = [1, 2]
        capacity = 0
        total_value = 10
        io.show_solution(solution, weights, capacity, total_value)
        captured = capsys.readouterr()
        assert "(0.00%)" in captured.out

class TestShowSelectedItems:
    @mock.patch("builtins.input", side_effect=["s", "n"])
    def test_show_selected_items_pagination(self, capsys):
        solution = np.array([1]*25)
        values = list(range(25))
        weights = [2]*25
        io.show_selected_items(solution, values, weights, block_size=10)
        captured = capsys.readouterr()

        assert "Detalhes dos itens selecionados" in captured.out
        assert "Índice Valor  Peso" in captured.out
        assert "0      0      2" in captured.out
        assert "19     19     2" in captured.out


    def test_show_selected_items_no_pagination(self, capsys):
        solution = np.array([1, 0, 1])
        values = [10, 20, 30]
        weights = [1, 2, 3]
        io.show_selected_items(solution, values, weights, block_size=10)
        captured = capsys.readouterr()
        assert "Detalhes dos itens selecionados" in captured.out
        assert "0      10     1" in captured.out

class TestGetManualInput:
    @mock.patch("builtins.input", side_effect=[
        "10 20", "1 2", "30",  # valid
    ])
    def test_valid_manual_input(self, ):
        values, weights, capacity = io.get_manual_input()
        assert values == [10, 20]
        assert weights == [1, 2]
        assert capacity == 30

    @mock.patch("builtins.input", side_effect=[
        "10 20", "1", "1 2", "0", "-5", "15", 
    ])
    def test_invalid_weights_and_capacity(self, capsys):
        values, weights, capacity = io.get_manual_input()
        captured = capsys.readouterr()
        assert "A quantidade de pesos deve ser igual à de valores" in captured.out
        assert "Digite um número inteiro positivo para a capacidade" in captured.out
        assert values == [10, 20]
        assert weights == [1, 2]
        assert capacity == 15

class TestParseListInput:
    def test_valid_list(self):
        assert io._parse_list_input("1 2 3") == [1, 2, 3]

    def test_invalid_list_negative(self, capsys):
        assert io._parse_list_input("1 -2 3") is None
        captured = capsys.readouterr()
        assert INVALID_INPUT_MESSAGE in captured.out

    def test_invalid_list_nonint(self, capsys):
        assert io._parse_list_input("a b c") is None
        captured = capsys.readouterr()
        assert INVALID_INPUT_MESSAGE in captured.out

    def test_empty_list(self, capsys):
        assert io._parse_list_input("") is None
        captured = capsys.readouterr()
        assert INVALID_INPUT_MESSAGE in captured.out
