import os
import glob
import maya.cmds as mc
import logging

path = r"C:\Users\KMR\Documents\maya\projects\default\scenes\*.ma"
shotID = "test"

def searchFiles():
   fListA = glob.glob(path)
   fListA = [os.path.basename(r) for r in fListA]
   print fListA
   fListB = []

   for item in fListA:
       if shotID in item :
           result = True
           fListB.append(item)

   result
   print result
   cnt = len(fListB)
   return cnt

mc.window(title='test', w=200)
mc.columnLayout(adj=True)
mc.separator( h=3 )
mc.text("testWin")
mc.separator( h=3 )
mc.button( label = '', w=100, h=40, command='search()')
mc.showWindow()