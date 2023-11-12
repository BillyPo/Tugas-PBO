import math

def hitung_luas_permukaan(jari_jari, tinggi_tabung):
    luas_permukaan = 2 * math.pi * jari_jari * (jari_jari + tinggi_tabung)
    return luas_permukaan

def hitung_volume(jari_jari, tinggi_tabung):
    volume = math.pi * (jari_jari ** 2) * tinggi_tabung
    return volume
