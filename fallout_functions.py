import curses
import time
import sys
from pathlib import Path as _Path
from playsound import playsound as _play
from threading import Thread
from time import sleep


LETTER_PAUSE = 5

INPUT_PAUSE = 500 # ms

TYPE_DELAY = 40

HIDDEN_MASK = '*'

NEWLINE = 10

DELETE = 330

BACKSPACE = 263

_playing = False

_soundQueue = []

global _queueRunning
_queueRunning = False

def slowWrite(window, text, pause = LETTER_PAUSE, fake_user = False, silent = False):
    """
    wrapper for curses.addstr() which writes the text slowly
    """
    if not fake_user and not silent:
        addSound("beep")
    for i in range(len(text)):
        window.addstr(text[i])
        window.refresh()
        curses.napms(pause)
    if fake_user and not silent:
        _playSound("keyenter", True)

def upperInput(window, hidden = False, can_newline = True):
    """
    Reads user input until enter key is pressed. Echoes the input in upper case

    hidden - if true the output will be masked
    can_newline - if true the input is followed by a newline and the screen is
                  scrolled if necessary
    """
    inchar = 0
    instr = ''
    while inchar != NEWLINE:
        inchar = window.getch()
        # convert lower case to upper
        if inchar > 96 and inchar < 123:
            inchar -= 32
        # deal with backspace
        if inchar in [DELETE, BACKSPACE]:
            if len(instr) > 0:
                #addSound("keyenter")
                instr = instr[:-1]
                cur = window.getyx()
                window.move(cur[0], cur[1] - 1)
                window.clrtobot()
            else:
                continue
        elif inchar > 255:
            continue
        # output the character
        elif inchar != NEWLINE:
            #addSound("keyenter")
            instr += chr(inchar)
            if hidden:
                window.addch(HIDDEN_MASK)
            else:
                window.addch(inchar)
        elif can_newline:
             #addSound("keyenter")
            window.addch(NEWLINE)
    return instr

def centeredWrite(window, text, pause = LETTER_PAUSE):
    """
    Writes to the current line but centers the text
    """
    width = window.getmaxyx()[1]
    window.move(window.getyx()[0], int(width / 2 - len(text) / 2))
    slowWrite(window, text, pause)


def _soundCheck():
    """
    Internal use - Checks if the user explicity disabled sound or not
    """
    return '--no-sound' not in sys.argv


def _playSound(file, block = False):
    """
    Internal use - plays a specific sound from the current directory
    """
    if _soundCheck():
        _play(str(_Path.cwd() / f'audio/{file}.wav'), block)


def _playQueue():
    """
    Internal use - play sounds from a queue
    """
    global _queueRunning
    global _soundQueue
    if _queueRunning:
        return
    _queueRunning = True
    while _soundCheck():
        if len(_soundQueue) > 0:
            _playSound(_soundQueue[0], True)
            _soundQueue.pop(0)
        else:
            sleep(0.02)


def queueIsEmpty():
    """
    Check if the sound queue is empty
    """
    return len(_soundQueue) == 0


def soundTest():
    addSound("beep")
    addSound("beep")
    addSound("keyenter")
    addSound("keyenter")
    addSound("wrongpass")
    addSound("wrongpass")
    addSound("correctpass")
    addSound("correctpass")
    addSound("poweron")
    addSound("poweron")
    addSound("poweroff")
    addSound("poweroff")
    global _soundQueue
    while not queueIsEmpty():
        sleep(0.2)


def addSound(file):
    """
    Add sounds to the queue
    """
    global _soundQueue
    if _soundCheck():
        _soundQueue.extend([file])


_queueMgr = Thread(target=_playQueue)
_queueMgr.daemon = True
_queueMgr.start()
