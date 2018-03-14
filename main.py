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
        self.port = []
        self.angles = []
        self.pins = []
        self.actions = []
        self.values = 0
        self.temp_varibal = ['', 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.SAVING = False
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
        self.exist_posistion = []
        ################## loop  ###########################################
        self.fluency = 1
        self.old_time = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.sort = True
        self.write = False


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

        self.play_butt = ttk.Button(self.master, text='>', command=self.some_play).grid(row=12, column=2)

        self.button = ttk.Button(self.master, text='pull value')
        self.button.grid(row=13, column=2)

        # self.preview = ttk.Button(self.master,text = "preview",command =self.just_one_action2).grid(row = 14 ,column=2)

        self.add_position = ttk.Button(self.master, text="add action", command=self.pin_init).grid(row=16, column=2)
        self.write = ttk.Button(self.master, text='write',command = self.write_position) .grid(row=17, column=2)

        self.time_scale = ttk.Scale(self.master, orient='horizontal', length=450, from_=0, to=180)
        self.time_scale.grid(row=22, column=2)

        # port for arduino
        self.port = StringVar()
        self.port_selector = ttk.Combobox(self.master, textvariable=self.port)
        self.port_selector.grid(row=11, column=3)
        self.port_b = ttk.Button(self.master, text='init', command=self.arduino_port_indit).grid(row=13, column=3)
        # show timer
        self.label_time = ttk.Label(self.master)
        self.label_time.grid(row=15, column=2)

        #write section




    # self.but_init = ttk.Button(self.master,text = 'initports',command = self.arduino_port_indit).grid(row= 12,column=2)

    ################################main func with angles########################
    def arduino_port_indit(self):
        self.ports = list(serial.tools.list_ports.comports())
        for p in self.ports:
            self.port = p
        self.port_selector = ttk.Combobox(self.master, textvariable=self.port)

    '''
    #mind this stuff after
    def just_one_action(self):
        dict(self.pins)
        self.pin_init()
        self.take_angle_box_answer()
        for angl in self.angles:
            for pin in self.pins:
                self.actions.append(str(pin)+'.write(%d)'%angl)
                print(self.actions)
    '''

    def close_windows(self):
        self.master.destroy()




    def pin_init(self):
        # init pin ardiuno
        port = '/dev/ttyACM0'
        port2 = '/dev/ttyUSB0'
        port3 = '/dev/cu.usbmodem1421'
        board = pyfirmata.Arduino(port2)
        #############important info#########
        '''
        self.right_e = board.get_pin('d:8:s')
        self.left_e = board.get_pin('d:9:s')
        self.sholder_right = board.get_pin('d:7:s')
        self.right_hand = board.get_pin('d:3:s')
        self.left_hand = board.get_pin('d:6:s')
        self.left_leg = board.get_pin('d:4:s')
        self.right_leg = board.get_pin('d:5:s')
        '''
        self.time_lapse()
        l_e_nine_pin = board.get_pin('d:9:s')
        r_e_eight_pin = board.get_pin('d:8:s')
        sh_r_seven_pin = board.get_pin('d:7:s')
        r_h_three_pin = board.get_pin('d:3:s')
        l_h_six_pin = board.get_pin('d:6:s')
        l_l_four_pin = board.get_pin('d:4:s')
        r_l_five_pin = board.get_pin('d:5:s')

        # take each angle on port arduino
        l_e_nine_pin.write(self.temp_varibal[-1][-9])
        r_e_eight_pin.write(self.temp_varibal[-1][-8])
        sh_r_seven_pin.write(self.temp_varibal[-1][-7])
        r_h_three_pin.write(self.temp_varibal[-1][-6])
        l_h_six_pin.write(self.temp_varibal[-1][-5])
        l_l_four_pin.write(self.temp_varibal[-1][-4])
        r_l_five_pin.write(self.temp_varibal[-1][-3])

    def take_position(self):
        self.temp_varibal.append([0.0, 0, 0, 0, 0, 0, 0, 0, 0])  # first list
        self.time_lapse()  # take all values from window
        self.write_position()  # write sql

    '''take each angle'''

    def time_lapse(self):  # time scaling
        # temp variable is value for  obtain time scale and save first number is time, after value of angles
        self.values = self.time_scale.get()
        self.temp_varibal.append([round(self.values)])  # add double list for time
        self.temp_varibal[-1].append(self.left_eye.get())  # each angle from each window
        self.temp_varibal[-1].append(self.right_e.get())
        self.temp_varibal[-1].append(self.right_sholder.get())
        self.temp_varibal[-1].append(self.right_hand.get())
        self.temp_varibal[-1].append(self.left_hand.get())
        self.temp_varibal[-1].append(self.left_leg.get())
        self.temp_varibal[-1].append(self.right_leg.get())
        self.temp_varibal[-1].append(self.reserved_1.get())
        self.temp_varibal[-1].append(self.reserved_2.get())
        print(self.temp_varibal[-1])

    def write_position(self):
        self.time_lapse()
        conn = sqlite3.connect('position.dms')
        cursor = conn.cursor()
        cursor.executescript("""
         insert into `positions` values (%d, %d, %d, %d, %d, %d, %d, %d,%d,%d)
        """ % (
        self.temp_varibal[-1][-10], self.temp_varibal[-1][-9],
        self.temp_varibal[-1][-8], self.temp_varibal[-1][-7],
        self.temp_varibal[-1][-6], self.temp_varibal[-1][-5],
        self.temp_varibal[-1][-4], self.temp_varibal[-1][-3],
        self.temp_varibal[-1][-2], self.temp_varibal[-1][-1]))

    def back_position(self):
        # take all from data base
        conn = sqlite3.connect('position.dms')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM `positions` order by `time` ")
        self.exist_posistion = cursor.fetchall()


    def sorting(self):
        print('start')
        old_time = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        while self.sort:
            self.back_position()
            for p in self.exist_posistion:
                #fixed problem
                if (p[0]-5)== self.timer_seconds:

                    # port = '/dev/ttyACM0'
                    port2 = '/dev/ttyUSB0'
                    port3 = '/dev/cu.usbmodem1421'
                    board = pyfirmata.Arduino(port2)
                    l_e_nine_pin = board.get_pin('d:9:s')
                    r_e_eight_pin = board.get_pin('d:8:s')
                    sh_r_seven_pin = board.get_pin('d:7:s')
                    r_h_three_pin = board.get_pin('d:3:s')
                    l_h_six_pin = board.get_pin('d:6:s')
                    l_l_four_pin = board.get_pin('d:4:s')
                    r_l_five_pin = board.get_pin('d:5:s')
                    res_1_ten_pin = board.get_pin('d:10:s')
                    res_2_eleven_pin = board.get_pin('d:11:s')
                    i = 0

                    #transit to write position if condition are met
                    # self.sort = False
                    # self.write = True
                    #comprasion and write just one,
                    # util value not equal value in sql table,
                    # after search  time and position again
                    while old_time != p:
                        self.sort = False
                        i += 1
                        if p[1] != old_time[1]:
                            l_e_nine_pin.write(i)
                            old_time[1] =i
                            print('s1')
                        if p[2] != old_time[2]:
                            r_e_eight_pin.write(i)
                            old_time[2] = i
                            print('s2')
                        if p[3] != old_time[3]:
                            sh_r_seven_pin.write(i)
                            old_time[3] = i
                            print('s3')
                        if p[4] != old_time[4]:
                            l_h_six_pin.write(i)
                            old_time[4] = i
                            print('s4')
                        if p[5] != old_time[5]:
                            r_h_three_pin.write(i)
                            old_time[5] = i
                            print('s5')
                        if p[6] != old_time[6]:
                            l_l_four_pin.write(i)
                            old_time[6] = i
                            print('s6')
                        if p[7] != old_time[7]:
                            r_l_five_pin.write(i)
                            old_time[7] = i
                            print('s7')
                        if p[8] != old_time[8]:
                            res_1_ten_pin.write(i)
                            old_time[8] = i
                            print('s8')
                        if p[9] != old_time[9]:
                            res_2_eleven_pin.write(i)
                            old_time[9] = i
                            print('s9')
                        else:
                            old_time[1] =p[1]
                            old_time[2] =p[2]
                            old_time[3] =p[3]
                            old_time[4] =p[4]
                            old_time[5] =p[5]
                            old_time[6] =p[6]
                            old_time[7] =p[7]
                            old_time[8] =p[8]
                            old_time[9] =p[9]

                            break





    def some_play(self):
        t1 = threading.Thread(target= self.sorting)
        t2 = threading.Thread(target=self.timer_tick)
        t2.start()
        t1.start()




    #######################play_section#############################

    def show_timer(self):
        #just only show
        m = self.timer_seconds // 60
        s = self.timer_seconds - m * 60
        self.label_time['text'] = '%02d:%02d' % (m, s)

    def timer_tick(self):

        self.label_time.after(1000, self.timer_tick)
        # увеличить таймер
        self.timer_seconds += 1
        self.show_timer()
        print(self.timer_seconds)
    def timer_start_pause(self):
        self.timer = False
        self.timer = not self.timer
        '''if self.timer:
            self.timer_tick()
        '''
    #####################################################################


def main():
    root = tk.Tk()
    root.title("SERVO_M")

    app = Demo1(root)
    root.mainloop()


if __name__ == '__main__':
    main()