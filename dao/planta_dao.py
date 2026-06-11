from dao.generic_dao import GenericDAO
from dao.db_config import DBConfig
from model.planta import Planta
from model.tipocultura_enum import TipoCultura

class PlantaDAO(GenericDAO):

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
            return cursor.fetchone()[0]  # retorna o id gerado
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM plantas WHERE planta_id = %s", (id,))
            row = cursor.fetchone()
            return self.__montar_planta(row) if row else None
        finally:
            conn.close()

    def listar_todos(self):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM plantas ORDER BY planta_nome")
            return [self.__montar_planta(row) for row in cursor.fetchall()]
        finally:
            conn.close()

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

    def remover(self, id):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM plantas WHERE planta_id = %s", (id,))
            conn.commit()
        finally:
            conn.close()

    def buscar_por_nome(self, nome):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM plantas WHERE planta_nome ILIKE %s", (f"%{nome}%",))
            return [self.__montar_planta(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    def __montar_planta(self, row):
        return Planta(
            nome=row[1],
            nome_cientifico=row[2],
            descricao=row[3],
            tipo=TipoCultura(row[4]),
            nota_verao=row[5],
            nota_outono=row[6],
            nota_inverno=row[7],
            nota_primavera=row[8]
        )