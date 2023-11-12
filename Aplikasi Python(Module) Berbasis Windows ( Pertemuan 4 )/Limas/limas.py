def hitung_luas_permukaan_segiempat(alas, tinggi_limas):
    luas_permukaan = alas**2 + 4 * (alas * tinggi_limas) / 2
    return luas_permukaan

def hitung_volume_segiempat(alas, tinggi_limas):
    volume = (alas**2 * tinggi_limas) / 3
    return volume

def hitung_luas_permukaan_segitiga(alas, tinggi_limas):
    luas_permukaan = (alas * alas) + (3 * (alas * tinggi_limas) / 2)
    return luas_permukaan

def hitung_volume_segitiga(alas, tinggi_limas):
    volume = (alas ** 2 * tinggi_limas) / 6
    return volume
