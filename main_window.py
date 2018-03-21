from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import threading
import sqlite3
from subprocess  import call,PIPE,Popen
import shutil
from sketchbooks.SW.run_servo import compiling
from db_input import *


class Demo2:
    def __init__(self, master):
        self.master = master
        self.master.geometry('800x400')
        self.frame = tk.Frame(self.master)
        self.master.title('серво менеджер')
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
        self.sql_time=[]
        self.sql_servo_1 = 0
        self.sql_servo_2 = 0
        self.sql_servo_3 = 0
        self.sql_servo_4 = 0
        self.sql_servo_5 = 0
        self.sql_servo_6 = 0
        self.sql_servo_7 = 0
        self.sql_servo_8 = 0
        self.sql_servo_9 = 0
        self.speed =0
        self.time = 0




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
        self.angle_box7 = ttk.Entry(self.master, textvariable = self.reserved_2, width=3)
        self.angle_box7.grid(row=9, column=3)

        self.play_butt = ttk.Button(self.master, text='проиграть',command=self.some_play).grid(row=12, column=2)

        self.button = ttk.Button(self.master, text='записать позиции',command =self.write_position)
        self.button.grid(row=13, column=2)



        self.write = ttk.Button(self.master, text='удалить все значения',command = self.create_new) .grid(row=15, column=2,)
        self.time_label = ttk.Label(self.master, text="время").grid(row=18, column=2, sticky='ws', padx=0)
        self.time_scale = ttk.Scale(self.master, orient='horizontal', length=400, from_=0, to=180,command =self.printime )
        self.time_scale.grid(row=19, column=2,pady=10)
        #digit near "время"
        self.time_digit = ttk.Label(self.master)
        self.time_digit.grid(row=18, column=2, sticky='w', padx=50)#padx control shift some construction , more this more to right



        self.speed_label = ttk.Label(self.master,text ="cкорость").grid(row=16,column =2,sticky = 'ws',padx=0)
        # digit near "скорость"
        self.speed_digit = ttk.Label(self.master)
        self.speed_digit.grid(row=16,column =2,sticky = 'w',padx=65)

        self.speed_slider =  ttk.Scale(self.master,orient = "horizontal", length =100,from_ = 0 ,to =100,command =self.prinw)
        self.speed_slider.grid(row=17,column =2,sticky = 'ws',padx=0)

        self.label_time = ttk.Label(self.master)
        self.label_time.grid(row=15, column=2)
        # self.background_image = tk.PhotoImage(...)
        # self.background_label = tk.Label(self.master, image=background_image)
        # self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.new = ttk.Button(self.master,text="новый сценарий",command = self.new_data).grid(row =1,column =10)
        self.window_curr = ttk.Button(self.master,text="выбрать сценарий",command = self.choose_db).grid(row =3,column =10,sticky = 'e')


    def prinw(self,val):
        #define for speed
        self.speed=round(float(val))
        #change label to define speed
        self.speed_digit.configure(text=round(self.speed))
    def printime(self,val):
        #define for speed
        self.time=round(float(val))
        m = self.time // 60
        s = self.time - m * 60
        self.time_digit.configure(text='%02d:%02d' % (m, s))
    def new_data(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = new_base(self.newWindow)
    def choose_db(self):
        fname = askopenfilename(filetypes=(("scenario", "*.db"),
                                           ("databases", "*.dms"),
                                           ("All files", "*.*") ))
    def write_position(self):
        #on sql
        conn = sqlite3.connect('position.dms')
        cursor = conn.cursor()
        cursor.executescript("""
         insert into `time` values (%d)
        """ % (round(self.time_scale.get()*1000)))#time
        cursor.executescript("""
        insert into `speed` values (%d)
        """ % (self.speed)) # time
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
        self.write_to_h()
        print(self.speed)



    def clear_strings(self):
        # clean by rubish
        f = open('template.h','r')
        o = open('VAL.h', 'w')
        while 1:
            line = f.readline()
            if not line: break
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.replace(',,', ',')
            line = line.replace("''", '0')
            line = line.replace('[][]','[]')
            line = line.replace('{[]}','{}')
            line = line.replace('{[','{')
            line = line.replace(']}','}')
            line = line.replace(')]};','')
            o.write(line)
        o.close()
        call('rm template.h',shell =True)
        # move VAL.h with values from sql to arduino library:******************
        shutil.move("/home/qbc/PycharmProjects/ard/VAL.h", "/usr/share/arduino/hardware/arduino/cores/arduino/VAL.h")
        # call('rm VAL.h',shell =True)




    def write_to_h(self):
        # take all from data base
        conn = sqlite3.connect('position.dms')
        cursor = conn.cursor()
        #time
        cursor.execute("SELECT * FROM `time` order by  `time_pos` ")
        self.sql_time = cursor.fetchall()
        # servo_1
        cursor.execute("SELECT * FROM `servo_1`  ")
        self.sql_servo_1 =cursor.fetchall()
        # servo_2
        cursor.execute("SELECT * FROM `servo_2`  ")
        self.sql_servo_2 = cursor.fetchall()
        # servo_3
        cursor.execute("SELECT * FROM `servo_3` ")
        self.sql_servo_3 = cursor.fetchall()
        # servo_4
        cursor.execute("SELECT * FROM `servo_4`  ")
        self.sql_servo_4 = cursor.fetchall()
        # servo_5
        cursor.execute("SELECT * FROM `servo_5`  ")
        self.sql_servo_5= cursor.fetchall()
        # servo_6
        cursor.execute("SELECT * FROM `servo_6`  ")
        self.sql_servo_6 = cursor.fetchall()
        # servo_7
        cursor.execute("SELECT * FROM `servo_7`  ")
        self.sql_servo_7 = cursor.fetchall()
        # servo_8
        cursor.execute("SELECT * FROM `servo_8`  ")
        self.sql_servo_8 = cursor.fetchall()
        # servo_9
        cursor.execute("SELECT * FROM `servo_9`  ")
        self.sql_servo_9 = cursor.fetchall()



        with open('template.h','w') as file:
            file.writelines('int time_play=1;\n')
            file.writelines('int speed_row[] = {')
            file.writelines(str(self.speed_slider.get()))
            file.writelines('};\n')
            file.writelines('int LEyeArray[][] = {')
            file.writelines(str(self.sql_servo_1))
            file.writelines('};\n')
            file.writelines('int REyeArray[] = {')
            file.writelines(str(self.sql_servo_2))
            file.writelines('};\n')
            file.writelines('int LArmArray[] = {')
            file.writelines(str(self.sql_servo_3))
            file.writelines('};\n')
            file.writelines('int RArmArray[] = {')
            file.writelines(str(self.sql_servo_4))
            file.writelines('};\n')
            file.writelines('int LhandArray[] = {')
            file.writelines(str(self.sql_servo_5))
            file.writelines('};\n')
            file.writelines('int RhandArray[] = {')
            file.writelines(str(self.sql_servo_6))
            file.writelines('};\n')
            file.writelines('int LLegArray[] = {')
            file.writelines(str(self.sql_servo_7))
            file.writelines('};\n')
            file.writelines('int RLegArray[] = {')
            file.writelines(str(self.sql_servo_8))
            file.writelines('};\n')
            file.writelines('int AssArray[] = {')
            file.writelines(str(self.sql_servo_9))
            file.writelines('};\n')
            file.writelines('unsigned long KeyArray[] = {')
            file.writelines(str(self.sql_time))
            file.writelines('};\n')
        self.clear_strings()

    def create_new(self):
        conn = sqlite3.connect('position.dms')
        cursor = conn.cursor()
        cursor.execute(
            'CREATE TABLE  servo_1 (servo1_pos integer );')
        cursor.execute(
            'CREATE TABLE  servo_2 (servo2_pos  integer );')
        cursor.execute(
            'CREATE TABLE  servo_3 (servo3_pos integer );')
        cursor.execute(
            'CREATE TABLE servo_4 (servo4_pos integer );')
        cursor.execute(
            'CREATE TABLE  servo_5 (servo5_pos integer );')
        cursor.execute(
            'CREATE TABLE  servo_6 (servo6_pos integer );')
        cursor.execute(
            'CREATE TABLE  servo_7 (servo7_pos integer );')
        cursor.execute(
            'CREATE TABLE servo_8 (servo8_pos integer );')
        cursor.execute(
            'CREATE TABLE  servo_9 (servo9_pos integer );')
        cursor.execute(
            'CREATE TABLE  speed (speed_pos integer );')
        cursor.execute(
            'CREATE TABLE  time (time_pos integer );')
        # self.deleteall()
    def deleteall(self):
        conn = sqlite3.connect('position.dms')
        cursor = conn.cursor()

        # cursor.execute('drop table `time`')
        # cursor.execute('drop table `speed`')
        # cursor.execute('drop table `servo_1`')
        # cursor.execute('drop table `servo_2`')
        # cursor.execute('drop table `servo_3`')
        # cursor.execute('drop table `servo_4`')
        # cursor.execute('drop table `servo_5`')
        # cursor.execute('drop table `servo_6`')
        # cursor.execute('drop table `servo_7`')
        # cursor.execute('drop table `servo_8`')
        # cursor.execute('drop table `servo_9`')
        cursor.execute('DELETE FROM  servo_1 ')
        cursor.execute('DELETE FROM  servo_2 ')
        cursor.execute('DELETE FROM  servo_3 ')
        cursor.execute('DELETE FROM  servo_4 ')
        cursor.execute('DELETE FROM  servo_5 ')
        cursor.execute('DELETE FROM  servo_6 ')
        cursor.execute('DELETE FROM  servo_7 ')
        cursor.execute('DELETE FROM  servo_8 ')
        cursor.execute('DELETE FROM  servo_9 ')
        cursor.execute('DELETE FROM  speed ')
        cursor.execute('DELETE FROM  time ')
        conn.commit()



    def some_play(self):
        t1 = threading.Thread(target=compiling)
        t1.start()



