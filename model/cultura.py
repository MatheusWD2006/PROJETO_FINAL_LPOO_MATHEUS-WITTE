from abc import ABC, abstractmethod
from model.classificacao_enum import ClassificacaoCultura
from model.tipocultura_enum import TipoCultura

class Cultura(ABC):
    def __init__(self, nome, nome_cientifico, descricao,
                 tipo: TipoCultura, classificacao: ClassificacaoCultura):

        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.descricao = descricao
        self.tipo = tipo
        self.classificacao = classificacao

  
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
    def classificacao(self):
        return self.__classificacao

    @classificacao.setter
    def classificacao(self, valor):
        if not isinstance(valor, ClassificacaoCultura):
            raise TypeError("O campo 'classificacao' deve receber um valor do enum ClassificacaoCultura.")
        self.__classificacao = valor

  
    def __str__(self):
        return (
            f"Nome: {self.__nome}\n"
            f"Nome Científico: {self.__nome_cientifico}\n"
            f"Descrição: {self.__descricao}\n"
            f"Tipo: {self.__tipo.name}\n"
            f"Classificação: {self.__classificacao.name}"
        )
    @abstractmethod
    def exibir_dados(self):
       pass