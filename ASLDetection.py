from tkinter import *
from tkinter import ttk
import customtkinter
import time
from set_histogram import *
#from gesturecreate import *
#from keras_trainingmodel import *
#from report import *
#from final import *

def showloadingscreen():
    loading_screen = Tk()
    loading_screen.title("Loading")
    loading_screen.geometry("400x100")
    loading_screen.resizable(False, False)
    loading_screen.configure(bg="black")
    loading_screen.overrideredirect(True)
    screen_width = loading_screen.winfo_screenwidth() # Get the screen width and height
    screen_height = loading_screen.winfo_screenheight()
    x = int(screen_width/2 - 150)     # Calculate the x and y coordinates to center the loading screen on the screen
    y = int(screen_height/2 - 50)
    loading_screen.geometry("+{}+{}".format(x, y)) # Set the position of the loading screen
    name_label = Label(loading_screen, text="SIGN LANGUAGE\nDETECTION", font=("AkiraExpanded-SuperBold", 20), fg="white", bg="black")
    name_label.pack(pady=1, anchor="center")
    label = Label(loading_screen, text="Loading...", font=("8514oem", 12), fg="white", bg="black")
    label.pack(pady=1, anchor="center")
    loading_screen.update()
    time.sleep(3) # Simulate loading process
    loading_screen.destroy()
    time.sleep(0.5) #Delay after loading

#showloadingscreen()

App = customtkinter.CTk()
App.geometry("500x500")
App.title("ASL")
App.config(bg="#000000")
set_histbtn = customtkinter.CTkButton(master = App, text = "Set Histogram",font=("Helvetica",15), width=15, command = get_hand_hist)
set_histbtn.configure(highlightbackground="#000000")
set_histbtn.place(x=150,y=100)

App.mainloop()