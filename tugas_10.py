# Latihan 

# 1. Tuple

# a. Membuat sebuah tuple yang berisi 3 data diri ( "Nama", "NIM", "Prodi" )
data_diri = ("Angga Dwi Safara", "2605060079", "Teknologi Informasi")
print(data_diri)

# b. Menampilkan data NIM dan Prodi dengan menggunakan indeks
print("NIM:", data_diri[1])
print("Prodi:", data_diri[2])

# c. Mengamati error yang muncul dan alasannya ketika menjalankan kode mahasiswa[2] = "Teknologi Informasi"
# mahasiswa[2] = "Teknologi Informasi"

# d. Membuat sebuah set
nilai_angka = {10, 4, 3, 2, 4, 10, 7, 5}
print("Nilai angka:", nilai_angka)

print("\n")

# 2. Manipulasi Dictionary

#a. Membuat sebuah dictionary bernama data_mahasiswa dengan key-value:
data_mahasiswa = {
    "nim": "2605060079",
    "nama": "Angga Dwi Safara",
    "prodi": "Teknologi Informasi"
}
print("Data mahasiswa:", data_mahasiswa)

# b. mengubah nilai "prodi" menjadi "Sastra Mesin"
data_mahasiswa["prodi"] = "Sastra Mesin"
print("Data mahasiswa :", data_mahasiswa)

# Menambah key baru "angkatan" dengan nilai 2026
data_mahasiswa["angkatan"] = 2026
print("Data mahasiswa :", data_mahasiswa)

# c. Menghapus data "nim" dan hasil akhir
del data_mahasiswa["nim"]
print("Data mahasiswa :", data_mahasiswa)

print("\n")

# 3. Perulangan pada Dictionary

#a. Membuat dictionary dengan data harga buah:
keranjang =  {"apel": 5000, "pisang": 3000, "jeruk": 7000, "anggur": 15000}

# Menampilkan setiap barang dan harganya menggunakan perulangan
for buah, harga in keranjang.items():
    print(f"Harga {buah} : Rp {harga}")
    
print("\n")

# c. Menampilkan total belanja
total_belanja = sum(keranjang.values())
print("Total belanja : Rp", total_belanja)