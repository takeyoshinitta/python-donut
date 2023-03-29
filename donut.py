import math
import pygame
import colorsys

#Pygame Initialization
pygame.init()

#Colors used for the background and text color.
white = (255, 255, 255)
black = (0, 0, 0)
hue = 0

#Window Size
WIDTH = 1440
HEIGHT = 850

#Donut Location and Size used to offset the donut in the center of the window.
x_start, y_start = 0, 0

x_separator = 10
y_separator = 20

rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0

theta_spacing = 10
phi_spacing = 1

#Character Set
chars = ".,-~:;=!*#$@"

#Screen Initialization
screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Donut")

#Font Initialization
font = pygame.font.SysFont("Arial", 18, bold=True)

#Color Conversion
def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

#Text Display
def text_display(letter, x_start, y_start):
    # text = font.render(str(letter), True, white)
    text = font.render(str(letter), True, hsv2rgb(hue, 1, 1))
    display_surface.blit(text, (x_start, y_start))

#Main Loop that continuously renders the donut on the screen.
run = True
while run:
    screen.fill((black))

    z = [0] * screen_size
    #List that contains the characters to be displayed for each point on the donut
    #The characters are chosen based on the angle and distance of each point from the viewer
    b = [' '] * screen_size

    #Drawing the Donut
    for i in range(0, 628, theta_spacing):
        for j in range(0, 628, phi_spacing):
            #Equations determine the position and rotation of each point on the donut.
            c = math.sin(j)
            d = math.cos(i)
            e = math.sin(A)
            f = math.sin(i)
            g = math.cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = math.cos(j)
            m = math.cos(B)
            n = math.sin(B)
            t = c * h * g - f * e
            x = int(x_offset + 40 * D * (l * h * m - t * n))
            y = int(y_offset + 20 * D * (l * h * n + t * m))
            o = int(x + columns * y)
            N = int(8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n))
            if rows > y and y > 0 and x > 0 and columns > x and D > z[o]:
                z[o] = D
                b[o] = chars[N if N > 0 else 0]

    if y_start == rows * y_separator - y_separator:
        y_start = 0

    #Displaying the Donut
    for i in range(len(b)):
        A += 0.00002
        B += 0.00001
        if i == 0 or i % columns:
            text_display(b[i], x_start, y_start)
            x_start += x_separator
        else:
            y_start += y_separator
            x_start = 0
            text_display(b[i], x_start, y_start)
            x_start += x_separator

    #Updating the Screen
    pygame.display.update()

    #Incrementing to change the color of the text.
    hue += 0.005

    #Handling Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
