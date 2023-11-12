import tkinter as tk
import kerucut

def hitung():
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())

        luas = kerucut.hitung_luas_permukaan(jari_jari, tinggi)
        volume = kerucut.hitung_volume(jari_jari, tinggi)

        hasil_text.set(f"Luas Permukaan: {luas:.5f}\nVolume: {volume:.5f}")

root = tk.Tk()
root.title("Kalkulator Kerucut")

def on_label_configure(event):
    label_width = event.width
    hasil_label.config(wraplength=label_width)

root.bind("<Configure>", on_label_configure)

root.geometry("350x200")
root.resizable(False, False)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.grid_rowconfigure(5, weight=1)

label_jari_jari = tk.Label(root, text="Jari-jari Alas:")
label_jari_jari.grid(row=0, column=0, padx=10, pady=5, sticky='e')

entry_jari_jari = tk.Entry(root, width=15)
entry_jari_jari.grid(row=0, column=1, padx=10, pady=5, sticky='w')

label_tinggi = tk.Label(root, text="Tinggi Kerucut:")
label_tinggi.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_tinggi = tk.Entry(root, width=15)
entry_tinggi.grid(row=1, column=1, padx=10, pady=5, sticky='w')

hitung_button = tk.Button(root, text="Hitung", command=hitung)
hitung_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

hasil_text = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil_text, anchor='center', justify='center', wraplength=300)
hasil_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
