
import random
from PIL import Image, ImageTk

from helper import get_photo_image
from random import choice
from time import sleep

class Karte:

    def __init__(self, number, color):

        self.number = number
        self.color = color
        self.width = 163
        self.height = 237
        self.get_bild()
        

    def get_bild(self):

        color_to_str = { 
            0: "BLAU",
            1: "ROT",
            2: "GELB",
            3: "GRUEN"
        }

        path = "UNO Karten/Karten " + color_to_str[self.color] + "/UNO Nummer \"" + str(self.number) + "\".jpg"
        self.bild = get_photo_image(path, (self.width, self.height))
		
		
class Kartenhand:

    def __init__(self, anzahl):

        self.karten = []
        self.karten_holen(anzahl)


    def karten_holen(self, anzahl):

      for _ in range(anzahl):
          self.karten.append(Karte(random.randint(0,4), random.randint(0,3)))


    def laenge(self):
        return len(self.karten)


class Spiel:

    def __init__(self, anzahl: int, gui) -> None:

        self.gui = gui

        self.spieler_hand = Kartenhand(anzahl)
        self.cpu_hand = Kartenhand(anzahl)
        self.gelegte_karte = None
        self.spieler_an_der_reihe = True 

        self.gui.initialize_hands(self.spieler_hand)


    def kann_legen(self, hand):

        if self.gelegte_karte is None: return True
        
        for karte in hand.karten:
            if karte.number == self.gelegte_karte.number or karte.color == self.gelegte_karte.color:
                return True
                
        return False 


    def spieler_legen(self) -> bool:

        karten_index = self.gui.zuletzt_geklickte_karte_ind
        self.gui.zuletzt_geklickte_karte_ind = None

        gewaehlte_karte = self.spieler_hand.karten[karten_index]

        if (self.gelegte_karte == None or gewaehlte_karte.number == self.gelegte_karte.number or gewaehlte_karte.color == self.gelegte_karte.color):

            self.gelegte_karte = gewaehlte_karte
            self.spieler_hand.karten.pop(karten_index)

            self.gui.lege_spieler_karte(karten_index)

            return True

        else:

            return False


    def cpu_legen(self) -> None:

        self.gelegte_karte = choice([karte for karte in self.cpu_hand.karten if karte.number == self.gelegte_karte.number or karte.color == self.gelegte_karte.color])
        self.cpu_hand.karten.remove(self.gelegte_karte)

        self.gui.lege_cpu_karte(self.gelegte_karte)

    
    def spielen(self, root, frame_laenge):

        root.after(frame_laenge, lambda fl=frame_laenge: self.spielen(root, fl))

        if self.spieler_hand.laenge() > 0 and self.cpu_hand.laenge() > 0:
            
            if self.spieler_an_der_reihe:

                if self.kann_legen(self.spieler_hand): 

                    if self.gui.zuletzt_geklickte_karte_ind is not None and self.spieler_legen():

                        self.spieler_an_der_reihe = not self.spieler_an_der_reihe

                else: 
                    pass # spieler zieht Karte

            else: 

                if self.kann_legen(self.cpu_hand): 

                    sleep(0.5)
                    self.cpu_legen()
                    self.spieler_an_der_reihe = not self.spieler_an_der_reihe

                else: 
                    pass # cpu zieht Karte


        
# naechste(r) Schritt(e) :
        # Kartenhand mal 2
        # Bereich festlegen, wo sich Karten treffen (geupdateter Platz auf Feld)
        # number, color Objekten - Bilder zuweisen? Check!!
        # Klasse(n) Spiellogik -> pr\u00fcfen ob Farbe oder Zahl liegt,
                              # bzw. schauen ob \u00fcberhaupt gelegt werden kann


# Nummern 0-4, Farben: Blau = 0, 
#                      Rot  = 1,
#                      Gelb = 2,
#                      Gruen = 3,


