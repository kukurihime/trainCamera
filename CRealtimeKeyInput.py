#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 22:23:28 2020

@author: kukurihime
"""

import sys
import termios
import time

class CRealtimeKeyInput:
    def __init__(self):
        self.key = ''
        
        self.fd = sys.stdin.fileno()
        self.newTermios = termios.tcgetattr(self.fd)
        self.oldTermios = termios.tcgetattr(self.fd)
        self.newTermios[3] &= ~termios.ICANON
        self.newTermios[3] &= ~termios.ECHO
        termios.tcsetattr(self.fd, termios.TCSANOW, self.newTermios)

    def keyInput(self):
        self.key = sys.stdin.read(1)
    
    def keyInputEcho( self ):
        self.keyInput()
        print( self.key, end = '')
        sys.stdout.flush()
            
    def getKey(self):
        return self.key
        
    def finish(self):
        termios.tcsetattr(self.fd, termios.TCSANOW, self.oldTermios)
        
if __name__ == "__main__":
    rki = CRealtimeKeyInput()
    count = 0
    print("keyInputTest")
    while not( rki.getKey() == 'q'):
        rki.keyInput()
        print( count, end = '')
        print( ':', end = '')
        print( rki.getKey(), end = '')
        sys.stdout.flush()
        
        count += 1
        time.sleep( 0.1)
    
    print("keyInputEchoTest")
    count = 0
    rki.key = ''
    
    while not( rki.getKey() == 'q'):
        rki.keyInputEcho()
        count += 1
        time.sleep(0.1)
        
    rki.finish()
    print( 'finish' )
        
    
    
    
    

        
    