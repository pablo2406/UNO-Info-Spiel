
import tkinter as tk
from helper import get_photo_image

from Spiel import Karte

class GUI: #Erstellung Klasse GUI mit Attributen

    def __init__(self, canvas) -> None: 

        self.canvas = canvas

        self.spieler_karten = []
        self.cpu_karten = []
        self.gelegte_karte = None

        self.zuletzt_geklickte_karte_ind = None

        self.create_static_elements()


    def initialize_hands(self, spieler_hand) -> None:  #Spielerhand und CPU-Hand wird erstellt mit Position

        HAND_LAENGE = len(spieler_hand.karten) #Anzahl der Karten in der Spielerhand, um Position zu bestimmen
        self.KARTEN_OVERLAP = 75 #Karten sollen übereinander liegen
        HAENDE_X_POSITION = (1920 / 2) - ((HAND_LAENGE - 1) * self.KARTEN_OVERLAP) / 2 #Position Spielerhand X-Achse 
        self.SPIELER_HAND_Y_POSITION = 1080 - spieler_hand.karten[0].height * 0.75 #Position Spielerhand Y-Achse
        self.CPU_HAND_Y_POSITION = spieler_hand.karten[0].height * 0.75 # Position Y-Achse CPU-Hand


        for karte_index in range(HAND_LAENGE):

            new_x = HAENDE_X_POSITION + karte_index * self.KARTEN_OVERLAP #X-Achse Position abhängig von den Karten in der Hand

            image = self.canvas.create_image(new_x, self.SPIELER_HAND_Y_POSITION, image=spieler_hand.karten[karte_index].bild)
            self.spieler_karten.append(image) #Image in Canvas als Platzhalter für Spielerkarten

            self.canvas.tag_bind(image, "<Button-1>", lambda event, img=image: self.click_aktualisieren(img))
            #Man möchte ein Event herbeiführen indem man ein Klick tätigt
        

        self.backside_image = get_photo_image("UNO Karten/UNO Karte Rückseite.jpg", (spieler_hand.karten[0].width, spieler_hand.karten[0].height))
           #Kartenrückseite für die CPU-Hand bestimmen mit Dateipfad
        for karte_index in range(HAND_LAENGE):

            new_x = HAENDE_X_POSITION + karte_index * self.KARTEN_OVERLAP

            image = self.canvas.create_image(new_x, self.CPU_HAND_Y_POSITION, image=self.backside_image)
            self.cpu_karten.append(image) #Position vom Image in Canvas für CPU-Karten Rückseiten

    
    def click_aktualisieren(self, image) -> None:

        if self.zuletzt_geklickte_karte_ind is not None: return

        self.zuletzt_geklickte_karte_ind = self.spieler_karten.index(image)


    def lege_spieler_karte(self, index) -> None:

        self.canvas.delete(self.gelegte_karte)

        self.gelegte_karte = self.spieler_karten.pop(index)

        ablage_coords = self.canvas.coords(self.ablageflaeche)[:2]
        self.canvas.moveto(self.gelegte_karte, ablage_coords[0] - 81, ablage_coords[1] - 118)
        self.spieler_hand_position_aktualisieren()


    def lege_cpu_karte(self, cpu_karte) -> None:

        self.canvas.delete(self.gelegte_karte)

        ablage_coords = self.canvas.coords(self.ablageflaeche)[:2]
        self.gelegte_karte = self.canvas.create_image(ablage_coords[0], ablage_coords[1], image=cpu_karte.bild)

        self.canvas.delete(self.cpu_karten[-1])
        self.cpu_karten.pop(-1)

        self.cpu_hand_position_aktualisieren()


    def spieler_hand_position_aktualisieren(self) -> None:

        HAND_LAENGE = len(self.spieler_karten)
        HAENDE_X_POSITION = (1920 / 2) - ((HAND_LAENGE - 1) * self.KARTEN_OVERLAP) / 2

        for karte_index in range(HAND_LAENGE):

            new_x = HAENDE_X_POSITION + karte_index * self.KARTEN_OVERLAP
            self.canvas.moveto(self.spieler_karten[karte_index], new_x - 81, self.SPIELER_HAND_Y_POSITION - 118)


    def cpu_hand_position_aktualisieren(self) -> None:

        HAND_LAENGE = len(self.cpu_karten)
        HAENDE_X_POSITION = (1920 / 2) - ((HAND_LAENGE - 1) * self.KARTEN_OVERLAP) / 2

        for karte_index in range(HAND_LAENGE):

            new_x = HAENDE_X_POSITION + karte_index * self.KARTEN_OVERLAP
            self.canvas.moveto(self.cpu_karten[karte_index], new_x - 81, self.CPU_HAND_Y_POSITION - 118)


    def create_static_elements(self) -> None:

        self.ablage_image = get_photo_image("UNO Karten/UNO Ablegefläche.jpg", (200, 275))
        self.ablageflaeche = self.canvas.create_image((1920 / 2) + 300, (1080 / 2), image=self.ablage_image)

        self.deck_image = get_photo_image("UNO Karten/UNO Karte Rückseite .jpg", (163, 237))
        self.canvas.create_image((1920 / 2) - 300, (1080 / 2), image=self.deck_image)


    def update_player_card_pos(self) -> None:

        # auf Basis von Anzahl der Karten neue Positionen ausrechnen
        # Positionen updaten -> self.canvas.move(id_von_Karte, x_difference, y_difference) oder move_to()

        

        pass
