import psycopg2

def create_tables():
	conn = psycopg2.connect(dbname=DB_NAME, user=USER, password=PASSWORD, host=HOST, port=PORT)
	cursor = conn.cursor()

    cursor.execute("""
	CREATE TABLE menu_items (
	   id SERIAL PRIMARY KEY, 
	   name VARCHAR(20),
	   price INT NOT NULL
	)
    """)


    cursor.execute("""
        CREATE TABLE orders (
            id SERIAL PRIMARY KEY,
            table_number INT NOT NULL,
            item_id INT NOT NULL REFERENCES menu_items(id),
	    quantity INT NOT NULL
            departure_time TIMESTAMP NOT NULL
        )
    """)

   
    cursor.execute("""
        INSERT INTO menu_items (name, price) VALUES (
            ('Burger', 250),
            ('Pizza', 400),
            ('Voda', 100),
            ('Kola', 110),
            ('Coffee', 120)
    """)

    cursor.execute("""
        INSERT INTO orders (table_number, item_id, quantity, order_time) VALUES (
            (1, 1, 2, (datetime.now()),
            (2, 2, 1, datetime.now()),
            (1, 3, 3, datetime.now()),
            (3, 5, 1, datetime.now())
    """)


    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_tables()

	
