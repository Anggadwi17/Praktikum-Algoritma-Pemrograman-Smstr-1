# Program 3.1 Menampilkan output dari operasi aritmatika sederhana
# Operasi aritmatika

a = 10
b = 3

# operasi tambah +
hasil = 10 + 3
print(10, "+", 3, "=", hasil)

# operasi kurang -
hasil = 10 - 3
print(10, "-", 3, "=", hasil)

# operasi perkalian *
hasil = 10 * 3
print(10, "*", 3, "=", hasil)

# operasi pembagian /
hasil = 10 / 3
print(10, "/", 3, "=", hasil)

# operasi eksponen (pangkat) **
hasil = 10 ** 3
print(10, "**", 3, "=", hasil)

# operasi modulus %
hasil = 10 % 3
print(10, "%", 3, "=", hasil)

# operasi floor division //
hasil = 10 // 3
print(10, "//", 3, "=", hasil)


# Program 3.2 konversi celcius ke satuan lain
# latihan konversi satuan temperature
# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input("Masukan suhu dalam celcius : "))
print("suhu adalah", celcius, "Celcius")

# reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")

# fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")


# Program 3.3 Operasi komperasi
# operasi komperasi
# setiap hasil dari operasi komperasi adalah boolean
# >,<,>=,<=,==,!=,is,is not

a = 4
b = 2

# lebih besar dari >
print("=============== lebih besar dari (>)")
hasil = a > 3
print(a,">",b,"=",hasil)

hasil = b > 3
print(b,">",3,"=",hasil)

hasil = b > 2
print(b,">",2,"=",hasil)


# kurang dari <
print("=============== kurang dari (<)")
hasil = a < 3
print(a,"<",b,"=",hasil)

hasil = b < 3
print(b,"<",3,"=",hasil)

hasil = b < 2
print(b,"<",2,"=",hasil)


# lebih dari sama dengan >=
print("=============== lebih dari sama dengan (>=)")

hasil = a >= 3
print(a,">=",b,"=",hasil)

hasil = b >= 3
print(b,">=",3,"=",hasil)

hasil = b >= 2
print(b,">=",2,"=",hasil)


# kurang dari sama dengan <=
print("=============== kurang dari sama dengan (<=)")

hasil = a <= 3
print(a,"<=",b,"=",hasil)

hasil = b <= 3
print(b,"<=",3,"=",hasil)

hasil = b <= 2
print(b,"<=",2,"=",hasil)


# sama dengan (==)
print("=============== sama dengan (==)")

hasil = a == 4
print(a,"==",4,"=",hasil)

hasil = b == 4
print(b,"==",4,"=",hasil)


# tidak sama dengan (!=)
print("=============== sama dengan (!=)")

hasil = a != 4
print(a,"!=",4,"=",hasil)

hasil = b != 4
print(b,"!=",4,"=",hasil)


# "is" sebagai komparasi obj identity (bukan literal)
x = 5 # ini adalah assignment membuat object
y = 5
hasil = x is y
print("x is y =",hasil)


# "is not" sebagai komparasi obj identity (bukan literal)
x = 5 # ini adalah assignment membuat object
y = 6
hasil = x is not y
print("x is not y =",hasil)