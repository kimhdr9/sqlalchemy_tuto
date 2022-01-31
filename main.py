from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column,String,Integer,DateTime
from datetime import datetime
from sqlalchemy import create_engine
from db.parser import config
import psycopg2

'''
configuration de la base de données postgresql
'''
filename='database.ini'
section='postgresql'

database=config(filename,section)
'''
chaine de connection : fonctionne sans le n° du port voir le fichier create_db.py
'''
string_connection='postgresql+psycopg2://'+database['user']+':'+database['password']+'@'+database['host']+'/'+database['name']
'''
moteur de connexion
'''
Base = declarative_base()
engine = create_engine(string_connection,echo=True)
Session = sessionmaker()


class User(Base):
    __tablename__='users'
    id=Column(Integer(),primary_key=True)
    username=Column(String(80),nullable=False,unique=True) 
    email=Column(String(80),nullable=False,unique=True) 
    date_created=Column(DateTime(),default=datetime.utcnow())

    def __str__(self) -> str:
        return f'{self.username} - {self.email}' 

user1 = User(id=1,username='toto',email='toto@mail.fr')

print(user1)
print(datetime.utcnow())
