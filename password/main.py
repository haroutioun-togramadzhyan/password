import random
import string
import hashlib
import json

def is_valid_password(password):
    return (
        len(password) >= 8 and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char.isdigit() for char in password) and
        any(char in "!@#$%^&*" for char in password)
    )

def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = "!@#$%^&*"
    all_chars = letters + digits + special_chars

    while True:
        password = ''.join(random.choice(all_chars) for _ in range(12))
        if is_valid_password(password):
            return password

def hash_password(password):

    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    hashed_password = sha256.hexdigest()
    return hashed_password


print("Pour créer un bon mot de passe, assurez-vous qu'il respecte les critères suivants :")
print("- Il doit contenir au moins huit caractères.")
print("- Il doit contenir au moins une lettre majuscule.")
print("- Il doit contenir au moins une lettre minuscule.")
print("- Il doit contenir au moins un chiffre.")
print("- Il doit contenir au moins un caractère spécial (!, @, #, $, %, ^, &, *).\n")


user_password = input("Veuillez entrer votre mot de passe : ")


hashed_password = hash_password(user_password)


while not is_valid_password(user_password):
    print("Mot de passe invalide ! Assurez-vous qu'il respecte les exigences de sécurité.")
    user_password = input("Veuillez entrer un mot de passe valide : ")


secure_password = generate_password()
print("Mot de passe sécurisé généré :", secure_password)


data = {"hashed_password": hashed_password}
with open("passwords.json", "w") as json_file:
    json.dump(data, json_file)

print("Mot de passe haché enregistré dans passwords.json")
