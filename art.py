import turtle
import random
import math

screen = turtle.Screen()
screen.bgcolor("black")

artist = turtle.Turtle()
artist.speed(0)
artist.width(2)

colors = [
    "red", "blue", "green", "yellow", "purple", "orange", "white", "cyan",
    "magenta", "lime", "pink", "turquoise", "gold", "silver", "maroon"
]

def draw_shape(sides, size, color):
    artist.color(color)
    for _ in range(sides):
        artist.forward(size)
        artist.right(360 / sides)

def draw_spiral(turn_angle, line_length, increment, repetitions, color):
    artist.color(color)
    for _ in range(repetitions):
        artist.forward(line_length)
        artist.right(turn_angle)
        line_length += increment

def draw_star(size, color):
    artist.color(color)
    artist.begin_fill()
    for _ in range(5):
        artist.forward(size)
        artist.right(144)
    artist.end_fill()

def draw_circle_pattern(radius, count, color):
    artist.color(color)
    for _ in range(count):
        artist.circle(radius)
        artist.right(360 / count)

def draw_gradient():
    screen.tracer(0)
    gradient_artist = turtle.Turtle()
    gradient_artist.speed(0)
    gradient_artist.penup()
    gradient_artist.hideturtle()
    
    color_set = ["darkblue", "midnightblue", "navy", "mediumblue", "blue", "royalblue"]
    height = 400
    width = 400
    step = height // len(color_set)
    
    for i, color in enumerate(color_set):
        gradient_artist.goto(-width//2, height//2 - i * step)
        gradient_artist.pendown()
        gradient_artist.color(color)
        gradient_artist.begin_fill()
        for _ in range(2):
            gradient_artist.forward(width)
            gradient_artist.right(90)
            gradient_artist.forward(step)
            gradient_artist.right(90)
        gradient_artist.end_fill()
        gradient_artist.penup()
    
    screen.tracer(1)

def draw_checkerboard(size):
    screen.tracer(0)
    for row in range(8):
        for col in range(8):
            artist.penup()
            artist.goto(col * size - 200, row * size - 200)
            artist.pendown()
            if (row + col) % 2 == 0:
                artist.begin_fill()
            for _ in range(4):
                artist.forward(size)
                artist.right(90)
            if (row + col) % 2 == 0:
                artist.end_fill()
    screen.tracer(1)


def draw_circles_grid():
    screen.tracer(0)
    for i in range(-200, 200, 50):
        for j in range(-200, 200, 50):
            artist.penup()
            artist.goto(i, j)
            artist.pendown()
            artist.color(random.choice(colors))
            artist.circle(20)
    screen.tracer(1)

def get_user_input():
    pieces = int(screen.numinput("Number of Pieces", "Enter the number of art pieces:", minval=1, maxval=100))
    return pieces

def generate_art(pieces):
    for _ in range(pieces):
        draw_radial_pattern()

def draw_radial_pattern(center_x, center_y, radius, num_shapes):
    artist.penup()
    artist.goto(center_x, center_y)
    artist.pendown()
    for i in range(num_shapes):
        angle = 360 / num_shapes * i
        artist.penup()
        artist.goto(center_x, center_y)
        artist.setheading(angle)
        artist.forward(radius)
        artist.pendown()
        draw_star(random.randint(20, 40), random.choice(colors))

def draw_flower_pattern():
    for i in range(12):
        artist.color(random.choice(colors))
        draw_shape(6, 50, random.choice(colors))
        artist.right(30)

def draw_complex_background():
    draw_gradient()
    draw_checkerboard(50)
    draw_circles_grid()

def draw_user_selected_shape():
    shapes = ["polygon", "star", "circle", "spiral"]
    shape_choice = screen.textinput("Shape Selection", f"Choose a shape: {', '.join(shapes)}")
    
    if shape_choice.lower() not in shapes:
        artist.write("Invalid shape choice!", align="center", font=("Arial", 16, "normal"))
        return

    color_choice = screen.textinput("Color Selection", f"Choose a color: {', '.join(colors)}")
    
    if color_choice.lower() not in colors:
        artist.write("Invalid color choice!", align="center", font=("Arial", 16, "normal"))
        return

    size = int(screen.numinput("Size", "Enter the size of the shape:", minval=10, maxval=200))
    
    if shape_choice.lower() == "polygon":
        sides = int(screen.numinput("Sides", "Enter the number of sides for the polygon:", minval=3, maxval=10))
        draw_shape(sides, size, color_choice)
    elif shape_choice.lower() == "star":
        draw_star(size, color_choice)
    elif shape_choice.lower() == "circle":
        draw_circle_pattern(size, 12, color_choice)
    elif shape_choice.lower() == "spiral":
        draw_spiral(60, size, 5, 20, color_choice)

def main():
    draw_complex_background()
    draw_user_selected_shape()
    pieces = get_user_input()
    generate_art(pieces)
    draw_radial_pattern(0, 0, 100, 12)
    draw_flower_pattern()
    screen.exitonclick()

def draw_wave_pattern(amplitude, wavelength, length, color):
    artist.penup()
    artist.goto(-length // 2, 0)
    artist.pendown()
    artist.color(color)
    for x in range(-length // 2, length // 2):
        y = amplitude * math.sin(x / wavelength)
        artist.goto(x, y)
