import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from tkinter import ttk, messagebox
from controller.cultura_control import CulturaController
from model.status_cultura_enum import StatusCultura
from view.formulario_cultura import FormCultura


class ListagemCulturas(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Culturas")
        self.geometry("900x400")
        self.controller = CulturaController()

        self._build_tabela()
        self._build_botoes()
        self._carregar()

   

    def _build_tabela(self):
        colunas = ("id", "planta", "tipo", "estacao", "status", "plantio", "colheita")
        self.tabela = ttk.Treeview(self, columns=colunas, show="headings")

        self.tabela.heading("id",       text="ID")
        self.tabela.heading("planta",   text="Planta")
        self.tabela.heading("tipo",     text="Tipo")
        self.tabela.heading("estacao",  text="Estação")
        self.tabela.heading("status",   text="Status")
        self.tabela.heading("plantio",  text="Data Plantio")
        self.tabela.heading("colheita", text="Data Colheita")

        self.tabela.column("id",       width=40,  anchor="center")
        self.tabela.column("planta",   width=180)
        self.tabela.column("tipo",     width=100, anchor="center")
        self.tabela.column("estacao",  width=100, anchor="center")
        self.tabela.column("status",   width=100, anchor="center")
        self.tabela.column("plantio",  width=110, anchor="center")
        self.tabela.column("colheita", width=110, anchor="center")

        scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=scroll.set)

        self.tabela.pack(side="left", fill="both", expand=True)
        scroll.pack(side="left", fill="y")

        self.tabela.bind("<<TreeviewSelect>>", self._ao_selecionar)

    
    def _build_botoes(self):
        frame = tk.Frame(self)
        frame.pack(side="right", fill="y", padx=10, pady=10)

        tk.Button(frame, text="Nova",    width=15, command=self._nova).pack(pady=3)
        tk.Button(frame, text="Editar",  width=15, command=self._editar).pack(pady=3)
        tk.Button(frame, text="Excluir", width=15, command=self._excluir).pack(pady=3)

        self.btn_plantar = tk.Button(frame, text="Plantar", width=15,
                                     command=self._plantar, state="disabled")
        self.btn_plantar.pack(pady=3)

        self.btn_colher = tk.Button(frame, text="Colher", width=15,
                                    command=self._colher, state="disabled")
        self.btn_colher.pack(pady=3)

   
    def _carregar(self):
        for row in self.tabela.get_children():
            self.tabela.delete(row)

        sucesso, culturas = self.controller.listar()
        if not sucesso:
            messagebox.showerror("Erro", culturas, parent=self)
            return

        for c in culturas:
            estacao = c.estacao.value if hasattr(c, "estacao") else "-"
            status  = c.status.value  if c.status else "-"
            plantio  = c.data_plantio.strftime("%d/%m/%Y")  if c.data_plantio  else "-"
            colheita = c.data_colheita.strftime("%d/%m/%Y") if c.data_colheita else "-"

            self.tabela.insert("", "end", iid=c.id, values=(
                c.id, c.planta.nome,
                "Ano Todo" if not hasattr(c, "estacao") else "Estação",
                estacao, status, plantio, colheita
            ))

    def _ao_selecionar(self, event):
        selecionado = self._get_selecionado()
        if selecionado is None:
            return

        status = selecionado[4]  

       
        if status == StatusCultura.COLHIDO.value:
            self.btn_plantar.config(state="disabled")
            self.btn_colher.config(state="disabled")
        elif status == StatusCultura.PLANTADO.value:
            self.btn_plantar.config(state="disabled")
            self.btn_colher.config(state="normal")
        else:  # sem status
            self.btn_plantar.config(state="normal")
            self.btn_colher.config(state="disabled")

   
    def _get_id_selecionado(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma cultura.", parent=self)
            return None
        return int(selecionado[0])

    def _get_selecionado(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            return None
        return self.tabela.item(selecionado[0])["values"]

    def _nova(self):
      
        form = FormCultura(self)
        
        self.wait_window(form)
        self._carregar()

    def _editar(self):
        id_ = self._get_id_selecionado()
        if id_ is None:
            return
       
        form = FormCultura(self, cultura_id=id_)
       
        self.wait_window(form)
        self._carregar()

        
    def _excluir(self):
        id_ = self._get_id_selecionado()
        if id_ is None:
            return
        if not messagebox.askyesno("Confirmar", "Deseja excluir esta cultura?", parent=self):
            return
        sucesso, msg = self.controller.deletar(id_)
        if sucesso:
            messagebox.showinfo("Sucesso", msg, parent=self)
            self._carregar()
        else:
            messagebox.showerror("Erro", msg, parent=self)

    def _plantar(self):
        id_ = self._get_id_selecionado()
        if id_ is None:
            return
        sucesso, msg = self.controller.plantar(id_)
        if sucesso:
            messagebox.showinfo("Sucesso", msg, parent=self)
            self._carregar()
        else:
            messagebox.showerror("Erro", msg, parent=self)

    def _colher(self):
        id_ = self._get_id_selecionado()
        if id_ is None:
            return
        sucesso, msg = self.controller.colher(id_)
        if sucesso:
            messagebox.showinfo("Sucesso", msg, parent=self)
            self._carregar()
        else:
            messagebox.showerror("Erro", msg, parent=self)