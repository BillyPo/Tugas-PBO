import tkinter as tk
import prisma

def hitung():
        alas_segitiga = float(entry_alas_segitiga.get())
        tinggi_segitiga = float(entry_tinggi_segitiga.get())
        tinggi_prisma = float(entry_tinggi_prisma.get())

        luas_permukaan = prisma.hitung_luas_permukaan_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma)
        volume = prisma.hitung_volume_segitiga(alas_segitiga, tinggi_segitiga, tinggi_prisma)

        hasil_text.set(f"Luas Permukaan: {luas_permukaan}\nVolume: {volume}")

root = tk.Tk()
root.title("Kalkulator Prisma Segitiga")

root.geometry("400x250")
root.resizable(False, False)

label_alas_segitiga = tk.Label(root, text="Alas Segitiga Prisma:")
label_alas_segitiga.grid(row=0, column=0, padx=10, pady=5, sticky='e')

entry_alas_segitiga = tk.Entry(root, width=15)
entry_alas_segitiga.grid(row=0, column=1, padx=10, pady=5, sticky='w')

label_tinggi_segitiga = tk.Label(root, text="Tinggi Segitiga Prisma:")
label_tinggi_segitiga.grid(row=1, column=0, padx=10, pady=5, sticky='e')

entry_tinggi_segitiga = tk.Entry(root, width=15)
entry_tinggi_segitiga.grid(row=1, column=1, padx=10, pady=5, sticky='w')

label_tinggi_prisma = tk.Label(root, text="Tinggi Prisma:")
label_tinggi_prisma.grid(row=2, column=0, padx=10, pady=5, sticky='e')

entry_tinggi_prisma = tk.Entry(root, width=15)
entry_tinggi_prisma.grid(row=2, column=1, padx=10, pady=5, sticky='w')

hitung_button = tk.Button(root, text="Hitung", command=hitung)
hitung_button.grid(row=3, column=0, columnspan=2, pady=10)

hasil_text = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil_text, anchor='center', justify='center', wraplength=350)
hasil_label.grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
