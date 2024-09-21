class Repositorio:

    def select(self, db_conn: any) -> None:
        conn = db_conn.conectar()
        print('conectei ao banco {}'.format(conn))
        print('Fazendo um SELECT * FROM...')
        

    def insert(self, db_conn: any) -> None:
        conn = db_conn.conectar()
        print('conectei ao banco {}'.format(conn))
        print('Fazendo um Insert...')
        
