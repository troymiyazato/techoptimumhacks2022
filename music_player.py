import pygame
import os
import tkinter as tk
import random


class MusicPlayer:
    def __init__(self):
        self.music_player = tk.Tk()
        self.music_player.title("Music Player")
        self.music_player.geometry("450x200")

        pygame.init()
        pygame.mixer.init()

    def get_music_list(self):
        music_list = os.listdir('./music')
        return music_list

    def play_music(self):
        music_filename = random.choice(self.get_music_list())
        pygame.mixer.music.set_volume(0.50)
        pygame.mixer.music.load(f"./music/{music_filename}")
        pygame.mixer.music.play(-1)

    def run(self):
        Button1 = tk.Button(self.music_player, width=5, height=3, font="Helvetica 12 bold",
                            text="CHANGE SONG", command=self.play_music, bg="black", fg="white")
        Button1.pack(fill="x")


if __name__ == '__main__':
    music_player = MusicPlayer()
    music_player.run()