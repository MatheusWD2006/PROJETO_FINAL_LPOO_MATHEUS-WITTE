from model.planta import Planta
from model.tipocultura_enum import TipoCultura
from dao.planta_dao import PlantaDAO

NOTA_MINIMA = 6.0

class PlantaController:

    def __init__(self):
        self.dao = PlantaDAO()

    def cadastrar(self, nome, nome_cientifico, descricao, tipo,
                  nota_inverno, nota_verao, nota_primavera, nota_outono):
        try:
            planta = Planta(
                nome=nome,
                nome_cientifico=nome_cientifico,
                descricao=descricao,
                tipo=TipoCultura(tipo),
                nota_inverno=float(nota_inverno),
                nota_verao=float(nota_verao),
                nota_primavera=float(nota_primavera),
                nota_outono=float(nota_outono)
            )
            self.dao.inserir(planta)
            return True, "Planta cadastrada com sucesso!"
        except (TypeError, ValueError) as e:
            return False, str(e)
        except Exception as e:
            return False, f"Erro inesperado: {e}"

    def listar(self):
        try:
            return True, self.dao.buscar_todos()
        except Exception as e:
            return False, f"Erro ao listar plantas: {e}"

    def buscar_por_id(self, id):
        try:
            planta = self.dao.buscar_por_id(id)
            if planta is None:
                return False, "Planta não encontrada."
            return True, planta
        except Exception as e:
            return False, f"Erro ao buscar planta: {e}"

    def buscar_por_nome(self, nome):
        try:
            return True, self.dao.buscar_por_nome(nome)
        except Exception as e:
            return False, f"Erro ao buscar planta: {e}"

    def buscar_disponiveis_por_tipo(self, tipo_cultura, estacao=None):
        try:
            sucesso, plantas = self.listar()
            if not sucesso:
                return False, plantas

            disponiveis = []
            for planta in plantas:
                if tipo_cultura == "ANO_TODO":
                    if all(nota >= NOTA_MINIMA for nota in [
                        planta.nota_inverno,
                        planta.nota_verao,
                        planta.nota_primavera,
                        planta.nota_outono
                    ]):
                        disponiveis.append(planta)

                elif tipo_cultura == "ESTACAO":
                    nota = {
                        "Verão":     planta.nota_verao,
                        "Primavera": planta.nota_primavera,
                        "Outono":    planta.nota_outono,
                        "Inverno":   planta.nota_inverno,
                    }.get(estacao, 0)

                    if nota >= NOTA_MINIMA:
                        disponiveis.append(planta)

            return True, disponiveis
        except Exception as e:
            return False, f"Erro ao buscar plantas disponíveis: {e}"

    def atualizar(self, id, nome, nome_cientifico, descricao, tipo,
                  nota_inverno, nota_verao, nota_primavera, nota_outono):
        try:
            planta = Planta(
                nome=nome,
                nome_cientifico=nome_cientifico,
                descricao=descricao,
                tipo=TipoCultura(tipo),
                nota_inverno=float(nota_inverno),
                nota_verao=float(nota_verao),
                nota_primavera=float(nota_primavera),
                nota_outono=float(nota_outono)
            )
            self.dao.atualizar(id, planta)
            return True, "Planta atualizada com sucesso!"
        except (TypeError, ValueError) as e:
            return False, str(e)
        except Exception as e:
            return False, f"Erro inesperado: {e}"

    def deletar(self, id):
        try:
            self.dao.deletar(id)
            return True, "Planta removida com sucesso!"
        except Exception as e:
            return False, f"Erro ao remover planta: {e}"