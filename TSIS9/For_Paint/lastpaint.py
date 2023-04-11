import pygame


# Add colors

white = (255, 255, 255)
black = (0, 0, 0)
green = (34, 139, 34)
blue = (0, 0, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (252, 154, 25)
pink = (250, 115, 234)
purple = (99, 2, 163)
lime = (3, 252, 65)
turquoise = (4, 207, 173)
aqua = (2, 155, 250)

# Display parametres

pygame.init()
surface = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
surface.fill((255, 255, 255))

# Set a Caption

pygame.display.set_caption('Paint')
icon = pygame.image.load('paint-icon.png')
pygame.display.set_icon(icon)

# Functions to draw figure


def drawLineBetween(screen, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * start[0] - 256))
    c2 = max(0, min(255, 2 * start[1]))

    color = color_mode
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

# function for rectangle


def drawRectangle(screen, mouse_pos, w, h, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)

# function for circle


def drawCircle(screen, mouse_pos, color):
    x = mouse_pos[0]
    y = mouse_pos[1]
    pygame.draw.circle(screen, color, (x, y), 100, 3)

# function for square


def drawSquare(screen, mouse_pos, w, h, color):

    x = mouse_pos[0]
    y = mouse_pos[1]
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, color, rect, 3)

# function for right triangle


def drawRightTriangle(screen, color, mouse_pos):

    # Define the points

    x = mouse_pos[0]
    y = mouse_pos[1]
    triangle_size = 50

    # Calculate the triangle's vertices

    triangle_points = [
        (x, y - triangle_size),
        (x - triangle_size, y + triangle_size),
        (x + triangle_size, y + triangle_size),
    ]

    # Draw the triangle

    pygame.draw.polygon(screen, color, triangle_points)

# function for equiteral triangle


def drawEquilateralTriangle(screen, color, mouse_pos):

    # Define the points

    x = mouse_pos[0]
    y = mouse_pos[1]
    triangle_size = 50

    # Calculate the triangle's vertices

    triangle_points = [
        (x, y - triangle_size - 100),
        (x - triangle_size, y + triangle_size),
        (x + triangle_size, y + triangle_size),
    ]

    # Draw the triangle

    pygame.draw.polygon(screen, color, triangle_points)


def drawRhombus(screen, color, mouse_pos):

    # Define the points

    x = mouse_pos[0]
    y = mouse_pos[1]
    rhombus_height = 50
    rhombus_width = 50

    # Calculate the rhombus's vertices
    rhombus_points = [
        (x, y - rhombus_height),
        (x + rhombus_width, y),
        (x, y + rhombus_height),
        (x - rhombus_width, y),
    ]

    # Drawing

    pygame.draw.polygon(screen, color, rhombus_points)

# Drawing taskbar


def taskBar():

    menu = pygame.image.load("Menu.png").convert_alpha()
    surface.blit(menu, (0, 0))

    # Color palette

    red_rect = (10, 5, 20, 20)
    pygame.draw.rect(surface, red, red_rect)

    orange_rect = (31, 5, 20, 20)
    pygame.draw.rect(surface, orange, orange_rect)

    yellow_rect = (52, 5, 20, 20)
    pygame.draw.rect(surface, yellow, yellow_rect)

    lime_rect = (73, 5, 20, 20)
    pygame.draw.rect(surface, lime, lime_rect)

    green_rect = (94, 5, 20, 20)
    pygame.draw.rect(surface, green, green_rect)

    blue_rect = (115, 5, 20, 20)
    pygame.draw.rect(surface, blue, blue_rect)

    aqua_rect = (136, 5, 20, 20)
    pygame.draw.rect(surface, aqua, aqua_rect)

    turquoise_rect = (157, 5, 20, 20)
    pygame.draw.rect(surface, turquoise, turquoise_rect)

    pink_rect = (178, 5, 20, 20)
    pygame.draw.rect(surface, pink, pink_rect)

    purple_rect = (199, 5, 20, 20)
    pygame.draw.rect(surface, purple, purple_rect)

    black_rect = (220, 5, 20, 20)
    pygame.draw.rect(surface, black, black_rect)

    # Icon settings

    size1Image = pygame.image.load("Light_Line.png").convert_alpha()
    size1Image = pygame.transform.scale(size1Image, (20, 20))
    surface.blit(size1Image, (275, 5))

    size2Image = pygame.image.load("Average_Line.png").convert_alpha()
    size2Image = pygame.transform.scale(size2Image, (20, 20))
    surface.blit(size2Image, (295, 5))

    size3Image = pygame.image.load("Big_Line.png").convert_alpha()
    size3Image = pygame.transform.scale(size3Image, (20, 20))
    surface.blit(size3Image, (315, 5))

    lineImage = pygame.image.load("Pen.png").convert_alpha()
    lineImage = pygame.transform.scale(lineImage, (20, 20))
    surface.blit(lineImage, (375, 5))

    rectImage = pygame.image.load("Rectangle.png").convert_alpha()
    rectImage = pygame.transform.scale(rectImage, (30, 30))
    surface.blit(rectImage, (400, 0))

    squareImage = pygame.image.load("Square.png").convert_alpha()
    squareImage = pygame.transform.scale(squareImage, (30, 30))
    surface.blit(squareImage, (435, 0))

    circleImage = pygame.image.load("Circle.png").convert_alpha()
    circleImage = pygame.transform.scale(circleImage, (25, 25))
    surface.blit(circleImage, (470, 3))

    etrienImage = pygame.image.load("Triangle.png").convert_alpha()
    etrienImage = pygame.transform.scale(etrienImage, (27, 27))
    surface.blit(etrienImage, (500, 0))

    trienImage = pygame.image.load("Right_Triangle.png").convert_alpha()
    trienImage = pygame.transform.scale(trienImage, (18, 25))
    surface.blit(trienImage, (532, 3))

    rhombusImage = pygame.image.load("Rhombus.png").convert_alpha()
    rhombusImage = pygame.transform.scale(rhombusImage, (30, 30))
    surface.blit(rhombusImage, (555, 0))

    eraserImage = pygame.image.load("Eraser.png").convert_alpha()
    eraserImage = pygame.transform.scale(eraserImage, (25, 25))
    surface.blit(eraserImage, (600, 2))


# main loop

# Start parametres

radius = 5
mode = black
last_pos = None
draw = "line"

# Main loop
exit = True
while exit:

    # Handle events

    mouseX, mouseY = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and draw == "line":
            # Start a new line
            last_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION and event.buttons[0] and draw == "line":

            # Draw line

            if last_pos is not None:
                start_pos = last_pos
                end_pos = pygame.mouse.get_pos()
                drawLineBetween(surface, start_pos, end_pos, radius, mode)
                last_pos = end_pos

    # Draw or not checker

        if (draw == "rect" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawRectangle(surface, pygame.mouse.get_pos(), 200, 100, mode)

        if (draw == "square" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawSquare(surface, pygame.mouse.get_pos(), 100, 100, mode)

        if (draw == "circle" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawCircle(surface, pygame.mouse.get_pos(), mode)

        if (draw == "etrien" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawRightTriangle(surface, mode, pygame.mouse.get_pos())
        
        if (draw == "trien" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawEquilateralTriangle(surface, mode, pygame.mouse.get_pos())

        if (draw == "rhombus" and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and mouseY > 30):
            drawRhombus(surface, mode, pygame.mouse.get_pos())

    # Command binding

    if (0 <= mouseY <= 30):
        if (10 <= mouseX <= 31):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mode = red

        elif (31 <= mouseX <= 52):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mode = orange

        elif (52 <= mouseX <= 73):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mode = yellow

        elif (73 <= mouseX <= 94):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mode = lime

        elif (94 <= mouseX <= 115):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mode = green

        elif (115 <= mouseX <= 136):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mode = blue

        elif (136 <= mouseX <= 157):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mode = aqua

        elif (157 <= mouseX <= 178):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mode = turquoise

        elif (178 <= mouseX <= 199):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mode = pink

        elif (199 <= mouseX <= 220):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                 mode = purple

        elif (220 <= mouseX <= 241):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mode = black

        elif (275 <= mouseX <= 295):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                radius = 5

        elif (295 <= mouseX <= 315):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
               radius = 10

        elif (315 <= mouseX <= 335):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                radius = 15

        elif (375 <= mouseX <= 395):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                draw = "line"

        elif (400 <= mouseX <= 430):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                draw = "rect"
        elif (435 <= mouseX <= 465):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                draw = "square"

        elif (470 <= mouseX <= 495):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                draw = "circle"

        elif (500 <= mouseX <= 527):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                draw = "etrien"

        elif (532 <= mouseX <= 550):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
               draw = "trien"

        elif (555 <= mouseX <= 585):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
             draw = "rhombus"

        elif (600 <= mouseX <= 630):
            if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                mode = white

    taskBar()
    pygame.display.flip()
    clock.tick(60)
