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
        self.speedTable = {'-1':(0, 0.6), '0':(0,0), '1':(0.6, 0),'2':(0.7, 0), '3':(0.8, 0), '4':(0.9, 0)}
        self.rpcMode = True
        if self.ts.getSystemMode() == 'dummy': 
            self.rpcMode = False
        
        self.rpc = CRPiControler.CRPiControler(self.rpcMode)
        self.rpc.ready()
        
         
    def run(self, spd):
        self.outputPWMPair(self.speedTable[str(spd)])
        
    def stop(self):
        self.outputPWMPair(self.speedTable[str(0)])
    
    def outPutPWMPair(self, PWMPair):
        self.rpc.PWMOutput(self.rpc.in1P, self.rpc.PWMDuty(PWMPair[0]))
        self.rpc.PWMOutput(self.rpc.in2P, self.rpc.PWMDuty(PWMPair[1]))