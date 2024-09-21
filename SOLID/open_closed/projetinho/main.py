from repositorio import Repositorio
from databases import PostgresDB

db = PostgresDB()
repo = Repositorio()


repo.insert(db)
repo.select(db)
