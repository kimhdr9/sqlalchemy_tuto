import random as r
from main import User, Session,engine


local_session=Session(bind=engine)

# tous les utilsateurs
users=local_session.query(User).all()

def randomphone():
    phone=0
    puissance=1

    for i in range(1,9) :
        phone= phone + r.randint(0,9)*puissance
        puissance = 10*puissance
    return phone

phones = []

for i in range(1,11):
    new_number = randomphone()
    phone_number = '0'+str(new_number)
    phones.append(phone_number)

print(len(phones))

test = True
if test :
    """
    ajout des téléphones 
    """
    i=0
    for u in users :
        # nouvelle adresse mail
        u.telephone=phones[i]
        i=i+1
        local_session.commit()    