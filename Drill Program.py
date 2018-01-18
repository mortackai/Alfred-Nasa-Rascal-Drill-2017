try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
#imports gpio interface for pi and displays error if not working

#set pin numbering to BOARD or BCM, uncomment one to activate
#GPIO.setmode(GPIO.BOARD)
#GPIO.setmode(GPIO.BCM)

#setup which pins are inputs and outputs
channel_in = []
channel_out = []
GPIO.setup(channel_in, GPIO.OUT)
GPIO.setup(channel_out, GPIO.IN)

#move the drill to base location or x=0 y=0 z=0
def zero():

    GPIO.cleanup()

#moves the drill assembly to the first designated position
def position_one():

    GPIO.cleanup()

#lowers the outer drill and drills to X depth and then stops
def outer_drill_lower():

    GPIO.cleanup()

#lowers the inner drill and drills to X depth and then stops
def inner_drill_lower():

    GPIO.cleanup()

#Turns on the heating element for X amount of time
def heating_element():

    GPIO.cleanup()

#turns on water pump for X amount of time
def pump():

    GPIO.cleanup()

#raises the inner drill
def inner_drill_raise():

    GPIO.cleanup()

#raises the outer drill
def outer_drill_raise():

    GPIO.cleanup()

#moves the drill to the second position
def position_two():

    GPIO.cleanup()
