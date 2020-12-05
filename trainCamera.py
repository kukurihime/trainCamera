#!/usr/bin/python3
# -*- coding: utf-8 -*-

import CTrainCamera
import CRealtimeKeyInput
import time
import sys


print("Train Camera Start!!")
time.sleep(0.5)

argv = sys.argv
if len( argv ) == 1:
    argv.append("real") 

tc = CTrainCamera.CTrainCamera(argv)
tc.start() #other thread

#command proccess loop
rki = CRealtimeKeyInput.CRealtimeKeyInput()
rki.setDaemon(True)
rki.start()
key = ''
while not key == 'q':
    if rki.hasNewKey():
        key = rki.getKey()
        tc.setCommand(key)
    else:
        key = tc.getCommand()
    #print("key:", key)
    if key == 'q':
        rki.stop()
        pass
        
    time.sleep(0.1)
    
        

print( "quit command")
rki.finish()
tc.finish()
tc.join()

print("Train Camera Finished!!")



