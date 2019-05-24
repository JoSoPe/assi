import sys
import select
import struct

# en el select tindrem 2 inputs, una del teclat ila altre del socket

def wait_input(llista):
    rlist, _, _= select.select(llista, [], [])
    if rlist[0] == llista[0]:
        data=sys.stdin.readline()
        print 'Teclat: '+data
    elif rlist[0] == llista[1]:
        pos=getMouseEvent()
        print ("L%d, M: %d, R: %d, x: %d, y: %d, z: %d"%pos);
    else:
        print 'impossible'

def getMouseEvent():
    buf = file.read(3);
    button = ord(buf[0]);
    bLeft = button & 0x1;
    bMiddle = (button & 0x2) >0;
    bRight = (button & 0x4) >0;
    x,y = struct.unpack("bb",buf [1:]);
    datam = (bLeft, bMiddle,bRight, x, y)
    return datam

file = open ("/dev/input/mice","rb")

print file.read()
file_d = [sys.stdin , file]
while 1:
    wait_input(file_d)
file.close()
