import tkinter as tk
import bola

def hitung():
        jari_jari = float(entry_jari_jari.get())

        luas = bola.hitung_luas_permukaan(jari_jari)
        volume = bola.hitung_volume(jari_jari)

        hasil_text.set(f"Luas Permukaan: {luas:.5f}\nVolume: {volume:.5f}")

root = tk.Tk()
root.title("Kalkulator Bola")

root.geometry("350x200")
root.resizable(False, False)

label_jari_jari = tk.Label(root, text="Jari-jari Bola:")
label_jari_jari.grid(row=0, column=0, padx=10, pady=5, sticky='e')

entry_jari_jari = tk.Entry(root, width=15)
entry_jari_jari.grid(row=0, column=1, padx=10, pady=5, sticky='w')

hitung_button = tk.Button(root, text="Hitung", command=hitung)
hitung_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

hasil_text = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil_text, anchor='center', justify='center', wraplength=300)
hasil_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
