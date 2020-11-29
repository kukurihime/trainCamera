#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import CTrainStatus
import CTrainControler
import CTrainCameraView
import CTrainCameraMQTTSub
import CRepetationalThread


class CTrainCamera(CRepetationalThread.CRepetationalThread):
    def __init__(self, argv, command):
        super().__init__(interval=0.1)
        self.ts = CTrainStatus.CTrainStatus(argv)
        self.tcv = CTrainCameraView.CTrainCameraView(self.ts)
        self.tc = CTrainControler.CTrainControler(self.ts)

        self.tcms = CTrainCameraMQTTSub.CTrainCameraMQTTSub(self.ts)
        self.mqttTimeout = 10 #if mqtt timeout this sec, train is stop
        self.command = command
        self.order = ""
        
        
        self.tcv.start()
        
        
    def order( self, s ):
        self.order = s
        
    def func(self):
        pass #in preparation

    def demo(self):
        time.sleep(1)
        self.tc.run(1)
        time.sleep(5)
               
        self.tc.run(2)
        time.sleep(5)
        
        self.tc.run(3)
        time.sleep(5)
        
        self.tc.run(4)
        time.sleep(5)

        self.tc.run(1)
        time.sleep(5)
        
        self.tc.run(-1)
        time.sleep(5)

    
    def finish(self):
        self.tcv.join()
        
        
        