#Jum'at, 11 September 2026

#Nama : Angga Dwi Safara
#NPM : 2605060079
#Rombel : 2
#Matkul : Praktikum Algoritma Pemrograman


#LATIHAN
#Buatlah program yang meminta user memasukkan usia seseorang, lalu kategorikan usia tersebut berdasarkan kriteria berikut: 
#0 - 12 tahun: Anak-anak 
#13 - 17 tahun: Remaja 
#18 - 59 tahun: Dewasa 
#60 tahun ke atas: lansia

usia = int(input("Masukkan usia seseorang: "))
if usia >= 0 and usia <= 12:    
    print("Kategori: Anak-anak")
elif usia >= 13 and usia <= 17:
    print("Kategori: Remaja")
elif usia >= 18 and usia <= 59:
    print("Kategori: Dewasa")
else:
    print("Kategori: Lansia")   
