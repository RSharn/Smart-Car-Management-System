from time import sleep
import pigpio
import RPi.GPIO as GPIO
import ultrasonic as u
import relay as r
import os

def jack_fnc():
        k=0
        DIR = 20     # Direction GPIO Pin
        STEP = 21    # Step GPIO Pin
        hall_pin = 22
        CW_pin=17
        CCW_pin=18
        Jack_pin=16

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(hall_pin_1,GPIO.IN)
        GPIO.setup(hall_pin_2,GPIO.IN)
        GPIO.setup(hall_pin_3,GPIO.IN)
        GPIO.setup(hall_pin_4,GPIO.IN)

        GPIO.setup(CW_pin,GPIO.IN)
        GPIO.setup(CCW_pin,GPIO.IN)
        GPIO.setup(rear_pin,GPIO.IN)
        GPIO.setup(front_pin,GPIO.IN)
        GPIO.setup(Jack_pin,GPIO.IN)

        GPIO.setup(CW_pin,GPIO.OUT)
        GPIO.setup(CCW_pin,GPIO.OUT)
        GPIO.setup(Jack_pin,GPIO.OUT)
        GPIO.setup(rear_pin,GPIO.OUT)
        GPIO.setup(front_pin,GPIO.OUT)
        GPIO.setup(DIR, GPIO.OUT)
        GPIO.setup(STEP, GPIO.OUT)

        hall_1= GPIO.input(hall_pin_1)
        hall_2= GPIO.input(hall_pin_2)
        hall_3= GPIO.input(hall_pin_3)
        hall_4= GPIO.input(hall_pin_4)
        cw=GPIO.input(CW_pin)
        ccw=GPIO.input(CCW_pin)
        jack=GPIO.input(Jack_pin)
        rr=GPIO.input(rear_pin)
        fr=GPIO.input(front_pin)


        # Connect to pigpiod daemon
        myCmd = 'sudo pigpio'
        os.system(myCmd)
        pi = pigpio.pi()

        # Set up pins as an output
        pi.set_mode(DIR, pigpio.OUTPUT)
        pi.set_mode(STEP, pigpio.OUTPUT)


        # Set duty cycle and frequency
        #       pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
        #       pi.set_PWM_frequency(STEP, 500)  # 500 pulses per second
        try:
                while(True):
        #               pi.set_PWM_dutycycle(STEP, 0)  # PWM off
        #               pi.stop()
                        cw=GPIO.input(CW_pin)
                        ccw=GPIO.input(CCW_pin)
                        jack=GPIO.input(Jack_pin)
                        rr=GPIO.input(rear_pin)
                        fr=GPIO.input(front_pin)
                                       
        ##################### For Front ###########################
                        if(fr==1):
                            if(cw==1):
                                while hall_1 == 1:
                                        k=1 # Manual control to stop motor 
                                        pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
                                        pi.set_PWM_frequency(STEP, 500)
                                        h=1  #Variable for setting direction of motor
                                        GPIO.output(DIR,h)
                                        sleep(.1)
                                        print("First loop",h)
                                        hall = GPIO.input(hall)
                            elif (ccw==1):
                                while hall_2 == 1:
                                        k=1
                                        pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
                                        pi.set_PWM_frequency(STEP, 500)
                                        h=0
                                        GPIO.output(DIR,h)
                                        sleep(.1)
                                        print("second loop",h)
                                        hall = GPIO.input(hall)
                            if(k==1):
                                pi.set_PWM_dutycycle(STEP, 0)  # PWM off
                                pi.stop()
                            d = u.dis()
                #           d=input("enter distance")
                            while(d<30):
                #               d=input("enter distance")
                #               print(1)
                                r.onrea()
                                sleep(0.1)
                                d=u.dis()
                            if(k==1):
                                r.offrea()

                            d = u.dis()
                #           d=input("enter distance")
                            print(jack,"jack_pin")
                            while(d>10):
                                if(jack==1):
                #                       d=input("enter distance")
                #                       print("yo")
                                        r.onreb()
                                        sleep(0.1)
                                        d=u.dis()
                            if(k==1):
                                r.offreb()
        ##################### For Rear ###############################
                        if(rr==1):
                            if(cw==1):
                                while hall_3 == 1:
                                        k=1 
                                        pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
                                        pi.set_PWM_frequency(STEP, 500)
                                        h=1
                                        GPIO.output(DIR,h)
                                        sleep(.1)
                                        print("First loop",h)
                                        hall = GPIO.input(hall)
                            elif (ccw==1):
                                while hall_4== 1:
                                        k=1
                                        pi.set_PWM_dutycycle(STEP, 128)  # PWM 1/2 On 1/2 Off
                                        pi.set_PWM_frequency(STEP, 500)
                                        h=0
                                        GPIO.output(DIR,h)
                                        sleep(.1)
                                        print("second loop",h)
                                        hall = GPIO.input(hall)
                            if(k==1):
                                pi.set_PWM_dutycycle(STEP, 0)  # PWM off
                                pi.stop()
                            d = u.dis()
                #           d=input("enter distance")
                            while(d<30):
                #               d=input("enter distance")
                #               print(1)
                                r.onrea()
                                sleep(0.1)
                                d=u.dis()
                            if(k==1):
                                r.offrea()

                            d = u.dis()
                #           d=input("enter distance")
                            print(jack,"jack_pin")
                            while(d>10):
                                if(jack==1):
                #                       d=input("enter distance")
                #                       print("yo")
                                        r.onreb()
                                        sleep(0.1)
                                        d=u.dis()
                            if(k==1):
                                r.offreb()

        except KeyboardInterrupt:
                      print ("\nCtrl-C pressed.  Stopping PIGPIO and exiting...")
        finally:
                      pi.set_PWM_dutycycle(STEP, 0)  # PWM off
                      pi.stop()
                      print("finally executed")
                      exit
