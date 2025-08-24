import pygame as pg
pg.init()
pg.display.init()
root = pg.display.set_mode((1280, 720), pg.RESIZABLE)
font_small = pg.font.SysFont("Arial", 18)
odd_button = pg.Rect(500 * 0.25 - 75, 300 * 0.60, 150, 50)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if odd_button.collidepoint(event.pos):
                running = False
    # Desenha fundo e botão
    root.fill(BRANCO)
    pg.draw.rect(root, VERMELHO, odd_button)
    pg.display.flip()
pg.quit()
