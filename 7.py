import random
import matplotlib.pyplot as plt


def roll_dice():
    return random.randint(1, 6)


def simulate_dice_rolls(num_rolls):
    results = {}

    for _ in range(num_rolls):
        roll_sum = roll_dice() + roll_dice()
        results[roll_sum] = results.get(roll_sum, 0) + 1

    probabilities = {k: v / num_rolls * 100 for k, v in results.items()}

    return probabilities


def print_probabilities(probabilities):
    print("Результат симуляції, з використанням методу Монте-Карло:\n")
    print("сума\tймовірність")
    for i in range(2, 13):
        print(f"{i}\t{probabilities.get(i, 0):.2f} %")


def print_table_of_errors(probabilities, table_of_probabilities):
    print("\nПохибка методу Монте-Карло:\n")
    print("сума\tпохибка")
    for i in range(2, 13):
        table_value = table_of_probabilities.get(i)
        prob_value = probabilities.get(i, 0)
        if table_value is not None:
            err = (table_value - prob_value) * 100 / table_value
            print(f"{i}\t{err:.6f} %")
        else:
            print(f"{i}\tНемає значення в таблиці ймовірностей")


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probabilities_values = list(probabilities.values())

    plt.bar(sums, probabilities_values, color='#1296F0')
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірності сум при кидках кубиків (Monte Carlo)')
    plt.show()


def main():
    table_of_probabilities = {
      2: 2.78,
      3: 5.56,
      4: 8.33,
      5: 11.11,
      6: 13.89,
      7: 16.67,
      8: 13.89,
      9: 11.11,
      10: 8.33,
      11: 5.56,
      12: 2.78        
    }
    
    num_rolls = 100000 
    probabilities = simulate_dice_rolls(num_rolls)
    print_probabilities(probabilities)
    print_table_of_errors(probabilities, table_of_probabilities)
    plot_probabilities(probabilities)
    

if __name__ == "__main__":
    main()