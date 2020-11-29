#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:52:45 2020

@author: kukurihime
"""

import datetime

class CTrainStatus:
    def __init__(self, argv):
        self.startTime = datetime.datetime.now()
        self.now = datetime.datetime.now()
        self.commandlineArgv = argv
        self.systemMode = argv[1]
        
        self.speed = 0
        self.camera = False
        self.mode = 'manual' #manual/demo/auto
        self.running = True #run or finish(main loop)
        self.mqttConnected = False #mqtt
        
    def clear(self):
        self.speed = 0
        self.mode = 'manual'
        
    def getSystemMode(self):
        return self.systemMode
        
    def getStartTime(self):
        return self.startTime
        
    def getNow(self):
        self.now = datetime.datetime.now()
        return self.now
    
    def getSpeed(self):
        return self.speed
    
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
        
        
        
    
        
        
        
                