import time
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

#accelerate X axis stepper to desired stepper speed and hold for desired time in desired direction
def xstepper(t,d):

    GPIO.setmode(GPIO.BOARD)
    xoutput = [3,5]
    xinput = []
    GPIO.setup(xoutput,GPIO.OUT)
    GPIO.setup(xinput,GPIO.IN)

    GPIO.output(3,d)
    time.sleep(0.5)    
    x = GPIO.PWM(5,1)
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

    x.stop()
    GPIO.cleanup()

#accelerate Y axis stepper to desired stepper speed and hold for desired time in desired direction
def ystepper(t,d):

    GPIO.setmode(GPIO.BOARD)
    youtput = [7,8]
    yinput = []
    GPIO.setup(youtput,GPIO.OUT)
    GPIO.setup(yinput,GPIO.IN)

    GPIO.output(7,d)
    time.sleep(0.5)
    freq = 1    
    y = GPIO.PWM(8,1)
    y.start(50)

    for n in xrange(0,400):
        freq += 10
        y.ChangeFrequency(freq)
        print freq
        time.sleep(0.05)
        
    time.sleep(t)
    
    for n in xrange(0,400):
        freq -= 10
        y.ChangeFrequency(freq)
        print freq
        time.sleep(0.05)

    y.stop()
    GPIO.cleanup()

#accelerate Z1 axis stepper to desired stepper speed and hold for desired time in desired direction
def z1stepper(t,d):

    GPIO.setmode(GPIO.BOARD)
    z1output = [10,11]
    z1input = []
    GPIO.setup(z1output,GPIO.OUT)
    GPIO.setup(z1input,GPIO.IN)

    GPIO.output(10,d)
    time.sleep(0.5)
    z1 = GPIO.PWM(11,1)
    z1.start(50)
    freq = 1

    for n in xrange(0,50):
        freq += 10
        z1.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)
        
    time.sleep(t)
    
    for n in xrange(0,50):
        freq -= 10
        z1.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)

    z1.stop()
    GPIO.cleanup()

#accelerate Z2 axis stepper to desired stepper speed and hold for desired time in desired direction
def z2stepper(t,d):

    GPIO.setmode(GPIO.BOARD)
    z2output = [12,13]
    z2input = []
    GPIO.setup(z2output,GPIO.OUT)
    GPIO.setup(z2input,GPIO.IN)

    GPIO.output(12,d)
    time.sleep(0.5)   
    z2 = GPIO.PWM(13,1)
    z2.start(50)
    freq = 1

    for n in xrange(0,50):
        freq += 10
        z2.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)
        
    time.sleep(t)
    
    for n in xrange(0,50):
        freq -= 10
        z2.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)

    z2.stop()
    GPIO.cleanup()

def z1z2stepper(t,d):

    GPIO.setmode(GPIO.BOARD)
    z1z2output = [10,11,12,13]
    z1z2input = []
    GPIO.setup(z1z2output,GPIO.OUT)
    GPIO.output(11,d)
    GPIO.output(12,d)
    time.sleep(0.5)
    
    z1 = GPIO.PWM(10,1)
    z2 = GPIO.PWM(13,1)
    z1.start(50)
    z2.start(50)
    freq = 1

    for n in xrange(0,10):
        freq += 10
	z1.ChangeFrequency(freq)
        z2.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)
        
    time.sleep(t)
    
    for n in xrange(0,10):
        freq -= 10
	z1.ChangeFrequency(freq)
        z2.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)

    GPIO.cleanup()

def z1z2inout(t,d):

    GPIO.setmode(GPIO.BOARD)
    z1z2output = [10,11,12,13,15,16,18,19]
    z1z2input = []
    GPIO.setup(z1z2output,GPIO.OUT)
    direction = [10,12,15,18]
    GPIO.output(direction,d)
    time.sleep(0.5)
    
    z1 = GPIO.PWM(11,1)
    z2 = GPIO.PWM(13,1)
    inner = GPIO.PWM(16,1)
    outer = GPIO.PWM(19,1)
    z1.start(50)
    z2.start(50)
    inner.start(50)
    outer.start(50)
    freq = 1

    for n in xrange(0,10):
        freq += 10
	z1.ChangeFrequency(freq)
        z2.ChangeFrequency(freq)
        inner.ChangeFrequency(freq)
        outer.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)
        
    time.sleep(t)
    
    for n in xrange(0,10):
        freq -= 10
	z1.ChangeFrequency(freq)
        z2.ChangeFrequency(freq)
        inner.ChangeFrequency(freq)
        outer.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)

    GPIO.cleanup()


#accelerate auger motor to top speed in direction for length of time
def inauger(t,d):

    GPIO.setmode(GPIO.BOARD)
    a1output = [15,16]
    a1input = []
    GPIO.setup(a1output,GPIO.OUT)
    GPIO.setup(a1input,GPIO.IN)

    GPIO.output(15,d)
    time.sleep(0.5)
    indrill = GPIO.PWM(16,1)
    indrill.start(90)
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

    indrill.stop()
    GPIO.cleanup()


#accelerate auger motor to top speed in direction for length of time
def outauger(t,d):

    GPIO.setmode(GPIO.BOARD)
    a2output = [18,19]
    a2input = []
    GPIO.setup(a2output,GPIO.OUT)
    GPIO.setup(a2input,GPIO.IN)

    GPIO.output(18,d)
    time.sleep(0.5)
    outdrill = GPIO.PWM(19,1)
    outdrill.start(90)
    freq = 1
        
    for n in xrange(0,10):
        freq += 100
        outdrill.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)
        
    time.sleep(t)
    
    for n in xrange(0,10):
        freq -= 100
        outdrill.ChangeFrequency(freq)
        print freq
        time.sleep(0.01)

    outdrill.stop()
    GPIO.cleanup()

def pump(t):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(21,GPIO.OUT)
    GPIO.output(21,1)
    print "Pump is on!"
    time.sleep(t)
    GPIO.output(21,0)
    print "Pump is off!"

    GPIO.cleanup()

def heat(t):

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(22,GPIO.OUT)
    GPIO.output(22,1)
    print "Heat is on!"
    time.sleep(t)
    GPIO.output(22,0)
    print "Heat is off!"

    GPIO.cleanup()





#pump(10)
#time.sleep(0.5)
#heat(1)
#time.sleep(0.5)
#xstepper(1,0)
#time.sleep(0.5)
#ystepper(1,1)
#time.sleep(0.5)
#z2stepper(1,0)
#time.sleep(0.5)
#z1stepper(1,1)
#time.sleep(0.5)
#inauger(1,0)
#time.sleep(1)
z1z2stepper(1,0)
#outauger(20,1)
#time.sleep(0.5)
GPIO.cleanup()
