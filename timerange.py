import maya.cmds as mc
import csv
import logging


def getTimerange(csvPath=r'', shotID=''):
    logging.debug('get time range')
    f = open(csvPath, 'r')
    x = 0
    shotID = shotID
    timeShotID = ""
    timeStart = 0
    timeEnd = 0

    reader = csv.reader(f)

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

    return [timeStart, timeEnd]