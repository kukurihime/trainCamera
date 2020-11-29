#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 00:31:54 2020

@author: kukurihime
"""
import CRepetationalThread
import sys
import os
import time
import CTrainStatus

class CTrainCameraView(CRepetationalThread.CRepetationalThread):
    def __init__(self, ts, interval=0.5):
        super().__init__(interval)
        self.ts = ts
        self.apliInfo = "SystemStartTime:" + ts.getStartTime().strftime('%Y/%m/%d %H:%M:%S') +'\n'\
            + "SystemMode:" + ts.getSystemMode()
        
        self.separator = "---------------------------------------------------"
        self.commandView = "q:quit\n"
        self.command ="command:"
        
    def func(self):
        os.system('clear')
        print(self.apliInfo)
        print(self.separator)
        print(self.commandView)
        print(self.command, '')
        
if __name__ == "__main__":
    tcv = CTrainCameraView(0.5)
    tcv.start()
    time.sleep(5)
    tcv.join()
    
        
            