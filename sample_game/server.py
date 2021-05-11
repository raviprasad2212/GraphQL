from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from sqlalchemy import Table, Column, String, MetaData


username = 'postgres'
password = 'Ravi@143'
server = 'localhost'




db_string = "postgresql://{}:{}@{}:5432/games".format(username, password, server)
db = create_engine(db_string)
print(dir(db))


meta = MetaData(db)  
film_table = Table('films', meta,  
                       Column('title', String),
                       Column('director', String),
                       Column('year', String))

with db.connect() as conn:

    # Create
    # film_table.create()
    insert_statement = film_table.insert().values(title="Doctor Strange", director="Scott Derrickson", year="2016")
    conn.execute(insert_statement)

    # Read
    select_statement = film_table.select()
    result_set = conn.execute(select_statement)
    for r in result_set:
        print(r)

    # Update
    update_statement = film_table.update().where(film_table.c.year=="2016").values(title = "Some2016Film")
    conn.execute(update_statement)

    # Delete
    delete_statement = film_table.delete().where(film_table.c.year == "2016")
    conn.execute(delete_statement)