#!/usr/bin/env python

from burp import IBurpExtender
from burp import IBurpExtenderCallbacks
from burp import IExtensionHelpers
from burp import IContextMenuFactory
from burp import IContextMenuInvocation

from javax.swing import JMenuItem

import socket
import json
import urllib2
import socket
import threading

API_KEY = "KEY_GOES_HERE"

class BurpExtender(IBurpExtender,IContextMenuFactory):

    def	registerExtenderCallbacks(self, callbacks):
        self.callbacks = callbacks
        self.helpers = callbacks.getHelpers()
        self.callbacks.setExtensionName("Shodan Scan")
        self.callbacks.registerContextMenuFactory(self)
        return

    def createMenuItems(self,invocation):
        menu_list = []
        menu_list.append(JMenuItem("Scan with Shodan",None,actionPerformed= lambda x, inv=invocation:self.startThreaded(self.shodan_scan,inv)))
        return menu_list

    def startThreaded(self,func,*args):
        th = threading.Thread(target=func,args=args)
        th.start()

    def shodan_scan(self,invocation):
        http_traffic = invocation.getSelectedMessages()
        if len(http_traffic) !=0:
                service = http_traffic[0].getHttpService()
                hostname = service.getHost()
                ip = socket.gethostbyname(hostname)
                r = urllib2.Request("https://api.shodan.io/shodan/host/"+ip+"?key="+API_KEY)
                data = json.loads(urllib2.urlopen(r).read())
                print ("Organization: {}".format(data['org']))
                print ("IP is {}".format(data['ip_str']))
                print ("Located in {}".format(data['country_name']))
                print ("Open ports : {}".format(data['ports']))