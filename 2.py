import turtle

def pythagorean_tree(t, order, size, angle=45):
    if order == 0:
        return
    else:
        t.forward(size)
        t.left(angle)
        pythagorean_tree(t, order - 1, size * 0.7, angle)
        t.right(2 * angle)
        pythagorean_tree(t, order - 1, size * 0.7, angle)
        t.left(angle)
        t.backward(size)

def draw_pythagorean_tree(order, size=100):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(2)
    t.penup()
    t.goto(0, 0)  
    t.left(90) 
    t.pendown()

    pythagorean_tree(t, order, size)

    window.mainloop()

n = int(input("Вкажіть бажаний рівень рекурсії для створення дерева Піфагора: "))
draw_pythagorean_tree(n)