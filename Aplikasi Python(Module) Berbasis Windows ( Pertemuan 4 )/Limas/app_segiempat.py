import tkinter as tk
import limas

def hitung_limas_segiempat():
        alas = float(entry_alas.get())
        tinggi_limas = float(entry_tinggi_limas.get())

        luas = limas.hitung_luas_permukaan_segiempat(alas, tinggi_limas)
        volume = limas.hitung_volume_segiempat(alas, tinggi_limas)

        hasil_text.set(f"Luas Permukaan: {luas}\nVolume: {volume}")

root = tk.Tk()
root.title("Kalkulator Limas Segiempat")

root.geometry("350x200")
root.resizable(False, False)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.grid_rowconfigure(5, weight=1)

label_alas = tk.Label(root, text="Alas Limas:")
label_alas.grid(row=0, column=0, padx=10, pady=5, sticky='e')

entry_alas = tk.Entry(root, width=15)
entry_alas.grid(row=0, column=1, padx=10, pady=5, sticky='w')

label_tinggi_limas = tk.Label(root, text="Tinggi Limas:")
label_tinggi_limas.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_tinggi_limas = tk.Entry(root, width=15)
entry_tinggi_limas.grid(row=1, column=1, padx=10, pady=5, sticky='w')

hitung_button = tk.Button(root, text="Hitung", command=hitung_limas_segiempat)
hitung_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

hasil_text = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil_text, anchor='center', justify='center', wraplength=300)
hasil_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
