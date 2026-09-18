#Latihan

#1. Buat program yang menampilkan bilangan ganjil dan genap dari 1 sampai 50 menggunakan perulangan! 
#2. Buat program yang menampilkan semua bilangan prima antara 1 sampai 100 menggunakan perulangan!

#1. Program yang menampilkan Bilangan ganjil dan genap dari 1 sampai 50
for i in range(1, 51):
    if i % 2 == 0:
        print(f"{i} adalah bilangan genap")

for i in range(1, 51):
    if i % 2 != 0:
        print(f"{i} adalah bilangan ganjil")


#2. Program yang menampilkan Bilangan prima 1 - 100
for angka in range(2, 101):
    prima = True
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            prima = False
            break
    if prima:
        print(f"{angka} adalah bilangan prima")