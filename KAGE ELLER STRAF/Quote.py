import pygame as py
import random
import sys
py.init()
py.font.init()

WIDTH, HEIGHT = 1000, 800
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("TORE QUOTE RANDOMIZER")

BAG = py.image.load("Velkommen.jpeg")
FONT = py.font.SysFont("Comic Sans", 20)

text = "TEEEEEEEEEEST!"

test = FONT.render("TEEEEEST!", 1, "white")

def main():
    run = True
    
    while run:
        
        WIN.fill("pink")
        WIN.blit(test, (20, 40))
        

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break
        py.display.update

    py.quit()

main()
    