#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 16:23:54 2020

@author: kukurihime
"""

import CRPiControler

class CTrainControler:
    def __init__(self, ts):
        self.ts = ts
        self.speedTable = { \
                           -1:(0.0, 0.6), \
                           0:(0.0, 0.0), \
                           1:(0.6, 0.0), \
                           2:(0.7, 0.0), \
                           3:(0.8, 0.0), \
                           4:(0.9, 0.0) \
                           }
        self.maxSpeed = 4
        self.minSpeed = -1
        self.rpcMode = True #full functional mode
        if self.ts.getSystemMode() == 'dummy': 
            self.rpcMode = False
        
        self.rpc = CRPiControler.CRPiControler(self.rpcMode)
        self.rpc.ready()

    def statusUpdate(self): 
        command = self.ts.getCommand()
        if command == 'q':
            self.stop()
        elif command == 'u':
            self.setTargetSpeed(self.ts.getStatusAt(0) + 1)
        elif command == 'y':
            self.setTargetSpeed(self.ts.getStatusAt(0) - 1)
        
        self.ts.setStatusFromTarget()
    
    def run(self):
        self.outputPWMPair(self.speedTable[self.ts.getStatusAt(0)])
        
        
    def stop(self):
        self.ts.setStatus([0])
        self.ts.update()
        self.run()
    
    def setTargetSpeed(self, num):
        if type(num) is not int:
            return
        
        if num > self.maxSpeed:
            num = self.maxSpeed
        elif num < self.minSpeed:
            num = self.minSpeed
        
        self.ts.setTargetAt(0, num)
                
        
    
    def outputPWMPair(self, PWMPair):
        self.rpc.PWMOutput(self.rpc.in1P, PWMPair[0])
        self.rpc.PWMOutput(self.rpc.in2P, PWMPair[1])
        
    
    def setMQTTConnected(self, flg):
        self.ts.setMQTTConnected(flg)
        
    def setCommand(self, command):
        self.ts.setCommand(command)