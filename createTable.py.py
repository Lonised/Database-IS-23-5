DB_PARAMS= {
       "dbname" = "postgres"
       "user" = "postgres"
       "password" = "12345"
       "host" = "localhost"
       "port" = "54321"
def createTable ():
      conn = psycora2.connect(**DB_PARAMS)
      cur = conn.cursor()

     cur.execute("""
           CREATE TABLE grades (
            id SERIAL PRIMARY KEY,
            student_id VARCHAR(50) NOT NULL,
            subject VARCHAR(50)
	    grade INTEGER
           )
""")

     cur.execute("""
           CREATE TABLE students (
           id SERIAL PRIMARY KEY,
           name VARCHAR(30),
           group_name VARCHAR(25),
           )
""")
  conn.commit()
  cur.close()
  conn.close()
}
If __name__="__main__":
     createTable()