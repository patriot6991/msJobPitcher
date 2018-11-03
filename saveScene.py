import maya.cmds as mc
import os
import searchFiles

def saveScene():
   # reload(searchFiles)
   cntID = searchFiles.searchFiles()
   fileName = "test.render.v{}".format(cntID+1)
   mc.file(rename=r"C:\Users\KMR\Documents\maya\projects\default\scenes\{}.ma".format(fileName))
   mc.file(save=True,type="mayaAscii")

mc.window(title='testWin', w=200)
mc.columnLayout(adj=True)
mc.separator( h=3 )
mc.text("testWin")
mc.separator( h=3 )
mc.button( label = '増分セーブ（仮）', w=100, h=40, command='saveScene()')
mc.showWindow()