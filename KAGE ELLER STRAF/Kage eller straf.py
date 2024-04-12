import pygame as py
import random
import sys
import time
py.init()
py.font.init()

# SKREVET AF GUI PRINSESSEN & KODESLAVEN #

WIDTH, HEIGHT = 1000, 800
WIN = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Tores Decisionmaker")

#Billeder
BG = py.image.load("Velkommen.jpeg")
StrafBG = py.transform.scale(py.image.load("StrafBG.png"), (WIDTH, HEIGHT))
StrafValg = py.transform.scale(py.image.load("Strafvalg.JPG"), (WIDTH, HEIGHT))
KageBG = py.transform.scale(py.image.load("KageBG.jpg"), (WIDTH, HEIGHT))
ValgBG = py.transform.scale(py.image.load("Background.png"), (WIDTH, HEIGHT))
SukBG = py.transform.scale(py.image.load("sukbg.jpg"), (WIDTH, HEIGHT))
LidtBG = py.transform.scale(py.image.load("lidtbg.jpg"), (WIDTH, HEIGHT))
MegetBG = py.transform.scale(py.image.load("megetbg.jpg"), (WIDTH, HEIGHT))

#Fonts
StorFont = py.font.SysFont("Comic Sans", 90)
FONT = py.font.SysFont("Comic Sans", 70)
LilleFont = py.font.SysFont("Comic Sans", 40)
StrafFont = py.font.SysFont("Comic Sans", 20)
new_press = True

#Lyde
Kage_sfx = py.mixer.Sound("cartoon-yay-140921.mp3")
Straf_sfx = py.mixer.Sound("slag.mp3")
Win_sfx = py.mixer.Sound("allidoiswin.mp3")
Knap_Press = py.image.load("Knap_hover.png")

#Lister
Meget_dygtig = ["Cheesecake", "Chokoladekage", "Tiramisu", "Red Velvet Cake", "Gulerodskage", "Citronfromage", "Tres Leches", "Bananbrød", "Angel Food"]
Lidt = ["Black Forest Kage", "Key Lime Pie", "Bakewell Tart", "Frugtkage", "Pavlova", "Boston Cream Pie", "Lava Kage", "Cupcakes"]
Suk = ["Jelly Roll", "Linzertorte", "Eccles", "Battenberg", "Parkin", "Stollen", "Sandkage"]
HStraf = ["En testikel i hvidløgspresseren", "To testikler i hvidløgspresseren", "Få Ørådet til at stemme Emil hjem til Odense.", "Det skal være noget med en ske og en langsom død", "Strøm. Høj spænding. God mængde Ampere", "Et lukket skab og en CO2 brandslukker", "Tvangsflyt dem til Næstved", "Hyr Bornholmske hackere til at gøre livet surt for dem i ti år" ]
MStraf = ["Jeg er flink i dag. Du kan nøjes med en 55 minutters prædiken",
                "Bliv siddende på gulvet indtil du har tænkt over om du vil være en GUI-prinsesse resten af livet",
                "Du må være tosset, hvis du tror, at du har fortjent en pause i dag", "Hent kaffe",
                "Send dem ned til svangerskabet for at hente strømvenderen",
                "Du er da vist fra Næstved. Du må godt tage hjem",
                "Bed dem om at lave en fuld netværksplan for Maersk"]

class Button:
    def __init__(self, text, x_pos, y_pos, enabled):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.enabled = enabled
        self.draw()

    def draw(self):  
        button_text = FONT.render(self.text, True, 'white')
        button_rect = py.rect.Rect((self.x_pos, self.y_pos),(400, 600))
        KNAP = py.image.load("Knap.png")
        WIN.blit(KNAP, (self.x_pos, self.y_pos))
        WIN.blit(button_text, (self.x_pos + 140, self.y_pos + 50))
    
    def check_click(self):
        mouse_pos = py.mouse.get_pos()
        left_click = py.mouse.get_pressed()[0]
        button_rect = py.rect.Rect((self.x_pos + 100, self.y_pos + 50),(200, 100))
        if left_click and button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False
        
    def hover(self):
        mouse_pos = py.mouse.get_pos()
        button_rect = py.rect.Rect((self.x_pos, self.y_pos),(400, 200))
        if button_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

def kage_MD():
 
    button_text = FONT.render(random.choice(Meget_dygtig), True, "black")   
    run = True    
    while run:
        
        WIN.blit(MegetBG, (0, 0))
        WIN.blit(button_text, (300, 350))
        Win_sfx.play()

        for event in py.event.get():
            if event.type == py.QUIT:
                Win_sfx.stop()
                run = False
                break
        
        py.display.update()

def kage_lidt():

    button_text = FONT.render(random.choice(Lidt), True, "black")   
    run = True    
    while run:
        
        WIN.blit(LidtBG, (0, 0))
        WIN.blit(button_text, (300, 350))

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break
        
        py.display.update()

def kage_suk():
    
    
    button_text = FONT.render(random.choice(Suk), True, "black")   
    run = True    
    while run:
        
        WIN.blit(SukBG, (0, 0))
        WIN.blit(button_text, (300, 350))

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break
        
        py.display.update()

def strafmild():
    
    button_text = StrafFont.render(random.choice(MStraf), True, "white")
    run = True    
    while run:
        
        WIN.blit(StrafValg, (0, 0))
        WIN.blit(button_text, (20, 350))
        
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break
        
        py.display.update()

def straf_hård():
    
    button_text = StrafFont.render(random.choice(HStraf), True, "white")
    run = True    
    while run:
        
        WIN.blit(StrafValg, (0, 0))
        WIN.blit(button_text, (20, 350))

        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break
        
        py.display.update()

def kage_menu():

    run = True    
    while run:

        WIN.blit(KageBG, (0, 0))
        Meget_dygtig1 = Button('Meget!!', 250, 175, True)
        Gode = Button('  Lidt', 250, 350, True)
        Suk = Button(' Suk...', 250, 525, True)
        
        
        if Meget_dygtig1.check_click():
            WIN.blit(Knap_Press, (250, 175))
            kage_MD()

        if Meget_dygtig1.hover():
            Kagetxt = FONT.render("Meget!!", True, "chartreuse")
            button_text = LilleFont.render("Godt valg!", True, "black")
            WIN.blit(button_text, (730, 250))
            WIN.blit(Knap_Press, (250, 175))
            WIN.blit(Kagetxt, (390, 225))

        if Gode.check_click():
            WIN.blit(Knap_Press, (250, 350))
            #Straf_sfx.play()
            kage_lidt()

        if Gode.hover():
            button_text1 = LilleFont.render("Aaarhhh, er du sikker?", True, "black")
            Straftxt = FONT.render("  Lidt", True, "chartreuse")
            WIN.blit(Knap_Press, (250, 350))
            WIN.blit(Straftxt, (390, 400))
            WIN.blit(button_text1, (100, 345))
        

        if Suk.check_click():
            WIN.blit(Knap_Press, (250, 525))
            #Straf_sfx.play()
            kage_suk()

        if Suk.hover():
            button_text1 = LilleFont.render("Har det været en lang dag?", True, "black")
            Straftxt = FONT.render(" Suk...", True, "chartreuse")
            WIN.blit(Knap_Press, (250, 525))
            WIN.blit(Straftxt, (390, 575))
            WIN.blit(button_text1, (250, 700))
        
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break
        
        py.display.update()
    
def straf_menu():
    run = True    
    while run:
        
        WIN.blit(StrafBG, (0, 0))
        HÅRD = Button('HÅRD!!', 30, 350, True)
        MILD = Button('Mild..', 480, 350, True)
      
        if HÅRD.check_click():
            WIN.blit(Knap_Press, (30, 350))
            #Kage_sfx.play()
            straf_hård()

        if HÅRD.hover():
            button_text = LilleFont.render("Robert, Kig lige væk...", True, "White")
            Kagetxt = FONT.render("HÅRD!!", True, "chartreuse")
            WIN.blit(button_text, (320, 600))
            WIN.blit(Knap_Press, (30, 350))
            WIN.blit(Kagetxt, (170, 400))

        if MILD.check_click():
            Straftxt = FONT.render("Mild..", True, "chartreuse")
            WIN.blit(Knap_Press, (480, 350))
            WIN.blit(Straftxt, (620, 400))
            #Straf_sfx.play()
            strafmild()

        if MILD.hover():
            Straftxt = FONT.render("Mild..", True, "chartreuse")
            button_text1 = LilleFont.render("Nu du kedelig..", True, "White")
            WIN.blit(button_text1, (350, 600))
            WIN.blit(Knap_Press, (480, 350))
            WIN.blit(Straftxt, (620, 400))
        
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break
        
        py.display.update()

def main_menu():

    run = True    
    while run:
        WIN.blit(BG, (0, 0))
        Hvadvildu = StorFont.render (f"Hvad vil du?", 1, "black")
        WIN.blit(Hvadvildu, (260, 370))
        Kageknap = Button('Kage?', 30, 500, True)
        Strafknap = Button('Straf?', 480, 500, True)  
        

        if Kageknap.check_click():
            WIN.blit(Knap_Press, (30, 500))
            Kage_sfx.play()
            kage_menu()

        if Kageknap.hover():
            button_text = LilleFont.render("WILLIAM! Hold op med det der!", True, "black")
            Kagetxt = FONT.render("Kage?", True, "chartreuse")
            WIN.blit(button_text, (200, 690))
            WIN.blit(Knap_Press, (30, 500))
            WIN.blit(Kagetxt, (170, 550))

        if Strafknap.check_click():
            WIN.blit(Knap_Press, (480, 500))
            Straf_sfx.play()
            straf_menu()

        if Strafknap.hover():
            Straftxt = FONT.render("Straf?", True, "chartreuse")
            button_text1 = LilleFont.render("Er det til en fra Næstved?", True, "black")
            WIN.blit(button_text1, (250, 690))
            WIN.blit(Knap_Press, (480, 500))
            WIN.blit(Straftxt, (620, 550))

       
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
                break
           
                
        py.display.update()

    py.quit()
    
main_menu()