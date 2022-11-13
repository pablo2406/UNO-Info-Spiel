
import random
from PIL import Image, ImageTk #Bibliotheken

from helper import get_photo_image
from random import choice
from time import sleep

class Karte: #Erstellung von Klasse Karte mit Attributen

    def __init__(self, number, color):

        self.number = number
        self.color = color
        self.width = 163
        self.height = 237
        self.get_bild()
        

    def get_bild(self): 

        color_to_str = {  #Farben in Form von Werten werden in Namen umgewandelt
            0: "BLAU",
            1: "ROT",
            2: "GELB",
            3: "GRUEN"
        }

        path = "UNO Karten/Karten " + color_to_str[self.color] + "/UNO Nummer \"" + str(self.number) + "\".jpg"
        self.bild = get_photo_image(path, (self.width, self.height)) #Variable mit Dateipfad für mehrmalige Verwendung
		
		
class Kartenhand: #Erstellung Klasse Kartenhand mit Attributen 

    def __init__(self, anzahl):

        self.karten = []
        self.karten_holen(anzahl)


    def karten_holen(self, anzahl): #Methode, die Liste füllt

      for _ in range(anzahl):
          self.karten.append(Karte(random.randint(0,4), random.randint(0,3))) #Liste wird ergänzt mit Karten(Wert,Farbe)


    def laenge(self):
        return len(self.karten)


class Spiel:

    def __init__(self, anzahl: int, gui) -> None: #Konstruktor mit Anzahl der Karten, Referenz auf Gui (Guidatei)

        self.gui = gui

        self.spieler_hand = Kartenhand(anzahl)
        self.cpu_hand = Kartenhand(anzahl)
        self.gelegte_karte = None        
        self.spieler_an_der_reihe = True   #Spieler Beginnt den Zug

        self.gui.initialize_hands(self.spieler_hand)


    def kann_legen(self, hand) -> bool: #Methode zur Prüfung von der Möglichkeit zu legen

        if self.gelegte_karte is None: return True
        
        for karte in hand.karten:
            if karte.number == self.gelegte_karte.number or karte.color == self.gelegte_karte.color: #Es wird bestimmt, was auf was gelegt werden darf
                return True
                
        return False #Wenn legen nicht mehr möglich, gibt falsch zurück


    def spieler_legen(self) -> bool:

        karten_index = self.gui.zuletzt_geklickte_karte_ind 
        self.gui.zuletzt_geklickte_karte_ind = None #Index wird auf "None" zurückgesetzt, sodass man wieder legen darf

        gewaehlte_karte = self.spieler_hand.karten[karten_index] #Aus dem Index wird eine Karte gewählt (gewählte Karte)
        
	#Bedingung, um zu prüfen ob gewählte Karte auf gelegte Karte möglich ist
        if (self.gelegte_karte == None or gewaehlte_karte.number == self.gelegte_karte.number or gewaehlte_karte.color == self.gelegte_karte.color):
            
            self.gelegte_karte = gewaehlte_karte 
            self.spieler_hand.karten.pop(karten_index)

            self.gui.lege_spieler_karte(karten_index)

            return True

        else: #wenn Bedingung nicht true, dann false (geht nicht)

            return False


    def cpu_legen(self) -> None: #Algorithmus, der bestimmt, welche Karte gespielt wird

        #Liste an möglichen Karten, die gelegt werden können
        self.gelegte_karte = choice([karte for karte in self.cpu_hand.karten if karte.number == self.gelegte_karte.number or karte.color == self.gelegte_karte.color])
        self.cpu_hand.karten.remove(self.gelegte_karte) #gelegte Karte wird aus der CPU Hand entfernt

        self.gui.lege_cpu_karte(self.gelegte_karte) #gelegte Karte in GUI entfernt (Anzahl Rückseite Karte - 1)

    
    def spielen(self, root, frame_laenge): #Methode, die den Spielablauf bestimmt

        root.after(frame_laenge, lambda fl=frame_laenge: self.spielen(root, fl)) #Bilder die Sekunde

        if self.spieler_hand.laenge() > 0 and self.cpu_hand.laenge() > 0:
            
            if self.spieler_an_der_reihe:

                if self.kann_legen(self.spieler_hand): 

                    if self.gui.zuletzt_geklickte_karte_ind is not None and self.spieler_legen(): #Wenn Spieler legbare Karte angeklickt hat

                        self.spieler_an_der_reihe = not self.spieler_an_der_reihe #Änderung zu CPU an der Reihe

                else: 
                    pass #Hier würde Spieler nachziehen

            else: 

                if self.kann_legen(self.cpu_hand):

                    sleep(0.5) #Wartet eine halbe Sekunde bevor CPU legt (Delay)
                    self.cpu_legen() #CPU legt Karte
                    self.spieler_an_der_reihe = not self.spieler_an_der_reihe #Wechsel von CPU auf Spieler an der Reihe

                else: 
                    pass #Hier würde CPU nachziehen


        


# Nummern 0-4, Farben: Blau = 0, 
#                      Rot  = 1,
#                      Gelb = 2,
#                      Gruen = 3,


