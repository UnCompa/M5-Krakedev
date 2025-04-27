import random
import tkinter as tk
from tkinter import ttk
from laptop import Laptop_Business
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.laptops = []
        self.imagenes = ['C:\\Users\Santiago Mosquera\\Documents\\M5-KRAKEDEV\\EVIDENCIA RETOS\\Reto 9\\imgs\\laptop1.jpg','C:\\Users\Santiago Mosquera\\Documents\\M5-KRAKEDEV\\EVIDENCIA RETOS\\Reto 9\\imgs\\laptop2.jpg']
        self.root.title("Laptop - Datos")
        self.setup_ui()
        
    def setup_ui(self):
        ttk.Label(self.root, text="Marca").grid(row=0,column=0)
        self.marca = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.marca).grid(row=0,column=1)
        ttk.Label(self.root, text="Procesador").grid(row=1,column=0)
        self.procesador = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.procesador).grid(row=1,column=1)
        ttk.Label(self.root, text="Memoria").grid(row=2,column=0)
        self.memoria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.memoria).grid(row=2,column=1)
        ttk.Label(self.root, text="Costo").grid(row=3,column=0)
        self.costo = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.costo).grid(row=3,column=1)
        ttk.Label(self.root, text="Impuestos").grid(row=4,column=0)
        self.impuesto = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.impuesto).grid(row=4,column=1)
        ttk.Label(self.root, text="Almacenamiento").grid(row=5,column=0)
        self.almacenamiento = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.almacenamiento).grid(row=5,column=1)
        ttk.Label(self.root, text="Duracion bateria").grid(row=6,column=0)
        self.duracion_bateria = tk.StringVar()
        ttk.Entry(self.root, textvariable=self.duracion_bateria).grid(row=6,column=1)
        ttk.Button(self.root, text="Agregar Laptop", command=self.agregar_laptop).grid(row=7,column=0,columnspan=2)
        self.mostrar_laptops = tk.Text(self.root, height=10, width=50)
        self.mostrar_laptops.grid(row=8, column=0, columnspan=2)
        self.canva = tk.Canvas(self.root, width=500, height=500)
        self.canva.grid(row=9, column=0, columnspan=2)
        pass
    def agregar_laptop(self):
        nueva_laptop = Laptop_Business(self.marca.get(), self.procesador.get(), self.memoria.get(), self.costo.get(), self.impuesto.get(), self.almacenamiento.get(), self.duracion_bateria.get())
        self.laptops.append(nueva_laptop)
        self.mostrar_laptops.insert(tk.END, f'{nueva_laptop}')
        self.mostrar_imagenes()
    def mostrar_imagenes(self):
        imagen_path = random.choice(self.imagenes)
        image = Image.open(imagen_path)
        image = image.resize((500, 500), Image.Resampling.LANCZOS)
        imageTk = ImageTk.PhotoImage(image)
        self.canva.create_image(0, 0, anchor=tk.NW, image=imageTk)
        self.canva.image = imageTk

root = tk.Tk()
app = App(root)
root.mainloop()