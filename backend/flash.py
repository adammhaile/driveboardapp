# Super Awesome LasaurGrbl python flash script.
# 
# Copyright (c) 2011 Nortd Labs
# Open Source by the terms of the Gnu Public License (GPL3) or higher.

import os, sys


def flash_upload(serial_port, data_root):
    DEVICE = "atmega328p"
    CLOCK = "16000000"
    PROGRAMMER = "avrisp"
    BITRATE = "115200"
    BUILDNAME = "LasaurGrbl"
 
    if sys.platform == "darwin":  # OSX
        AVRDUDEAPP    = os.path.join(data_root, "firmware/tools_osx/avrdude")
        AVRDUDECONFIG = os.path.join(data_root, "firmware/tools_osx/avrdude.conf")
    
    elif sys.platform == "win32": # Windows
        AVRDUDEAPP    = os.path.join(data_root, "firmware/tools_win32/avrdude")
        AVRDUDECONFIG = os.path.join(data_root, "firmware/tools_win32/avrdude.conf")
    
    elif sys.platform == "linux" or sys.platform == "linux2":  #Linux
        AVRDUDEAPP    = os.path.join(data_root, "firmware/tools_linux32/avrdude")
        AVRDUDECONFIG = os.path.join(data_root, "firmware/tools_linux32/avrdude.conf")
              
    os.system('%(dude)s -c %(programmer)s -b %(bps)s -P %(port)s -p %(device)s -C %(dudeconf)s -B 10 -F -U flash:w:%(product)s.hex:i' 
        % {'dude':AVRDUDEAPP, 'programmer':PROGRAMMER, 'bps':BITRATE, 'port':serial_port, 'device':DEVICE, 'dudeconf':AVRDUDECONFIG, 'product':BUILDNAME})

    # fuse setting taken over from Makefile for reference
    #os.system('%(dude)s -U hfuse:w:0xd2:m -U lfuse:w:0xff:m' % {'dude':AVRDUDEAPP})
        
