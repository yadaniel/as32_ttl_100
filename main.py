#!/cygdrive/c/Python37/python

import sys, argparse
import serial, atexit

comPort = "com8"

comSettings = {
    "port": comPort,
    "baudrate": 9600,
    "bytesize": serial.EIGHTBITS,
    "parity": serial.PARITY_NONE,
    "timeout": 0.5
}

try:
    com = serial.Serial(**comSettings)
    atexit.register(lambda: (com.close(), sys.stdout.write("com port %s closed" % comPort)))
except:
    print("could not open com port %s" % comPort)
    sys.exit()


def showConfig():
    # com.write(b"\xC1\xC1\xC1")            # option 1
    com.write(bytes.fromhex("C1C1C1"))      # option 2
    ans = com.read(100)
    sys.stdout.write(",".join(map(lambda b: "%02X" % b, ans)) + "\n")
    sys.stdout.flush()

def read():
    while True:
        # sys.stdout.write(com.read(100))
        sys.stdout.flush()

if __name__ == "__main__":
    showConfig()
    read()



