# Aplikasi Manajemen dan Tracking Kegiatan Freelance
# Deskripsi:
# Aplikasi ini digunakan untuk membantu freelancer dalam mencatat, mengelola, dan memantau
# proyek yang sedang maupun telah dikerjakan. Sistem menyimpan data proyek seperti nama proyek,
# nama klien, deadline, pembayaran, dan status pengerjaan sehingga pengguna dapat memantau
# perkembangan pekerjaan dengan lebih mudah dan terstruktur.

import json # Penambahan
from datetime import datetime # Penambahan

FILE = "data_proyek.json" # Penambahan

dataProyek = []


# Validasi ID
def inputID(x): # Penambahan
    while True:
        nilai = input(x).strip()
        if nilai == "":
            print("ID tidak boleh kosong!")
        elif not nilai.isalnum():
            print("ID hanya boleh berisi huruf dan angka!")
        else:
            return nilai


# Validasi Pembayaran
def inputPembayaran(x): # Penambahan
    while True:
        try:
            nilai = int(input(x))
            if nilai < 0:
                print("Pembayaran tidak boleh negatif!")
            else:
                return nilai
        except ValueError:
            print("Masukkan angka yang valid!")


# Validasi Deadline
def inputDeadline(x): # Penambahan
    while True:
        nilai = input(x).strip()
        try:
            datetime.strptime(nilai, "%d/%m/%Y")  # validasi format DD/MM/YYYY
            return nilai
        except ValueError:
            print("Format deadline salah! Gunakan format DD/MM/YYYY (contoh: 25/12/2025)")


# Tambah Proyek
def tambahProyek():
    print("\n========= Tambah Proyek ==========")

    idProyek = inputID("Masukkan ID Proyek : ")
    namaProyek = input("Masukkan Nama Proyek : ")
    namaKlien = input("Masukkan Nama Klien : ")

    print("Format deadline : DD/MM/YYYY")
    deadline = inputDeadline("Masukkan Deadline : ") # Perubahan

    pembayaran = inputPembayaran("Masukkan Pembayaran : ") # Perubahan
    status = input("Masukkan Status(Pending/Dikerjakan/Revisi/Selesai) : ")

    proyek = {
        "id": idProyek,
        "nama": namaProyek,
        "klien": namaKlien,
        "deadline": deadline,
        "bayar": pembayaran,
        "status": status,
    }

    for p in dataProyek: # Penambahan
        if p["id"] == idProyek:
            print("ID sudah digunakan! Gunakan ID lain.\n")
            return
            
    dataProyek.append(proyek)
    simpanData() # Penambahan
    print("Proyek berhasil ditambahkan!\n")


# Menampilkan Data
def tampilData():
    print("\n=========== Data Proyek ============")

    if len(dataProyek) == 0:
        print("Belum ada data proyek\n")
    else:
        for proyek in dataProyek:
            print("----------------------------")
            print("ID Proyek  :", proyek["id"])
            print("Nama Proyek:", proyek["nama"])
            print("Nama Klien :", proyek["klien"])
            print("Deadline   :", proyek["deadline"])
            print("Pembayaran :", proyek["bayar"])
            print("Status     :", proyek["status"])
        print()


# Mengubah Proyek
def ubahProyek():
    cari = input("Masukkan ID proyek yang ingin diubah : ")

    ditemukan = False

    for proyek in dataProyek:
        if proyek["id"] == cari:

            proyek["nama"] = input("Nama proyek baru : ")
            proyek["klien"] = input("Nama klien baru : ")
            print("Format deadline : DD/MM/YYYY")
            proyek["deadline"] = inputDeadline("Deadline baru : ")
            proyek["bayar"] = inputPembayaran("Pembayaran baru : ")
            proyek["status"] = input("Status baru : ")

            print("Data berhasil diubah\n")
            simpanData() # Penambahan
            ditemukan = True
            break

    if ditemukan == False:
        print("Data tidak ditemukan\n")


# Menghapus Proyek
def hapusProyek():
    cari = input("Masukkan ID proyek yang ingin dihapus : ")

    ditemukan = False

    for proyek in dataProyek:
        if proyek["id"] == cari:
            dataProyek.remove(proyek)
            simpanData() # Penambahan
            print("Data berhasil dihapus\n")
            ditemukan = True
            break

    if ditemukan == False:
        print("Data tidak ditemukan\n")


# Sequential Search
def sequentialSearch():
    cari = input("Cari nama proyek/klien : ").lower()
    ketemu = False

    for proyek in dataProyek:
        if cari in proyek["nama"].lower() or cari in proyek["klien"].lower():
            print("\nData ditemukan")
            print("----------------------------")
            print("ID Proyek  :", proyek["id"])
            print("Nama Proyek:", proyek["nama"])
            print("Nama Klien :", proyek["klien"])
            print("Deadline   :", proyek["deadline"])
            print("Pembayaran :", proyek["bayar"])
            print("Status     :", proyek["status"])
            ketemu = True

    if ketemu == False:
        print("Data tidak ditemukan\n")


# Binary Search
def binarySearch():
    if len(dataProyek) == 0:
        print("Belum ada data proyek\n")
        return

    dataProyek.sort(key=lambda x: x["nama"].lower())
    cari = input("Masukkan nama proyek : ").lower()
    kiri = 0
    kanan = len(dataProyek) - 1

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        namaTengah = dataProyek[tengah]["nama"].lower()

        if namaTengah == cari:
            print("\nData ditemukan")
            print("----------------------------")
            print("ID Proyek  :", dataProyek[tengah]["id"])
            print("Nama Proyek:", dataProyek[tengah]["nama"])
            print("Nama Klien :", dataProyek[tengah]["klien"])
            print("Deadline   :", dataProyek[tengah]["deadline"])
            print("Pembayaran :", dataProyek[tengah]["bayar"])
            print("Status     :", dataProyek[tengah]["status"])
            return
        elif namaTengah < cari:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    print("Data tidak ditemukan\n")


# Selection Sort
def selectionSort():
    for i in range(len(dataProyek)):
        maxIndex = i
        for j in range(i + 1, len(dataProyek)):
            if dataProyek[j]["bayar"] > dataProyek[maxIndex]["bayar"]:
                maxIndex = j
        dataProyek[i], dataProyek[maxIndex] = dataProyek[maxIndex], dataProyek[i]
    print("Data berhasil diurutkan berdasarkan pembayaran terbesar\n")


# Insertion Sort
def insertionSort():
    for i in range(1, len(dataProyek)):
        dataSementara = dataProyek[i]
        tglSementara = datetime.strptime(dataSementara["deadline"], "%d/%m/%Y") # Penambahan
        j = i - 1

        while j >= 0 and datetime.strptime(dataProyek[j]["deadline"], "%d/%m/%Y") > tglSementara: # Penambahan
            dataProyek[j + 1] = dataProyek[j]
            j -= 1

        dataProyek[j + 1] = dataSementara
    print("Data berhasil diurutkan berdasarkan deadline (terlama ke terbaru)\n")


# Update Status
def updateStatus():
    cari = input("Masukkan ID proyek : ")
    ditemukan = False

    for proyek in dataProyek:
        if proyek["id"] == cari:
            print("1. Pending")
            print("2. Dikerjakan")
            print("3. Revisi")
            print("4. Selesai")

            pilih = input("Pilih status : ")
            if pilih == "1":
                proyek["status"] = "Pending"
            elif pilih == "2":
                proyek["status"] = "Dikerjakan"
            elif pilih == "3":
                proyek["status"] = "Revisi"
            elif pilih == "4":
                proyek["status"] = "Selesai"
            else:
                print("Pilihan tidak tersedia")
                return
            
            print("Status berhasil diupdate\n") # Perubahan
            simpanData() # Penambahan
            ditemukan = True
            break

    if ditemukan == False:
        print("Data tidak ditemukan\n")


# Laporan
def laporan():
    proyekSelesai = 0
    proyekBerjalan = 0
    totalPendapatan = 0

    for proyek in dataProyek:
        totalPendapatan += proyek["bayar"]
        if proyek["status"].lower() == "selesai":
            proyekSelesai += 1
        else:
            proyekBerjalan += 1

    print("\n============ Laporan Proyek =============")
    print("Proyek selesai  :", proyekSelesai)
    print("Proyek berjalan :", proyekBerjalan)
    print("Total pendapatan:", totalPendapatan)
    print()


# Memuat data
def muatData(): # Penambahan
    global dataProyek
    try:
        with open(FILE, "r") as f:
            dataProyek = json.load(f)
    except FileNotFoundError:
        dataProyek = []

# Menyimpan Data
def simpanData(): # Penambahan
    with open(FILE, "w") as f:
        json.dump(dataProyek, f, indent=2)

muatData()

# Menu Utama
while True:
    print("========== Menu Program ==========")
    print("1. Tambah Proyek")
    print("2. Tampilkan Proyek")
    print("3. Ubah Proyek")
    print("4. Hapus Proyek")
    print("5. Sequential Search")
    print("6. Binary Search")
    print("7. Selection Sort")
    print("8. Insertion Sort")
    print("9. Update Status")
    print("10. Laporan")
    print("0. Keluar")

    menu = input("Pilih menu : ")
    if menu == "1":
        tambahProyek()
    elif menu == "2":
        tampilData()
    elif menu == "3":
        ubahProyek()
    elif menu == "4":
        hapusProyek()
    elif menu == "5":
        sequentialSearch()
    elif menu == "6":
        binarySearch()
    elif menu == "7":
        selectionSort()
    elif menu == "8":
        insertionSort()
    elif menu == "9":
        updateStatus()
    elif menu == "10":
        laporan()
    elif menu == "0":
        print("Program selesai")
        break
    else:
        print("Menu tidak tersedia\n")
