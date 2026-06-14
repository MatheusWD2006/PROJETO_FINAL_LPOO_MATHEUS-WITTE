import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.CulturaFactory import CulturaFactory
from model.estacao_enum import NomeEstacao
from model.status_cultura_enum import StatusCultura
from dao.cultura_dao import CulturaDAO
from dao.planta_dao import PlantaDAO
from datetime import date

class CulturaController:

    # Inicializa a nova instância da classe.
    def __init__(self):
        self.dao = CulturaDAO()
        self.planta_dao = PlantaDAO()

    # Método auxiliar para processamento interno.
    def _validar_datas_status(self, status, data_plantio, data_colheita):
        if status == StatusCultura.PLANTADO.value:
            if not data_plantio:
                return False, "Data de plantio obrigatória para status Plantado."
        if status == StatusCultura.COLHIDO.value:
            if not data_plantio or not data_colheita:
                return False, "Ambas as datas são obrigatórias para status Colhido."
        return True, None

    # Realiza a ação cadastrar.
    def cadastrar(self, planta_id, tipo_cultura, status, data_plantio,
                  data_colheita, estacao=None):
        try:
            if status:
                ok, msg = self._validar_datas_status(status, data_plantio, data_colheita)
                if not ok:
                    return False, msg

            planta = self.planta_dao.buscar_por_id(planta_id)
            if planta is None:
                return False, "Planta não encontrada."

            kwargs = {
                "planta": planta,
                "status": StatusCultura(status) if status else None,
                "data_plantio": data_plantio,
                "data_colheita": data_colheita,
            }
            if tipo_cultura.upper() == "ESTACAO":
                if not estacao:
                    return False, "Estação obrigatória para cultura de estação."
                kwargs["estacao"] = NomeEstacao(estacao)

            cultura = CulturaFactory.criar_cultura(tipo_cultura, **kwargs)
            self.dao.salvar(cultura, planta_id)
            return True, "Cultura cadastrada com sucesso!"
        except (TypeError, ValueError) as e:
            return False, str(e)
        except Exception as e:
            return False, f"Erro inesperado: {e}"

    # Retorna uma lista de registros.
    def listar(self):
        try:
            return True, self.dao.listar_todos()
        except Exception as e:
            return False, f"Erro ao listar culturas: {e}"

    # Busca um registro pelo identificador.
    def buscar_por_id(self, id):
        try:
            cultura = self.dao.buscar_por_id(id)
            if cultura is None:
                return False, "Cultura não encontrada."
            return True, cultura
        except Exception as e:
            return False, f"Erro ao buscar cultura: {e}"

    # Atualiza o registro existente no banco de dados.
    def atualizar(self, id, status, data_plantio, data_colheita):
        try:
            if status:
                ok, msg = self._validar_datas_status(status, data_plantio, data_colheita)
                if not ok:
                    return False, msg

            sucesso, cultura = self.buscar_por_id(id)
            if not sucesso:
                return False, cultura

            cultura.status = StatusCultura(status) if status else None
            cultura.data_plantio = data_plantio
            cultura.data_colheita = data_colheita

            self.dao.atualizar(id, cultura)
            return True, "Cultura atualizada com sucesso!"
        except (TypeError, ValueError) as e:
            return False, str(e)
        except Exception as e:
            return False, f"Erro inesperado: {e}"

    # Marca a cultura como plantada e registra a data de plantio.
    def plantar(self, id):
        try:
            sucesso, cultura = self.buscar_por_id(id)
            if not sucesso:
                return False, cultura

            cultura.status = StatusCultura.PLANTADO
            cultura.data_plantio = date.today()
            self.dao.atualizar(id, cultura)
            return True, "Cultura plantada com sucesso!"
        except (TypeError, ValueError) as e:
            return False, str(e)
        except Exception as e:
            return False, f"Erro inesperado: {e}"

    # Marca a cultura como colhida e registra a data de colheita.
    def colher(self, id):
        try:
            sucesso, cultura = self.buscar_por_id(id)
            if not sucesso:
                return False, cultura

            cultura.colher()
            self.dao.atualizar(id, cultura)
            return True, "Cultura colhida com sucesso!"
        except (TypeError, ValueError) as e:
            return False, str(e)
        except Exception as e:
            return False, f"Erro inesperado: {e}"

    # Remove o registro selecionado.
    def deletar(self, id):
        try:
            self.dao.remover(id)
            return True, "Cultura removida com sucesso!"
        except Exception as e:
            return False, f"Erro ao remover cultura: {e}"