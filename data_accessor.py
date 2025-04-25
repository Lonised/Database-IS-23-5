import psycopg2

DB_NAME = "cafe_db"
USER = "postgres"
PASSWORD = "1234"
HOST = "localhost"
PORT = "5432"

class DataAccessor:
    def __init__(self):
        self.conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
        self.cursor = self.conn.cursor()

   
    def get_order(self):
        self.cursor.execute("""
            SELECT orders.id, table_number, name, quantity, order_time FROM orders
            JOIN menu_items ON orders.item_id = menu_items.id
        """)
        return self.cursor.fetchall()


    def add_pos(self, table_number, item_id, quantity, order_time):
        self.cursor.execute(""" INSERT INTO orders (table_number, item_id, quantity, order_time) VALUES (
        VALUES (%s, %s, %s, %s)
        """, (table_number, item_id, quantity, order_time))
        self.conn.commit()


    def delete_order(self, order_id):
        self.cursor.execute("DELETE FROM orders WHERE id = %s", (order_id,))
        self.conn.commit()


    def close(self):
        self.cursor.close()
        self.conn.close()

        


    

        
         
