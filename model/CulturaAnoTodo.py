from datetime import date, datetime
from model.status_cultura_enum import StatusCultura


class CulturaAnoTodo:
    def __init__(self, planta, status="StatusCultura", data_plantio=None, data_colheita=None):
        self.planta = planta
        self.data_plantio = data_plantio
        self.data_colheita = data_colheita
        self.status = status


   
    @property
    def data_plantio(self):
        return self.__data_plantio

    @data_plantio.setter
    def data_plantio(self, valor):

        if valor is None:
            self.__data_plantio = None
            return

        if isinstance(valor, date):
            self.__data_plantio = valor
            return

        if isinstance(valor, str):
            valor = valor.strip()
            try:
                self.__data_plantio = datetime.strptime(valor, "%d-%m-%Y").date()
                return
            except ValueError:
                raise ValueError("data_plantio deve estar no formato dd-mm-YYYY.")


    @property
    def data_colheita(self):
        return self.__data_colheita

    @data_colheita.setter
    def data_colheita(self, valor):

        if valor is None:
            self.__data_colheita = None
            return

        if isinstance(valor, date):
            self.__data_colheita = valor
            return

        if isinstance(valor, str):
            valor = valor.strip()
            try:
                self.__data_colheita = datetime.strptime(valor, "%d-%m-%Y").date()
                return
            except ValueError:
                raise ValueError("data_colheita deve estar no formato dd-mm-YYYY.")

       

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        if not isinstance(valor, str):
            raise TypeError("status deve ser uma string.")
        self.__status = valor.upper()

   
    def concluir(self):

        if self.data_plantio and self.data_colheita:
            if self.data_colheita > self.data_plantio:
                self.status = StatusCultura.CONCLUIDA.name
            else:
                raise ValueError("data_colheita deve ser posterior a data_plantio.")
        else:
            raise ValueError("data_plantio e data_colheita devem ser definidas para concluir a cultura.")

    def exibir_dados(self):

        return (
            
            f"{self.planta}\n"
            f"Status: {self.__status}\n"
            f"Data de Plantio: {self.__data_plantio.strftime('%d/%m/%Y') if self.__data_plantio else 'N/A'}\n"
            f"Data de Colheita: {self.__data_colheita.strftime('%d/%m/%Y') if self.__data_colheita else 'N/A'}"
        )

    def __str__(self):
        return self.exibir_dados()
