#================================
# MUHAMMAD KHAERIL ANWAR
# TUGAS PRAKTEK DASAR PEMROGRAMAN
#================================

def baris(nomor):
    global hlm
    hlm = nomor

def gajian():
    global tunJab, tunPend, lembur, gaji
    tunJab = jab * 300000
    tunPend = pend * 300000
    lembur = jamLembur * 3500
    gaji = 300000 + tunJab + tunPend + lembur

def hasil():
    print(54 * "-")
    print("\tKaryawan yang bernama", nama)
    print("\tHonor yang diterima")
    print("\t   Tunjangan Jabatan\t  Rp.", int(tunJab))
    print("\t   Tunjangan Pendidikan\t  Rp.", int(tunPend))
    print("\t   Honor lembur\t\t  Rp.", lembur)
    print("")
    print("\t   Total Gaji\t\t  Rp.", int(gaji))
    print("(Gaji pokok + tunjangan + lembur)")

hlm = 0
while True:
    if hlm == 0:
        print("PROGRAM HITUNG GAJI KARYAWAN".center(54))
        print(54 * "-")
        nama = input("\tNama Karyawan : ").upper()
        golJab = input("\t  Golongan Jabatan : ")
        if golJab == "1":
            jab = 0.05
            baris(1)
        elif golJab == "2":
            jab = 0.1
            baris(1)
        elif golJab == "3":
            jab = 0.15
            baris(1)
        else:
            print("Maaf, Anda salah memasukkan data")
            baris(0)
    
    elif hlm == 1:
        pendidikan = input("\t  Pendidikan\t   : ").upper()
        if pendidikan == "SMA":
            pend = 0.025
            baris(2)
        elif pendidikan == "D1":
            pend = 0.05
            baris(2)
        elif pendidikan == "D3":
            pend = 0.2
            baris(2)
        elif pendidikan == "S1":
            pend = 0.3
            baris(2)
        else:
            print(f"Tidak ada pilihan {pendidikan}")
            baris(1)

    elif hlm == 2:
        jamKerja = int(input("\t  Jumlah jam kerja : "))
        jamLembur = jamKerja - 8
        
        gajian()
        hasil()
        baris(3)

    elif hlm == 3:
        print("\nApakah anda ingin mengulang ? (Ya/Tidak)")
        ulang = input("Tulis disini : ")
        if ulang == "Ya":
            baris(0)
        elif ulang == "Tidak":
            print(f"-----SEMOGA HARI HARIMU MENYENANGKAN {nama}-----")
            break
        else:
            print("Maaf, anda salah input")
            hlm(3)