from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
from pytesseract import pytesseract

class ImageToTextConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Text Converter")

        self.path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        self.path_to_image = 'Media\OOP.png'
        pytesseract.tesseract_cmd = self.path_to_tesseract

        self.create_widgets()

    def create_widgets(self):
        # Load Image button
        load_button = tk.Button(self.root, text="Load Image", command=self.load_image)
        load_button.pack(pady=10)

        # Display Image
        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        # Convert to Text button
        convert_button = tk.Button(self.root, text="Convert to Text", command=self.extract_text)
        convert_button.pack(pady=10)

        # Text area to display result
        self.text_result = tk.Text(self.root, height=10, width=50)
        self.text_result.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])
        if file_path:
            self.path_to_image = file_path
            image = Image.open(file_path)
            image = image.resize((300, 300))  # Adjust size for display
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def extract_text(self):
        if self.path_to_image:
            img = Image.open(self.path_to_image)
            text = pytesseract.image_to_string(img)
            self.text_result.delete(1.0, tk.END)  # Clear previous text
            self.text_result.insert(tk.END, text)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextConverterApp(root)
    root.mainloop()
