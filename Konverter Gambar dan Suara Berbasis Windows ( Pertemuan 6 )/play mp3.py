import pygame
from tkinter import Tk, Button, Label

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pemutar Lagu")
        self.root.geometry("300x150")

        # Inisialisasi pygame
        pygame.init()
        pygame.mixer.music.load("Media\Dewa - Arjuna.mp3")
        pygame.mixer.music.set_volume(0.5)

        # Label untuk menampilkan nama lagu
        self.song_label = Label(root, text="Dewa - Arjuna.mp3", font=("Helvetica", 12))
        self.song_label.pack(pady=10)

        # Tombol Play
        self.play_button = Button(root, text="Play", command=self.play_music)
        self.play_button.pack(pady=10)

        # Tombol Stop
        self.stop_button = Button(root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=10)

    def play_music(self):
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

if __name__ == "__main__":
    root = Tk()
    app = MusicPlayer(root)
    root.mainloop()

# Keluar dari pygame setelah aplikasi ditutup
pygame.quit()
