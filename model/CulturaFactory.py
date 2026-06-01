from model.CulturaEstacao import CulturaEstacao
from model.CulturaAnoTodo import CulturaAnoTodo


class CulturaFactory:

    @staticmethod
    def criar_cultura(tipo_cultura: str, **kwargs):
        
        tipo_cultura = tipo_cultura.upper().strip()

        if tipo_cultura == "ESTACAO":
            return CulturaEstacao(
                planta=kwargs.get("planta"),
                tipo=kwargs.get("tipo"),
                estacao=kwargs.get("estacao"),
                status=kwargs.get("status"),    
                data_plantio=kwargs.get("data_plantio"),
                data_colheita=kwargs.get("data_colheita")
            )

        elif tipo_cultura == "ANO_TODO":
            return CulturaAnoTodo(
                planta=kwargs.get("planta"),
                tipo=kwargs.get("tipo"),
                status=kwargs.get("status"),
                data_plantio=kwargs.get("data_plantio"),
                data_colheita=kwargs.get("data_colheita")
            )

        else:
            raise ValueError(
                "Tipo de cultura inválido. Use 'ESTACAO' ou 'ANO_TODO'."
            )