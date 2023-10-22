print("Menghitung Volume dan Luas Prisma Segitiga")

a = 25
T = 15
t = 10
s1 = 10
s2 = 5
s3 = 15

volume = a * t * T / 2
luas_sisi = (s1 + s2 + s3) * T
luas_permukaan = (s1 + s2 + s3) * T + a * t

print("Alas =",a)
print("Tinggi Prisma =", T)
print("Tinggi Alas =",t)
print("Luas Sisi 1 =",s1)
print("Luas Sisi 2 =",s2)
print("Luas Sisi 3 =",s3)
print("Volume =",volume)
print("Luas Sisi =",luas_sisi)
print("Luas Permukaan =",luas_permukaan) 