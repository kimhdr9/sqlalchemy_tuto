from configparser import ConfigParser

def config(filename,section) :
    #  un 
    parser = ConfigParser()
    # lire le fichier de configuration
    parser.read(filename)
    # dictionnaire contenant les infos
    db={}
    if parser.has_section(section):
        params = parser.items(section)

        for param in params:
            db[param[0]]= param[1]
    else :
        raise Exception(f"{section} introuvable dans {filename}")

    return db