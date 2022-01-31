from main import User, Session,engine


local_session=Session(bind=engine)

# tous les utilsateurs
users=local_session.query(User).all()

# seulement ceux dont le nom contient 
users=local_session.query(User).filter(User.username=='titi')

for u in users :
    print(u)
    local_session.delete(u)
    local_session.commit()

