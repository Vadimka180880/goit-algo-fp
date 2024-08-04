import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_trials):
    # Ініціалізуємо словник для підрахунку кількості кожної суми
    sums_count = {i: 0 for i in range(2, 13)}
    
    # Симулюємо кидки кубиків
    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2
        sums_count[dice_sum] += 1
    
    # Обчислюємо ймовірності для кожної суми
    probabilities = {k: v / num_trials for k, v in sums_count.items()}
    
    return probabilities

def plot_probabilities(probabilities, analytical_probabilities):
    sums = list(probabilities.keys())
    simulation_probs = [probabilities[s] for s in sums]
    analytical_probs = [analytical_probabilities[s] for s in sums]

    fig, ax = plt.subplots()
    
    ax.bar(sums, simulation_probs, width=0.4, label='Simulation', align='center')
    ax.bar(sums, analytical_probs, width=0.4, label='Analytical', align='edge')
    
    ax.set_xlabel('Сума')
    ax.set_ylabel('Ймовірність')
    ax.set_title('Ймовірність сум при киданні двох кубиків')
    ax.legend()
    
    plt.show()

# Аналітичні ймовірності
analytical_probabilities = {
    2: 2.78 / 100,
    3: 5.56 / 100,
    4: 8.33 / 100,
    5: 11.11 / 100,
    6: 13.89 / 100,
    7: 16.67 / 100,
    8: 13.89 / 100,
    9: 11.11 / 100,
    10: 8.33 / 100,
    11: 5.56 / 100,
    12: 2.78 / 100
}

# Кількість симуляцій
num_trials = 100000

# Виконуємо симуляцію Монте-Карло
simulation_probabilities = monte_carlo_simulation(num_trials)

# Виводимо результати
print("Ймовірності (симуляція):")
for sum_val, prob in simulation_probabilities.items():
    print(f"Сума {sum_val}: {prob:.2%}")

print("\nЙмовірності (аналітичні):")
for sum_val, prob in analytical_probabilities.items():
    print(f"Сума {sum_val}: {prob:.2%}")

# Створюємо графік
plot_probabilities(simulation_probabilities, analytical_probabilities)
