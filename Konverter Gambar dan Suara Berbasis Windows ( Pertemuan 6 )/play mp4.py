import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

class VideoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="OpenCV Video Player")
        self.label.pack(pady=10)

        self.btn_open = ttk.Button(self.root, text="Open Video File", command=self.open_file)
        self.btn_open.pack(pady=10)

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()

        self.btn_play = ttk.Button(self.root, text="Play", command=self.play_video)
        self.btn_play.pack(pady=10)

        self.btn_stop = ttk.Button(self.root, text="Stop", command=self.stop_video)
        self.btn_stop.pack(pady=10)

        self.cap = None
        self.is_playing = False

    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.avi")])
        if file_path:
            self.cap = cv2.VideoCapture(file_path)
            self.fps = self.cap.get(cv2.CAP_PROP_FPS)

    def play_video(self):
        if self.cap is not None and not self.is_playing:
            self.is_playing = True
            while self.is_playing:
                ret, frame = self.cap.read()
                if ret:
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = self.resize_frame(frame)
                    img = Image.fromarray(frame)
                    img = ImageTk.PhotoImage(image=img)
                    self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
                    self.root.update_idletasks()
                    self.root.update()
                    delay = int(1000 / self.fps)  # Calculate delay based on frame rate
                    self.root.after(delay, self.play_video)  # Schedule the next frame
                else:
                    self.stop_video()

    def stop_video(self):
        self.is_playing = False
        if self.cap is not None:
            self.cap.release()

    def resize_frame(self, frame):
        # Get the size of the Tkinter window
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()

        # Get the size of the video frame
        frame_width, frame_height = frame.shape[1], frame.shape[0]

        # Calculate the scaling factors
        scale_x = window_width / frame_width
        scale_y = window_height / frame_height

        # Choose the minimum scale factor to maintain the aspect ratio
        scale_factor = min(scale_x, scale_y)

        # Resize the frame
        new_width = int(frame_width * scale_factor)
        new_height = int(frame_height * scale_factor)
        resized_frame = cv2.resize(frame, (new_width, new_height))

        return resized_frame

if __name__ == "__main__":
    from PIL import Image, ImageTk

    root = tk.Tk()
    app = VideoApp(root)
    root.mainloop()
