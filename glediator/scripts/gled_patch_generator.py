import socket

x_size = 10
y_size = 25
pixel_count = 250
channel_count = pixel_count * 3
pixels_per_universe = 170
universe_count = 2
artnet_host = '172.20.0.3'

print('#GLEDIATOR Patch File')
print('Patch_Matrix_Size_X=%d' % x_size)
print('Patch_Matrix_Size_Y=%d' % y_size)
print('Patch_Num_Unis=%d' % universe_count)

ip1, ip2, ip3, ip4 = str(artnet_host).split('.')


counter = 0
uni_counter = 0
uni_id = 0

for y in range(0, y_size):
    for x in range(0, x_size):
        if uni_counter == pixels_per_universe:
            uni_counter = 0
            uni_id = uni_id + 1

        if uni_counter == 0:
            print('Patch_Uni_ID_%d_IP1=%s' % (uni_id, ip1))
            print('Patch_Uni_ID_%d_IP2=%s' % (uni_id, ip2))
            print('Patch_Uni_ID_%d_IP3=%s' % (uni_id, ip3))
            print('Patch_Uni_ID_%d_IP4=%s' % (uni_id, ip4))
            print('Patch_Uni_ID_%d_Net_Nr=0' % uni_id)
            print('Patch_Uni_ID_%d_Sub_Net_Nr=0' % uni_id)
            print('Patch_Uni_ID_%d_Uni_Nr=%d' % (uni_id, uni_id+1))
            print('Patch_Uni_ID_%d_Num_Ch=%d' % (uni_id, pixels_per_universe*3))


        print('Patch_Pixel_X_%d_Y_%d_Ch_R = %d' % (x, y, uni_counter*3))
        print('Patch_Pixel_X_%d_Y_%d_Ch_G = %d' % (x, y, uni_counter*3+1))
        print('Patch_Pixel_X_%d_Y_%d_Ch_B = %d' % (x, y, uni_counter*3+2))
        print('Patch_Pixel_X_%d_Y_%d_Uni_ID = %d' % (x, y, uni_id))
        counter = counter + 1
        uni_counter = uni_counter + 1
        # print('Counter: %d  Universe Counter: %d' % (counter, uni_counter))
