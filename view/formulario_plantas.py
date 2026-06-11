import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from tkinter import ttk, messagebox
from controller.planta_control import PlantaController
from model.tipocultura_enum import TipoCultura


class FormPlanta(tk.Toplevel):

    def __init__(self, parent, planta_id=None):
        super().__init__(parent)
        self.title("Nova Planta" if planta_id is None else "Editar Planta")
        self.resizable(False, False)
        self.grab_set()

        self.controller = PlantaController()
        self.planta_id = planta_id

        self._build_form()

        if planta_id:
            self._preencher_edicao()

   

    def _build_form(self):
        pad = {"padx": 10, "pady": 5}

        
        tk.Label(self, text="Nome *").grid(row=0, column=0, sticky="w", **pad)
        self.nome_var = tk.StringVar()
        tk.Entry(self, textvariable=self.nome_var, width=35).grid(row=0, column=1, **pad)

       
        tk.Label(self, text="Nome Científico *").grid(row=1, column=0, sticky="w", **pad)
        self.nome_cientifico_var = tk.StringVar()
        tk.Entry(self, textvariable=self.nome_cientifico_var, width=35).grid(row=1, column=1, **pad)

        
        tk.Label(self, text="Descrição").grid(row=2, column=0, sticky="nw", **pad)
        self.descricao_text = tk.Text(self, width=35, height=4)
        self.descricao_text.grid(row=2, column=1, **pad)

        
        tk.Label(self, text="Tipo *").grid(row=3, column=0, sticky="w", **pad)
        self.tipo_var = tk.StringVar()
        self.combo_tipo = ttk.Combobox(
            self,
            textvariable=self.tipo_var,
            values=[t.value for t in TipoCultura],
            state="readonly",
            width=33
        )
        self.combo_tipo.grid(row=3, column=1, **pad)

       
        tk.Label(self, text="Nota Verão (0-10) *").grid(row=4, column=0, sticky="w", **pad)
        self.nota_verao_var = tk.StringVar()
        tk.Entry(self, textvariable=self.nota_verao_var, width=35).grid(row=4, column=1, **pad)

        tk.Label(self, text="Nota Outono (0-10) *").grid(row=5, column=0, sticky="w", **pad)
        self.nota_outono_var = tk.StringVar()
        tk.Entry(self, textvariable=self.nota_outono_var, width=35).grid(row=5, column=1, **pad)

        tk.Label(self, text="Nota Inverno (0-10) *").grid(row=6, column=0, sticky="w", **pad)
        self.nota_inverno_var = tk.StringVar()
        tk.Entry(self, textvariable=self.nota_inverno_var, width=35).grid(row=6, column=1, **pad)

        tk.Label(self, text="Nota Primavera (0-10) *").grid(row=7, column=0, sticky="w", **pad)
        self.nota_primavera_var = tk.StringVar()
        tk.Entry(self, textvariable=self.nota_primavera_var, width=35).grid(row=7, column=1, **pad)

        # --- Botões ---
        frame_botoes = tk.Frame(self)
        frame_botoes.grid(row=8, column=0, columnspan=2, pady=10)
        tk.Button(frame_botoes, text="Salvar",   width=15, command=self._salvar).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Cancelar", width=15, command=self.destroy).pack(side="left", padx=5)

   

    def _validar(self):
        if not self.nome_var.get().strip():
            messagebox.showerror("Erro", "Nome é obrigatório.", parent=self)
            return False
        if not self.nome_cientifico_var.get().strip():
            messagebox.showerror("Erro", "Nome científico é obrigatório.", parent=self)
            return False
        if not self.tipo_var.get():
            messagebox.showerror("Erro", "Tipo é obrigatório.", parent=self)
            return False
        for campo, var in [
            ("Nota Verão",     self.nota_verao_var),
            ("Nota Outono",    self.nota_outono_var),
            ("Nota Inverno",   self.nota_inverno_var),
            ("Nota Primavera", self.nota_primavera_var),
        ]:
            valor = var.get().strip()
            if not valor:
                messagebox.showerror("Erro", f"{campo} é obrigatória.", parent=self)
                return False
            try:
                n = float(valor)
                if n < 0 or n > 10:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Erro", f"{campo} deve ser um número entre 0 e 10.", parent=self)
                return False
        return True

   

    def _salvar(self):
        if not self._validar():
            return

        nome            = self.nome_var.get().strip()
        nome_cientifico = self.nome_cientifico_var.get().strip()
        descricao       = self.descricao_text.get("1.0", "end").strip()
        tipo            = self.tipo_var.get()
        nota_verao      = self.nota_verao_var.get().strip()
        nota_outono     = self.nota_outono_var.get().strip()
        nota_inverno    = self.nota_inverno_var.get().strip()
        nota_primavera  = self.nota_primavera_var.get().strip()

        if self.planta_id is None:
            sucesso, msg = self.controller.cadastrar(
                nome, nome_cientifico, descricao, tipo,
                nota_inverno, nota_verao, nota_primavera, nota_outono
            )
        else:
            sucesso, msg = self.controller.atualizar(
                self.planta_id, nome, nome_cientifico, descricao, tipo,
                nota_inverno, nota_verao, nota_primavera, nota_outono
            )

        if sucesso:
            messagebox.showinfo("Sucesso", msg, parent=self)
            self.destroy()
        else:
            messagebox.showerror("Erro", msg, parent=self)

   
    def _preencher_edicao(self):
        sucesso, planta = self.controller.buscar_por_id(self.planta_id)
        if not sucesso:
            messagebox.showerror("Erro", planta, parent=self)
            self.destroy()
            return

        self.nome_var.set(planta.nome)
        self.nome_cientifico_var.set(planta.nome_cientifico)
        self.descricao_text.insert("1.0", planta.descricao or "")
        self.tipo_var.set(planta.tipo.value)
        self.nota_verao_var.set(planta.nota_verao)
        self.nota_outono_var.set(planta.nota_outono)
        self.nota_inverno_var.set(planta.nota_inverno)
        self.nota_primavera_var.set(planta.nota_primavera)