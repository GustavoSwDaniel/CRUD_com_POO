import bcrypt
password = 'Gustavo'
print(password)
# Hash a password for the first time, with a certain number of rounds
hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(14))
# Check that a unhashed password matches one that has previously been
#   hashed
print(hashed)
password_user = input('Senhar: ').encode('utf-8')

print(password_user)
#password_user = bcrypt.hashpw(password_user, bcrypt.gensalt(14))
if bcrypt.checkpw(password_user, hashed):
    print("senhas são iguais")
else:
    print("Senhas diferentes :(")
