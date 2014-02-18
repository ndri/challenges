#!/usr/bin/env python
# 68 - Graphical Digital Clock (GUI)
import pygtk
pygtk.require('2.0')
import gtk
import gobject
from datetime import datetime

class Clock:
    def __init__(self):
	self.window = gtk.Window()
	self.window.set_title("Clock")
	self.window.connect('destroy', self.quit)
	self.window.set_border_width(12)
	
	self.box = gtk.HBox()
	self.window.add(self.box)
	
	time = str(datetime.now())[11:19]
	self.label = gtk.Label(time)
	
	self.box.add(self.label)
	self.window.show_all()
	
	gobject.timeout_add_seconds(1, self.update)

    def quit(self, widget, callback_data=None):
        gtk.main_quit()
	
    def update(self):
	time = str(datetime.now())[11:19]
	self.label.set_label(time)
	return True

if __name__ == "__main__":
    app = Clock()
    gtk.main()
