def hitung_luas_permukaan_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma):
    luas_permukaan_segitiga = (1/2) * alas_segitiga * tinggi_segitiga
    luas_permukaan = 3 * luas_permukaan_segitiga
    return luas_permukaan

def hitung_volume_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma):
    volume_segitiga = (1/6) * alas_segitiga * tinggi_segitiga
    volume = volume_segitiga * tinggi_prisma
    return volume
