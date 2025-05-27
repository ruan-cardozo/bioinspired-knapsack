MENU_OPTION_MANUAL = "1"
MENU_OPTION_AUTO = "2"
MIN_ITEMS = 0
MIN_CAPACITY = 0
BLOCK_SIZE_DEFAULT = 20
TABLE_WIDTH = 22

def show_menu():
    print("📦 Problema da Mochila 0/1 com Algoritmo Genético")
    print(f"{MENU_OPTION_MANUAL} - Inserir dados manualmente")
    print(f"{MENU_OPTION_AUTO} - Gerar dados automaticamente")

def get_user_choice():
    while True:
        choice = input("Escolha uma opção (1 ou 2): ")
        if choice in {MENU_OPTION_MANUAL, MENU_OPTION_AUTO}:
            return choice
        print(f"❌ Opção inválida. Escolha {MENU_OPTION_MANUAL} ou {MENU_OPTION_AUTO}.")

def get_num_items():
    while True:
        try:
            num_items = int(input("Quantos itens deseja gerar? (ex: 10, 100, 2500): "))
            if num_items <= MIN_ITEMS:
                raise ValueError
            return num_items
        except ValueError:
            print("❌ Digite um número inteiro positivo.")

def show_generation_info(num_items, capacity):
    print(f"\n🔧 {num_items} itens gerados automaticamente.")
    print(f"Capacidade da mochila: {capacity}")

def show_solution(solution, weights, capacity, total_value):
    selected_items = [i for i, bit in enumerate(solution) if bit == 1]
    total_weight = sum(weights[i] for i in selected_items)
    capacity_used_pct = (total_weight / capacity) * 100 if capacity > 0 else 0

    print("\n🎯 Melhor solução encontrada:")
    print(f"👉 Itens selecionados (índices): {selected_items}")
    print(f"🧠 Representação binária da solução: {solution.tolist()}")
    print(f"📦 Peso total da mochila: {total_weight} / {capacity} ({capacity_used_pct:.2f}%)")
    print(f"💰 Valor total obtido: {total_value}")
    print(f"📊 Quantidade de itens escolhidos: {len(selected_items)}")

def show_selected_items(solution, values, weights, block_size=BLOCK_SIZE_DEFAULT):
    selected_items = [i for i, bit in enumerate(solution) if bit == 1]

    print("\n📋 Detalhes dos itens selecionados:")
    print(f"{'Índice':<6} {'Valor':<6} {'Peso':<6}")
    print("-" * TABLE_WIDTH)
    total = len(selected_items)

    for start in range(0, total, block_size):
        end = min(start + block_size, total)
        for i in selected_items[start:end]:
            print(f"{i:<6} {values[i]:<6} {weights[i]:<6}")
        if end < total:
            response = input(f"... Mostrando itens {start + 1}-{end} de {total}. Ver mais? (s/n): ")
            lower_response = response.lower()

            if lower_response != 's':
                break

def get_manual_input():
    while True:
        v_input = input("Digite os VALORES dos itens (separados por espaço): ")
        values = _parse_list_input(v_input)
        if values:
            break

    while True:
        w_input = input("Digite os PESOS dos itens (separados por espaço): ")
        weights = _parse_list_input(w_input)
        if weights and len(weights) == len(values):
            break
        print("❌ A quantidade de pesos deve ser igual à de valores.")

    while True:
        try:
            capacity = int(input("Digite a capacidade da mochila: "))
            if capacity <= MIN_CAPACITY:
                raise ValueError
            break
        except ValueError:
            print("❌ Digite um número inteiro positivo para a capacidade.")

    return values, weights, capacity

def _parse_list_input(text):
    try:
        values = list(map(int, text.strip().split()))
        if not values or any(v < 0 for v in values):
            raise ValueError
        return values
    except ValueError:
        print("❌ Entrada inválida. Digite números inteiros positivos separados por espaço.")
        return None
