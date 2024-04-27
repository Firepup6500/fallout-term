#! /usr/bin/env python
import fallout_login as login
import fallout_boot as boot
import fallout_locked as locked
import fallout_hack as hack
import fallout_selection as select
import fallout_data as data
from fallout_functions import soundTest, isQueueEmpty, addSound
from time import sleep
import sys

hard = False
if '--hard' in sys.argv:
    hard = True

skip = False
if '--skip' in sys.argv:
    skip = True

if '--preload' in sys.argv:
    soundTest()

try:
    addSound("poweron")
    while not isQueueEmpty():
        sleep(0.2)
    if skip or boot.beginBoot(hard):
        while not isQueueEmpty():
            sleep(0.2)
        pwd = None
        if not skip:
            pwd = hack.beginLogin()
        else:
            pwd = "VERYVERYSECUREPASSWORD"
        if pwd != None:
            login.beginLogin(hard, 'ADMIN', pwd)
            while not isQueueEmpty():
                sleep(0.2)
            sel = 0
            while sel != 3:
                sel = select.beginSelection(data.ROBCO_HEADERS, data.SOFT_HEADERS, data.MAIN_MENU)
                while not isQueueEmpty():
                    sleep(0.2)
                if   sel == 0:
                    loc = 0
                    while loc != 1:
                        MENU = [data.LOCK_MENU[tog][data.LOCK_CONDS[tog]] for tog in data.LOCK_CONDS.keys()]
                        MSGS = [data.LOCK_MSGS[tog][data.LOCK_CONDS[tog]] for tog in data.LOCK_CONDS.keys()]
                        loc = select.beginSelection(data.ROBCO_HEADERS, data.SOFT_HEADERS, MENU, MSGS)
                        if loc == 0:
                            if data.LOCK_CONDS['LOCKED']:
                                data.LOCK_CONDS['LOCKED'] = 0
                            else:
                                data.LOCK_CONDS['LOCKED'] = 1
                elif sel == 1:
                    tur = 0
                    while tur != 2:
                        MENU = [data.TURRET_MENU[tog][data.TURRET_CONDS[tog]] for tog in data.TURRET_CONDS.keys()]
                        MSGS = [data.TURRET_MSGS[tog][data.TURRET_CONDS[tog]] for tog in data.TURRET_CONDS.keys()]
                        tur = select.beginSelection(data.TURRET_HEADERS, data.TURRET_HEADERS2, MENU, MSGS)
                        if   tur == 0:
                            data.TURRET_CONDS['TARGETING'] = 1
                        elif tur == 1:
                            if data.TURRET_CONDS['ENABLED']:
                                data.TURRET_CONDS['ENABLED'] = 0
                            else:
                                data.TURRET_CONDS['ENABLED'] = 1
                elif sel == 2:
                    log = 0
                    while log != data.LOG_RET_ID:
                        log = select.beginSelection(data.ROBCO_HEADERS, data.SOFT_HEADERS, data.LOG_NAMES)
                        if log != data.LOG_RET_ID:
                            select.beginSelection(data.ROBCO_HEADERS, data.LOGS[data.LOG_NAMES[log]].split("\n"), ["Return"])
        else:
            locked.beginLocked()
            print('Login failed')
except KeyboardInterrupt:
    pass

addSound("poweroff")
while not isQueueEmpty():
	sleep(0.2)
