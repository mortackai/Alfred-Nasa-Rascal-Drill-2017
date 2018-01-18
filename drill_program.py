import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

outputpins = [12,16,18,22,29,31,32,33,35,36,38,40,7,11,13,15,8]
inputpins = []
GPIO.setup(outputpins,GPIO.OUT)
GPIO.setup(inputpins,GPIO.IN)

#accelerate X axis stepper to desired stepper speed and hold for desired time in desired direction
def xstepper(t,d):

    GPIO.output(16,d)
    time.sleep(0.5)    
    x = GPIO.PWM(12,1)
    x.start(50)
    freq = 1

    for n in xrange(0,400):
        freq += 10
        x.ChangeFrequency(freq)
        print freq
        time.sleep(0.05)
        
    time.sleep(t)
    
    for n in xrange(0,400):
        freq -= 10
        x.ChangeFrequency(freq)
        print freq
        time.sleep(0.05)

    GPIO.cleanup()

#accelerate Y axis stepper to desired stepper speed and hold for desired time in desired direction
def ystepper(t,d):

    GPIO.output(22,d)
    time.sleep(0.5)
    freq = 1    
    y = GPIO.PWM(18,1)
    y.start(50)

    for n in xrange(0,100):
        freq += 10
        y.ChangeFrequency(freq)
        print freq
        time.sleep(0.1)
        
    time.sleep(t)
    
    for n in xrange(0,100):
        freq -= 10
        y.ChangeFrequency(freq)
        print freq
        time.sleep(0.1)

    GPIO.cleanup()

#accelerate Z1 axis stepper to desired stepper speed and hold for desired time in desired direction
def z1stepper(t,d):

    GPIO.output(11,d)
    time.sleep(0.5)
    z1 = GPIO.PWM(7,1)
    z1.start(50)
    freq = 1

    for n in xrange(0,500):
        freq += 10
        z1.ChangeFrequency(freq)
        print freq
        time.sleep(0.05)
        
    time.sleep(t)
    
    for n in xrange(0,500):
        freq -= 10
        z1.ChangeFrequency(freq)
        print freq
        time.sleep(0.05)

    GPIO.cleanup()

'''#accelerate Z2 axis stepper to desired stepper speed and hold for desired time in desired direction
def z2stepper(t,d):

    GPIO.output( ,d)
    time.sleep(0.5)
    
    z2 = GPIO.PWM( ,0)
    z2.start(50)

    for n in xrange(0,500):
        freq += 10
        z2.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)
        
    time.sleep(t)
    
    for n in xrange(0,500):
        freq -= 10
        z2.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)

    GPIO.cleanup()

'''
#accelerate auger motor to top speed in direction for length of time
def inauger(t,d):

    GPIO.setmode(GPIO.BOARD)
    pins = [12, 8]
    GPIO.setup(pins,GPIO.OUT)
    GPIO.output(12,d)
    time.sleep(0.5)
    indrill = GPIO.PWM(8,1)
    indrill.start(100)
    freq = 1
        
    for n in xrange(0,10):
        freq += 100
        indrill.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)
        
    time.sleep(t)
    
    for n in xrange(0,10):
        freq -= 100
        indrill.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)

    GPIO.cleanup()


'''#accelerate auger motor to top speed in direction for length of time
def outauger(t,d):

    GPIO.output(11,d)
    time.sleep(0.5)
    indrill = GPIO.PWM(7,1)
    freq = 0
        
    for n in xrange(0,100):
        freq += 1
        indrill.ChangeFrequency(freq)
        print freq
        time.sleep(1)
        
    time.sleep(t)
    
    for n in xrange(0,100):
        freq -= 1
        indrill.ChangeFrequency(freq)
        print freq
        time.sleep(1)

    indrill.stop()
    GPIO.cleanup()'''


inauger(5,1)
time.sleep(1)
inauger(5,0)
GPIO.cleanup()
