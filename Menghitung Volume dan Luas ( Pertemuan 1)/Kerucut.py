print("Menghitung Volume dan Luas Kerucut")

r = 50
T = 120
s = 30

volume = 3.14 * r**2 * T / 3
ls = 3.14 * r * s
lp = ls + (3.14 * r**2)

print("Radius =",r)
print("Tinggi Kerucut =",T)
print("Garis Pelukis =",s)
print("Volume =",volume)
print("Luas Selimut =",ls)
print("Luas Permukaan =",lp)