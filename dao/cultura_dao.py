import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from dao.generic_dao import GenericDAO
from dao.db_config import DBConfig
from model.CulturaFactory import CulturaFactory
from model.status_cultura_enum import StatusCultura
from model.estacao_enum import NomeEstacao

class CulturaDAO(GenericDAO):

    def __init__(self):
        from dao.planta_dao import PlantaDAO
        self.planta_dao = PlantaDAO()

    def salvar(self, cultura, planta_id):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            estacao = None
            tipo_cultura = "ANO_TODO"

            if hasattr(cultura, 'estacao'):
                tipo_cultura = "ESTACAO"
                estacao = cultura.estacao.value

            cursor.execute("""
                INSERT INTO culturas (planta_id, cultura_status, cultura_data_plantio,
                    cultura_data_colheita, cultura_tipo, cultura_estacao)
                VALUES (%s, %s, %s, %s, %s, %s)
                RETURNING cultura_id
            """, (
                planta_id,
                cultura.status.value if isinstance(cultura.status, StatusCultura) else cultura.status,
                cultura.data_plantio,
                cultura.data_colheita,
                tipo_cultura,
                estacao
            ))
            conn.commit()
            return cursor.fetchone()[0]
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT cultura_id, planta_id, cultura_status, cultura_data_plantio, 
                       cultura_data_colheita, cultura_tipo, cultura_estacao 
                FROM culturas WHERE cultura_id = %s
            """, (id,))
            row = cursor.fetchone()
            return self.__montar_cultura(row) if row else None
        finally:
            conn.close()

    def listar_todos(self):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
           
            cursor.execute("""
                SELECT cultura_id, planta_id, cultura_status, cultura_data_plantio, 
                       cultura_data_colheita, cultura_tipo, cultura_estacao 
                FROM culturas ORDER BY cultura_id
            """)
            return [self.__montar_cultura(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    def atualizar(self, id, cultura):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            estacao = None
            if hasattr(cultura, 'estacao'):
                estacao = cultura.estacao.value

            cursor.execute("""
                UPDATE culturas SET
                    cultura_status = %s, cultura_data_plantio = %s,
                    cultura_data_colheita = %s, cultura_estacao = %s
                WHERE cultura_id = %s
            """, (
                cultura.status.value if isinstance(cultura.status, StatusCultura) else cultura.status,
                cultura.data_plantio,
                cultura.data_colheita,
                estacao, id
            ))
            conn.commit()
        finally:
            conn.close()

    def remover(self, id):
        conn = DBConfig.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM culturas WHERE cultura_id = %s", (id,))
            conn.commit()
        finally:
            conn.close()

    def __montar_cultura(self, row):
        
        planta = self.planta_dao.buscar_por_id(row[1])
        tipo = row[5]
        estacao = row[6]

        kwargs = {
            "planta": planta,
            "status": StatusCultura(row[2]) if row[2] else None,
            "data_plantio": row[3],
            "data_colheita": row[4],
        }
        if tipo == "ESTACAO":
            kwargs["estacao"] = NomeEstacao(estacao) if estacao else None

       
        cultura = CulturaFactory.criar_cultura(tipo, **kwargs)
        
        
        cultura.cultura_id = row[0]
        
        return cultura