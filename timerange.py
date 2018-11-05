import maya.cmds as mc
import csv

csvPath = '/Users/ryota/Documents/python/timerange.csv'

def getTimerange():
    f = open(csvPath, 'r')
    # print f
    x = 0
    shotID = "s15c02"
    timeShotID = ""
    timeStart = 0
    timeEnd = 0

    reader = csv.reader(f)
    # header = next(reader)
    for row in reader:
        # print row
        if shotID in row:
            timeShotID = row[0]
            timeStart = row[2]
            timeEnd = row[3]
            
            if row[2] == '' or row[3] == '':
                timeStart = 0
                timeEnd = 0
                print "show CSV File ==>> {}".format(csvPath)
                break

    f.close()

    return [timeStart,timeEnd]

    # setTimeRange.....
    # mc.setAttr('defaultRenderGlobals.startFrame', timeStart)
    # mc.setAttr('defaultRenderGlobals.endFrame', timeEnd)

mc.window(title='test', w=200)
mc.columnLayout(adj=True)
mc.button( label = 'csvTest', w=100, h=40, command='getTimerange()')

mc.showWindow()

