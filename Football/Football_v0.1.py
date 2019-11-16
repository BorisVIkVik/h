# Untitled - By: boris - Сб ноя 16 2019

import sensor, image, time

EXPOSURE_TIME_SCALE = 5.0

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_auto_gain(True) # must be turned off for color tracking
sensor.set_auto_exposure(True)
sensor.set_auto_whitebal(True) # must be turned off for color tracking
sensor.skip_frames(time = 500)


#sensor.set_auto_gain(False) # must be turned off for color tracking
#sensor.set_auto_exposure(False)
sensor.set_auto_whitebal(True) # must be turned off for color tracking
sensor.set_auto_gain(False)
sensor.set_auto_exposure(False)
current_exposure_time_in_microseconds=  sensor.get_exposure_us()
sensor.set_auto_exposure(False, \
    exposure_us = int(current_exposure_time_in_microseconds* EXPOSURE_TIME_SCALE))
sensor.skip_frames(time = 2000)

clock = time.clock()

threshold_blue=(15, 50, 2, 35, -47, -21)
threshold_yellow=(41, 100, -1, 35, 14, 127)

while(True):
    clock.tick()
    img = sensor.snapshot()
   # print(clock.fps())
    blobsPreviousMas = 0
    biggestBlueBlob = 0
    count =0
    blobsBlue=[]
    for blueBlob in img.find_blobs([threshold_blue],roi=(0,0,319,239), pixels_threshold=200, area_threshold=200, merge=True):
        blobsBlue.append(blueBlob)
        if(blueBlob.area() > blobsPreviousMas):
            biggestBlueBlob = count
            blobsPreviosMas =blueBlob.area()
        count+=1
    try:
        img.draw_rectangle(blobsBlue[biggestBlueBlob].rect())
        #img.draw_cross(blobsBlue[biggestBlueBlob].cx(),blobsBlue[biggestBlueBlob].cy())
    except: pass
    PreviousMas = 0
    biggestYellowBlob = 0
    count =0
    blobsYellow=[]
    for yellowBlob in img.find_blobs([threshold_yellow],roi=(0,0,319,239), pixels_threshold=200, area_threshold=200, merge=True):
        blobsYellow.append(yellowBlob)
        print(yellowBlob.area())
        print(" ")
#        print(blobPreviousMas)
        if yellowBlob.area() > PreviousMas:
            biggestYellowBlob = count
            PreviousMas = yellowBlob.area()
            print(PreviousMas)
        count+=1
    try:
        img.draw_rectangle(blobsYellow[biggestYellowBlob].rect())
        img.draw_cross(blobsYellow[biggestYellowBlob].cx(),blobsYellow[biggestYellowBlob].cy())
    except: pass

#    for c in img.find_circles(roi=(100,0,100,200),x_margin=5, y_margin=5, r_margin=5,r_max=15):
#        img.draw_circle(c.x(), c.y(), c.r(), color=(255,0,0))
