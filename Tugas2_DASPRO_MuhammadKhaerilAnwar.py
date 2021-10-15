#==============================
# MUHAMMAD KHAERIL ANWAR
# TUGAS 2 PERTEMUAN 5
# PROGRAM GEROBAK FRIED CHICKEN
# MATA KULIAH DASAR PEMROGRAMAN
#==============================

# PRINT OUT AWAL
print("GEROBAK FRIED CHICKEN".center(30))
print("KODE\tJENIS POTONG\tHARGA")
print("--------------------------------")
print(" D\t Dada\t\tRp.2500")
print(" P\t Paha\t\tRp.2000")
print(" S\t Sayap\t\tRp.1500")
print("---------------------------------")
print("")
# INPUT USER
banyakJenis = int(input("Banyak Jenis : "))

# VARIABEL LIST KOSONG
kodePotong = []
jenisPotong = []
banyakPotong = []
harga = []
jumlah = []

# LOOPING FOR
for u in range(banyakJenis):
    print("Jenis Ke -", u+1)
    kopot = input("Kode Potong [D/P/S] : ").upper()
    bapot = int(input("Banyak Potong\t    : "))
    kodePotong.append(kopot)
    banyakPotong.append(bapot)
    if kopot == "D":
        jenisPotong.append("Dada")
        harga.append(2500)
        jumlah.append(2500 * bapot)
    elif kopot == "P":
        jenisPotong.append("Paha")
        harga.append(2000)
        jumlah.append(2000 * bapot)
    elif kopot == "S":
        jenisPotong.append("Sayap")
        harga.append(1500)
        jumlah.append(1500 * bapot)
    else:
        jenisPotong.append("-")
        harga.append(0)
        jumlah.append(0)

# PRINTOUT HASIL PROGRAM
print("")
print("GEROBAK FRIED CHICKEN".center(43))
print(43 * "-")
print("No.\tJenis\tHarga\tBanyak\tJumlah")
print("\tPotong\tSatuan\tBeli\tHarga")
print(43 * "-")

# LOOPING UNTUK HASIL
i = 0
while i < banyakJenis:
    print("{}\t{}\t{}\t{}\tRp. {}".format((i+1), jenisPotong[i], harga[i], banyakPotong[i], jumlah[i]))
    i += 1
print(43 * "-")

# OPERASI HITUNG HARGA
jumlahBayar = sum(jumlah)
pajak = jumlahBayar * (10/100)
totalBayar = jumlahBayar + pajak

# LANJUTAN PRINT OUT HASIL
print("\t\t  Jumlah Bayar  Rp.", jumlahBayar)
print("\t\t  Pajak 10%\tRp.", int(pajak))
print("\t\t  Total Bayar   Rp.", int(totalBayar))