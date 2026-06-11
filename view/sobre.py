import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk


class Sobre(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Sobre")
        self.geometry("800x500")
        self.resizable(False, False)
        self.grab_set()

        self.construir()

    def construir(self):
        frame = tk.Frame(self, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            frame,
            text="Sistema de Gestão de Culturas",
            font=("Arial", 13, "bold")
        ).pack(pady=(0, 10))

        tk.Label(
            frame,
            text="Descrição: Este sistema foi desenvolvido para auxiliar agricultores " \
            "e gestores agrícolas a monitorar e gerenciar suas culturas de forma eficiente. " \
            "Ele oferece funcionalidades como cadastro de culturas, " \
            "plantas disponíveis para plantio dependendo da época bem " \
            "como ter um controle do que e quando foi plantado/colhido," \
            " o que ajuda na hora das rotações de culturas." \
            "Desenvolvi esse sistema com base em minha vivência própia, onde desde pequeno vivi em uma propriedade rural" \
            " e sempre tive interesse em tecnologia," \
            " então decidi unir as duas coisas e criar um sistema que pudesse ajudar outros" \
            " agricultores a gerenciar suas culturas de forma mais eficiente.",
            font=("Arial", 10),
            wraplength=340,
            justify="center"
        ).pack(pady=(0, 20))

        tk.Label(
            frame,
            text="Desenvolvido por: Matheus Witte Ditz, " \
            "estudante no 3° ano de Ciências da Computação no IFSUL de Passo Fundo RS.",
            font=("Arial", 10, "bold")
        ).pack()

        tk.Label(
            frame,
            text="Curso: Bacharelado em Ciência da Computação",
            font=("Arial", 10)
        ).pack(pady=(5, 0))

        tk.Label(
            frame,
            text="Disciplina: LPOO — 2026/1",
            font=("Arial", 10)
        ).pack()

        tk.Button(
            frame,
            text="Fechar",
            width=12,
            command=self.destroy
        ).pack(pady=(20, 0))