#!/usr/bin/env python3
"""
PWM Tone Generator

based on https://www.coderdojotc.org/micropython/sound/04-play-scale/
"""

import machine
import utime

# GP16 is the speaker pin
SPEAKER_PIN = 16

# create a Pulse Width Modulation Object on this pin
speaker = machine.PWM(machine.Pin(SPEAKER_PIN))


def playtone(frequency: float, duration: float) -> None:
    speaker.duty_u16(2000)
    speaker.freq(frequency)
    utime.sleep(duration)


def quiet():
    speaker.duty_u16(0)

notes = [
    (247, 0.6),  
    (330, 0.6),  
    (370, 0.6),  
    (392, 0.6),  
    (370, 0.6),  
    (330, 0.6),  
    (261, 0.6),  
]

freq: float = 30
duration: float = 0.1  

print("Playing frequency (Hz):")

for freq, duration in notes:
    print(freq)
    playtone(freq, duration)
    utime.sleep(.1)

# Turn off the PWM
quiet()
