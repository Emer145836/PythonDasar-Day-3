import turtle

t = turtle.Turtle()
t.speed(0)
t.width(2)

colors = ["magenta", "pink", "black", "yellow", "cyan"]

for i in range(100):
    t.color(colors[i % len(colors)])
    t.circle(100)
    t.left(360 / 10)

turtle.done()