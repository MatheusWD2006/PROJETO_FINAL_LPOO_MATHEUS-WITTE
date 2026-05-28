from model.estacao_enum import NomeEstacao
from datetime import date, datetime

class CulturaEstacao:

    def __init__(self, planta, estacao: NomeEstacao, data_plantio=None, data_colheita=None):
        self.planta = planta
        if not isinstance(estacao, NomeEstacao):
            raise TypeError("estacao deve ser um objeto NomeEstacao.")
        self.__estacao = estacao
        self.data_plantio = data_plantio
        self.data_colheita = data_colheita

    @property
    def estacao(self):
        return self.__estacao
    
    @property
    def data_plantio(self):
        return self.__data_plantio
    
    @data_plantio.setter
    def data_plantio(self, valor):
        if valor is None:
            self.__data_plantio = None
            return

        if isinstance(valor, str):
            valor = valor.strip()
            try:
                self.__data_plantio = datetime.strptime(valor, "%d-%m-%Y").date()
                return
            except ValueError:
                raise ValueError("data_plantio deve estar no formato dd-mm-YYYY.")
        
        if isinstance(valor, date):
            self.__data_plantio = valor
            return
        
    @property
    def data_colheita(self):
        return self.__data_colheita
    
    @data_colheita.setter
    def data_colheita(self, valor):
        if valor is None:
            self.__data_colheita = None
            return

        if isinstance(valor, str):
            valor = valor.strip()
            try:
                self.__data_colheita = datetime.strptime(valor, "%d-%m-%Y").date()
                return
            except ValueError:
                raise ValueError("data_colheita deve estar no formato dd-mm-YYYY.")
        
        if isinstance(valor, date):
            self.__data_colheita = valor
            return

    def exibir_dados(self):
         return (
            f"{self.planta}\n"
            f"Estação: {self.__estacao.nome.value}\n"
            f"Data de Plantio: {self.__data_plantio}\n"
            f"Data de Colheita: {self.__data_colheita}\n"
        )


    def __str__(self):
        return self.exibir_dados()
