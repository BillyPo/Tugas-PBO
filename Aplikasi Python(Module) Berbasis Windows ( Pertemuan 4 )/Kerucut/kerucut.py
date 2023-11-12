import math

def hitung_luas_permukaan(jari_jari, tinggi):
    sisi_miring = math.sqrt((jari_jari ** 2) + (tinggi ** 2))
    luas_permukaan = math.pi * jari_jari * (jari_jari + sisi_miring)
    return luas_permukaan

def hitung_volume(jari_jari, tinggi):
    volume = (1/3) * math.pi * (jari_jari ** 2) * tinggi
    return volume
