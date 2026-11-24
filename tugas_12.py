# A. FUNGSI LUAS PERSEGI PANJANG
import math


def luas_persegi_panjang(panjang, lebar):
    hasil = panjang * lebar
    return hasil


# B. FUNGSI VOLUME BALOK
def volume_balok(panjang, lebar, tinggi):
    hasil = panjang * lebar * tinggi
    return hasil


# C. FUNGSI LUAS LINGKARAN
def luas_lingkaran(jari_jari):
    hasil = math.pi * jari_jari ** 2
    return hasil


# D. FUNGSI VOLUME BOLA
def volume_bola(jari_jari):
    hasil = (4/3) * math.pi * jari_jari ** 3
    return hasil


print(" PROGRAM MENGHITUNG LUAS DAN VOLUME")

# A. Menghitung luas persegi panjang
print("\nA. LUAS PERSEGI PANJANG")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

hasil = luas_persegi_panjang(panjang, lebar)
print(f"Luas persegi panjang = {hasil}")


# B. Menghitung volume balok
print("\nB. VOLUME BALOK")
panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))
tinggi = float(input("Masukkan tinggi: "))

hasil = volume_balok(panjang, lebar, tinggi)
print(f"Volume balok = {hasil}")


# C. Menghitung luas lingkaran
print("\nC. LUAS LINGKARAN")
jari_jari = float(input("Masukkan jari-jari: "))

hasil = luas_lingkaran(jari_jari)
print(f"Luas lingkaran = {hasil:.2f}")


# D. Menghitung volume bola
print("\nD. VOLUME BOLA")
jari_jari = float(input("Masukkan jari-jari: "))

hasil = volume_bola(jari_jari)
print(f"Volume bola = {hasil:.2f}")

print("\n")

print("PROGRAM SELESAI")