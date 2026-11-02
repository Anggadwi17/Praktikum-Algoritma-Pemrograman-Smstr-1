#Latihan

#1. ( manipulasi list )

# Diberikan list berikut: 
#kendaraan = ['motor', 'mobil', 'sepeda', 'bus'] 
#a. Tambahkan 'truk' di akhir list 
data_kendaraan = kendaraan = ['motor', 'mobil', 'sepeda', 'bus'] 
print(f"data awal = {kendaraan}")
kendaraan.append('truk') 
print(f"a. data setelah menambahkan 'truk' di akhir list= {kendaraan}") 

#b. Sisipkan 'becak' pada index ke-1 
kendaraan.insert(1, 'becak') 
print(f"b. data setelah menyisipkan 'becak' pada index ke-1= {kendaraan}") 

#c. Hapus data yang berada paling belakang dari list tersebut. 
kendaraan.pop() 
print(f"c. data setelah menghapus data yang berada paling belakang dari list tersebut= {kendaraan}") 

#d. Ubah elemen 'sepeda' menjadi 'skuter'. 
kendaraan[3] = 'skuter' 
print(f"d. data setelah mengubah elemen 'sepeda' menjadi 'skuter'= {kendaraan}") 

#e. Tampilkan informasi jumlah total data di dalam list tersebut
print(f"e. Jumlah total data: {len(kendaraan)}")

print("\n")

#2. ( operasi list )
# Diberikan list berikut: 
#angka = [75, 80, 90, 75, 85, 100, 65] 
#a. Cari tahu di indeks ke berapa skor 100 berada. 
data_angka = angka = [75, 80, 90, 75, 85, 100, 65]
print(f"a. Indeks skor 100: {angka.index(100)}")

#b. Hitung ada berapa banyak siswa yang mendapatkan skor 75.
print(f"b. Banyak siswa yang mendapatkan skor 75: {angka.count(75)}")

#c. Urutkan list skor_ujian tersebut dari nilai terkecil hingga terbesar. 
angka.sort()
print(f"c. List setelah diurutkan: {angka}")

#d. Balikkan urutan list yang sudah diurutkan tersebut sehingga menjadi dari terbesar ke terkecil.
angka.reverse()
print(f"d. List setelah dibalik: {angka}")

print("\n")

#3. ( menggabungkan list )

#data
menu_utama = ["Nasi Goreng", "Mie Ayam"] 
menu_tambahan = ["Kerupuk", "Es Teh"] 

#fungsi yang digunakan untuk menggabungkan menu_tambahan ke dalam menu_utama
menu_utama.extend(menu_tambahan)

#menampilkan hasil dari data gabungan
print(f"3. Menu gabungan: {menu_utama}")

print("\n")

# 4. ( nested list )
#data
data_barang = [["Buku", 5000], ["Pensil", 2000], ["Penggaris", 3000]]

# a. Tampilkan harga dari "Pensil" (yaitu 2000)
Harga_Pensil = data_barang[1][1]
print(f"a. Harga dari Pensil adalah: {Harga_Pensil}")

#b. membaca data satu per satu menggunakan perulangan
print("b. Data barang satu per satu:")
for barang in data_barang:
    print(f"Nama: {barang[0]}, Harga: {barang[1]}")
