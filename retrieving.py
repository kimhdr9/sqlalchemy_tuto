from main import User, Session,engine


local_session=Session(bind=engine)

# tous les utilsateurs
users=local_session.query(User).all()

# seulement ceux dont le nom contient 
users=local_session.query(User).filter(User.username.like('%o%'))

for u in users :
    print(u)

# mise à jour des adresses mails

for u in users :
    new_email=u.email.replace('mail.com','free.fr')
    u.email=new_email
    local_session.commit()