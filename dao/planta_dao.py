import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dao.generic_dao import GenericDAO
from dao.db_config import DBConfig
from model.planta import Planta
from model.tipocultura_enum import TipoCultura

class PlantaDAO(GenericDAO):

    # Salva o objeto no banco de dados.
    def salvar(self, planta: Planta):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO plantas (planta_nome, planta_nome_cientifico, planta_descricao,
                    planta_tipo, planta_nota_verao, planta_nota_outono,
                    planta_nota_inverno, planta_nota_primavera)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                RETURNING planta_id
            """, (
                planta.nome, planta.nome_cientifico, planta.descricao,
                planta.tipo.value, planta.nota_verao, planta.nota_outono,
                planta.nota_inverno, planta.nota_primavera
            ))
            conn.commit()
            return cursor.fetchone()[0]
        finally:
            conn.close()

    # Busca um registro pelo identificador.
    def buscar_por_id(self, id):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM plantas WHERE planta_id = %s", (id,))
            row = cursor.fetchone()
            return self.montar_planta(row) if row else None
        finally:
            conn.close()

    # Retorna todos os registros tratados por este DAO.
    def listar_todos(self):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM plantas ORDER BY planta_nome")
            return [self.montar_planta(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    # Atualiza o registro existente no banco de dados.
    def atualizar(self, id, planta: Planta):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE plantas SET
                    planta_nome = %s, planta_nome_cientifico = %s, planta_descricao = %s,
                    planta_tipo = %s, planta_nota_verao = %s, planta_nota_outono = %s,
                    planta_nota_inverno = %s, planta_nota_primavera = %s
                WHERE planta_id = %s
            """, (
                planta.nome, planta.nome_cientifico, planta.descricao,
                planta.tipo.value, planta.nota_verao, planta.nota_outono,
                planta.nota_inverno, planta.nota_primavera, id
            ))
            conn.commit()
        finally:
            conn.close()

    # Remove o registro identificado no banco de dados.
    def remover(self, id):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM plantas WHERE planta_id = %s", (id,))
            conn.commit()
        finally:
            conn.close()

    # Busca registros cuja nome contenha a sequência informada.
    def buscar_por_nome(self, nome):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM plantas WHERE planta_nome ILIKE %s", (f"%{nome}%",))
            return [self.montar_planta(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    # Constrói um objeto Planta a partir de uma linha do banco de dados.
    def montar_planta(self, row):
        
        return Planta(
            nome=row[1],
            nome_cientifico=row[2],
            descricao=row[3],
            tipo=TipoCultura(row[4]),
            nota_verao=row[5],
            nota_outono=row[6],
            nota_inverno=row[7],
            nota_primavera=row[8],
            planta_id=row[0] 
        )