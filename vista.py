import tkinter as tk
from main import *


class MiAplicacion(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title('Don\'t Play League')
        self.geometry('300x200')
        self.configure(bg='lightgreen')
        # Composición
        self.widget = Boton(self)
        self.widget.pack()
        self.label = tk.Label(self, text="", bg='white', fg='black', font=('Arial', 12))
        self.label.pack(pady=10)


class Boton(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg='blue')
        # evento
        self.button = tk.Button(self, text="Iniciar contador!", command=self.saludar_ya, bg='lightblue')
        self.button.pack(pady=10)


    def saludar_ya(self):
        count_time()
        app.label.config(text=count_time())


app = MiAplicacion()
app.mainloop()
