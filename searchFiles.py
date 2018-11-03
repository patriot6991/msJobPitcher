import os
import glob
import logging


def searchFiles(shotID, path):
    logging.debug('searchFiles')
    path = path + r'\*.*'
    fListA = glob.glob(path)
    fListA = [os.path.basename(r) for r in fListA]
    fListB = []

    for item in fListA:
        if shotID in item:
            fListB.append(item)

    return len(fListB)

