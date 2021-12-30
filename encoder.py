from RotaryEncoder import RotaryEncoder
from rotary_irq_rp2 import RotaryIRQ
from machine import Pin

def onValueChange(sender: RotaryEncoder):
    print("Value: ")
    print(sender.Value())


def onValueSelect(sender: RotaryEncoder):
    print("Select: ")
    print(sender.Value())

buttonPin = 13  # purple
encClkPin = 11  # white
encDataPin = 12  # grey

fileEncoder = RotaryEncoder(encClkPin, encDataPin, buttonPin)
fileEncoder.UpdateEncoder(10)
fileEncoder.on("value_change", onValueChange)
fileEncoder.on("select", onValueSelect)
