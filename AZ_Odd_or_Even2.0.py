#all imports
#Pygame has features focused on games and also its own graphical interface (I even had to remove Tkinter because of it), and random was just used to create the random number generation system
import pygame as pg
import random as rd #random events
import threading as tdh #xbox and ps controlers
import os
#This's SOOOO boring...
#init pygame and display
pg.mixer.pre_init(44100, -16, 2, 512)
pg.init()
pg.mixer.init()
pg.mixer.music.set_volume(0.5)
current_music_path = None
current_sound_path = None
sound_end_event = pg.USEREVENT + 10
#initialize display
pg.display.init()
#initialize joystick
pg.joystick.init()
#initialize font
pg.font.init()
#window width and height
Init_Width, Init_Height = 1000, 800
#defining window properties
root = pg.display.set_mode((Init_Width, Init_Height), pg.RESIZABLE)
pg.display.set_caption("AZ Odd or Even 2.0")
#FPS control
clock = pg.time.Clock()
#random Number Generator
number=rd.randint(1, 100)
#Function to update the message after the response
message = "Where Is Your Motivation?"
#Font sizes to be used in the game
font_small = pg.font.SysFont("Arial", 18)
font_medium = pg.font.SysFont("Arial", 30)
font_large = pg.font.SysFont("Arial", 50)
font_very_large = pg.font.SysFont("Arial", 70)
#Menu variable
menu_open = False
F = False #Yeah, this is necessary. For fullscreen mode ...this is strange
menu_width, menu_height, menu_open= 300, 500, False
game_state = "main_menu"
#variable rank
ScoreIfMissing = 800
ScoreDrainedNormal = 40
ScoreDrainedRankC = 50
ScoreDrainedRankB = 60
ScoreDrainedRankA = 70
ScoreDrainedRankS = 80
ScoreDrainedRankSS = 100
ScoreDrainedRankSSS = 160
ScoreDrainedRankAZ = 200
RankD = 2200
RankC = 5200
RankB = 9800
RankA = 11800
RankS = 15200
RankSS = 20200
RankSSS = 28200
RankAZ = 35000
#drain speed
Drain_time = 300
#Devil Trigger variable
devil_trigger = 0
DTactive = False
#game state variables
main_menu = "main_menu"
game_themes = "game_themes"
game_config = "game_config"
game_start = "game_start"
game_menu = "game_menu"
#game sounds EFX
sound = ""
menus_buttons_sounds = "menus_buttons_sounds"
back_buttons_sounds = "back_buttons_sounds"
exed_sounds = "exed_sounds"
max_exed_sounds = "max_exed_sounds"
RankD_sounds = "RankD_sounds"
RankC_sounds = "RankC_sounds"
RankB_sounds = "RankB_sounds"
RankA_sounds = "RankA_sounds"
RankS_sounds = "RankS_sounds"
RankSS_sounds = "RankSS_sounds"
RankSSS1_sounds = "RankSSS1_sounds"
RankSSS2_sounds = "RankSSS2_sounds"
RankAZ_sounds = "RankAZ_sounds"
#max exed counter
#max_exed_counter = []
#Colors
#shades of gray
WHITE = (255, 255, 255)
GRAY = (80, 80, 80)
BLACK = (0, 0, 0)
#shades of red
RED = (255, 0, 0)
SALMON = (250, 128, 114)
CRIMSON = (220, 20, 60)
TOMATO = (255, 99, 71)
DARK_RED = (139, 0, 0)
#shades of blue
LIGHT_BLUE = (173, 216, 230)
DEEP_SKY_BLUE = (0, 191, 255)
POWDER_BLUE = (176, 224, 230)
DARK_BLUE = (0, 0, 139)
#shades of purple
PURPLE = (255, 0, 255)
#shades of green
GREEN = (0, 255, 0)
running = True
#score variable
score = 0
rank_text = ""
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
#Main menu draw event
def draw_main_menu():
    root.fill(BLACK)
    #Title
    title_label = font_very_large.render("AZ Odd or Even", True, RED)
    #Title position
    title_assistant_position_X = WIDTH // 2
    title_height_assistant_position_Y = HEIGHT * 0.1
    title_position_X = title_assistant_position_X - title_label.get_width() // 2
    title_height_position_Y = title_height_assistant_position_Y - title_label.get_height() // 2
    #Title draw
    root.blit(title_label, (title_position_X, title_height_position_Y))
    #Theme
    theme_label = font_medium.render("Temas", True, WHITE)
    #Theme position
    theme_position_assistant_X = WIDTH // 2
    theme_position_assistant_Y = HEIGHT * 0.4
    theme_button_position_X = theme_position_assistant_X - theme_label.get_width() // 2
    theme_button_position_Y = theme_position_assistant_Y - theme_label.get_height() // 2
    theme_button = pg.Rect(theme_button_position_X, theme_button_position_Y, theme_label.get_width(), theme_label.get_height())
    pg.draw.rect(root, GRAY, theme_button)
    #Theme draw
    root.blit(theme_label, (theme_button_position_X, theme_button_position_Y))
    #Configuration
    configuration_label = font_medium.render("Configurações", True, WHITE)
    #Configuration position
    configuration_position_assistant_X = WIDTH // 2
    configuration_position_assistant_Y = HEIGHT * 0.5
    configuration_button_position_X = configuration_position_assistant_X - configuration_label.get_width() // 2
    configuration_button_position_Y = configuration_position_assistant_Y - configuration_label.get_height() // 2
    configuration_button = pg.Rect(configuration_button_position_X, configuration_button_position_Y, configuration_label.get_width(), configuration_label.get_height())
    pg.draw.rect(root, GRAY, configuration_button)
    #Configuration draw
    root.blit(configuration_label, (configuration_button_position_X, configuration_button_position_Y))
    #Exit
    exit_label = font_medium.render("Sair", True, WHITE)
    #Exit position
    exit_position_assistant_X = WIDTH // 2
    exit_position_assistant_Y = HEIGHT * 0.6
    exit_button_position_X = exit_position_assistant_X - exit_label.get_width() // 2
    exit_button_position_Y = exit_position_assistant_Y - exit_label.get_height() // 2
    exit_button = pg.Rect(exit_button_position_X, exit_button_position_Y, exit_label.get_width(), exit_label.get_height())
    pg.draw.rect(root, GRAY, exit_button)
    #Exit draw
    root.blit(exit_label, (exit_button_position_X, exit_button_position_Y))
    return theme_button, configuration_button, exit_button
#Sounds efects
def sounds_choice(sound):
    if sound == "":
        return None
    if sound == menus_buttons_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "menu_button_sound.mp3")
        return sound_path
    if sound == back_buttons_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "whoosh_efects.mp3")
        return sound_path
    if sound == exed_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "exed.mp3")
        return sound_path
    if sound == max_exed_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "max_exed.mp3")
        return sound_path
    if sound == RankD_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "rank_sounds_D.mp3")
        return sound_path
    if sound == RankC_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "rank_sounds_C.mp3")
        return sound_path
    if sound == RankB_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "rank_sound_B.mp3")
        return sound_path
    if sound == RankA_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "rank_sounds_A.mp3")
        return sound_path
    if sound == RankS_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "rank_sound_S.mp3")
        return sound_path
    if sound == RankSS_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "rank_sound_SS.mp3")
        return sound_path
    if sound == RankSSS1_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "rank_sound_SSS1.mp3")
        return sound_path
    if sound == RankSSS2_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "rank_sound_SSS2.mp3")
        return sound_path
    if sound == RankAZ_sounds:
        #sound
        sound_path = os.path.join("Sonds_Efects", "sound_rank_AZ.mp3")
        return sound_path
def sounds_play():
    global current_sound_path
    sound_path = sounds_choice(sound)
    #print(sound_path)
    if sound_path and sound_path != current_sound_path and game_state == game_start:
        try:
            s = pg.mixer.Sound(sound_path)
            s.set_volume(0.5)
            chan = pg.mixer.find_channel()
            if chan:
                chan.set_endevent(sound_end_event)
                chan.play(s)
                current_sound_path = sound_path
        except Exception:
            current_sound_path = None
#draw themes
def draw_game_themes():
    root.fill(BLACK)
    #Title
    title_label = font_very_large.render("Temas", True, GRAY)
    #Title position
    title_assistant_position_X = WIDTH // 2
    title_assistant_position_Y = HEIGHT * 0.1
    title_position_X = title_assistant_position_X - title_label.get_width() // 2
    title_height_position_Y = title_assistant_position_Y - title_label.get_height() // 2
    #Title draw
    root.blit(title_label, (title_position_X, title_height_position_Y))
    #Back
    back_label = font_medium.render("Back", True, WHITE)
    #Back position
    back_assistant_position_X = WIDTH * 0.1
    back_assistant_position_Y = HEIGHT * 0.1
    back_button_position_X = back_assistant_position_X - back_label.get_width() // 2
    back_button_position_Y = back_assistant_position_Y - back_label.get_height() // 2
    back_button = pg.Rect(back_button_position_X, back_button_position_Y, back_label.get_width(), back_label.get_height())
    pg.draw.rect(root, GRAY, back_button)
    #Back draw
    root.blit(back_label, (back_button_position_X, back_button_position_Y))
    #Dante Theme
    dante_theme_label = font_medium.render("Dante", True, CRIMSON)
    #Dante theme position
    dante_assistant_position_X = WIDTH * 0.15
    dante_assistant_position_Y = HEIGHT * 0.3
    dante_button_position_X = dante_assistant_position_X
    dante_button_position_Y = dante_assistant_position_Y
    dante_button = pg.Rect(dante_button_position_X, dante_button_position_Y, dante_theme_label.get_width(), dante_theme_label.get_height())
    pg.draw.rect(root, SALMON, dante_button)
    #Draw Dante theme button
    root.blit(dante_theme_label, (dante_button_position_X, dante_button_position_Y))
    #DMC Dante
    #DMCDante Theme
    DMC_dante_theme_label = font_medium.render("DMC Dante", True, RED)
    #Dante theme position
    DMC_dante_assistant_position_X = WIDTH * 0.15
    DMC_dante_assistant_position_Y = HEIGHT * 0.4
    DMC_dante_button_position_X = DMC_dante_assistant_position_X
    DMC_dante_button_position_Y = DMC_dante_assistant_position_Y
    DMC_dante_button = pg.Rect(DMC_dante_button_position_X, DMC_dante_button_position_Y, DMC_dante_theme_label.get_width(), DMC_dante_theme_label.get_height())
    pg.draw.rect(root, DARK_RED, DMC_dante_button)
    #Draw Dante theme button
    root.blit(DMC_dante_theme_label, (DMC_dante_button_position_X, DMC_dante_button_position_Y))
    #Vergil Theme
    vergil_theme_label =font_medium.render("Vergil", True, DEEP_SKY_BLUE)
    #Vergil theme position
    vergil_assistant_position_X = WIDTH * 0.15
    vergil_assistant_position_Y = HEIGHT * 0.5
    vergil_button_position_X = vergil_assistant_position_X
    vergil_button_position_Y = vergil_assistant_position_Y
    vergil_button = pg.Rect(vergil_button_position_X, vergil_button_position_Y, vergil_theme_label.get_width(), vergil_theme_label.get_height())
    pg.draw.rect(root, POWDER_BLUE, vergil_button)
    #Draw Vergil theme button
    root.blit(vergil_theme_label, (vergil_button_position_X, vergil_button_position_Y))
    #DMC3 Vergil Theme
    DMC3_vergil_theme_label =font_medium.render("DMC3 Vergil", True, DEEP_SKY_BLUE)
    #DMC3 Vergil theme position
    DMC3_vergil_assistant_position_X = WIDTH * 0.15
    DMC3_vergil_assistant_position_Y = HEIGHT * 0.6
    DMC3_vergil_button_position_X = DMC3_vergil_assistant_position_X
    DMC3_vergil_button_position_Y = DMC3_vergil_assistant_position_Y
    DMC3_vergil_button = pg.Rect(DMC3_vergil_button_position_X, DMC3_vergil_button_position_Y, DMC3_vergil_theme_label.get_width(), DMC3_vergil_theme_label.get_height())
    pg.draw.rect(root, DARK_BLUE, DMC3_vergil_button)
    #Draw DMC3 Dante theme button
    root.blit(DMC3_vergil_theme_label, (DMC3_vergil_button_position_X, DMC3_vergil_button_position_Y))
    #DMC3 Dante Theme
    DMC3_dante_theme_label =font_medium.render("DMC3 Dante", True, DEEP_SKY_BLUE)
    #DMC3 Dante theme position
    DMC3_dante_assistant_position_X = WIDTH * 0.15
    DMC3_dante_assistant_position_Y = HEIGHT * 0.7
    DMC3_dante_button_position_X = DMC3_dante_assistant_position_X
    DMC3_dante_button_position_Y = DMC3_dante_assistant_position_Y
    DMC3_dante_button = pg.Rect(DMC3_dante_button_position_X, DMC3_dante_button_position_Y, DMC3_dante_theme_label.get_width(), DMC3_dante_theme_label.get_height())
    pg.draw.rect(root, DARK_BLUE, DMC3_dante_button)
    #Draw V theme button
    root.blit(DMC3_dante_theme_label, (DMC3_dante_button_position_X, DMC3_dante_button_position_Y))
    #Draw V theme button
    #V Theme
    v_theme_label =font_medium.render("V", True, DEEP_SKY_BLUE)
    #V theme position
    v_assistant_position_X = WIDTH * 0.15
    v_assistant_position_Y = HEIGHT * 0.8
    v_button_position_X = v_assistant_position_X
    v_button_position_Y = v_assistant_position_Y
    v_button = pg.Rect(v_button_position_X, v_button_position_Y, v_theme_label.get_width(), v_theme_label.get_height())
    pg.draw.rect(root, DARK_BLUE, v_button)
    #Draw V theme button
    root.blit(v_theme_label, (v_button_position_X, v_button_position_Y))
    return back_button, dante_button, DMC_dante_button, vergil_button, DMC3_vergil_button, DMC3_dante_button, v_button
Theme = {
    "Theme0": "Dante", 
    "Theme1": "DMC_Dante", 
    "Theme2": "Vergil", 
    "Theme3": "DMC3_Vergil",
    "Theme4": "DMC3_Dante",
    "Theme5": "V"}
selected_theme = ""
def background_theme(selected_theme):
    if selected_theme == "":
        return None, None
    elif selected_theme == "Dante":
        #background
        img_path = os.path.join("Backgrounds", "dante_4k.jpg")
        theme_select = img_path
        #Musics
        music_path = os.path.join("Musics", "Devil_May_Cry 5_Subhuman_[EPIC METAL COVER]_(Little V).mp3")
        return theme_select, music_path
    elif selected_theme == "DMC_Dante":
        #background
        img_path = os.path.join("Backgrounds", "Dante_DMC_Devil_May_Cry.jpg")
        theme_select = img_path
        #Musics
        music_path = os.path.join("Musics", "sent-to-destroy-dmc-devil-may-cry.mp3")
        return theme_select, music_path
    elif selected_theme == "Vergil":
        #background
        img_path = os.path.join("Backgrounds", "vergil_DMC5.png")
        theme_select = img_path
        #Musics
        music_path = os.path.join("Musics", "")
        return theme_select, music_path
    elif selected_theme == "DMC3_Vergil":
        #background
        img_path = os.path.join("Backgrounds", "Vergil_DMC3.jpg")
        theme_select = img_path
        #Musics
        music_path = os.path.join("Musics", "vergil-battle-2-extended-version.mp3")
        return theme_select, music_path
    elif selected_theme == "DMC3_Dante":
        #background
        img_path = os.path.join("Backgrounds", "Dante_DMC3.jpg")
        theme_select = img_path
        #Musics
        music_path = os.path.join("Musics", "Devil May Cry 3 - Devils Never Cry [EPIC METAL COVER] (Little V)(MP3_128K).mp3")
        return theme_select, music_path
    elif selected_theme == "V":
        #background
        img_path = os.path.join("Backgrounds", "V.jpg")
        theme_select = img_path
        #Musics
        music_path = os.path.join("Musics", "Devil May Cry 5 - Crimson Cloud [EPIC METAL COVER] (Little V)(MP3_128K).mp3")
        return theme_select, music_path
def draw_game():
    global current_music_path
    #draw background and button 
    #root.fill(BLACK) #I set the background color. In the future, I’ll add an image—but that’s only for version 3.0. For now, we’re still on version 2.0.
    theme_select, music_path = background_theme(selected_theme)
    if theme_select:
        background = pg.image.load(theme_select)
        background = pg.transform.scale(background, (WIDTH, HEIGHT))
        root.blit(background, (0, 0))
    if music_path and music_path != current_music_path and game_state == game_start:
        if not os.path.exists(music_path):
            #print("Music missing:", music_path)
            None
        else:
            try:
                pg.mixer.music.load(music_path)
                pg.mixer.music.play(-1)
                current_music_path = music_path
            except Exception:
                current_music_path = None
    #Label, question background, and overall background
    pergunta_label = font_medium.render(f"O número {number} é Ímpar ou Par?", True, RED)
    result_text = font_large.render(message, True, GREEN if "POWER" in message else RED)
    root.blit(result_text, (WIDTH // 2 - result_text.get_width() // 2, 120))
    root.blit(pergunta_label, (WIDTH // 2 - pergunta_label.get_width() // 2, 50))#To draw, we need the surface (the window or the background of things—this is everywhere in this program and in all others that exist).
#We already created the surface with the root (up there). The ".blit" draws another surface on top of whichever one we choose—in this case, "root". That’s where we place the phrase stored in the variable "pergunta". Now comes the interesting part:
#root.blit(pergunta, (WIDTH // 2 - pergunta.get_width() // 2, 50)) — inside the parentheses "(pergunta, (WIDTH // 2 - pergunta.get_width() // 2, 50))", the first part defines what goes inside: the content (pergunta)...
#...and the position of that pergunta (WIDTH // 2 - pergunta.get_width() // 2, 50) is the second part. We could write "(pergunta, (50, 50))" — that would place it 50 pixels down and 50 pixels across, meaning we can position it...
#...wherever we want. But we can use "WIDTH // 2" — that grabs the width of "root" (whatever it may be) and places the pergunta in the middle. However, there’s a problem: the size of the text...
#...would make it not appear centered since it takes up space. So we use "- pergunta.get_width() // 2" — that gets (.get) the width (_width) of pergunta (the "()" after width refers to pergunta) and subtracts it
#from the root’s width, placing it in the center. The ", 50" is the height… that’s it. We could’ve done the same thing for height, but it wasn’t necessary in this case.
#From here on, it’s the same stuff I’ve already explained.If you want, I can help you turn this into clean bilingual comments for your code — makes it easier to share or document for others. Want me to format it that way?
    pergunta_x = WIDTH // 2 - pergunta_label.get_width() // 2
    pergunta_y = 50
    pergunta_background = pg.Rect(pergunta_x -10, pergunta_y -5, pergunta_label.get_width() + 20, pergunta_label.get_height() + 10)
    pg.draw.rect(root, BLACK, pergunta_background)
    root.blit(pergunta_label, (pergunta_x, pergunta_y))
    #score
    ponto = font_medium.render(f"{score}", True, WHITE)
    root.blit(ponto, (WIDTH * 0.90 - ponto.get_width() // 2, HEIGHT * 0.20))
    #Odd and Even buttons
    odd_x = WIDTH // 3 - HEIGHT // 6
    odd_y = HEIGHT // 1.7
    odd_button = pg.Rect(odd_x, odd_y, 130, 50)
    even_x = WIDTH // 1.3 - HEIGHT // 6
    even_y = HEIGHT // 1.7
    even_button = pg.Rect(even_x, even_y, 130, 50)
    pg.draw.rect(root, RED, odd_button)
    pg.draw.rect(root, RED, even_button)
    odd_label = font_small.render("Impar (X)", True, WHITE)
    even_label = font_small.render("Par (B)", True, WHITE)
    root.blit(odd_label, odd_button.move(25, 10))
    root.blit(even_label, even_button.move(25, 10))
    #Devil Trigger bar
    Min_DT_Bar_X = WIDTH * 0.30 - 75 + 700 * 0.2857
    Min_DT_Bar_Y_Start = HEIGHT * 0.90
    Min_DT_Bar_Y_End = HEIGHT * 0.90 + 40
    DT = pg.Rect(WIDTH * 0.30 - 75, HEIGHT * 0.90, devil_trigger, 50)
    pg.draw.rect(root, PURPLE, DT)
    Bar_DT_limit = pg.draw.rect(root, GRAY, pg.Rect(WIDTH * 0.30 - 75, HEIGHT * 0.90, 700, 50), 10)
    Bar_DT_Min = pg.draw.line(root, GRAY, (Min_DT_Bar_X, Min_DT_Bar_Y_Start), (Min_DT_Bar_X, Min_DT_Bar_Y_End), 10)
    #Rank message
    rank_view = font_medium.render(f"{rank_text}", True, WHITE)
    root.blit(rank_view, (WIDTH * 0.90 - rank_view.get_width() // 2, HEIGHT * 0.14))
    #Open menu
    menu_button = pg.Rect(WIDTH * 0.01 - 20, HEIGHT * 0.01, 80, 40)
    pg.draw.rect(root, GRAY, menu_button)
    menu_button_label = font_small.render("MENU", True, WHITE)
    root.blit(menu_button_label, (10, 10))
    return menu_button, odd_button, even_button, DT, Bar_DT_limit, Bar_DT_Min
def draw_menu():
    overlay = pg.Surface((WIDTH, HEIGHT))#Creates a surface with the size (WIDTH, HEIGHT), in this case the same size as the initial screen. From this point on, "overlay" is equal to a surface of size (WIDTH, HEIGHT)
    #Background
    overlay.set_alpha(200)
    overlay.fill((BLACK))
    root.blit(overlay, (0, 0))
    #menu box label
    menu_label = font_medium.render("Menu", True, WHITE)
    #menu box position
    menu_box = pg.Rect(WIDTH // 2 - menu_width // 2, HEIGHT // 2 - menu_height // 2, menu_width, menu_height)
    pg.draw.rect(root, GRAY, menu_box)
    #menu box draw
    root.blit(menu_label, (menu_box.centerx - menu_label.get_width() // 2, menu_box.top + 20))
    #Menu buttons
    #Back menu
    menu_back_label = font_small.render("Back", True, BLACK)
    #Back position
    menu_back_button = pg.Rect(menu_box.centerx - 100, menu_box.centery - 55, 200, 40)
    pg.draw.rect(root, WHITE, menu_back_button)
    #Back draw
    root.blit(menu_back_label, (menu_back_button.centerx - menu_back_label.get_width() // 2, menu_back_button.top + 10))
    #Fullscreen label
    full_label = font_small.render("Fullscreen", True, BLACK)
    #Fullscreen btn position
    full_button = pg.Rect(menu_box.centerx - 100, menu_box.centery - 120, 200, 40)
    pg.draw.rect(root, WHITE, full_button)
    #Fullscreen draw
    root.blit(full_label, (full_button.centerx - full_label.get_width() // 2, full_button.top + 10))
    #Close button label
    close_label = font_small.render("Fechar Menu", True, WHITE)
    #Close button position
    close_button = pg.Rect(menu_box.centerx - 100, menu_box.centery - 185, 200, 40)
    pg.draw.rect(root, RED, close_button)
    #Close button draw
    root.blit(close_label, (close_button.centerx - close_label.get_width() // 2, close_button.top + 10))
    return full_button, close_button, menu_back_button
def reset_message():
    global message
    message = ""
#Function to handle the score—it always decreases by the normal amount, and as you increase your rank, new deductions are added, with more and more amounts being subtracted from your score.
def decrease_score():
    global score
    score -= ScoreDrainedNormal
    if score > RankC:
        score -= ScoreDrainedRankC
    elif score >= RankB:
        score -= ScoreDrainedRankB
    elif score >= RankA:
        score -= ScoreDrainedRankA
    elif score >= RankS:
        score -= ScoreDrainedRankS
    elif score >= RankSS:
        score -= ScoreDrainedRankSS
    elif score >= RankSSS:
        score -= ScoreDrainedRankSSS
    elif score >= RankAZ:
        score -= ScoreDrainedRankAZ
    if score < 0:
        score = 0
    pg.time.set_timer(pg.USEREVENT + 2, Drain_time)
pg.time.set_timer(pg.USEREVENT + 2, Drain_time)#Yes, this's necessary, lol
#function that refreshes the random number after user input
def update_number():
    global number
    number=rd.randint(1, 100)
def rank_announcer(response):
    global sound
    if response and RankAZ <= score <= RankAZ + 700:
        sound = RankAZ_sounds
    elif response and RankSSS <= score <= RankSSS + 700:
        sound = RankSSS1_sounds
    elif response and RankSS <= score <= RankSS + 700:
        sound = RankSS_sounds
    elif response and RankS <= score <= RankS + 700:
        sound = RankS_sounds
    elif response and RankA <= score <= RankA + 700:
        sound = RankA_sounds
    elif response and RankB <= score <= RankB + 700:
        sound = RankB_sounds
    elif response and RankC <= score <= RankC + 700:
        sound = RankC_sounds
    elif response and RankD <= score <= RankD + 700:
        sound = RankD_sounds
#Odd or Even function
def check(AZ):
    global number, message, sound
    if game_state != game_start:
        return
    response = (number % 2 == 0 and AZ == "Even") or (number % 2 != 0 and AZ == "Odd")
    message = "YOU HAVE POWER!" if response else "You need more Energy..."
    #print(response)
    Points_Devil_trigger(response)
    V(response)
    update_rank()
    rank_announcer(response)
    pg.time.set_timer(pg.USEREVENT + 1, Drain_time)
#reset message function
def reset_message():
    global message
    message = ""
#Score function. Starting with the negative situations first... I don’t know, it just feels like it makes more sense :/
def V(response):
    global score
    if response and DTactive:
        score += 800
    elif response and not DTactive:
        score += 500
    else:
        score -= ScoreIfMissing
    if score < 0:
        score = 0
#Function to update rank
def update_rank():
    global score, rank_text
    if score >= RankAZ:
        rank_text = "AZHEAVEN"
    elif score >= RankSSS:
        rank_text = "SSS"
    elif score >= RankSS:
        rank_text = "SS"
    elif score >= RankS:
        rank_text = "S"
    elif score >= RankA:
        rank_text = "A"
    elif score>= RankB:
        rank_text = "B"
    elif score>= RankC:
        rank_text = "C"
    elif score>=RankD:
        rank_text = "D"
    else:
        rank_text = ""
def Points_Devil_trigger(response):
    global devil_trigger
    if devil_trigger >= 700 and response and not DTactive or devil_trigger >= 700 and response and DTactive:
        devil_trigger += 0
        devil_trigger = 700
    elif response and not DTactive:
        devil_trigger += 20
def Drain_devil_trigger():
    global devil_trigger, DTactive
    if DTactive:
        devil_trigger -= 40
        if devil_trigger <= 0:
            devil_trigger = 0
            DTactive = False
    pg.time.set_timer(pg.USEREVENT + 3, Drain_time)
pg.time.set_timer(pg.USEREVENT + 3, Drain_time)
def Joystick_Def():
    if pg.joystick.get_count() > 0:
        joystick = pg.joystick.Joystick(0)
        joystick.init()
thread_controle = tdh.Thread(target=Joystick_Def, daemon=True)
thread_controle.start()
def game_drawings_events(game_state):
    if game_state == main_menu:
        return draw_main_menu()
    elif game_state == game_themes:
        return draw_game_themes()
    elif game_state == game_start:
        return draw_game()
    elif game_state == game_menu:
        return draw_menu()
    else:
        return None
while running:#It starts active by default, since we set it to "True", which makes it run without being explicitly called. Ideal for things that should run continuously. "while" = as long as "running" is True
    WIDTH, HEIGHT = root.get_size()
    update_rank()
    sounds_choice(sound)
    sounds_play()
    #game_drawings()
    #print(game_state)
    #print(menu_open)
    #print(event)
    #print(menu_open)
    theme_button = configuration_button = exit_button = None
    back_button = dante_button = DMC_dante_button = vergil_button = DMC3_vergil_button = DMC3_dante_button = v_button = None
    menu_button = odd_button = even_button = DT = Bar_DT_limit = Bar_DT_Min = None
    full_button = close_button = menu_back_button = None
    result = game_drawings_events(game_state)
    #state_confirm(game_state)
    #print(pg.mixer.get_init())
    if result:
        if game_state == main_menu:
            theme_button, configuration_button, exit_button = result
        elif game_state == game_themes:
            back_button, dante_button, DMC_dante_button, vergil_button, DMC3_vergil_button, DMC3_dante_button, v_button = result
            devil_trigger = 0
            score = 0
        elif game_state == game_start:
            menu_button, odd_button, even_button, DT, Bar_DT_limit, Bar_DT_Min = result
        elif game_state == game_menu:
            full_button, close_button, menu_back_button = result
    for event in pg.event.get():#"for event in pg.event.get()""for" = makes it so that for each thing inside "event", which are the events that happen"in" inside "pg.event", Pygame events".get()"
     #to read or search inside pg.event. Pygame stores all user interactions in a list, and pg.event.get() searches for one of those already listed events—in this case, "event"
        if event.type == sound_end_event:
            sound = ""
            current_sound_path = None
        if event.type == pg.JOYDEVICEADDED:
            joystick = pg.joystick.Joystick(event.device_index)
            joystick.init()
            #print(joystick.get_name)
        if event.type == pg.QUIT:#Here it's to exit the window, so we change running from True to False. if = "event.type" some event from Pygame"==" is equal to"pg.QUIT" which makes the program close
            running = False
        #All keyboard events
        #main menu keyboard
        #Menu keyboard
        if event.type == pg.KEYDOWN:
            #print(event.key == pg.K_ESCAPE)
            #Esc opens the menu
            if event.key == pg.K_ESCAPE and not menu_open and game_state == game_start:#From this point on, it’s all syntax, so it’s more about researching and positioning these things
                game_state = game_menu
                sound = menus_buttons_sounds
                menu_open = True
                print(sound)
                print(game_state)
                print(menu_open)
            elif event.key == pg.K_ESCAPE and menu_open and game_state == game_menu:
                game_state = game_start
                sound = menus_buttons_sounds
                menu_open = False
                print(game_state)
                print(menu_open)
            #If the menu isn’t open, then the buttons, mouse, and eventually a controller will work
            #Odd and Even keyboard
            if game_state == game_start:
                #Odd
                if event.key == pg.K_a:
                    check("Odd")
                #Even
                elif event.key == pg.K_d:
                    check("Even")
                elif event.key == pg.K_SPACE and devil_trigger >= 200 and not DTactive and game_state == game_start:
                    DTactive = True
                elif event.key == pg.K_SPACE and DTactive and game_state == game_start:
                    DTactive = False
        #All mouse events
        #main menu mouse
        elif event.type == pg.MOUSEBUTTONDOWN and game_state == main_menu:
            x, y = event.pos
            if theme_button and theme_button.collidepoint((x, y)):
                sound = menus_buttons_sounds
                game_state = game_themes
                #print(game_state)
                #print(sound)
            elif configuration_button and configuration_button.collidepoint((x, y)):
                sound = menus_buttons_sounds
                game_state = game_config
            elif exit_button and exit_button.collidepoint((x, y)):
                running = False
        elif event.type == pg.MOUSEBUTTONDOWN and game_state == game_themes:
            x, y = event.pos
            if back_button and back_button.collidepoint((x, y)):
                game_state = main_menu
                sound = menus_buttons_sounds
                #print(game_state)
                #print(sound)
                #print(current_sound_path)
            elif dante_button and dante_button.collidepoint((x, y)):
                selected_theme = Theme.get("Theme0")
                game_state = game_start
                sound = menus_buttons_sounds
                #print(game_state)
                #print(sound)
                #print(current_sound_path)
            elif DMC_dante_button and DMC_dante_button.collidepoint((x, y)):
                selected_theme = Theme.get("Theme1")
                game_state = game_start
                sound = menus_buttons_sounds
                #print(game_state)
                #print(sound)
                #print(current_sound_path)
            elif vergil_button and vergil_button.collidepoint((x, y)):
                selected_theme = Theme.get("Theme2")
                game_state = game_start
                sound = menus_buttons_sounds
                #print(game_state)
                #print(sound)
                #print(current_sound_path)
            elif DMC3_vergil_button and DMC3_vergil_button.collidepoint((x, y)):
                selected_theme = Theme.get("Theme3")
                game_state = game_start
                sound = menus_buttons_sounds
                #print(game_state)
                #print(sound)
                #print(current_sound_path)
            elif DMC3_dante_button and DMC3_dante_button.collidepoint((x, y)):
                selected_theme = Theme.get("Theme4")
                game_state = game_start
                sound = menus_buttons_sounds
                #print(game_state)
                #print(sound)
                #print(current_sound_path)
            elif v_button and v_button.collidepoint((x, y)):
                selected_theme = Theme.get("Theme5")
                game_state = game_start
                sound = menus_buttons_sounds
                #print(game_state)
                #print(sound)
                #print(current_sound_path)
        #Menu mouse
        elif event.type == pg.MOUSEBUTTONDOWN and menu_open and game_state == game_menu:
            x, y = event.pos
            if full_button and full_button.collidepoint((x, y)):
                F = not F
                if F:
                    pg.display.set_mode((0, 0), pg.FULLSCREEN)
                else:
                    pg.display.set_mode((WIDTH, HEIGHT), pg.RESIZABLE)
            #Close Menu
            if close_button and close_button.collidepoint((x, y)) and game_state == game_menu:
                game_state= game_start
                sound = menus_buttons_sounds
                menu_open = F
                #print(game_state)
                #print(menu_open)
                pg.mixer.music.unpause()
            elif menu_back_button and menu_back_button.collidepoint((x, y)) and game_state == game_menu:
                game_state = main_menu
                sound = menus_buttons_sounds
                menu_open = F
                pg.mixer.music.fadeout(1000)
        #Odd and Even mouse
        elif event.type == pg.MOUSEBUTTONDOWN and not menu_open:
            x, y = event.pos
            #Menu botton
            if menu_button and menu_button.collidepoint((x, y)) and game_state == game_start:
                game_state = game_menu
                sound = menus_buttons_sounds
                menu_open = True
                #print(game_state)
                #print(menu_open)
                pg.mixer.music.pause()
            #Odd
            elif odd_button and odd_button.collidepoint((x, y)):
                check("Odd")
            #Even
            elif even_button and even_button.collidepoint((x, y)):
                check("Even")
        #All Controller events
        #Menu controller
        if event.type == pg.JOYBUTTONDOWN:
            if event.button == 7 and not menu_open and game_state == game_start:
                game_state = game_menu
                sound = menus_buttons_sounds
                menu_open = True
            #close menu
            elif event.button == 7 and menu_open and game_state == game_menu:
                game_state = game_start
                sound = menus_buttons_sounds
                menu_open = False
        #Odd and Even controller
        if event.type == pg.JOYBUTTONDOWN and not menu_open and game_state == game_start:
            if event.button == 2:
                check("Odd")
            elif event.button == 1:
                check("Even")
        #Message and random number update
        elif event.type == pg.USEREVENT + 1:
            message = ""
            update_number()
            pg.time.set_timer(pg.USEREVENT + 1, 0)#Cancels this timer until the next correct answer
        #Insert the decreasing score into the main loop
        elif event.type == pg.USEREVENT + 2:
            decrease_score()
        elif event.type == pg.USEREVENT + 3:
            Drain_devil_trigger()
    pg.display.flip()#When we draw text, buttons, shapes… everything gets placed onto an “invisible screen” (buffer). The flip() flips that screen and displays it to the player—in other words, it renders everything.
    #That’s why we use pg.display.flip() at the end, to show the entire game to the player. 
    #This is part of Pygame—it’s how the library is structured, and it varies a lot depending on which one you’re using. Tkinter, for example, has a completely different structure.
    clock.tick(60)#Makes the game run at 60fps. We can place a variable inside the parentheses and use something to change it, creating a configuration.
pg.quit()#End of the code that only runs when "running" is set to False
