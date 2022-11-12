
import tkinter as tk
from PIL import Image, ImageTk #Zusatzbibliothek, um verschiede Bilddateiformate zu nutzen (python imaging library)

from GUI import GUI
from Spiel import Karte, Kartenhand, Spiel

def main(): #Erstellung von Spielfläche mit angegebenen Maßen
    
    root = tk.Tk()
    root.title("UNO Spiel")
    root.attributes('-fullscreen',True)
    root.geometry("1920x1080")
    
    main_canvas = tk.Canvas(master=root, bg ='#006600') #Erstellung Canvas-Element um grafische Möglichkeiten zu haben
    main_canvas.pack(fill="both", expand=True)

    gui = GUI(main_canvas) #Angeben wo sich die Gui befinden soll
    game = Spiel(6, gui)

    bilder_pro_sekunde = 60
    game.spielen(root, int(1000 / bilder_pro_sekunde)) #Angabe wie oft geupdatet wird (fps)

    root.mainloop()


if __name__ == "__main__":
    main()
