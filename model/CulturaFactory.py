from model.CulturaEstacao import CulturaEstacao
from model.CulturaAnoTodo import CulturaAnoTodo


class CulturaFactory:

    @staticmethod
    def criar_cultura(tipo_cultura: str, **kwargs):
        
        tipo_cultura = tipo_cultura.upper().strip()

        if tipo_cultura == "ESTACAO":
            return CulturaEstacao(
                nome=kwargs.get("nome"),
                nome_cientifico=kwargs.get("nome_cientifico"),
                descricao=kwargs.get("descricao"),
                tipo=kwargs.get("tipo"),
                classificacao=kwargs.get("classificacao"),
                estacao=kwargs.get("estacao"),
                nota_produtividade=kwargs.get("nota_produtividade"),
                nota_resistencia=kwargs.get("nota_resistencia")
            )

        elif tipo_cultura == "ANO_TODO":
            return CulturaAnoTodo(
                nome=kwargs.get("nome"),
                nome_cientifico=kwargs.get("nome_cientifico"),
                descricao=kwargs.get("descricao"),
                tipo=kwargs.get("tipo"),
                classificacao=kwargs.get("classificacao")
            )

        else:
            raise ValueError(
                "Tipo de cultura inválido. Use 'ESTACAO' ou 'ANO_TODO'."
            )