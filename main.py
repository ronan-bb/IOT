import pycom
import time
import machine

def clignote():
    """
    pycom.rgbled(0xff00)
    pycom.heartbeat(False)
    for cycles in range(10): # stop after 10 cycles
        pycom.rgbled(0x000099) # green
        pycom.rgbled(0x000000) # yellow
        pycom.rgbled(0xff0000) # red"""
    for cycles in range(20):
        pycom.rgbled(0xEE2C2C)
        time.sleep(0.5)



def thermo():
    adc = machine.ADC()
    apin = adc.channel(pin='P13', attn=adc.ATTN_11DB)
    q=4096/6
    while True:
        val = apin()
        if val<q:
            pycom.rgbled(0x00BFFF) # ocean
        elif q<val<2*q:
            pycom.rgbled(0x0000EE) #bleu
        elif 2*q<val<3*q:
            pycom.rgbled(0x54FF9F) #vert clair
        elif 3*q<val<4*q:
            pycom.rgbled(0x7FFF00) #vert
        elif 4*q<val<5*q:
            pycom.rgbled(0xFFB90F) #orange
        elif 5*q<val<6*q:
            clignote()
            #pycom.rgbled(0xEE2C2C) #rouge
        print(val)
        time.sleep(0.2)
    pycom.heartbeat(False)
    print(val)
thermo()
