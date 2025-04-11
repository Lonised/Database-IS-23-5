import psycopg2

class DataAccessor:
    def __init__(self):
        db_parametres = {
            "dbname": "Kontrol_rabota",
            "user": "postgres",
            "password": "QweAsd12345@"
        }
        self.connection = psycopg2.connect(**db_parametres)
        self.cursor = self.connection.cursor()

    def insert_product(self, name, price, category_id):
        self.cursor.execute(
            "INSERT INTO products(name, price, category_id) VALUES (%s, %s, %s)",
            (name, price, category_id)
        )

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def delete_product(self, product_id):
        self.cursor.execute("DELETE FROM products WHERE id = %s", (product_id,))

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def get_all_products(self):
        self.cursor.execute("SELECT id, name, price, category_id FROM products")
        rows = self.cursor.fetchall()
        self.cursor.close()
        self.connection.close()
        return rows
  