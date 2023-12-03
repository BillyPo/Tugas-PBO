from gtts import gTTS
from playsound import playsound
import tkinter as tk
from tkinter import ttk

def generate_and_play_audio():
    mytext = 'Selamat Belajar Python! Bismillah'
    language = 'id'
    myobj = gTTS(text=mytext, lang=language, slow=False)
    
    # Save the audio file
    myobj.save("selamat_belajar.mp3")
    
    # Play the audio file
    playsound("selamat_belajar.mp3", True)

def main():
    # Create the main window
    root = tk.Tk()
    root.title("Text to Speech App")
    
    # Create a button to generate and play audio
    generate_button = ttk.Button(root, text="Generate and Play Audio", command=generate_and_play_audio)
    generate_button.pack(pady=20)
    
    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
