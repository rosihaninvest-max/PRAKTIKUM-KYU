#prktikum 1
kalimat = "ini adalah contoh kalimat untuk menghitung frekuensi kata"
kata_frekuensi = {}

for kata in kalimat.split():
    if kata in kata_frekuensi:
        kata_frekuensi[kata] += 1
    else:
        kata_frekuensi[kata] = 1

print(kata_frekuensi)



print("===========================")
#prkatikum 2

print("=" * 5, "CONTOH 1", "=" * 5)
# tipe data:set(himpunan)
StokMobil = {"Toyot",
             "Kijang",
             "Karimun",
             "Daihatsu"}

StokMobil.add("Hyundai")
StokMobil.add("Daihatsu")
StokMobil.add("Daihatsuu")

print(StokMobil)
print("\n")
#contoh 2

print("=" * 5, "CONTOH 2", "=" * 5)
kendaraan = set()

kendaraan.add("sepeda")
kendaraan.add("Mobil")
kendaraan.add("Pesawat")
kendaraan.add("Kapal Laut")
kendaraan.add("Dokar")

print(kendaraan)
print(sorted(kendaraan))
print("\n")

#contoh 3
print("=" * 5, "CONTOH 3", "=" * 5)
Barang = set()

Barang.add("Tang")
Barang.add("Obeng")
Barang.add("Martil")
Barang.add("Pencabut Paku")
Barang.add("Kayu")
Barang.add(12345)

print(Barang)

print("\n")

#contoh 4

print("=" * 5, "CONTOH 4", "=" * 5)

Bilangan_Ganjil = {1, 3, 5, 7, 9,}
Bilangan_Genap = {2, 4, 6, 8, 10}
Bilangan_Prima = {2, 3, 5, 7}

print(Bilangan_Ganjil.union(Bilangan_Genap))
print(Bilangan_Ganjil.intersection(Bilangan_Genap))
print(Bilangan_Ganjil.intersection(Bilangan_Prima))
O
x
