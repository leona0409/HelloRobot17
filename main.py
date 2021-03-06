from gopigo import *
import time

### MY CLASS

class Piggy(object):

    def __init__(self):

        print("I AM ALIVE")

    def pulse(self):
        """chdck for obstacles, drive fixed amount forward"""
        look = us_dist(15)  # store the distance reading
        if look > 80:
            fwd()
            time.sleep(1)
            stop()

    def cruise(self):
        """drive forward, stop if sensor detects obstacle"""
        fwd()
        while{True}:
            if us_dist(15) < 30:
                stop()
            time.sleep(.2)

    def servo_sweep(self):
        """loops in a 120 degree arc and moves servo"""
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.2)

    def cha_cha(self):
        for x in range(5):
            right_rot()
            time_sleep(.5)
            left_rot()
            time.sleep(.5)
            stop()


### MY APP

poncho = Piggy()
#poncho.cha_cha()

def menu():
    while True:
        input = raw_input("Press 1 for cruise \n Press 2 for pulse \n Press 3 for sweep")
        if "1" in input:
            poncho.cruise()
        elif "2" in input:
            poncho.pulse()
        elif "3" in input:
            poncho.servo_sweep()

try:
    menu()
except Exception as ee:
    from gopigo import *
    stop()