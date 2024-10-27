import random
import time

karakterler="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parola_uzunlugu=int(input("Parola kaç karakterli olsun?:"))
parola=""

for i in range(parola_uzunlugu):
    parola+=random.choice(karakterler)

print(parola)
time.sleep(2)
print("Şimdi sizin robot olup olmadığınızı tespit etmek için bir kod göndereceğiz.")
kod_uzunlugu = int(input("Kodunuz kaç karakterden oluşsun?:"))
kod = ""

for i in range(kod_uzunlugu):
    kod+=random.choice(karakterler)

print(kod)
x = input("Kodunuzu giriniz:")

if x == kod:
    print("İşlem başarıyla tamamlandı!")

else:
    print("Robot musunuz?")

