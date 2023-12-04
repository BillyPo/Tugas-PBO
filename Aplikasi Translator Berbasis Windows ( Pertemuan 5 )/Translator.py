from tkinter import Frame, Label, Entry, Button, YES, BOTH, END, Tk, W, StringVar, OptionMenu
from googletrans import Translator

class FrmTranslator:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("500x250")  # Tambahkan sedikit ketinggian untuk dropdown
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)

        # Pasang Label
        Label(mainFrame, text='Bahasa Sumber:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Masukkan teks:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Hasil Terjemahan:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        Label(mainFrame, text='Pilih Bahasa:').grid(row=2, column=0, sticky=W, padx=5, pady=5)

        # Pasang textbox
        self.txtBahasaSumber = Entry(mainFrame, width=50) 
        self.txtBahasaSumber.grid(row=0, column=1, padx=5, pady=5)
        self.txtBahasaSumber.insert(END, "Indonesian")

        self.txtSumber = Entry(mainFrame, width=50) 
        self.txtSumber.grid(row=1, column=1, padx=5, pady=5)

        self.txtHasil = Entry(mainFrame, width=50) 
        self.txtHasil.grid(row=4, column=1, padx=5, pady=5)

        # Pasang Dropdown
        self.selected_lang = StringVar(mainFrame)
        self.selected_lang.set("Japanese")  # Default bahasa terjemahan
        languages = ["Japanese", "German", "Dutch"]
        dropdown = OptionMenu(mainFrame, self.selected_lang, *languages)
        dropdown.grid(row=2, column=1, padx=5, pady=5)

        # Pasang Button
        self.btnTranslate = Button(mainFrame, text='Translate!', command=self.onTranslate)
        self.btnTranslate.grid(row=3, column=1, padx=5, pady=5) 

    def onTranslate(self):
        # Membuat instance object
        penterjemah = Translator()

        # Mendapatkan kode bahasa terpilih
        lang_code = {'Japanese': 'ja', 'German': 'de', 'Dutch': 'nl'}
        dest_lang = lang_code[self.selected_lang.get()]

        # Menterjemahkan
        hasil = penterjemah.translate(self.txtSumber.get(), src='id', dest=dest_lang) 
       
        # Menampilkan hasil terjemahan
        self.txtBahasaSumber.delete(0, END)
        self.txtBahasaSumber.insert(END, "Indonesian")
        
        self.txtHasil.delete(0, END)  # Menghapus teks sebelumnya
        self.txtHasil.insert(END, hasil.text)

    def onKeluar(self, event=None):
        # Memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmTranslator(root, "Program Translator")
    root.mainloop() 
