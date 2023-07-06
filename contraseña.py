import random

characters= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length=int(input("introduce la longuitud de la contraseña"))

password=""

for i in range(length):
    password+=random.choice(characters)
                            
print("esta es la contraseña generada aleatoriamente:",password)
