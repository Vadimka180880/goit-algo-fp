import turtle
import math

# Функція для малювання гілки дерева
def draw_tree(t, branch_length, level):
    if level == 0:
        return

    # Малюємо основну гілку
    t.forward(branch_length)

    # Поворот і малювання лівої гілки
    t.left(45)
    draw_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Повернення до початкового положення
    t.right(90)
    draw_tree(t, branch_length * math.sqrt(2) / 2, level - 1)

    # Повернення до початкового положення і кута
    t.left(45)
    t.backward(branch_length)

# Головна функція для створення вікна і запуску малювання
def main():
    screen = turtle.Screen()
    screen.title("Pythagoras Tree")

    t = turtle.Turtle()
    t.speed(0)
    t.left(90)  # Початковий напрямок вгору

    level = int(input("Введіть рівень рекурсії (наприклад, 5): "))
    branch_length = 100  # Початкова довжина гілки

    draw_tree(t, branch_length, level)

    screen.mainloop()

if __name__ == "__main__":
    main()
