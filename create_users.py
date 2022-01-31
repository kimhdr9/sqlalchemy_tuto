from main import User, Session,engine
import names


local_session=Session(bind=engine)

for i in range(10):
    """
     liste d'utilisatrices
    """
    rand_name=names.get_full_name(gender='female')
    email = rand_name.replace(' ','.')
    email = email+'@mail.com'
    """
    ajout dans la table
    """
    user=User(username=rand_name,email=email)

    local_session.add(user)
    local_session.commit()
