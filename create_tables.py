import psycopg2

db_params = {
    "dbname": "Kontrol_rabota",
    "user": "postgres",
    "password": "QweAsd12345@"
}

connection = psycopg2.connect(**db_params)
cursor = connection.cursor() 

def create_table(cursor):
    #cursor.execute("""Create table categories (
    #                           id serial primary key,
     #                          name varchar(40)
    #                  );
    #                       Create table products (
    #                           id serial primary key,
    #                           name varchar(40) not null,
    #                           category_id int references categories(id) not null,
    #                           price int not null
    #                  );
    #""")
   
    cursor.execute("""insert into categories(name) values ('Moloko'), ('Xleb')""")
    connection.commit()
    cursor.close()
    connection.commit()

if __name__ == "__main__":
    create_table(cursor)