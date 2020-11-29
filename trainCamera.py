#!/usr/bin/python3
# -*- coding: utf-8 -*-

import CTrainCamera
import CRealtimeKeyInput
import time
import sys

print("Train Camera Start!!")
argv = sys.argv

command = ''
tc = CTrainCamera.CTrainCamera(argv, command)
tc.start() #other thead

#command proccess loop
rki = CRealtimeKeyInput.CRealtimeKeyInput()
while not( command == 'q'):
    rki.keyInput()
    command = rki.getKey()

rki.finish()
tc.finish()
tc.join()

print("Train Camera Finished!!")
      



