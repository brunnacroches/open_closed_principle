class MysqlDB:

    def __init__(self) -> None:
        self.__connection = 'Mysql'
    
    def connect(self) -> str:
        print('Conection Mysql...')
        return self.__connection
    
    def disconnect(self) -> str:
        print('Disconnecting postgress Mysql...')


# connection, connect, disconnect
# conexao , conectar