import turtle

t = turtle.Turtle()

with open(r'C:\Users\ruifa\OneDrive\Documentos\FP\aula06\Meu\drawing.txt', 'r') as numbers:
    for line in numbers:
        if line == 'UP\n':
            t.up()
        elif line == 'DOWN\n':
            t.down()
        else:
            t.goto(int(line.split()[0]), int(line.split()[1]))

turtle.Screen().exitonclick()

