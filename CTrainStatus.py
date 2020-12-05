#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:52:45 2020

@author: kukurihime
"""

import copy
import datetime

class CTrainStatus:
    def __init__(self, argv):
        self.command = ""
        
        self.startTime = datetime.datetime.now()
        self.now = datetime.datetime.now()
        self.commandlineArgv = argv
        self.systemMode = argv[1]
        self.status = [0] #speed
        self.target = [0]
        self.camera = False
        self.mode = 'manual' #manual/demo/auto
        self.running = True #run or finish(main loop)
        self.mqttConnected = False #mqtt
        
    def clear(self):
        self.status[0] = 0
        self.mode = 'manual'
        
    def setCommand(self, command):
        self.command = command
    
    def getCommand(self):
        return self.command
    
    def getSystemMode(self):
        return self.systemMode
        
    def getStartTime(self):
        return self.startTime
        
    def getNow(self):
        self.now = datetime.datetime.now()
        return self.now
    
    def setStatus(self, statusList):
        self.status = statusList
        
    def getStatus(self):
        return self.status
      
    def getStatusAt(self, index):
        return self.status[index]
    
   
    def setTarget(self, targetList):
        self.target = targetList
        
    def setTargetAt(self, index, val):
        self.target[index] = val
                
    def getTarget(self):
        return self.target
    
    def getTargetAt(self, index):
        return self.target[index]
    
    def getCameraState(self):
        return self.camera
    
    def getMode(self):
        return self.mode
    
    def getRuning(self):
        return self.running
    
    def getMQTTConnected(self):
        return self.mqttConnected
    
    def setMQTTConnected(self, flg):
        self.mqttConnected = flg
    
    def setStatusFromTarget(self):
        self.status = copy.copy(self.target)
    
    def update(self):
        self.now = datetime.datetime.now()
    