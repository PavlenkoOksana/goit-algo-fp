def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"])
    selected_items = []
    total_cost = 0
    total_calories = 0

    for item_name, item_info in sorted_items:
        if total_cost + item_info["cost"] <= budget:
            selected_items.append(item_name)
            total_cost += item_info["cost"]
            total_calories += item_info["calories"]

    return {
        "selected_items": selected_items,
        "total_cost": total_cost,
        "total_calories": total_calories
    }


def dynamic_programming(items, budget):
    # Створюємо динамічну таблицю
    table = [[0] * (budget + 1) for _ in range(len(items) + 1)]

    # Заповнюємо динамічну таблицю
    for i, (item_name, item_info) in enumerate(items.items(), start=1):
        for j in range(budget + 1):
            # Якщо вартість страви менше або дорівнює поточному бюджету
            if item_info["cost"] <= j:
                # Вибираємо максимум із калорій, які можна отримати без поточної страви із вибором поточної страви
                table[i][j] = max(table[i - 1][j], table[i - 1][j - item_info["cost"]] + item_info["calories"])
            else:
                # Якщо вартість страви більше поточного бюджету, використовуємо значення без поточної страви
                table[i][j] = table[i - 1][j]

    # Отримуємо оптимальний набір страв
    selected_items = []
    i, j = len(items), budget
    while i > 0 and j > 0:
        if table[i][j] != table[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]
        i -= 1

    return {
        "selected_items": selected_items[::-1],  # Повертаємо зворотній порядок, оскільки вибір відбувався з кінця
        "total_cost": sum(items[item]["cost"] for item in selected_items),
        "total_calories": sum(items[item]["calories"] for item in selected_items)
    }


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 60

# Виклик жадібного алгоритму
result = greedy_algorithm(items, budget)

# Вивід результатів
print("\nЖадібний алгоритм:")
print("Обрані страви:", result["selected_items"])
print("Загальна вартість:", result["total_cost"])
print("Загальна калорійність:", result["total_calories"])

# Виклик алгоритму динамічного програмування
result_dp = dynamic_programming(items, budget)

# Вивід результатів
print("\nАлгоритм динамічного програмування:")
print("Обрані страви:", result_dp["selected_items"])
print("Загальна вартість:", result_dp["total_cost"])
print("Загальна калорійність:", result_dp["total_calories"])