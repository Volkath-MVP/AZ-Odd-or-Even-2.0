#all imports
#Pygame has features focused on games and also its own graphical interface (I even had to remove Tkinter because of it), and random was just used to create the random number generation system
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
#Menu variable
menu_open = False
F = False #Yeah, this is necessary. For fullscreen mode ...this is strange
#Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GRAY = (80, 80, 80)
running = True
#score variable
score = 0
#Just ignore this...
#       ⢸⠢⡀                        ⡠⡆
#       ⢸ ⣈⠢⡀                  ⡠⠊  ⡇
#       ⢸ ⣿⣷⣌⠢⠖⠊⠉⠉⠉⠉⠒⠢⠤  ⠊⣠⣾⡇ ⡇
#       ⢸ ⣿⣿⡿⠗      ⣀⠤⠒⠒⢄⡀⠘⠿⣿⡇ ⡇
#       ⢸  ⠉⠁      ⡠⠊          ⠈⠑⢄  ⠁⠈⠢⡀  ⢀⡀
#     ⢠⠃        ⢠⢊⣴⡄            ⢀⣶⠑⢄    ⠈⠉⠁⢈⠆
#⢠⠢⣀⣸        ⢰⠁⢸⣿⡇            ⣸⣿    ⢣    ⠐⡍⠁
#⠈⠢⣀⣠        ⡇  ⠸⡿⠁  ⡀        ⠹⠟  ⡠⠊⢇    ⠸⡀
#     ⠘⣄      ⣇⡀        ⠙⠒⠒⠊  ⣀⠤⠒⠁  ⢸    ⢀⠇
#       ⠈⠢⡀  ⢣⣨⣝⡒⢶⣶⡒⠲⣶⠊⢻⣧⣩⣶⠖⠢⢎  ⢀⠎
#         ⢀⡈⠙⢅    ⠉⢹⣿⣿⣷⣿⣷⣿⣿⣿⣇⡀⢀⠜⡔⠁
#         ⢸⣿⡦  ⠑⠒⢾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⣔⠕⢊⠆
#         ⠈⠙⠿⣦⣤⣤⣾⣿⣿⡿⠁    ⠑⢌⡻⣿⣿⣦⠤⠔⠁
#Function to draw all game interfaces
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
    #score
    ponto = font_medium.render(f"{score}", True, WHITE)
    root.blit(ponto, (WIDTH * 0.90 - ponto.get_width() // 2, HEIGHT * 0.20))
    #Odd and Even buttons
    odd_button = pg.Rect(WIDTH * 0.25 - 75, HEIGHT * 0.60, 150, 50)
    even_button = pg.Rect(WIDTH * 0.75 - 75, HEIGHT * 0.60, 150, 50)
    pg.draw.rect(root, GREEN, odd_button)
    pg.draw.rect(root, GREEN, even_button)
    odd_label = font_small.render("Impar (X)", True, BLACK)
    even_label = font_small.render("Par (B)", True, BLACK)
    root.blit(odd_label, odd_button.move(25, 10))
    root.blit(even_label, even_button.move(25, 10))
    #Open menu
    menu_btn = pg.Rect(WIDTH * 0.01 - 20, HEIGHT * 0.01, 80, 40)
    pg.draw.rect(root, GRAY, menu_btn)
    menu_btn_label = font_small.render("MENU", True, WHITE)
    root.blit(menu_btn_label, (10, 10))
    return odd_button, even_button, menu_btn
#Menu variable
menu_width, menu_height, menu_open= 300, 500, False
def draw_menu():
    overlay = pg.Surface((WIDTH, HEIGHT))#Creates a surface with the size (WIDTH, HEIGHT), in this case the same size as the initial screen. From this point on, "overlay" is equal to a surface of size (WIDTH, HEIGHT)
    #Background
    overlay.set_alpha(200)
    overlay.fill((BLACK))
    root.blit(overlay, (0, 0))
    #menu background
    menu_box = pg.Rect(WIDTH // 2 - menu_width // 2, HEIGHT // 2 - menu_height // 2, menu_width, menu_height)
    pg.draw.rect(root, GRAY, menu_box)
    menu_text = font_medium.render("Menu", True, WHITE)
    root.blit(menu_text, (menu_box.centerx - menu_text.get_width() // 2, menu_box.top + 20))
    #Menu buttons
    full_btn = pg.Rect(menu_box.centerx - 100, menu_box.centery - 120, 200, 40)
    pg.draw.rect(root, WHITE, full_btn)
    full_label = font_small.render("Fullscreen", True, BLACK)
    root.blit(full_label, (full_btn.centerx - full_label.get_width() // 2, full_btn.top + 10))
    close_btn = pg.Rect(menu_box.centerx - 100, menu_box.centery - 185, 200, 40)
    pg.draw.rect(root, RED, close_btn)
    close_label = font_small.render("Fechar Menu", True, WHITE)
    root.blit(close_label, (close_btn.centerx - close_label.get_width() // 2, close_btn.top + 10))
    return full_btn, close_btn
#random Number Generator
number=rd.randint(1, 99)
#Function to update the message after the response
message = "Where Is Your Motivation?"
def reset_message():
    global message
    message = ""
#Function to handle the score—it always decreases by the normal amount, and as you increase your rank, new deductions are added, with more and more amounts being subtracted from your score.
def decrease_score():
    global score
    score -= 50
    if score < 0:
        score = 0
    if score > 1000:
        score -= 50
    pg.time.set_timer(pg.USEREVENT + 2, 1000)
pg.time.set_timer(pg.USEREVENT + 2, 1000)#Yes, this's necessary, lol
#function that refreshes the random number after user input
def update_number():
    global number
    number=rd.randint(1, 99)
#Odd or Even function
def check(AZ):
    global number, message
    response = (number % 2 == 0 and AZ == "Even") or (number % 2 != 0 and AZ == "Odd")
    message = "YOU HAVE POWER!" if response else "You need more Energy..."
    pg.time.set_timer(pg.USEREVENT + 1, 800)
    V(response)
#reset message function
def reset_message():
    global message
    message = ""
#Score function. Starting with the negative situations first... I don’t know, it just feels like it makes more sense :/
def V(response):
    global score
    if response:
        score += 500
    else:
        score -= 800
#loop
while running:#It starts active by default, since we set it to "True", which makes it run without being explicitly called. Ideal for things that should run continuously. "while" = as long as "running" is True
    WIDTH, HEIGHT = root.get_size()
    odd_btn, even_btn, menu_btn = draw_game() if not menu_open else (None, None, None)
    if menu_open:
        fullscreen_btn, close_btn = draw_menu()
    for event in pg.event.get():#"for event in pg.event.get()""for" = makes it so that for each thing inside "event", which are the events that happen"in" inside "pg.event", Pygame events".get()"
     #to read or search inside pg.event. Pygame stores all user interactions in a list, and pg.event.get() searches for one of those already listed events—in this case, "event"
        if event.type == pg.QUIT:#Here it's to exit the window, so we change running from True to False. if = "event.type" some event from Pygame"==" is equal to"pg.QUIT" which makes the program close
            running = False
        #Odd and Even buttons
        elif event.type == pg.MOUSEBUTTONDOWN and not menu_open:
            x, y = event.pos
            if odd_btn.collidepoint((x, y)):
                check("Odd")
            elif even_btn.collidepoint((x, y)):
                check("Even")
            #Menu botton
            if menu_btn.collidepoint((x, y)):
                menu_open = True
        #Menu collision
        elif event.type == pg.MOUSEBUTTONDOWN and menu_open:
            x, y = event.pos
            if fullscreen_btn.collidepoint((x, y)):
                F = not F
                if F:
                    pg.display.set_mode((0, 0), pg.FULLSCREEN)
                else:
                    pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
            #Close Menu
            elif close_btn.collidepoint((x, y)):
                menu_open = False
        #Message and random number update
        if event.type == pg.USEREVENT + 1:
            message = ""
            update_number()
            pg.time.set_timer(pg.USEREVENT + 1, 0)#Cancels this timer until the next correct answer
        #Insert the decreasing score into the main loop
        if event.type == pg.USEREVENT + 2:
            decrease_score()
    pg.display.flip()#When we draw text, buttons, shapes… everything gets placed onto an “invisible screen” (buffer). The flip() flips that screen and displays it to the player—in other words, it renders everything.
    #That’s why we use pg.display.flip() at the end, to show the entire game to the player. 
    #This is part of Pygame—it’s how the library is structured, and it varies a lot depending on which one you’re using. Tkinter, for example, has a completely different structure.
    clock.tick(60)#Makes the game run at 60fps. We can place a variable inside the parentheses and use something to change it, creating a configuration.
pg.quit()#End of the code that only runs when "running" is set to False
