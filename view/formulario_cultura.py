import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import tkinter as tk
from tkinter import ttk, messagebox
from controller.cultura_control import CulturaController
from controller.planta_control import PlantaController
from model.estacao_enum import NomeEstacao
from model.status_cultura_enum import StatusCultura


class FormCultura(tk.Toplevel):

    def __init__(self, parent, cultura_id=None):
        super().__init__(parent)
        self.title("Nova Cultura" if cultura_id is None else "Editar Cultura")
        self.resizable(False, False)
        self.grab_set()

        self.cultura_controller = CulturaController()
        self.planta_controller = PlantaController()
        self.cultura_id = cultura_id
        self._plantas_disponiveis = []

        self._build_form()

        if cultura_id:
            self._preencher_edicao()

   

    def _build_form(self):
        pad = {"padx": 10, "pady": 5}

       
        tk.Label(self, text="Tipo *").grid(row=0, column=0, sticky="w", **pad)
        self.tipo_var = tk.StringVar()
        self.combo_tipo = ttk.Combobox(
            self,
            textvariable=self.tipo_var,
            values=["ANO_TODO", "ESTACAO"],
            state="readonly",
            width=35
        )
        self.combo_tipo.grid(row=0, column=1, **pad)
        self.combo_tipo.bind("<<ComboboxSelected>>", self._ao_mudar_tipo)

      
        tk.Label(self, text="Estação").grid(row=1, column=0, sticky="w", **pad)
        self.estacao_var = tk.StringVar()
        self.combo_estacao = ttk.Combobox(
            self,
            textvariable=self.estacao_var,
            values=[e.value for e in NomeEstacao],
            state="disabled",
            width=35
        )
        self.combo_estacao.grid(row=1, column=1, **pad)
        self.estacao_var.trace_add("write", self._filtrar_estacao)
        self.combo_estacao.bind("<<ComboboxSelected>>", self._ao_mudar_estacao)

   
        self.btn_buscar = tk.Button(
            self,
            text="Buscar Plantas Disponíveis",
            command=self._buscar_plantas,
            state="disabled"
        )
        self.btn_buscar.grid(row=2, column=0, columnspan=2, pady=5)

      
        tk.Label(self, text="Planta *").grid(row=3, column=0, sticky="w", **pad)
        self.planta_var = tk.StringVar()
        self.combo_planta = ttk.Combobox(
            self,
            textvariable=self.planta_var,
            state="disabled",
            width=35
        )
        self.combo_planta.grid(row=3, column=1, **pad)
        self.planta_var.trace_add("write", self._filtrar_plantas)

        
        tk.Label(self, text="Status").grid(row=4, column=0, sticky="w", **pad)
        self.status_var = tk.StringVar()
        self.combo_status = ttk.Combobox(
            self,
            textvariable=self.status_var,
            values=[""] + [s.value for s in StatusCultura],
            state="readonly",
            width=35
        )
        self.combo_status.grid(row=4, column=1, **pad)

       
        tk.Label(self, text="Data de Plantio (dd-mm-aaaa)").grid(row=5, column=0, sticky="w", **pad)
        self.data_plantio_var = tk.StringVar()
        self.entry_plantio = tk.Entry(self, textvariable=self.data_plantio_var, width=37)
        self.entry_plantio.grid(row=5, column=1, **pad)

        
        tk.Label(self, text="Data de Colheita (dd-mm-aaaa)").grid(row=6, column=0, sticky="w", **pad)
        self.data_colheita_var = tk.StringVar()
        self.entry_colheita = tk.Entry(self, textvariable=self.data_colheita_var, width=37)
        self.entry_colheita.grid(row=6, column=1, **pad)

        
        frame_botoes = tk.Frame(self)
        frame_botoes.grid(row=7, column=0, columnspan=2, pady=10)
        tk.Button(frame_botoes, text="Salvar", width=15, command=self._salvar).pack(side="left", padx=5)
        tk.Button(frame_botoes, text="Cancelar", width=15, command=self.destroy).pack(side="left", padx=5)

    

    def _ao_mudar_tipo(self, event):
        tipo = self.tipo_var.get()
        if tipo == "ESTACAO":
            self.combo_estacao.config(state="normal")
            self.btn_buscar.config(state="disabled") 
        else:
            self.estacao_var.set("")
            self.combo_estacao.config(state="disabled")
            self.btn_buscar.config(state="normal") 
       
        self.planta_var.set("")
        self.combo_planta.config(state="disabled")
        self._plantas_disponiveis = []

    def _ao_mudar_estacao(self, event):
        if self.estacao_var.get():
            self.btn_buscar.config(state="normal")

    def _filtrar_estacao(self, *args):
        if self.combo_estacao["state"] == "disabled":
            return
        texto = self.estacao_var.get().lower()
        filtradas = [e.value for e in NomeEstacao if texto in e.value.lower()]
        self.combo_estacao["values"] = filtradas

    

    def _buscar_plantas(self):
        tipo = self.tipo_var.get()
        estacao = self.estacao_var.get() if tipo == "ESTACAO" else None

        sucesso, resultado = self.planta_controller.buscar_disponiveis_por_tipo(tipo, estacao)
        if not sucesso:
            messagebox.showerror("Erro", resultado, parent=self)
            return

        if not resultado:
            messagebox.showinfo("Aviso", "Nenhuma planta disponível para essa seleção.", parent=self)
            return

        self._plantas_disponiveis = resultado
        self.combo_planta["values"] = [p.nome for p in resultado]
        self.combo_planta.config(state="normal")
        self.planta_var.set("")

    def _filtrar_plantas(self, *args):
        if self.combo_planta["state"] == "disabled":
            return
        texto = self.planta_var.get().lower()
        filtradas = [p.nome for p in self._plantas_disponiveis if texto in p.nome.lower()]
        self.combo_planta["values"] = filtradas

    

    def _validar(self):
        if not self.tipo_var.get():
            messagebox.showerror("Erro", "Selecione o tipo de cultura.", parent=self)
            return False
        if self.tipo_var.get() == "ESTACAO" and not self.estacao_var.get().strip():
            messagebox.showerror("Erro", "Selecione a estação.", parent=self)
            return False
        if not self.planta_var.get().strip():
            messagebox.showerror("Erro", "Selecione uma planta.", parent=self)
            return False
        return True

    

    def _get_planta_id(self):
        nome = self.planta_var.get().strip()
        for p in self._plantas_disponiveis:
            if p.nome == nome:
                return p.planta_id
        return None

    def _salvar(self):
        if not self._validar():
            return

        planta_id = self._get_planta_id()
        if planta_id is None:
            messagebox.showerror("Erro", "Planta não encontrada.", parent=self)
            return

        tipo = self.tipo_var.get()
        estacao = self.estacao_var.get() if tipo == "ESTACAO" else None
        status = self.status_var.get() or None
        data_plantio = self.data_plantio_var.get().strip() or None
        data_colheita = self.data_colheita_var.get().strip() or None

        if self.cultura_id is None:
            sucesso, msg = self.cultura_controller.cadastrar(
                planta_id=planta_id,
                tipo_cultura=tipo,
                status=status,
                data_plantio=data_plantio,
                data_colheita=data_colheita,
                estacao=estacao
            )
        else:
            sucesso, msg = self.cultura_controller.atualizar(
                self.cultura_id, status, data_plantio, data_colheita
            )

        if sucesso:
            messagebox.showinfo("Sucesso", msg, parent=self)
            self.destroy()
        else:
            messagebox.showerror("Erro", msg, parent=self)

   

    def _preencher_edicao(self):
        sucesso, cultura = self.cultura_controller.buscar_por_id(self.cultura_id)
        if not sucesso:
            messagebox.showerror("Erro", cultura, parent=self)
            self.destroy()
            return

       
        self.combo_tipo.config(state="disabled")
        self.combo_estacao.config(state="disabled")
        self.btn_buscar.config(state="disabled")

        if hasattr(cultura, "estacao"):
            self.tipo_var.set("ESTACAO")
            self.estacao_var.set(cultura.estacao.value)
        else:
            self.tipo_var.set("ANO_TODO")

      
        self.planta_var.set(cultura.planta.nome)
        self.combo_planta.config(state="disabled")

        if cultura.status:
            self.status_var.set(cultura.status.value)

        if cultura.data_plantio:
            self.data_plantio_var.set(cultura.data_plantio.strftime("%d-%m-%Y"))

        if cultura.data_colheita:
            self.data_colheita_var.set(cultura.data_colheita.strftime("%d-%m-%Y"))