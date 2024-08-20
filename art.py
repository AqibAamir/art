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
