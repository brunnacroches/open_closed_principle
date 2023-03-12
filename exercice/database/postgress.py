class PostgressDB:

    def __init__(self) -> None:
        self.__connection = 'Postgress'
    
    def connect(self) -> str:
        print('Conection DataBase...')
        return self.__connection
    
    def disconnect(self) -> str:
        print('Disconnecting postgress database...')


# connection, connect, disconnect
# conexao , conectar