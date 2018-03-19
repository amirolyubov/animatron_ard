from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox

import os
import pygame
from tinytag import TinyTag
import time
import pyfirmata
import threading
import sqlite3




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


class Demo2:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x400')
        self.frame = tk.Frame(self.master)

        ##########angles from window######################
        self.left_eye = 0
        self.right_e = 0
        self.right_sholder = 0
        self.right_hand = 0
        self.left_hand = 0
        self.left_leg = 0
        self.right_leg = 0
        self.reserved_1 = 0
        self.reserved_2 = 0
        #################VALUES FOR TIMER##################################
        self.timer = False
        self.default_seconds = 0
        self.timer_seconds = self.default_seconds
        self.sql_servo_1 = []
        self.sql_time=[]




        self.lab_ser_1 = ttk.Label(self.master, text='глаз левый ').grid(row=0, column=1)
        self.left_eye = IntVar()
        self.angle_box1 = ttk.Entry(self.master, textvariable=self.left_eye, width=3)
        self.angle_box1.grid(row=1, column=1)

        self.lab_ser_2 = ttk.Label(self.master, text='глаз правый').grid(row=4, column=1)
        self.right_e = IntVar()
        self.angle_box2 = ttk.Entry(self.master, textvariable=self.right_e, width=3)
        self.angle_box2.grid(row=5, column=1)

        self.lab_ser_3 = ttk.Label(self.master, text='плечо правое').grid(row=8, column=1)
        self.right_sholder = IntVar()
        self.angle_box3 = ttk.Entry(self.master, textvariable=self.right_sholder, width=3)
        self.angle_box3.grid(row=9, column=1)

        self.lab_ser_4 = ttk.Label(self.master, text='рука правая').grid(row=0, column=2)
        self.right_hand = IntVar()
        self.angle_box4 = ttk.Entry(self.master, textvariable=self.right_hand, width=3)
        self.angle_box4.grid(row=1, column=2)

        self.lab_ser_5 = ttk.Label(self.master, text='рука левая').grid(row=4, column=2)
        self.left_hand = IntVar()
        self.angle_box5 = ttk.Entry(self.master, textvariable=self.left_hand, width=3)
        self.angle_box5.grid(row=5, column=2)

        self.lab_ser_6 = ttk.Label(self.master, text='нога левая').grid(row=8, column=2)
        self.left_leg = IntVar()
        self.angle_box6 = ttk.Entry(self.master, textvariable=self.left_leg, width=3)
        self.angle_box6.grid(row=9, column=2)

        self.lab_ser_7 = ttk.Label(self.master, text='нога правая ').grid(row=0, column=3)
        self.right_leg = IntVar()
        self.angle_box7 = ttk.Entry(self.master, textvariable=self.right_leg, width=3)
        self.angle_box7.grid(row=1, column=3)

        self.lab_ser_8 = ttk.Label(self.master, text='reserved_1 ').grid(row=4, column=3)
        self.reserved_1 = IntVar()
        self.angle_box7 = ttk.Entry(self.master, textvariable=self.reserved_1, width=3)
        self.angle_box7.grid(row=5, column=3)

        self.lab_ser_9 = ttk.Label(self.master, text='reserved_2 ').grid(row=8, column=3)
        self.reserved_2 = IntVar()
        self.angle_box7 = ttk.Entry(self.master, textvariable=self.reserved_2, width=3)
        self.angle_box7.grid(row=9, column=3)

        self.play_butt = ttk.Button(self.master, text='clear', command=self.clear_strings).grid(row=12, column=2)

        self.button = ttk.Button(self.master, text='show',command =self.write_to_h)
        self.button.grid(row=13, column=2)



        self.write = ttk.Button(self.master, text='sql',command = self.write_position) .grid(row=17, column=2)

        self.time_scale = ttk.Scale(self.master, orient='horizontal', length=400, from_=0, to=180)
        self.time_scale.grid(row=19, column=2,pady=14)
        self.speed_slider =  ttk.Scale(self.master,orient = "vertical", length =100,from_ = 0 ,to =30).grid(row=17,column =7,sticky = 'ws')


        self.label_time = ttk.Label(self.master)
        self.label_time.grid(row=15, column=2)


    def write_position(self):
        #on sql
        conn = sqlite3.connect('position.dms')
        cursor = conn.cursor()
        cursor.executescript("""
         insert into `time` values (%d)
        """ % (round(self.time_scale.get())))#time
        cursor.executescript("""
        insert into `servo_2` values (%d)
        """ % (self.left_eye.get()))#servo_1
        cursor.executescript("""
        insert into `servo_1` values (%d)
        """ % (self.right_e.get()))#servo_2
        cursor.executescript("""
        insert into `servo_3` values (%d)
        """ % (self.right_sholder.get()))#servo_3
        cursor.executescript("""
        insert into `servo_4` values (%d)
        """ % (self.left_hand.get()))#servo_4
        cursor.executescript("""
        insert into `servo_5` values (%d)
        """ % (self.right_hand.get()))#servo_5
        cursor.executescript("""
        insert into `servo_6` values (%d)
        """ % (self.right_leg.get()))# servo_6
        cursor.executescript("""
        insert into `servo_7` values (%d)
        """ % (self.left_leg.get()))# servo_7
        cursor.executescript("""
        insert into `servo_8` values (%d)
        """ % (self.reserved_1.get()))#servo_8
        cursor.executescript("""
        insert into `servo_9` values (%d)
        """ % (self.reserved_2.get()))#servo_9

    def write_to_h(self):
        # take all from data base
        conn = sqlite3.connect('position.dms')
        cursor = conn.cursor()
        # cursor.execute("SELECT * FROM `time` order by  `time_pos` ")
        cursor.execute("SELECT * FROM `servo_1` order by  `servo1_pos` ")
        self.sql_time = cursor.fetchall()
        # self.sql_servo_1 = cursor.fetchall()
        with open('Val.h','a+') as file:

            file.writelines('int time_play={')
            file.writelines(str(self.sql_time))
            file.writelines('}\n')
            file.writelines('int key[] = {')
            file.writelines(str(self.sql_servo_1))
            file.writelines('}\n')
            file.close()


    def clear_strings(self):
            with open('Val.h', "r") as f:
                new_f = f.readlines()
                with open('Val.h', "r+") as new_new_F:
                    for line in new_f:
                        for new_line in new_new_F:
                            if '),' in line:
                                print('replacing')
                                new_line.replace('),','1')

    #####################################################################


def main():
    root = tk.Tk()
    root.title("SERVO_M")

    app = Demo1(root)
    root.mainloop()


if __name__ == '__main__':
    main()
