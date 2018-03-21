from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
import pyfirmata
import pygame
from tinytag import TinyTag
from main_window import *





class Demo1:

    def __init__(self, master):
        ##########
        self.position = 0
        self.playing = False
        self.paused = False
        self.port1 = '/Users/evgeshakrasava/PycharmProjects/c.mp3'
        self.port2 = '/home/qbc/Downloads/c.mp3'

        ##########
        self.pr_time = 0
        self.fin_time = 0
        self.min = 0
        self.sec = 0
        self.values = 1
        self.info = ''
        ##########

        self.master = master
        self.master.geometry('300x200')
        self.master.title('плеер')
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.button1 = tk.Button(self.frame, text='servo_config', width=25, command=self.new_window)
        self.button1.pack()

        self.scale = ttk.Scale(orient='horizontal', from_=0.01, to=0.9, command=self.loud).pack()

        self.p_bar = ttk.Progressbar(self.frame, orient='horizontal', length=200)
        self.p_bar.pack()

        self.b = ttk.Button(self.frame, text="play/replay", command=self.play_music)
        self.b.pack()

        self.pause = ttk.Button(self.frame, text='pause/unpause', command=self.pause)
        self.pause.pack()

        self.loop_butt = ttk.Button(self.frame, text='loop', command=self.loop).pack()

        self.open_new = ttk.Button(self.frame, text='open', command=self.add).pack()

        self.m_time = ttk.Label(self.frame, text='')
        self.m_time.pack()

    def play_music(self):
        self.playing = True
        pygame.init()
        pygame.mixer.music.load(self.port2)
        pygame.mixer.music.set_volume(0)  # set volume on zero before play
        pygame.mixer.music.play(-1, 0.0)

        if self.playing == True:
            self.p_bar.config(mode='determinate', maximum=self.fin_time, value=1)
            self.p_bar.start(1000)
            self.conventer_durability()
            self._on_scale()

    def _on_scale(self):
        # initialize time track
        time = int(pygame.mixer.music.get_pos() / 1000)
        m, s = divmod(time, 60)
        h, m = divmod(m, 60)
        self.m_time.configure(text="%2.2d:%2.2d" % (m, s))
        self.frame.after(1000, self._on_scale)

    '''
    def update_timeslider(self, _=None):
        time = (pygame.mixer.music.get_pos() / 1000)
        timeslider.set(time)
        self.after(10, self.update_timeslider)
    '''

    def pause(self):
        pygame.init()
        self.playing = False

        if self.paused:

            pygame.mixer.music.unpause()
            self.paused = False
        else:
            self.p_bar.stop()
            self.paused = True
            pygame.mixer.music.pause()

    def loud(self, value):
        pygame.init()
        pygame.mixer.music.set_volume((float(value)))  # put on pygame module value from scale widget

    def loop(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.play(-1, 0.0)

    def conventer_durability(self):
        tag = TinyTag.get(self.port2)
        self.fin_time = tag.duration
        self.fin_time = int(self.fin_time)
        minutes = self.fin_time / 60
        sec = self.fin_time % 60

    def add(self):
        file = ttk.askopenfilenames(initialdir='qbc/Downloads')
        songsTuple = self.frame.splitlist(file)  # turn user's opened filenames into tuple
        songsList = list(songsTuple)  # convert to list
        # Add the full filename of songto playlist list, and a shortened version to the listBox
        for song in songsList:
            playlist.append(song);
            tempArray = song.split('/')
            songShort = tempArray[len(tempArray) - 1]
            self.playlistbox.insert(END, songShort)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

    def print_value(self):
        print(self.value)

    def createsound_path(self):
        pass




def main():
    root = tk.Tk()
    root.title("SERVO_M")

    app = Demo1(root)
    root.mainloop()


if __name__ == '__main__':
    main()