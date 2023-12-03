import tkinter as tk
from tkinter import ttk
from temperature_converter import TemperatureConverter

class TemperatureApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Konversi Suhu")

        self.create_widgets()

    def create_widgets(self):
        # Membuat label dan entry untuk input suhu
        self.label_input = ttk.Label(self.master, text="Masukkan Suhu (dalam celcius):")
        self.label_input.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.entry_input = ttk.Entry(self.master)
        self.entry_input.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Membuat label untuk hasil konversi
        self.label_result = ttk.Label(self.master, text="Hasil Konversi:")
        self.label_result.grid(row=2, column=0, columnspan=2, pady=10)

        # Membuat tombol konversi
        self.button_convert = ttk.Button(self.master, text="Konversi", command=self.convert_temperature)
        self.button_convert.grid(row=1, column=0, columnspan=2, pady=10)

    def convert_temperature(self):
        try:
            input_temperature = float(self.entry_input.get())
            celsius = input_temperature

            fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
            reaumur = TemperatureConverter.celsius_to_reaumur(celsius)
            kelvin = TemperatureConverter.celsius_to_kelvin(celsius)

            result_text = f"Fahrenheit: {fahrenheit:.2f} F\nReaumur: {reaumur:.2f} Re\nKelvin: {kelvin:.2f} K"
            self.label_result.config(text=result_text)
        except ValueError:
            self.label_result.config(text="Masukkan angka yang valid!")
