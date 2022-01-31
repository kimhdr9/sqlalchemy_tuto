from main import User,engine,Base,string_connection


print(string_connection)

"""
cette fonction ci-dessous crée les tables dans la base de données postgresql attention le n° de port n'est pas utilisé.
"""

Base.metadata.create_all(engine)