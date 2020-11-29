#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 31 12:49:06 2020

@author: kukurihime
"""
import paho.mqtt.client as mqtt
import CTrainStatus

class CTrainCameraMQTTSub:
    def __init__(self, ts):
        self.ts = ts
        
        self.host = '127.0.0.1'
        self.port = 1883
        self.topic = 'trainCameraOrder'
        self.client = mqtt.Client(protocol = mqtt.MQTTv311)
        self.keepalive = 60

        
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        try:
            self.connect()
        except ConnectionRefusedError as e:
            self.ts.setMQTTConnected(False)
        else:
            self.ts.setMQTTConnected(True)
            
    def connect(self):
        self.client.connect(self.host, port = self.port, keepalive = self.keepalive)
        self.client.loop_forever()
        
    def on_connect(self, client, userdata, flags, respons_code):
        print('status{0}'.format(respons_code))
        
        client.subscribe(self.topic)
        
    def on_message(self, client, userdata, msg):
        print(msg.topic + ' ' + str(msg.payload))
        
        