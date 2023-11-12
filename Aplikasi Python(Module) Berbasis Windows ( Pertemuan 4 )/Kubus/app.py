import tkinter as tk
import kubus

def hitung():
        rusuk = float(entry_rusuk.get())

        luas = kubus.hitung_luas_permukaan(rusuk)
        volume = kubus.hitung_volume(rusuk)

        hasil_text.set(f"Luas Permukaan: {luas}\nVolume: {volume}")

root = tk.Tk()
root.title("Kalkulator Kubus")

def on_label_configure(event):
    label_width = event.width
    hasil_label.config(wraplength=label_width)

root.bind("<Configure>", on_label_configure)

root.geometry("350x200")
root.resizable(False, False)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

root.grid_rowconfigure(5, weight=1)

label_rusuk = tk.Label(root, text="Rusuk Kubus:")
label_rusuk.grid(row=0, column=0, padx=10, pady=5, sticky='e')

entry_rusuk = tk.Entry(root, width=15)
entry_rusuk.grid(row=0, column=1, padx=10, pady=5, sticky='w')

hitung_button = tk.Button(root, text="Hitung", command=hitung)
hitung_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

hasil_text = tk.StringVar()
hasil_label = tk.Label(root, textvariable=hasil_text, anchor='center', justify='center', wraplength=300)
hasil_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
