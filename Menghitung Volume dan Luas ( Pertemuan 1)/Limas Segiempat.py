print("Menghitung Volume dan Luas Limas Segiempat (persegi panjang)")

panjang = 40
lebar = 25
tinggi = 30
tinggiST = 45


volume = (panjang * lebar * tinggi) / 3
luas = (panjang * lebar) + 2 * ((panjang * tinggiST) / 3) + 2 * ((lebar * tinggiST) / 3)

print("Panjang =",panjang)
print("Lebar =",lebar)
print("Tinggi =",tinggi)
print("Tinggi Sisi =",tinggiST)
print("Volume =",volume)
print("Luas =",luas)