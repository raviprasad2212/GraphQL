from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import psycopg2
from sqlalchemy import Table, Column, String, MetaData
import sqlalchemy

username = 'postgres'
password = 'Ravi@143'
server = 'localhost'


db_string = "postgresql://{}:{}@{}:5432/games".format(username, password, server)
db = create_engine(db_string)

print(db)

meta = MetaData(db)  
UserModel = Table('users', meta,  
                       Column('username', String(20), primary_key=True),
                       Column('password', String(20)))



# for i in meta.tables:
#     if UserModel == i:
#         print('yes')

# print(dir(UserModel))

# with db.connect() as conn:
#     try:
#         # Create
#         UserModel.create()
#         insert_statement = UserModel.insert().values(username="Doctor Strange", password="Scott Derrickson")
#         conn.execute(insert_statement)
#     except sqlalchemy.exc.DatabaseError as e:
#         if psycopg2.errors.DuplicateTable:
#             print('table exists')
