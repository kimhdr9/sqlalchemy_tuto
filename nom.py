import names

print(names.__doc__)

for i in range(10):
    rand_name=names.get_full_name(gender='female')
    email = rand_name.replace(' ','.')
    email = email+'@mail.com'
    print(email)