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
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
#Tamanhos de fonte para serem usados no jogo.
font_small = pg.font.SysFont("Arial", 18)
font_medium = pg.font.SysFont("Arial", 30)
font_large = pg.font.SysFont("Arial", 50)
running = True
#random Number Generator
number=rd.randint(1, 99)
#function that refreshes the random number after user input
def update_number():
    global number
    number = rd.randint(1, 99)
def draw_game():
    #draw background and button
    root.fill(BLACK)
    number_text = font_small.render(str(number), True, (0, 0, 0))
    root.blit(number_text, (Init_Width // 2 - number_text.get_width() // 2, Init_Height // 2 - number_text.get_height() // 2))
    odd_button = pg.Rect(1000 * 0.25 - 75, 70 * 0.60, 150, 50)
    even_button = pg.Rect(200 * 0.75 - 75, 70 * 0.60, 150, 50)
    pg.draw.rect(root, GREEN, odd_button)
    pg.draw.rect(root, GREEN, even_button)
    odd_label = font_small.render("Impar (X)", True, BLACK)
    even_label = font_small.render("Par (B)", True, BLACK)
    root.blit(odd_label, odd_button.move(25, 10))
    root.blit(even_label, even_button.move(25, 10))
    pg.display.flip()
    return odd_button, even_button
#loop
while running:
    #draw_game()
    odd_btn, even_btn = draw_game()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            if odd_btn.collidepoint((x, y)):
                running = False
            if even_btn.collidepoint((x, y)):
                running = False
pg.quit()
