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
message = "Where Is Your Motivation?"
def reset_message():
    global message
    message = ""
#function that refreshes the random number after user input
def update_number():
    global number
    number
def draw_game():
    #draw background and button
    root.fill(BLACK) #I set the background color. In the future, I’ll add an image—but that’s only for version 3.0. For now, we’re still on version 2.0.
    pergunta = font_medium.render(f"O número {number} é Ímpar ou Par?", True, WHITE)
    root.blit(pergunta, (WIDTH // 2 - pergunta.get_width() // 2, 50))#To draw, we need the surface (the window or the background of things—this is everywhere in this program and in all others that exist).
#We already created the surface with the root (up there). The ".blit" draws another surface on top of whichever one we choose—in this case, "root". That’s where we place the phrase stored in the variable "pergunta". Now comes the interesting part:
#root.blit(pergunta, (WIDTH // 2 - pergunta.get_width() // 2, 50)) — inside the parentheses "(pergunta, (WIDTH // 2 - pergunta.get_width() // 2, 50))", the first part defines what goes inside: the content (pergunta)...
#...and the position of that pergunta (WIDTH // 2 - pergunta.get_width() // 2, 50) is the second part. We could write "(pergunta, (50, 50))" — that would place it 50 pixels down and 50 pixels across, meaning we can position it...
#...wherever we want. But we can use "WIDTH // 2" — that grabs the width of "root" (whatever it may be) and places the pergunta in the middle. However, there’s a problem: the size of the text...
#...would make it not appear centered since it takes up space. So we use "- pergunta.get_width() // 2" — that gets (.get) the width (_width) of pergunta (the "()" after width refers to pergunta) and subtracts it
#from the root’s width, placing it in the center. The ", 50" is the height… that’s it. We could’ve done the same thing for height, but it wasn’t necessary in this case.
#From here on, it’s the same stuff I’ve already explained.If you want, I can help you turn this into clean bilingual comments for your code — makes it easier to share or document for others. Want me to format it that way?
    result_text = font_large.render(message, True, GREEN if "POWER" in message else RED)
    root.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 120))
    odd_button = pg.Rect(WIDTH * 0.25 - 75, HEIGHT * 0.60, 150, 50)
    even_button = pg.Rect(WIDTH * 0.75 - 75, HEIGHT * 0.60, 150, 50)
    pg.draw.rect(root, GREEN, odd_button)
    pg.draw.rect(root, GREEN, even_button)
    odd_label = font_small.render("Impar (X)", True, BLACK)
    even_label = font_small.render("Par (B)", True, BLACK)
    root.blit(odd_label, odd_button.move(25, 10))
    root.blit(even_label, even_button.move(25, 10))
    pg.display.flip()
    return odd_button, even_button
#Odd or Even function
def check(AZ):
    global number, message
    response = (number % 2 == 0 and AZ == "Even") or (number % 2 != 0 and AZ == "Odd")
    message = "YOU HAVE POWER!" if response else "You need more Energy..."
    pg.time.set_timer(pg.USEREVENT + 1, 800)
#reset message function
def reset_message():
    global message
    message = ""
#loop
while running:
    WIDTH, HEIGHT = root.get_size()
    #draw_game()
    odd_btn, even_btn = draw_game()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = event.pos
            if odd_btn.collidepoint((x, y)):
                check("Odd")
            if even_btn.collidepoint((x, y)):
                check("Even")
        elif event.type == pg.USEREVENT + 1:
            message = ""
            update_number()
            pg.time.set_timer(pg.USEREVENT + 1, 0)
    pg.display.flip()
    clock.tick(60)
pg.quit()
