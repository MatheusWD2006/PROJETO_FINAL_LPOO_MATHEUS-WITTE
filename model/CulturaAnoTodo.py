from datetime import date, datetime
from model.status_cultura_enum import StatusCultura


class CulturaAnoTodo:

    def __init__(
        self,
        planta,
        status: StatusCultura =None,
        data_plantio=None,
        data_colheita=None
    ):
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
                self.__data_plantio = datetime.strptime(
                    valor,
                    "%d-%m-%Y"
                ).date()
                return

            except ValueError:
                raise ValueError(
                    "data_plantio deve estar no formato dd-mm-YYYY."
                )

        raise TypeError(
            "data_plantio deve ser date, string no formato dd-mm-YYYY ou None."
        )

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
                self.__data_colheita = datetime.strptime(
                    valor,
                    "%d-%m-%Y"
                ).date()
                return

            except ValueError:
                raise ValueError(
                    "data_colheita deve estar no formato dd-mm-YYYY."
                )

        raise TypeError(
            "data_colheita deve ser date, string no formato dd-mm-YYYY ou None."
        )

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):

        if valor is None:
            self.__status = None
            return

        if not isinstance(valor, StatusCultura):
            raise TypeError(
                "status deve ser None ou uma instância de StatusCultura."
            )

        self.__status = valor

    def plantar(self):
        if self.status == StatusCultura.PLANTADO:
            raise ValueError("Cultura já está plantada.")
        if self.status == StatusCultura.COLHIDO:
            raise ValueError("Cultura já foi colhida.")
        self.status = StatusCultura.PLANTADO
        self.data_plantio = date.today()

    def colher(self):
        if self.data_plantio is None:
            raise ValueError("data_plantio deve estar definida.")
        if self.status != StatusCultura.PLANTADO:
            raise ValueError("Cultura precisa estar plantada para ser colhida.")
        self.status = StatusCultura.COLHIDO
        self.data_colheita = date.today()

    def exibir_dados(self):

        return (
            f"Planta: {self.planta}\n"
            f"Status: {self.__status.value if self.__status else 'N/A'}\n"
            f"Data de Plantio: "
            f"{self.__data_plantio.strftime('%d/%m/%Y') if self.__data_plantio else 'N/A'}\n"
            f"Data de Colheita: "
            f"{self.__data_colheita.strftime('%d/%m/%Y') if self.__data_colheita else 'N/A'}"
        )

    def __str__(self):
        return self.exibir_dados()