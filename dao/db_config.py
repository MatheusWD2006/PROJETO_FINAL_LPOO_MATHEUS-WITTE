import psycopg2
from psycopg2 import Error

class DBConfig:
    @staticmethod
    def get_connection():
        try:
            conexao = psycopg2.connect(
                host="localhost",
                database="culturas",
                user="postgres",
                password="postgres",
                port = "5432"
              
            )
            return conexao

        except Error as e:
            print(f"Erro ao conectar ao PostgreSQL: {e}")
            return None

