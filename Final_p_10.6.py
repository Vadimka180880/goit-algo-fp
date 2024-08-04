items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for item, details in sorted_items:
        if total_cost + details['cost'] <= budget:
            selected_items.append(item)
            total_cost += details['cost']
            total_calories += details['calories']
    
    return selected_items, total_cost, total_calories

def dynamic_programming(items, budget):
    n = len(items)
    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]
    
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
    
    selected_items = []
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(names[i - 1])
            w -= costs[i - 1]
    
    total_cost = sum(items[item]['cost'] for item in selected_items)
    total_calories = sum(items[item]['calories'] for item in selected_items)
    
    return selected_items, total_cost, total_calories

# Приклад використання
budget = 300

# Жадібний алгоритм
selected_items_greedy, total_cost_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", selected_items_greedy)
print("Загальна вартість:", total_cost_greedy)
print("Загальна калорійність:", total_calories_greedy)

# Алгоритм динамічного програмування
selected_items_dp, total_cost_dp, total_calories_dp = dynamic_programming(items, budget)
print("Алгоритм динамічного програмування:")
print("Вибрані страви:", selected_items_dp)
print("Загальна вартість:", total_cost_dp)
print("Загальна калорійність:", total_calories_dp)
