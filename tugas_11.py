import datetime
import os
import string
import random

# Template dictionary buku
buku_template = {
    'judul_buku': 'judul',
    'penulis': 'penulis',
    'tahun_terbit': 0,
    'tanggal_terakhir_pinjam': datetime.datetime(1111, 1, 11),
    'status': 'TERSEDIA'
}

data_buku = {}

while True:

    # Membersihkan terminal
    os.system("cls" if os.name == "nt" else "clear")

    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'SISTEM MANAJEMEN PERPUSTAKAAN':^30}")
    print("-" * 50)

    # Membuat dictionary buku baru
    buku = dict.fromkeys(buku_template.keys())

    buku['judul_buku'] = input("Judul Buku: ")
    buku['penulis'] = input("Nama Penulis: ")
    buku['tahun_terbit'] = int(input("Tahun Terbit: "))

    TAHUN = int(input("Tahun Terakhir Pinjam: "))
    BULAN = int(input("Bulan Terakhir Pinjam: "))
    TANGGAL = int(input("Tanggal Terakhir Pinjam: "))

    buku['tanggal_terakhir_pinjam'] = datetime.datetime(
        TAHUN, BULAN, TANGGAL
    )

    print("\nStatus Buku:")
    print("1. TERSEDIA")
    print("2. TIDAK")

    status_buku = input("Pilih Status (1/2): ")

    if status_buku == "1":
        buku['status'] = "TERSEDIA"
    else:
        buku['status'] = "TIDAK"

    # Membuat KEY buku secara otomatis
    KEY = ''.join(
        random.choice(string.ascii_uppercase)
        for i in range(6)
    )

    data_buku.update({KEY: buku})

    # Menampilkan data buku
    print("\nDATA BUKU PERPUSTAKAAN")
    print("-" * 100)

    print(
        f"{'KEY':<8} "
        f"{'JUDUL BUKU':<20} "
        f"{'PENULIS':<18} "
        f"{'TAHUN':<8} "
        f"{'TERAKHIR PINJAM':<18} "
        f"{'STATUS':<12}"
    )

    print("-" * 100)

    for buku in data_buku:

        KEY = buku

        JUDUL = data_buku[KEY]['judul_buku']
        PENULIS = data_buku[KEY]['penulis']
        TAHUN = data_buku[KEY]['tahun_terbit']
        PINJAM = data_buku[KEY]['tanggal_terakhir_pinjam'].strftime("%d-%m-%Y")
        STATUS = data_buku[KEY]['status']

        print(
            f"{KEY:<8} "
            f"{JUDUL:<20} "
            f"{PENULIS:<18} "
            f"{TAHUN:<8} "
            f"{PINJAM:<18} "
            f"{STATUS:<12}"
        )

    print("\n")

    is_done = input("Mau tambah buku lagi bro (y/n)? ")

    if is_done.lower() == "n":
        break

print("\nAkhir dari program, terima kasih")
