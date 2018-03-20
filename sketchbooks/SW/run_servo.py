import os
from subprocess import call


def compiling():
    os.chdir('/home/qbc/PycharmProjects/ard/sketchbooks/SW')
    call('make',shell=True)
    call("make upload",shell=True)







#ARDUINO_CORE_PATH  = $(HOME)/arduino/hardware/tiny/cores/tiny


