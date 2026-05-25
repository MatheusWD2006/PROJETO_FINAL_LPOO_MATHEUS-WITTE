from datetime import date, datetime
from model.cultura_estacao import CulturaEstacao


class StatusCulturaEstacao:

    def __init__(self, cultura_estacao: CulturaEstacao,
                 data_plantio=None,
                 data_colheita=None,
                 status=""):

        if not isinstance(cultura_estacao, CulturaEstacao):
            raise TypeError("StatusCulturaEstacao deve ser associado a um objeto CulturaEstacao.")

        self.__cultura_estacao = cultura_estacao

      
        self.data_plantio = data_plantio
        self.data_colheita = data_colheita
        self.status = status 

    @property
    def cultura_estacao(self):
        return self.__cultura_estacao

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

        raise TypeError("data_plantio deve ser date ou string dd-mm-YYYY.")

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

        raise TypeError("data_colheita deve ser date ou string dd-mm-YYYY.")

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):
        if not isinstance(valor, str):
            raise TypeError("status deve ser string.")
        self.__status = valor.upper()


    def concluir(self):

        if self.__status == "":
            self.__status = "PLANTADO"
            if self.__data_plantio is None:
              self.__data_plantio = date.today()

        elif self.__status == "PLANTADO":
            self.__status = "COLHIDO"
            if self.__data_colheita is None:
              self.__data_colheita = date.today()

        else:
            print("Cultura já colhida. Nada a concluir.")


    def exibir_dados(self):
  
        return (
            f"Cultura:\n"
            f"{self.__cultura_estacao.exibir_dados()}\n"
            f"Status: {self.__status}\n"
            f"Data de Plantio: {self.__data_plantio.strftime('%d/%m/%Y') if self.__data_plantio else 'N/A' }\n"
            f"Data de Colheita: {self.__data_colheita.strftime('%d/%m/%Y') if self.__data_colheita else 'N/A'}"
        )

    def __str__(self):
        return self.exibir_dados()
