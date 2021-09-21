
#           ==========NOMOR 1==========

print("TUGAS MATA KULIAH LOGIKA ALGORITMA".center(56, "="))
# VARIABEL
uang = int(input("Berapa uang yang di bawa ibu ke pasar : "))
berat = int(input("Berapa kg telur yang ingin ibu beli : "))
harga = int(input("Harga telur perkilogram : "))
ongkos = int(input("Harga transport ibu ke pasar : "))
# OPERASI
sisa = uang - ((harga * berat) + (2 * ongkos))
print(f"\nHasil sisa uang yang dibawa ibu ke pasar adalah Rp.{sisa}")

#           ==========NOMOR 2==========

print("TUGAS MATA KULIAH LOGIKA ALGORITMA".center(56, "="))
print((34 * "=").center(56))
print("\n=> HARGA MANGGA PER KG = 12.000")
# MEMASUKKAN DATA
berat = int(input("Mangga yang dibeli per kg : "))
harga = int(input("Harga mangga per kg : "))
# OPERASI
bayar = harga * berat
print(f"\nUang yang harus dibayar oleh pembeli adalah Rp.{bayar}")

#           ==========NOMOR 3==========

# TIPE DATA BOOLEAN
data = True
print(data)

# TIPE DATA STRING
kalimat = "Anwar kuliah di UBSI Kampus Tegal"
print(kalimat)

# TIPE DATA INTEGER
angka = 1402
print(angka)

# TIPE DATA FLOAT
angka = 2002.19
print(angka)

# TIPE DATA HEXADECIMAL
# print(9a)

# TIPE DATA LIST
data = ["Khaeril", 1992, 89.56]
print(data)

# TIPE DATA TUPLE
data = ("Python", 1981, True, 18.2, "C++")
print(data)

# TIPE DATA DICTIONARY
data = {'nama':'Anwar', 'usia':19}
print(data)

# TIPE DATA DICTIONARY DALAM VARIABEL BIODATA
biodata = {'nama':'Muhammad Khaeril Anwar', 'NIM':12210952, 'nilai':96.5}
print(f"""{"BIODATA SAYA".center(32, '=')}

Nama\t: {biodata['nama']}
NIM\t: {biodata['NIM']}
Nilai\t: {biodata['nilai']}""")

#           ==========NOMOR 4==========

# OPERATOR ARITMATIKA PENJUMLAHAN
penjumlahan = 19 + 9
print(penjumlahan)

# OPERATOR ARITMATIKA PENGURANGAN
pengurangan = 19 - 9
print(pengurangan)

# OPERATOR ARITMATIKA PERKALIAN
perkalian = 19 * 9
print(perkalian)

# OPERATOR ARITMATIKA PEMBAGIAN
pembagian = 20 / 4
print(pembagian)

# OPERATOR ARITMATIKA MODULUS
modulus = 19 % 4
print(modulus)

# OPERATOR ARITMATIKA PANGKAT
pangkat = 2 ** 4
print(pangkat)
