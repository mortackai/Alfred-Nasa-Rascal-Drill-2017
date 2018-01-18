import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pins = [12,16,18,22]
GPIO.setup(pins, GPIO.OUT)

#accelerate to desired stepper speed and hold for desired time
def accel(t):

    at = 0.05
    dtcy = 0
    freq = 1
    indrill = GPIO.PWM(12,20000)
    indrill.start(0)
    outdrill = GPIO.PWM(18,20000)
    outdrill.start(0)
    GPIO.output(16,0)
    GPIO.output(22,1)
        
    for n in xrange(0,50):
        #freq += 1
	dtcy += 1
        indrill.ChangeDutyCycle(dtcy)
	#indrill.ChangeFrequency(freq)
        #print freq
	outdrill.ChangeDutyCycle(dtcy)
	print dtcy
	time.sleep(at)
        
    time.sleep(t)
    
    for n in xrange(0,50):
        #freq -= 1
	dtcy -= 1
	indrill.ChangeDutyCycle(dtcy)
        #indrill.ChangeFrequency(freq)
        #print freq
	outdrill.ChangeDutyCycle(dtcy)
	print dtcy
	time.sleep(at)

    GPIO.output(16,1)
    time.sleep(0.5)

    for n in xrange(0,50):
        #freq += 1
	dtcy += 1
	indrill.ChangeDutyCycle(dtcy)
        #indrill.ChangeFrequency(freq)
        #print freq
	outdrill.ChangeDutyCycle(dtcy)
	print dtcy
        time.sleep(at)

    time.sleep(t)
    
    for n in xrange(0,50):
        #freq -= 1
        #indrill.ChangeFrequency(freq)
        #print freq
	dtcy -= 1
	indrill.ChangeDutyCycle(dtcy)
	outdrill.ChangeDutyCycle(dtcy)
	print dtcy
	time.sleep(at)

    GPIO.cleanup()

accel(10)
