import tkinter as tk
from tkinter import ttk, messagebox
from controller.planta_control import PlantaController
from view.formulario_plantas import FormPlanta


class ListagemPlantas(tk.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)
        self.title("Plantas")
        self.geometry("850x400")
        self.controller = PlantaController()

        self._build_tabela()
        self._build_botoes()
        self._carregar()

   
    def _build_tabela(self):
        colunas = ("id", "nome", "nome_cientifico", "tipo",
                   "nota_verao", "nota_outono", "nota_inverno", "nota_primavera")
        self.tabela = ttk.Treeview(self, columns=colunas, show="headings")

        self.tabela.heading("id",              text="ID")
        self.tabela.heading("nome",            text="Nome")
        self.tabela.heading("nome_cientifico", text="Nome Científico")
        self.tabela.heading("tipo",            text="Tipo")
        self.tabela.heading("nota_verao",      text="Verão")
        self.tabela.heading("nota_outono",     text="Outono")
        self.tabela.heading("nota_inverno",    text="Inverno")
        self.tabela.heading("nota_primavera",  text="Primavera")

        self.tabela.column("id",              width=40,  anchor="center")
        self.tabela.column("nome",            width=160)
        self.tabela.column("nome_cientifico", width=160)
        self.tabela.column("tipo",            width=100, anchor="center")
        self.tabela.column("nota_verao",      width=60,  anchor="center")
        self.tabela.column("nota_outono",     width=60,  anchor="center")
        self.tabela.column("nota_inverno",    width=60,  anchor="center")
        self.tabela.column("nota_primavera",  width=80,  anchor="center")

        scroll = ttk.Scrollbar(self, orient="vertical", command=self.tabela.yview)
        self.tabela.configure(yscrollcommand=scroll.set)

        self.tabela.pack(side="left", fill="both", expand=True)
        scroll.pack(side="left", fill="y")

    

    def _build_botoes(self):
        frame = tk.Frame(self)
        frame.pack(side="right", fill="y", padx=10, pady=10)

        tk.Button(frame, text="Nova",    width=15, command=self._nova).pack(pady=3)
        tk.Button(frame, text="Editar",  width=15, command=self._editar).pack(pady=3)
        tk.Button(frame, text="Excluir", width=15, command=self._excluir).pack(pady=3)

    

    def _carregar(self):
        for row in self.tabela.get_children():
            self.tabela.delete(row)

        sucesso, plantas = self.controller.listar()
        if not sucesso:
            messagebox.showerror("Erro", plantas, parent=self)
            return

        for p in plantas:
            self.tabela.insert("", "end", iid=p.id, values=(
                p.id, p.nome, p.nome_cientifico, p.tipo.value,
                p.nota_verao, p.nota_outono, p.nota_inverno, p.nota_primavera
            ))

   

    def _get_id_selecionado(self):
        selecionado = self.tabela.selection()
        if not selecionado:
            messagebox.showwarning("Aviso", "Selecione uma planta.", parent=self)
            return None
        return int(selecionado[0])

    def _nova(self):
        FormPlanta(self)
        self.wait_window()
        self._carregar()

    def _editar(self):
        id_ = self._get_id_selecionado()
        if id_ is None:
            return
        FormPlanta(self, planta_id=id_)
        self.wait_window()
        self._carregar()

    def _excluir(self):
        id_ = self._get_id_selecionado()
        if id_ is None:
            return
        if not messagebox.askyesno("Confirmar", "Deseja excluir esta planta?", parent=self):
            return
        sucesso, msg = self.controller.deletar(id_)
        if sucesso:
            messagebox.showinfo("Sucesso", msg, parent=self)
            self._carregar()
        else:
            messagebox.showerror("Erro", msg, parent=self)