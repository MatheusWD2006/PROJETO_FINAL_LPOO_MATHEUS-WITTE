import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.tipocultura_enum import TipoCultura

class Planta:
    def __init__(self, nome, nome_cientifico, descricao, tipo: TipoCultura, 
                 nota_inverno=0, nota_verao=0, nota_primavera=0, nota_outono=0, planta_id=None):

        self.planta_id = planta_id  
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.descricao = descricao
        self.tipo = tipo
        self.nota_inverno = nota_inverno
        self.nota_verao = nota_verao
        self.nota_primavera = nota_primavera
        self.nota_outono = nota_outono
        
    @property
    def planta_id(self):
        return self.__planta_id

    @planta_id.setter
    def planta_id(self, valor):
        self.__planta_id = valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def nome_cientifico(self):
        return self.__nome_cientifico

    @nome_cientifico.setter
    def nome_cientifico(self, valor):
        self.__nome_cientifico = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        if not isinstance(valor, TipoCultura):
            raise TypeError("O campo 'tipo' deve receber um valor do enum TipoCultura.")
        self.__tipo = valor

    @property
    def nota_inverno(self):
        return self.__nota_inverno
    
    @nota_inverno.setter
    def nota_inverno(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("nota_inverno deve ser numérica.")
        if valor < 0 or valor > 10:
            raise ValueError("nota_inverno deve estar entre 0 e 10.")
        self.__nota_inverno = valor

    @property
    def nota_verao(self):
        return self.__nota_verao
    
    @nota_verao.setter
    def nota_verao(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("nota_verao deve ser numérica.")
        if valor < 0 or valor > 10:
            raise ValueError("nota_verao deve estar entre 0 e 10.")
        self.__nota_verao = valor

    @property
    def nota_primavera(self):
        return self.__nota_primavera
    
    @nota_primavera.setter
    def nota_primavera(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("nota_primavera deve ser numérica.")
        if valor < 0 or valor > 10:
            raise ValueError("nota_primavera deve estar entre 0 e 10.")
        self.__nota_primavera = valor

    @property
    def nota_outono(self):
        return self.__nota_outono
    
    @nota_outono.setter
    def nota_outono(self, valor):
        if not isinstance(valor, (int, float)):
            raise TypeError("nota_outono deve ser numérica.")
        if valor < 0 or valor > 10:
            raise ValueError("nota_outono deve estar entre 0 e 10.")
        self.__nota_outono = valor

    def __str__(self):
        return f"{self.nome} ({self.nome_cientifico}) - {self.tipo.name}"
    
    def exibir_dados(self):
        return (
            f"Nome: {self.__nome}\n"
            f"Nome Científico: {self.__nome_cientifico}\n"
            f"Descrição: {self.__descricao}\n"
            f"Tipo: {self.__tipo.name}\n"
        )