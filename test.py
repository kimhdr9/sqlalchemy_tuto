from db.parser import config

filename='database.ini'
section='postgresql'

database=config(filename,section)

print(database)