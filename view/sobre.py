import tkinter as tk


class Sobre(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Sobre")
        self.geometry("400x300")
        self.resizable(False, False)
        self.grab_set()

        self._build()

    def _build(self):
        frame = tk.Frame(self, padx=20, pady=20)
        frame.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(
            frame,
            text="Sistema de Gestão de Culturas",
            font=("Arial", 13, "bold")
        ).pack(pady=(0, 10))

        tk.Label(
            frame,
            text="Descrição do sistema aqui.",
            font=("Arial", 10),
            wraplength=340,
            justify="center"
        ).pack(pady=(0, 20))

        tk.Label(
            frame,
            text="Desenvolvido por:",
            font=("Arial", 10, "bold")
        ).pack()

        tk.Label(
            frame,
            text="Seu Nome Aqui",
            font=("Arial", 10)
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