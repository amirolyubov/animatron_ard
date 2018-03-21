from tkinter import *
import tkinter as tk
from tkinter import ttk
from subprocess import call
import sqlite3


class new_base:
    def __init__(self,master):


        #####variables######

        self.db_name=''

        self.master = master
        self.master.geometry('300x70')
        self.master.title('создать новый сценарий')
        self.frame = tk.Frame(self.master)
        self.db_name = StringVar()
        self.name_label = ttk.Label(self.master,text= 'имя сценария')
        self.name_label.grid(row=1,column=1,sticky = 'w',padx=10 )
        self.data_base = ttk.Entry(self.master,textvariable = self.db_name,width=30)
        self.data_base.grid(row=3,column=1,sticky="w",padx=10)

        self.ok_b = ttk.Button(self.master,text = 'создать',command = self.create_newdb)
        self.ok_b.grid(row =4 ,column =1,sticky='w',padx=30,pady=5)
        self.cancell_but = ttk.Button(self.master,text = 'отмена',command = self.cancell)
        self.cancell_but.grid(row=4,column=1,padx=120,pady=5)

    def create_newdb(self):
        print()
        path = '{}.db'.format(self.db_name.get())
        con = sqlite3.connect(path)
        cursor = con.cursor()
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
        con.commit()
        call('mv {}.db /home/qbc/PycharmProjects/ard/scenario'.format(self.db_name.get()),shell =True)

    def cancell(self):
        self.master.destroy()