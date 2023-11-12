import tkinter as tk
import balok

def hitung():
        panjang = float(entry_panjang.get())
        lebar = float(entry_lebar.get())
        tinggi = float(entry_tinggi.get())

        luas = balok.hitung_luas_permukaan(panjang, lebar, tinggi)
        volume = balok.hitung_volume(panjang, lebar, tinggi)

        hasil_text.set(f"Luas Permukaan: {luas}\nVolume: {volume}")

root = tk.Tk()
root.title("Kalkulator Balok")

def on_label_configure(event):
    label_width = event.width
    hasil_label.config(wraplength=label_width)

root.bind("<Configure>", on_label_configure)

root.geometry("350x200")
root.resizable(False, False)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.grid_rowconfigure(5, weight=1)

label_panjang = tk.Label(root, text="Panjang:")
label_panjang.grid(row=0, column=0, padx=10, pady=5, sticky='e')

entry_panjang = tk.Entry(root, width=15)
entry_panjang.grid(row=0, column=1, padx=10, pady=5, sticky='w')

label_lebar = tk.Label(root, text="Lebar:")
label_lebar.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_lebar = tk.Entry(root, width=15)
entry_lebar.grid(row=1, column=1, padx=10, pady=5, sticky='w')

label_tinggi = tk.Label(root, text="Tinggi:")
label_tinggi.grid(row=2, column=0, padx=10, pady=5, sticky='e')

entry_tinggi = tk.Entry(root, width=15)
entry_tinggi.grid(row=2, column=1, padx=10, pady=5, sticky='w')

hitung_button = tk.Button(root, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

hasil_text = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil_text, anchor='center', justify='center')
hasil_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
