#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Oct 19, 2018 01:20:39 AM CEST  platform: Windows NT
#
# Author : Florian GRANTE

import sys
import time
import threading
import csv


from serial import *
import matplotlib.pyplot as plt
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

recording = False
plotting = False

timestamp = []
setpoint = []
pos_encodeur = []
pwm_envoye = []
erreur_derivative = []
erreur_integrale = []

ki = 0
kp = 0
kd = 0

def step_backward():
    start()
    serial_port.write("p\n")
    serial_port.write("-25\n")
    time.sleep(0.5)
    stop()

def step_forward():
    start()
    serial_port.write("p\n")
    serial_port.write("25\n")
    time.sleep(0.5)
    stop()

def start():
    global recording
    recording = True
    serial_port.write("start\n")


def stop():
    global recording,plotting, timestamp, setpoint, pos_encodeur, pwm_envoye, erreur_derivative, erreur_integrale
    recording = False
    serial_port.write("stop\n")
    print(len(timestamp))
    if recording == False and plotting == True:
        retranchage = int(timestamp[0])
        print(retranchage)
        for i in range(len(timestamp)):
            timestamp[i] = int(timestamp[i]) - retranchage
        print(timestamp)
        # plt.plot(timestamp, pos_encodeur)
        # plt.show()
        plt.close()
        plt.plot(timestamp, pos_encodeur, "r", timestamp, setpoint,'b')
        plt.ion()
        plt.show()
        timestamp = []
        setpoint = []
        pos_encodeur = []
        pwm_envoye = []
        erreur_derivative = []
        erreur_integrale = []
        plotting = False

class MyThread(threading.Thread):
    def run(self):
        global recording, plotting, timestamp, setpoint, pos_encodeur, pwm_envoye, erreur_derivative, erreur_integrale
        while True:
            while recording == True:
                if serial_port.isOpen():
                    data = str(serial_port.readline())
                    list_data = data.split()
                    if(list_data[0] != "ORDER"):
                        #c.writerow(["Timestamp", "setpoint", "pos_encodeur", "pwm_envoye", "erreur_derivative", "erreur_integrale"])
                        c.writerow(list_data)
                        timestamp.append(int(list_data[0]))
                        setpoint.append(float(list_data[1]))
                        pos_encodeur.append(float(list_data[2]))
                        pwm_envoye.append(float(list_data[3]))
                        erreur_derivative.append(float(list_data[4]))
                        erreur_integrale.append(float(list_data[5]))
                        plotting = True

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
#    unknown_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
#    unknown_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None

class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'

        top.geometry("876x497+736+119")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.Stop = Button(top, command=stop)
        self.Stop.place(relx=0.126, rely=0.342, height=34, width=57)
        self.Stop.configure(activebackground="#d9d9d9")
        self.Stop.configure(activeforeground="#000000")
        self.Stop.configure(background="#d9d9d9")
        self.Stop.configure(disabledforeground="#a3a3a3")
        self.Stop.configure(foreground="#000000")
        self.Stop.configure(highlightbackground="#d9d9d9")
        self.Stop.configure(highlightcolor="black")
        self.Stop.configure(pady="0")
        self.Stop.configure(text='''Stop''')
        self.Stop.configure(width=57)

        self.Start = Button(top, command=start)
        self.Start.place(relx=0.023, rely=0.342, height=34, width=57)
        self.Start.configure(activebackground="#d9d9d9")
        self.Start.configure(activeforeground="#000000")
        self.Start.configure(background="#d9d9d9")
        self.Start.configure(disabledforeground="#a3a3a3")
        self.Start.configure(foreground="#000000")
        self.Start.configure(highlightbackground="#d9d9d9")
        self.Start.configure(highlightcolor="black")
        self.Start.configure(pady="0")
        self.Start.configure(text='''Start''')
        self.Start.configure(width=57)

        self.entry_kp = Entry(top)
        self.entry_kp.place(relx=0.068, rely=0.141,height=30, relwidth=0.05)
        self.entry_kp.configure(background="white")
        self.entry_kp.configure(disabledforeground="#a3a3a3")
        self.entry_kp.configure(font="TkFixedFont")
        self.entry_kp.configure(foreground="#000000")
        self.entry_kp.configure(insertbackground="black")
        self.entry_kp.configure(width=44)

        self.entry_kd = Entry(top)
        self.entry_kd.place(relx=0.068, rely=0.262,height=30, relwidth=0.05)
        self.entry_kd.configure(background="white")
        self.entry_kd.configure(disabledforeground="#a3a3a3")
        self.entry_kd.configure(font="TkFixedFont")
        self.entry_kd.configure(foreground="#000000")
        self.entry_kd.configure(highlightbackground="#d9d9d9")
        self.entry_kd.configure(highlightcolor="black")
        self.entry_kd.configure(insertbackground="black")
        self.entry_kd.configure(selectbackground="#c4c4c4")
        self.entry_kd.configure(selectforeground="black")

        self.entry_ki = Entry(top)
        self.entry_ki.place(relx=0.068, rely=0.201,height=30, relwidth=0.05)
        self.entry_ki.configure(background="white")
        self.entry_ki.configure(disabledforeground="#a3a3a3")
        self.entry_ki.configure(font="TkFixedFont")
        self.entry_ki.configure(foreground="#000000")
        self.entry_ki.configure(highlightbackground="#d9d9d9")
        self.entry_ki.configure(highlightcolor="black")
        self.entry_ki.configure(insertbackground="black")
        self.entry_ki.configure(selectbackground="#c4c4c4")
        self.entry_ki.configure(selectforeground="black")

        self.label_kp = Label(top)
        self.label_kp.place(relx=0.011, rely=0.141, height=31, width=44)
        self.label_kp.configure(background="#d9d9d9")
        self.label_kp.configure(disabledforeground="#a3a3a3")
        self.label_kp.configure(foreground="#000000")
        self.label_kp.configure(text='''Kp''')
        self.label_kp.configure(width=44)

        self.label_ki = Label(top)
        self.label_ki.place(relx=0.011, rely=0.201, height=31, width=44)
        self.label_ki.configure(activebackground="#f9f9f9")
        self.label_ki.configure(activeforeground="black")
        self.label_ki.configure(background="#d9d9d9")
        self.label_ki.configure(disabledforeground="#a3a3a3")
        self.label_ki.configure(foreground="#000000")
        self.label_ki.configure(highlightbackground="#d9d9d9")
        self.label_ki.configure(highlightcolor="black")
        self.label_ki.configure(text='''Ki''')

        self.label_kd = Label(top)
        self.label_kd.place(relx=0.011, rely=0.262, height=31, width=44)
        self.label_kd.configure(activebackground="#f9f9f9")
        self.label_kd.configure(activeforeground="black")
        self.label_kd.configure(background="#d9d9d9")
        self.label_kd.configure(disabledforeground="#a3a3a3")
        self.label_kd.configure(foreground="#000000")
        self.label_kd.configure(highlightbackground="#d9d9d9")
        self.label_kd.configure(highlightcolor="black")
        self.label_kd.configure(text='''Kd''')

        self.button_kp = Button(top, command=self.set_kp)
        self.button_kp.place(relx=0.126, rely=0.141, height=24, width=57)
        self.button_kp.configure(activebackground="#d9d9d9")
        self.button_kp.configure(activeforeground="#000000")
        self.button_kp.configure(background="#d9d9d9")
        self.button_kp.configure(disabledforeground="#a3a3a3")
        self.button_kp.configure(foreground="#000000")
        self.button_kp.configure(highlightbackground="#d9d9d9")
        self.button_kp.configure(highlightcolor="black")
        self.button_kp.configure(pady="0")
        self.button_kp.configure(text='''Set Kp''')
        self.button_kp.configure(width=57)

        self.button_ki = Button(top, command = self.set_ki)
        self.button_ki.place(relx=0.126, rely=0.201, height=24, width=57)
        self.button_ki.configure(activebackground="#d9d9d9")
        self.button_ki.configure(activeforeground="#000000")
        self.button_ki.configure(background="#d9d9d9")
        self.button_ki.configure(disabledforeground="#a3a3a3")
        self.button_ki.configure(foreground="#000000")
        self.button_ki.configure(highlightbackground="#d9d9d9")
        self.button_ki.configure(highlightcolor="black")
        self.button_ki.configure(pady="0")
        self.button_ki.configure(text='''Set Ki''')

        self.button_kd = Button(top, command = self.set_kd)
        self.button_kd.place(relx=0.126, rely=0.262, height=24, width=57)
        self.button_kd.configure(activebackground="#d9d9d9")
        self.button_kd.configure(activeforeground="#000000")
        self.button_kd.configure(background="#d9d9d9")
        self.button_kd.configure(disabledforeground="#a3a3a3")
        self.button_kd.configure(foreground="#000000")
        self.button_kd.configure(highlightbackground="#d9d9d9")
        self.button_kd.configure(highlightcolor="black")
        self.button_kd.configure(pady="0")
        self.button_kd.configure(text='''Set Kd''')

        self.response = Canvas(top)
        self.response.place(relx=0.228, rely=0.02, relheight=0.952, relwidth=0.757)
        self.response.configure(background="#d9d9d9")
        self.response.configure(borderwidth="2")
        self.response.configure(insertbackground="black")
        self.response.configure(relief=RIDGE)
        self.response.configure(selectbackground="#c4c4c4")
        self.response.configure(selectforeground="black")
        self.response.configure(width=663)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.011, rely=0.02, height=41, width=174)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''PID TUNING''')
        self.Label1.configure(width=174)

        self.tick_down = Button(top, command=step_backward)
        self.tick_down.place(relx=0.033, rely=0.733, height=24, width=55)
        self.tick_down.configure(activebackground="#d9d9d9")
        self.tick_down.configure(activeforeground="#000000")
        self.tick_down.configure(background="#d9d9d9")
        self.tick_down.configure(disabledforeground="#a3a3a3")
        self.tick_down.configure(foreground="#000000")
        self.tick_down.configure(highlightbackground="#d9d9d9")
        self.tick_down.configure(highlightcolor="black")
        self.tick_down.configure(pady="0")
        self.tick_down.configure(text='''-25 ticks''')

        self.tick_up = Button(top, command=step_forward)
        self.tick_up.place(relx=0.15, rely=0.733, height=24, width=55)
        self.tick_up.configure(activebackground="#d9d9d9")
        self.tick_up.configure(activeforeground="#000000")
        self.tick_up.configure(background="#d9d9d9")
        self.tick_up.configure(disabledforeground="#a3a3a3")
        self.tick_up.configure(foreground="#000000")
        self.tick_up.configure(highlightbackground="#d9d9d9")
        self.tick_up.configure(highlightcolor="black")
        self.tick_up.configure(pady="0")
        self.tick_up.configure(text='''+25 ticks''')

    def set_kp(self):
        kp = self.entry_kp.get()
        serial_port.write("kp\n")
        serial_port.write(kp+"\n")

    def set_ki(self):
        ki = self.entry_ki.get()
        serial_port.write("ki\n")
        serial_port.write(ki+"\n")

    def set_kd(self):
        kd = self.entry_kd.get()
        serial_port.write("kd\n")
        serial_port.write(kd+"\n")

if __name__ == '__main__':
    serial_port = Serial(port="COM7", baudrate=9600)
    c = csv.writer(open("MONFICHIER.csv", "wb"))
    Thread = MyThread()
    Thread.start()
    vp_start_gui()