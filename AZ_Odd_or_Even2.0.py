#all imports
import pygame as pg
import random as rd
#init pygame and display
pg.init()
pg.display.init()
#window width and height
Init_Width, Init_Height = 1280, 720
#defining window properties
root = pg.display.set_mode((Init_Width, Init_Height), pg.RESIZABLE)
pg.display.set_caption("AZ Odd or Even")
#variables
font_small = pg.font.SysFont("Arial", 18)
odd_button = pg.Rect(500 * 0.25 - 75, 300 * 0.60, 150, 50)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
running = True
#random Number Generator
number=rd.randint(1, 99)
#function that refreshes the random number after user input
def update_number():
    global number
    number = rd.randint(1, 99)
def draw_game():
    #draw background and button
    root.fill(BRANCO)
    pg.draw.rect(root, VERMELHO, odd_button)
    number_text = font_small.render(str(number), True, (0, 0, 0))
    root.blit(number_text, (Init_Width // 2 - number_text.get_width() // 2, Init_Height // 2 - number_text.get_height() // 2))
    pg.display.flip()
#loop
while running:
    draw_game()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if odd_button.collidepoint(event.pos):
                running = False
pg.quit()
