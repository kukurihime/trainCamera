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
        self.update()
        
    def func(self):
        os.system('clear')
        self.update()
        print(self.apliInfo)
        print(self.separator)
        print(self.status)
        print(self.separator)
        print(self.commandView)
        print(self.command, '')
    
    def update(self):
        self.apliInfo = "SystemStartTime:\t" + self.ts.getStartTime().strftime('%Y/%m/%d %H:%M:%S') +'\n' \
            + "now:\t\t\t" + self.ts.getNow().strftime('%Y/%m/%d %H:%M:%S') + '\n' \
            + "SystemMode:" + self.ts.getSystemMode()
        
        self.separator = "---------------------------------------------------"
        self.status = "MQTT Connected:\t" + str(self.ts.getMQTTConnected())+'\n' \
                    + "TrainSpeed:\t" + str(self.ts.getStatusAt(0)) + '\n' \
                    + "Command:" + self.ts.getCommand() + "\tCommandID:" + str(id(self.ts.getCommand()))
        
        self.commandView = "q:quit\n" \
                            "y:speedDown\tu:speedup"
        self.command ="command:"
        
        
if __name__ == "__main__":
    tcv = CTrainCameraView("dummy",0.5)
    tcv.start()
    time.sleep(5)
    tcv.join()
    
        
            