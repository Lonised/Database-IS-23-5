import psycorg2

DB_PARAMS = { 
	"dbname" = "postgres",
	"user" = "postgres",
	"password" = "2680",
	"host" = "localhost",
	"port" = "5432"
}

def createTable():
	conn = psycorg2.connect(**DB_PARAMS)
	cur = conn.cursor()

	cur.execute("""
		CREATE TABLE tables (
		ID SERIAL PRIMARY KEY, 
		table_number INT NOT NULL,
		capacity VARCHAR(255) NOT NULL
		)
	""")

	cur.execute("""
		CREATE TABLE orders (
		ID SERIAL PRIMARY KEY,
		table_id REFERENCES orders(id),
		order_time VARCHAR(255) NOT NULL,
		total_price VARCHAR(255) NOT NULL,
		)
	""")
	
	conn.commit()
	cur.close()
	conn.close()
}

If __name__ = "__main__":
	createTable()

