import datetime
from faker import Faker

# =====================================
# EXERCICE 4 : Date actuelle
# =====================================

aujourd_hui = datetime.date.today()
print(f"Aujourd'hui : {aujourd_hui.strftime('%d/%m/%Y')}")


# =====================================
# EXERCICE 5 : Temps avant le 1er janvier
# =====================================

maintenant = datetime.datetime.now()
prochain_janvier = datetime.datetime(2027, 1, 1)
difference = prochain_janvier - maintenant
print(f"Temps avant le 1er janvier : {difference}")


# =====================================
# EXERCICE 7 : Faker
# =====================================

fake = Faker()
users = []

def ajouter_users(nombre):
    for i in range(nombre):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)

ajouter_users(3)
print(users)