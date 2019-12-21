#!/usr/bin/env python
import opc, time

numLEDs = 250
client = opc.Client('172.20.0.2:7890')

black = [ (0,0,0) ] * numLEDs
client.put_pixels(black)
client.put_pixels(black)