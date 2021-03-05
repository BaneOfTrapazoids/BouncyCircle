import pygame
import sys
from random import randint, uniform, choice


ran_or_cus = input("Do you want random or custom colours?: ")
if ran_or_cus == "random":
    pass
elif ran_or_cus == "custom":
    colour_list = []
    colour_num = int(input("How many colours do you want?: "))
    for i in range(colour_num):
        colour_val = input("Please input the RGB value for one of your colours, separate each value by a comma: ")
        colour_val = colour_val.split(",")
        for i in range(len(colour_val)):
            colour_val[i] = int(colour_val[i])
        colour_val = tuple(colour_val)
        colour_list += [colour_val]
    print(colour_list)
        

pygame.init()

screen = pygame.display.set_mode((800, 500), pygame.RESIZABLE)

x = randint(100, 700)
y = randint(100, 400)
direction = "UR"
corner_count = 0


clock = pygame.time.Clock()
screen.fill((255,255,255))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen_size = pygame.display.get_window_size()

    if ran_or_cus == "random":
        colour_list = [(randint(0,255), randint(0,255), randint(0,255))]

    pygame.draw.circle(screen, choice(colour_list), (x,y), 20)
    pygame.display.update()

    if x >= screen_size[0]-20 and direction == "DR":
        direction = "DL"

    if y <= 20 and direction == "UR":
        direction = "DR"

    if y >= screen_size[1]-20 and direction == "DL":
        direction = "UL"

    if y <= 20 and direction == "UL":
        direction = "DL"

    if x <= 20 and direction == "DL":
        direction = "DR"

    if y >= screen_size[1]-20 and direction == "DR":
        direction = "UR"

    if x >= screen_size[0]-20 and direction == "UR":
        direction = "UL"

    if x <= 20 and direction == "UL":
        direction = "UR"

    if x >= screen_size[0]-20 and y >= screen_size[1]-20 or x >= screen_size[0]-20 and y <= 20 or x <= 20 and y <= 20 or x <= 20 and y >= screen_size[1]-20:
        corner_count += 1
        print(f"The corner has been hit {corner_count} times! Reseting the circle.")
        x = randint(30, 770)
        y = randint(30, 470)
    else:
        direction_statements = {
            "DR":(uniform(0.5, 2), uniform(0.5, 2)),
            "DL":(uniform(-0.5, -2), uniform(0.5, 2)),
            "UR":(uniform(0.5, 2), uniform(-0.5, -2)),
            "UL":(uniform(-0.5, -2), uniform(-0.5, -2))
        }
        x += direction_statements[direction][0]
        y += direction_statements[direction][1]
    clock.tick(10000)
