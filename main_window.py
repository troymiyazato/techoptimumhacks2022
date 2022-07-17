import tkinter as tk
from tkinter import ttk

from speaker import Speaker
from music_player import MusicPlayer
from counsel_window import CounselWindow


class MainWindow:
    def __init__(self):
        self.speaker = Speaker()
        self.music_player = None
        self.main_window = tk.Tk()
        self.main_window.geometry("500x750+600+200")
        self.main_window.resizable(False, False)
        self.main_window.title("Mental Health Care Program v.1.0.1")

        self.title_label = None

        self.music_button = None
        self.joke_button = None
        self.affirmation_button = None
        self.counsel_button = None

        self.set_layout()

    def set_layout(self):
        self.main_window.rowconfigure(0, weight=2)
        self.main_window.rowconfigure(1, weight=1)
        self.main_window.rowconfigure(2, weight=1)

        self.set_label()
        self.set_buttons()

    def set_buttons(self):
        self.joke_button = ttk.Button(self.main_window, text="Joke", command=self.speaker.read_joke)
        self.joke_button.grid(column=0, row=1, ipadx=50, ipady=50, padx=(50, 0), pady=(50, 0))

        self.affirmation_button = ttk.Button(self.main_window, text="Affirmation", command=self.speaker.read_affirm)
        self.affirmation_button.grid(column=1, row=1, ipadx=50, ipady=50, padx=(50, 0), pady=(50, 0))

        self.music_button = ttk.Button(self.main_window, text="Play Music", command=self.open_music_player)
        self.music_button.grid(column=0, row=2, ipadx=50, ipady=50, padx=(50, 0), pady=(0, 50))

        self.counsel_button = ttk.Button(self.main_window, text="Counsel", command=self.open_counsel_window)
        self.counsel_button.grid(column=1, row=2, ipadx=50, ipady=50, padx=(50, 0), pady=(0, 50))

    def set_label(self):
        self.title_label = ttk.Label(self.main_window, text="Mental Health Care Manager", font=("Arial", 20))
        self.title_label.place(x=75, y=100)

    def open_counsel_window(self):
        counsel_window = CounselWindow()
        counsel_window.run()

    def open_music_player(self):
        self.music_player = MusicPlayer()
        self.music_player.run()
        self.music_player.play_music()

    def run(self):
        self.main_window.mainloop()


if __name__ == '__main__':
    window = MainWindow()
    window.run()
