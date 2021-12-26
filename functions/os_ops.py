import os
import subprocess as sp

paths = {
    "calculator": "C:\\Windows\\System32\\calc.exe",
    "terminal": "C:\\Users\\Indranil\\cmder\\Cmder.exe",
    "atom": "C:\\Users\\Indranil\\AppData\\Local\\atom\\atom.exe",
    "code": "C:\\Users\\Indranil\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "chrome": "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
}


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    os.startfile(paths['calculator'])


def open_terminal():
    os.startfile(paths['terminal'])


def open_atom():
    os.startfile(paths['atom'])


def open_vscode():
    os.startfile(paths['code'])


def open_chrome():
    os.startfile(paths['chrome'])


def open_cmd():
    os.system('start cmd')
