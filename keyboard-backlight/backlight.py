#!/usr/bin/ env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkinter as tk
import subprocess ,tkFont
from subprocess import *

root = tk.Tk()
root.title(" ==> Backlight <== ")
root.resizable(0, 0)
back = tk.Frame(master=root,  bg='#000000')
back.pack_propagate(0) 
back.pack(fill=tk.BOTH, expand=True)


def s3():

   subprocess.check_output('cd cmake-build-debug && echo | sudo ./openauranb FF0000', shell=True)

def s4():

   subprocess.check_output('cd cmake-build-debug && echo | sudo ./openauranb 00FF00', shell=True)

def s5():

   subprocess.check_output('cd cmake-build-debug && echo | sudo ./openauranb 000000', shell=True)

def s6():

   subprocess.check_output('cd cmake-build-debug && echo | sudo ./openauranb FFFFFF', shell=True)

def s7():

   subprocess.check_output('cd cmake-build-debug && echo | sudo ./openauranb 8A2BE2', shell=True)

def s8():

   subprocess.check_output('cd cmake-build-debug && echo | sudo ./openauranb 00FFFF', shell=True)

h = tkFont.Font(family='Hack', size=10, weight=tkFont.BOLD )

stip = tk.Button(master=back, text='Red', bg='red', font=h , fg="white" , command=s3)
stip.pack()
stip.config( height=3, width = 13 )
stip.pack(side=tk.LEFT)
stip.grid(row=1, column=0)


spip = tk.Button(master=back, text='Green', bg='green',fg="white", font=h , command=s4)
spip.pack()
spip.config( height=3, width = 13 )
spip.pack(side=tk.LEFT)
spip.grid(row=1, column=1)

ship = tk.Button(master=back, text='Black', bg='black',fg="white", font=h , command=s5)
ship.pack()
ship.config( height=3, width = 14 )
ship.pack(side=tk.LEFT)
ship.grid(row=1, column=2)

stip = tk.Button(master=back, text='White', bg='White', font=h , fg="black" , command=s6)
stip.pack()
stip.config( height=3, width = 13 )
stip.pack(side=tk.LEFT)
stip.grid(row=2, column=0)

spip = tk.Button(master=back, text='violet', bg='violet', font=h , fg="white" , command=s7)
spip.pack()
spip.config( height=3, width = 13 )
spip.pack(side=tk.LEFT)
spip.grid(row=2, column=1)

ship = tk.Button(master=back, text='Aqua', bg='aqua', font=h , fg="white" , command=s8)
ship.pack()
ship.config( height=3, width = 14 )
ship.pack(side=tk.LEFT)
ship.grid(row=2, column=2)

root.mainloop()




