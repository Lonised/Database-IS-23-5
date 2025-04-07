Import psycorg 2

DB_PARAMS= {
       "dbname" = "postgres"
       "user" = "postgres"
       "password" = "12345"
       "host" = "localhost"
       "port" = "5432"
}
def insertTable():
     conn = psycora2.connect(**DB_PARAMS)
      cur = conn.cursor()

cur.execute("""
 INSERT INTO grades (student_id, subject, grade) VALUES (1, 'Information_System', 4);
""")

conn.commit()
cur.close()
conn.close()

}

def selectTable():
      conn = psycora2.connect(**DB_PARAMS)
      cur = conn.cursor()
      cur.execute("""
       SELECT 
      grades.student_id 
      grades.subject
      grades.grade
FROM students 
JOIN grades ON student.student_id = student.id
""")
conn.commit()
cur.close()
conn.close()
}

if _name_ == "_main_":
  insertTable()
  selectTable()

