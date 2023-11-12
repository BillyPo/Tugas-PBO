import tkinter as tk
import tabung

def hitung_tabung():
        jari_jari = float(entry_jari_jari.get())
        tinggi_tabung = float(entry_tinggi_tabung.get())

        luas = tabung.hitung_luas_permukaan(jari_jari, tinggi_tabung)
        volume = tabung.hitung_volume(jari_jari, tinggi_tabung)

        hasil_text.set(f"Luas Permukaan: {luas:.5f}\nVolume: {volume:.5f}")

root = tk.Tk()
root.title("Kalkulator Tabung")

root.geometry("350x200")
root.resizable(False, False)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.grid_rowconfigure(5, weight=1)

label_jari_jari = tk.Label(root, text="Jari-jari Tabung:")
label_jari_jari.grid(row=0, column=0, padx=10, pady=5, sticky='e')

entry_jari_jari = tk.Entry(root, width=15)
entry_jari_jari.grid(row=0, column=1, padx=10, pady=5, sticky='w')

label_tinggi_tabung = tk.Label(root, text="Tinggi Tabung:")
label_tinggi_tabung.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_tinggi_tabung = tk.Entry(root, width=15)
entry_tinggi_tabung.grid(row=1, column=1, padx=10, pady=5, sticky='w')

hitung_button = tk.Button(root, text="Hitung", command=hitung_tabung)
hitung_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

hasil_text = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil_text, anchor='center', justify='center', wraplength=300)
hasil_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
