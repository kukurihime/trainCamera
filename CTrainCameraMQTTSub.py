#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:49:06 2020

@author: kukurihime
"""
import paho.mqtt.client as mqtt
import CTrainControler
import time

class CTrainCameraMQTTSub:
    def __init__(self, tc):
        self.tc = tc
        self.host = '127.0.0.1'
        self.port = 1883
        self.topic = 'trainCamera/command'
        self.client = mqtt.Client(protocol = mqtt.MQTTv311)
        self.keepalive = 60
        self.reconnectWaitTime = 0.5
        
        self.client.on_connect = self.onConnect
        self.client.on_disconnect = self.onDisconnect
        self.client.on_message = self.onMessage
        
        self.connect()
        
        self.com = ""
            
    def connect(self):
        try:
            self.client.connect(self.host, port = self.port, keepalive = self.keepalive)
        except ConnectionRefusedError as e:
            self.tc.setMQTTConnected(False)
            return False
        else:
            self.tc.setMQTTConnected(True)
        
        self.client.loop_start()
        
    def isConnected(self):
        return self.client.isconnected()
        
    def onConnect(self, client, userdata, flags, responsCode):
        self.tc.setMQTTConnected(responsCode)
        client.subscribe(self.topic)
        
    def onDisconnect(self,client, userdata, flags, responsCode):
        self.tc.setMQTTConnected(responsCode)
        
    def onMessage(self, client, userdata, msg):
        self.com = msg.payload
        self.com = self.com.decode()
        self.tc.setCommand(self.com)
        