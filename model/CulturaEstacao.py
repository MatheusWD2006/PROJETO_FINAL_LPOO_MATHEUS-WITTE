from model.estacao_enum import NomeEstacao
from datetime import date, datetime
from model.status_cultura_enum import StatusCultura


class CulturaEstacao:

    def __init__(
        self,
        planta,
        estacao: NomeEstacao,
        status: StatusCultura = None,
        data_plantio=None,
        data_colheita=None
    ):
        self.planta = planta

        if not isinstance(estacao, NomeEstacao):
            raise TypeError(
                "estacao deve ser um objeto NomeEstacao."
            )

        self.__estacao = estacao

        self.status = status
        self.data_plantio = data_plantio
        self.data_colheita = data_colheita

    @property
    def estacao(self):
        return self.__estacao

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, valor):

        if valor is not None and not isinstance(
            valor,
            StatusCultura
        ):
            raise TypeError(
                "status deve ser um objeto StatusCultura ou None."
            )

        self.__status = valor

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
                self.__data_plantio = datetime.strptime(
                    valor,
                    "%d-%m-%Y"
                ).date()

                return

            except ValueError:
                raise ValueError(
                    "data_plantio deve estar no formato dd-mm-YYYY."
                )

        if isinstance(valor, date):
            self.__data_plantio = valor
            return

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

        if isinstance(valor, date):
            self.__data_colheita = valor
            return

        raise TypeError(
            "data_colheita deve ser date, string no formato dd-mm-YYYY ou None."
        )

    def exibir_dados(self):

        return (
            f"Planta: {self.planta}\n"
            f"Status: {self.__status.value if self.__status else 'N/A'}\n"
            f"Estação: {self.__estacao.value}\n"
            f"Data de Plantio: "
            f"{self.__data_plantio.strftime('%d/%m/%Y') if self.__data_plantio else 'N/A'}\n"
            f"Data de Colheita: "
            f"{self.__data_colheita.strftime('%d/%m/%Y') if self.__data_colheita else 'N/A'}\n"
        )

    def __str__(self):
        return self.exibir_dados()