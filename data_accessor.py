import psycopg2

DB_PARAMS = {
	"dbname": "postgres",
	"user": "postgres",
	"password": "2680",
	"host": "localhost",
	"port": "5432",
}

def selectTable():
	conn = psycopg2.connect(**DB_PARAMS)
	cur = conn.cursor()

	cur.execute("""
		SELECT 
			tables.id, orders.order_time, orders.total_price
		FROM tables 
		JOIN orders ON orders.table_id = tables.id 
		
	""")

	conn.commit()
	cur.close()
	conn.close()


if __name__ == "__main__":
	selectTable()
	