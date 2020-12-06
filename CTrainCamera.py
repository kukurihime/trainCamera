#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import CTrainStatus
import CTrainControler
import CTrainCameraView
import CTrainCameraMQTTSub
import CRepetationalThread


class CTrainCamera(CRepetationalThread.CRepetationalThread):
    def __init__(self, argv, interval = 0.1):
        super().__init__(interval)
        self.ts = CTrainStatus.CTrainStatus(argv)
        self.tcv = CTrainCameraView.CTrainCameraView(self.ts) #another thread
        self.tc = CTrainControler.CTrainControler(self.ts)

        self.tcms = CTrainCameraMQTTSub.CTrainCameraMQTTSub(self.tc)
        
        #self.tcv.start()
        
    def func(self):
        #if not self.tcms.isConnected():
        #    print('test2')
        #    self.tcms.connect()
        
        self.valueUpdate()
        self.targetUpdate()
        self.execute()
        if not self.ts.getCommand() == 'q':
            self.setCommand( "")
    
    def valueUpdate(self):
        self.ts.update()
    
    def targetUpdate(self):
        self.tc.statusUpdate()

    def execute(self): 
        self.tc.run()
        
    def setCommand(self, command):
        self.command = command
        self.tc.setCommand(command)
        
    def getCommand(self):
        return self.ts.getCommand()
    
    def finish(self):
        self.tcv.join()
    
    
    def demo(self):
        time.sleep(1)
        self.tc.setStatus({1})
        self.tc.run()
        time.sleep(5)
               
        self.tc.setStatus({2})
        self.tc.run()
        time.sleep(5)
        
        self.tc.setStatus({3})
        self.tc.run()
        time.sleep(5)
        
        time.sleep(1)
        self.tc.setStatus({4})
        self.tc.run()
        time.sleep(5)

        self.tc.setStatus({1})
        self.tc.run()
        time.sleep(5)
        
        self.tc.setStatus({-1})
        self.tc.run()
        time.sleep(5)
