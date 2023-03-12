class Repository:

    def select(self, db_connection: any) -> None:
        connection = db_connection.connect()
        print('Conection dabatabase {}'.format(connection))
        print('Making a SELECT *FROM...')
        db_connection.disconnect()
    
    def insert(self, db_connection:any) -> None:
        connection = db_connection.connect()
        print('Conection dabatabase {}'.format(connection))
        print('Making a SELECT *FROM...')
        db_connection.disconnect()