import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pwmpins = 12
dirpins = 16
GPIO.setup(pwmpins, GPIO.OUT)
GPIO.setup(dirpins,GPIO.OUT)

#accelerate to desired stepper speed and hold for desired time
def accel(t):

    GPIO.output(16,0)
    freq = 1
    time.sleep(0.5)
    x = GPIO.PWM(12,1)
    x.start(50)
#    y = GPIO.PWM(16,1)
#    y.start(50)
#    z1 = GPIO.PWM(18,1)
#    z1.start(50)
#    z2 = GPIO.PWM(22,1)
#    z2.start(50)

#    xdir = GPIO.output(number, d)
        
    for n in xrange(0,500):
        freq += 10
        x.ChangeFrequency(freq)
#	y.ChangeFrequency(freq)
#	z1.ChangeFrequency(freq)
#	z2.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)
    time.sleep(t)
    
    for n in xrange(0,500):
        freq -= 10
        x.ChangeFrequency(freq)
#	y.ChangeFrequency(freq)
#	z1.ChangeFrequency(freq)
#	z2.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)

    time.sleep(0.5)
    GPIO.output(16,GPIO.HIGH)

    for n in xrange(0,500):
	freq += 10
	x.ChangeFrequency(freq)
	print freq
	time.sleep(0.01)

    time.sleep(t)

    for n in xrange(0,500):
	freq -= 10
	x.ChangeFrequency(freq)
	print freq
	time.sleep(0.01)

accel(14)

GPIO.cleanup()
