import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from view.listagem_cultura import ListagemCulturas
from view.listagem_plantas import ListagemPlantas
from view.sobre import Sobre


class Menu(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Sistema de Gestão de Culturas")
        self.geometry("400x300")
        self.resizable(False, False)
        self._build()

    def _build(self):
       
        frame = tk.Frame(self)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            frame,
            text="Sistema de Gestão de Culturas",
            font=("Arial", 14, "bold")
        ).pack(pady=(0, 20))

        tk.Button(
            frame,
            text="Plantas",
            width=20,
            height=2,
            command=lambda: ListagemPlantas(self)
        ).pack(pady=5)

        tk.Button(
            frame,
            text="Culturas",
            width=20,
            height=2,
            command=lambda: ListagemCulturas(self)
        ).pack(pady=5)

        tk.Button(
            frame,
            text="Sobre",
            width=20,
            height=2,
            command=lambda: Sobre(self)
        ).pack(pady=5)


