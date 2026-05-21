# Aplikasi Mnajemen dan Tracking Kegiatan Freelance
#Deskripsi 
#A plikasi ini digunakan untuk membantu freelancer dalam mencatat, mengelola, dan memantau proyek yang sedang maupun telah dikerjakan. Sistem menyimpan data proyek seperti nama proyek, nama klien, deadline, pembayaran, dan status pengerjaan sehingga pengguna dapat memantau perkembangan pekerjaan dengan lebih mudah dan terstruktur.

dataProyek = []

# ================= TAMBAH PROYEK =================
def tambahProyek():
    print("\n========= Tambah Proyek ==========")

    idProyek = input("Masukkan ID Proyek : ")
    namaProyek = input("Masukkan Nama Proyek : ")
    namaKlien = input("Masukkan Nama Klien : ")

    print("Format deadline : YYYY-MM-DD")
    deadline = input("Masukkan Deadline : ")

    pembayaran = int(input("Masukkan Pembayaran : "))
    status = input("Masukkan Status : ")

    proyek = {
        "id": idProyek,
        "nama": namaProyek,
        "klien": namaKlien,
        "deadline": deadline,
        "bayar": pembayaran,
        "status": status,
    }

    dataProyek.append(proyek)
    print("Proyek berhasil ditambahkan!\n")


# ================= TAMPIL DATA =================
def tampilData():
    print("\n=========== Data Proyek ============")

    if len(dataProyek) == 0:
        print("Belum ada data proyek\n")
    else:
        for proyek in dataProyek:
            print("----------------------------")
            print("ID Proyek :", proyek["id"])
            print("Nama Proyek :", proyek["nama"])
            print("Nama Klien :", proyek["klien"])
            print("Deadline :", proyek["deadline"])
            print("Pembayaran :", proyek["bayar"])
            print("Status :", proyek["status"])
        print()


# ================= UBAH PROYEK =================
def ubahProyek():
    cari = input("Masukkan ID proyek yang ingin diubah : ")

    ditemukan = False

    for proyek in dataProyek:
        if proyek["id"] == cari:

            proyek["nama"] = input("Nama proyek baru : ")
            proyek["klien"] = input("Nama klien baru : ")
            proyek["deadline"] = input("Deadline baru : ")
            proyek["bayar"] = int(input("Pembayaran baru : "))
            proyek["status"] = input("Status baru : ")

            print("Data berhasil diubah\n")
            ditemukan = True
            break

    if ditemukan == False:
        print("Data tidak ditemukan\n")


# ================= HAPUS PROYEK =================
def hapusProyek():
    cari = input("Masukkan ID proyek yang ingin dihapus : ")

    ditemukan = False

    for proyek in dataProyek:
        if proyek["id"] == cari:
            dataProyek.remove(proyek)
            print("Data berhasil dihapus\n")
            ditemukan = True
            break

    if ditemukan == False:
        print("Data tidak ditemukan\n")


# ================= SEQUENTIAL SEARCH =================
def sequentialSearch():
    cari = input("Cari nama proyek/klien : ").lower()
    ketemu = False

    for proyek in dataProyek:
        if cari in proyek["nama"].lower() or cari in proyek["klien"].lower():
            print("\nData ditemukan")
            print("----------------------------")
            print("ID Proyek :", proyek["id"])
            print("Nama Proyek :", proyek["nama"])
            print("Nama Klien :", proyek["klien"])
            print("Deadline :", proyek["deadline"])
            print("Pembayaran :", proyek["bayar"])
            print("Status :", proyek["status"])
            ketemu = True
    if ketemu == False:
        print("Data tidak ditemukan\n")

# ================= BINARY SEARCH =================
def binarySearch():
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
            print("ID Proyek :", dataProyek[tengah]["id"])
            print("Nama Proyek :", dataProyek[tengah]["nama"])
            print("Nama Klien :", dataProyek[tengah]["klien"])
            print("Deadline :", dataProyek[tengah]["deadline"])
            print("Pembayaran :", dataProyek[tengah]["bayar"])
            print("Status :", dataProyek[tengah]["status"])
            return
        elif namaTengah < cari:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
    print("Data tidak ditemukan\n")


# ================= SELECTION SORT =================
def selectionSort():
    for i in range(len(dataProyek)):
        maxIndex = i
        for j in range(i + 1, len(dataProyek)):
            if dataProyek[j]["bayar"] > dataProyek[maxIndex]["bayar"]:
                maxIndex = j
        dataProyek[i], dataProyek[maxIndex] = dataProyek[maxIndex], dataProyek[i]
    print("Data berhasil diurutkan berdasarkan pembayaran terbesar\n")


# ================= INSERTION SORT =================
def insertionSort():
    for i in range(1, len(dataProyek)):
        dataSementara = dataProyek[i]
        j = i - 1
        while j >= 0 and dataProyek[j]["deadline"] > dataSementara["deadline"]:

            dataProyek[j + 1] = dataProyek[j]

            j -= 1
        dataProyek[j + 1] = dataSementara
    print("Data berhasil diurutkan berdasarkan deadline\n")


# ================= UPDATE STATUS =================
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
            print("Status berhasil diupdate\n")
            ditemukan = True
            break
    if ditemukan == False:
        print("Data tidak ditemukan\n")


# ================= LAPORAN =================
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
    print("Proyek selesai :", proyekSelesai)
    print("Proyek berjalan :", proyekBerjalan)
    print("Total pendapatan :", totalPendapatan)
    print()

# ================= MENU UTAMA =================
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


    


        
