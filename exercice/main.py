from repository import Repository
from database import PostgressDB, MysqlDB

# db_conn = PostgressDB()
db_conn_postgress = PostgressDB()
db_conn_mysql = MysqlDB()

repo = Repository()

repo.insert(db_conn_postgress)
print()
repo.select(db_conn_mysql)