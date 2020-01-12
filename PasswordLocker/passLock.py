#!/usr/bin/pythom
# passLock.py 
import sys
import pyperclip

passwords = {
    'emails' : '##########',
    'overwatch' : '@@@@@@@@@'
    }

if len(sys.argv) < 2:
    print('Usage: python passLock.py [insert account here] to copy password into clipboard')
    sys.exit()

print(passwords)

