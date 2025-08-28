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
pg.display.set_caption("AZ Odd or Even 2.0")
#initialize font
pg.font.init()
#FPS control
clock = pg.time.Clock()
#Font sizes to be used in the game
font_small = pg.font.SysFont("Arial", 18)
font_medium = pg.font.SysFont("Arial", 30)
font_large = pg.font.SysFont("Arial", 50)
#variables
font_small = pg.font.SysFont("Arial", 18)
odd_button = pg.Rect(500 * 0.25 - 75, 300 * 0.60, 150, 50)
#Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
running = True
#random Number Generator
number=rd.randint(1, 99)
#Function to update the message after the response
message = "Where is your motivation?"
def reset_message():
    global message
    message = ""
#function that refreshes the random number after user input
def update_number():
    global number
    number = rd.randint(1, 99)
def draw_game():
    #draw background and button
    root.fill(BLACK) #I set the background color. In the future, I’ll add an image—but that’s only for version 3.0. For now, we’re still on version 2.0.
    pergunta = font_medium.render(f"O número {number} é Ímpar ou Par?", True, WHITE)
    root.blit(pergunta, (300, 500))
    result_text = font_large.render(message, True, GREEN if "POWER" in message else RED)
    root.blit(result_text, (300, 400))
    odd_button = pg.Rect(1000, 70, 150, 50)
    even_button = pg.Rect(200, 70, 150, 50)
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
