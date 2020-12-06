#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pigpio
import time

class CRPiControler:
        def __init__(self, mode):
            self.dummyFlg = not mode #True:with pigpiod, False:without pigpiod
            if not self.dummyFlg:
                self.pi = pigpio.pi()
                
            self.vccP = 26 #VccIn
            self.in1P = 12 #hardwarePWM0
            self.in2P = 13 #hardwarePWM1
            self.ledP = 21 #LED

            self.H = 1
            self.L = 0
                
            self.freq = 1000 #PWMFrequency
            self.raspberryPiPWMValue = 1000000 #raspberryPi PWM
            
        def ready(self):
            if self.dummyFlg:
                return
            self.pi.set_mode(self.vccP, pigpio.OUTPUT)
            self.pi.set_mode(self.in1P, pigpio.ALT0)
            self.pi.set_mode(self.in2P, pigpio.ALT0)
            self.pi.set_mode(self.ledP, pigpio.OUTPUT)

            self.on(self.vccP)
            self.off(self.in1P)
            self.off(self.in2P)
            self.off(self.ledP)
            
        def finish(self):
            if self.dummyFlg:
                return
            
            self.PWMStop(self.in1P)
            self.PWMStop(self.in2P)
            time.sleep(1)
            self.off(self.vccP)
            self.off(self.ledP)
        
            self.pi.set_mode(self.in1P, pigpio.INPUT)
            self.pi.set_mode(self.in2P, pigpio.INPUT)
            self.pi.set_mode(self.vccP, pigpio.INPUT)
            self.pi.set_mode(self.ledP, pigpio.INPUT)
            self.pi.stop()

        def PWMDuty(self, dutyRatio):
            return int(self.raspberryPiPWMValue * dutyRatio)
        
        def PWMOutput(self, pin, dutyRatio):
            if self.dummyFlg:
                return
            
            self.pi.hardware_PWM(pin, self.freq, self.PWMDuty(dutyRatio))
        
        def PWMStop(self, pin):
            if self.dummyFlg:
                return
            
            self.pi.hardware_PWM(pin, self.freq, 0)
        
        def on(self, pin):
            if self.dummyFlg:
                return
            
            self.pi.write(pin, self.H)
            
        def off(self, pin):
            if self.dummyFlg:
                return
            self.pi.write(pin, self.L)