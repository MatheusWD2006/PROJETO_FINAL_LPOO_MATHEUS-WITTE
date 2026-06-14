import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model.planta import Planta
from model.tipocultura_enum import TipoCultura
from dao.planta_dao import PlantaDAO

NOTA_MINIMA = 6.0

class PlantaController:

    # Inicializa a nova instância da classe.
    def __init__(self):
        self.dao = PlantaDAO()

    # Formata o nome científico no padrão correto de maiúsculas e minúsculas.
    def formatar_nome_cientifico(self, nome: str) -> str:
        partes = nome.strip().split()
        if not partes:
            return ""
        partes[0] = partes[0].capitalize()
        for i in range(1, len(partes)):
            partes[i] = partes[i].lower()
        return " ".join(partes)

    # Realiza a ação cadastrar.
    def cadastrar(self, nome, nome_cientifico, descricao, tipo,
                  nota_inverno, nota_verao, nota_primavera, nota_outono):
        try:
            nome_cientifico_correto = self.formatar_nome_cientifico(nome_cientifico)
            planta = Planta(
                nome=nome,
                nome_cientifico=nome_cientifico_correto,
                descricao=descricao,
                tipo=TipoCultura(tipo),
                nota_inverno=float(nota_inverno),
                nota_verao=float(nota_verao),
                nota_primavera=float(nota_primavera),
                nota_outono=float(nota_outono)
            )
            self.dao.salvar(planta)
            return True, "Planta cadastrada com sucesso!"
        except (TypeError, ValueError) as e:
            return False, str(e)
        except Exception as e:
            return False, f"Erro inesperado: {e}"

    # Retorna uma lista de registros.
    def listar(self):
        try:
            return True, self.dao.listar_todos()
        except Exception as e:
            return False, f"Erro ao listar plantas: {e}"

    # Busca um registro pelo identificador.
    def buscar_por_id(self, id):
        try:
            planta = self.dao.buscar_por_id(id)
            if planta is None:
                return False, "Planta não encontrada."
            return True, planta
        except Exception as e:
            return False, f"Erro ao buscar planta: {e}"

    # Busca registros cuja nome contenha a sequência informada.
    def buscar_por_nome(self, nome):
        try:
            return True, self.dao.buscar_por_nome(nome)
        except Exception as e:
            return False, f"Erro ao buscar planta: {e}"

    # Retorna as plantas disponíveis conforme o tipo de cultura e estação.
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

    # Atualiza o registro existente no banco de dados.
    def atualizar(self, id, nome, nome_cientifico, descricao, tipo,
                  nota_inverno, nota_verao, nota_primavera, nota_outono):
        try:
            nome_cientifico_correto = self.formatar_nome_cientifico(nome_cientifico)
            planta = Planta(
                nome=nome,
                nome_cientifico=nome_cientifico_correto,
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

    # Remove o registro selecionado.
    def deletar(self, id):
        try:
            self.dao.remover(id)
            return True, "Planta removida com sucesso!"
        except Exception as e:
            return False, f"Erro ao remover planta: {e}"