from gopigo import *
import time

### MY CLASS

class Piggy(object):

    def __init__(self):

        print("Hello, I'm your robot")
        self.dance()

    def dance(self):
        fwd()
        time.sleep(1.5)
        right_rot()
        time.sleep(.5)
        stop()

### MY APP

poncho = Piggy()