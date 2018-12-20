# Art-Net protocol for Fadecandy
#Adapted from https://github.com/chunk100/Glediator-with-Fadecandy

#Fadecandy stuff
import opc, time

#Artnet stuff
from twisted.internet import protocol, endpoints
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

#Initialise Fadecandy stuff
numLEDs = 250
client = opc.Client('172.20.0.2:7890')
black = (0, 0, 0)
x_size = 10
y_size = 25

# This tells the software where the split between 2 universes is
uni_1_y_size = 17
uni_2_y_size = 8


gridarray = [ [0],
[0, 0,49,50,99,100,149,150,199,200,249],
[0, 1,48,51,98,101,148,151,198,201,248],
[0, 2,47,52,97,102,147,152,197,202,247],
[0, 3,46,53,96,103,146,153,196,203,246],
[0, 4,45,54,95,104,145,154,195,204,245],
[0, 5,44,55,94,105,144,155,194,205,244],
[0, 6,43,56,93,106,143,156,193,206,243],
[0, 7,42,57,92,107,142,157,192,207,242],
[0, 8,41,58,91,108,141,158,191,208,241],
[0, 9,40,59,90,109,140,159,190,209,240],
[0, 10,	39,	60,	89,	110,	139,	160,	189,	210,	239],
[0, 11,	38,	61,	88,	111,	138,	161,	188,	211,	238],
[0, 12,	37,	62,	87,	112,	137,	162,	187,	212,	237],
[0, 13,	36,	63,	86,	113,	136,	163,	186,	213,	236],
[0, 14,	35,	64,	85,	114,	135,	164,	185,	214,	235],
[0, 15,	34,	65,	84,	115,	134,	165,	184,	215,	234],
[0, 16,	33,	66,	83,	116,	133,	166,	183,	216,	233],
[0, 17,	32,	67,	82,	117,	132,	167,	182,	217,	232],
[0, 18,	31,	68,	81,	118,	131,	168,	181,	218,	231],
[0, 19,	30,	69,	80,	119,	130,	169,	180,	219,	230],
[0, 20,	29,	70,	79,	120,	129,	170,	179,	220,	229],
[0, 21,	28,	71,	78,	121,	128,	171,	178,	221,	228],
[0, 22,	27,	72,	77,	122,	127,	172,	177,	222,	227],
[0, 23,	26,	73,	76,	123,	126,	173,	176,	223,	226],
[0, 24,	25,	74,	75,	124,	125,	174,	175,	224,	225]]


class ArtNet(DatagramProtocol):
    def __init__(self):
        self.pixels = [ black ] * numLEDs
        self.uni_1_data_received = 0
        self.uni_2_data_received = 0

    def write_pixels(self):
        if self.uni_1_data_received == 1 and self.uni_2_data_received == 1:
            client.put_pixels(self.pixels)
            self.uni_1_data_received = 0
            self.uni_2_data_received = 0

    def datagramReceived(self, data, (host, port)):
        if ((len(data) > 18) and (data[0:8] == "Art-Net\x00")):
            rawbytes = map(ord, data)
            # print(rawbytes)
            opcode = rawbytes[8] + (rawbytes[9] << 8)
            protocolVersion = (rawbytes[10] << 8) + rawbytes[11]
            if ((opcode == 0x5000) and (protocolVersion >= 14)):
                sequence = rawbytes[12]
                physical = rawbytes[13]
                sub_net = (rawbytes[14] & 0xF0) >> 4
                universe = rawbytes[14] & 0x0F
                net = rawbytes[15]
                rgb_length = (rawbytes[16] << 8) + rawbytes[17]
                # print "seq %d phy %d sub_net %d uni %d net %d len %d" % \
                    # (sequence, physical, sub_net, universe, net, rgb_length)
                idx = 18
                x = 1

                if universe == 1:
                    y = 1

                    while ((idx < (rgb_length+18)) and (y <= uni_1_y_size)):
                        r = rawbytes[idx]
                        idx += 1
                        g = rawbytes[idx]
                        idx += 1
                        b = rawbytes[idx]
                        idx += 1
                        # print("x= " + str(x) + ", y=" + str(y) + " r=" + str(r) + ", g=" + str(g) + "b= " +str(b))
                        self.pixels[gridarray[y][x]] = (r, g, b)
                        x += 1
                        if (x > x_size):
                            x = 1
                            y += 1

                    self.uni_1_data_received = 1

                if universe == 2:
                    y = y_size - uni_2_y_size + 1

                    while ((idx < (rgb_length+18)) and (y <= y_size)):
                        r = rawbytes[idx]
                        idx += 1
                        g = rawbytes[idx]
                        idx += 1
                        b = rawbytes[idx]
                        idx += 1
                        # print("x= " + str(x) + ", y=" + str(y) + " r=" + str(r) + ", g=" + str(g) + "b= " +str(b))
                        self.pixels[gridarray[y][x]] = (r, g, b)
                        x += 1
                        if (x > x_size):
                            x = 1
                            y += 1

                    self.uni_2_data_received = 1


                self.write_pixels()


reactor.listenUDP(6454, ArtNet())
reactor.run()
