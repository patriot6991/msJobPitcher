# coding:UTF-8
import maya.cmds as mc
import maya.mel as mel
import os
import logging
import myLogger
import time
import RenderSetting
import AOVsReader
import browsFile
import createRenderNode
import configSetting
import importScenes
import saveScene
import searchFiles
import timerange


class UiClass(object):
    def __init__(self):
        self.shotID = r''
        self.cam_path = r''
        self.anim_path = r''
        self.projectPath = r''
        self.stagePath = r''
        self.extra1Path = r''
        self.extra2Path = r''
        self.extra3Path = r''
        self.extra4Path = r''
        self.extra5Path = r''
        self.extra6Path = r''
        self.extra7Path = r''
        self.extra8Path = r''
        self.extra9Path = r''
        self.renderSettingPath = r''
        self.AOVsSettingPath = r''
        self.deadlineSettingPath = r''
        self.minTime = ''
        self.maxTime = ''
        self.timerangePath =r''

    def develop(self, *args):
        reload(myLogger)
        reload(RenderSetting)
        reload(AOVsReader)
        reload(browsFile)
        reload(createRenderNode)
        reload(configSetting)
        reload(importScenes)
        reload(saveScene)
        reload(searchFiles)
        reload(timerange)

    def jobNewScenes(self, *args):
        logging.debug('jobNewScenes')
        mc.file(f=True, new=True)

    def jobOpenStage(self, *args):
        logging.debug('jobOpenStage')
        self.stagePath = mc.textField('f2', q=True, text=True)
        mc.file(self.stagePath, open=True)

    def jobImportCamera(self, *args):
        logging.debug('jobImportCamera')
        self.cam_path = mc.textField('f3', q=True, text=True)
        importScenes.importScenes(self.cam_path)

    def jobImportAnimation(self, *args):
        logging.debug('jobImportAnimation')
        self.anim_path = mc.textField('f4', q=True, text=True)
        importScenes.importScenes(self.anim_path)

    def jobExtra1(self, *args):
        logging.debug('jobExtra1')
        self.extra1Path = mc.textField('f5', q=True, text=True)
        ex1 = mc.textField('f5', q=True, tx=True)
        importScenes.importScenes(ex1)

    def jobEctra2(self, *args):
        logging.debug('jobExtra2')
        self.extra2Path = mc.textField('f6', q=True, text=True)
        ex2 = mc.textField('f6', q=True, tx=True)
        importScenes.importScenes(ex2)

    def jobExtra3(self, *args):
        logging.debug('jobExtra3')
        self.extra3Path = mc.textField('f7', q=True, text=True)
        ex3 = mc.textField('f7', q=True, tx=True)
        importScenes.importScenes(ex3)

    def jobExtra4(self, *args):
        logging.debug('jobExtra4')
        self.extra4Path = mc.textField('f8', q=True, text=True)
        ex4 = mc.textField('f8', q=True, tx=True)
        importScenes.importScenes(ex4)

    def jobExtra5(self, *args):
        logging.debug('jobExtra5')
        self.extra5Path = mc.textField('f9', q=True, text=True)
        ex5 = mc.textField('f9', q=True, tx=True)
        importScenes.importScenes(ex5)

    def jobExtra6(self, *args):
        logging.debug('jobExtra6')
        self.extra6Path = mc.textField('f10', q=True, text=True)
        ex6 = mc.textField('f10', q=True, tx=True)
        importScenes.importScenes(ex6)

    def jobExtra7(self, *args):
        logging.debug('jobExtra7')
        self.extra7Path = mc.textField('f11', q=True, text=True)
        ex7 = mc.textField('f11', q=True, tx=True)
        importScenes.importScenes(ex7)

    def jobExtra8(self, *args):
        logging.debug('jobExtra8')
        self.extra8Path = mc.textField('f12', q=True, text=True)
        ex8 = mc.textField('f12', q=True, tx=True)
        importScenes.importScenes(ex8)

    def jobExtra9(self, *args):
        logging.debug('jobExtra9')
        self.extra9Path = mc.textField('f13', q=True, text=True)
        ex9 = mc.textField('f13', q=True, tx=True)
        importScenes.importScenes(ex9)

    def jobRenderSettings(self, *args):
        logging.debug('jobRenderSetting')
        self.renderSettingPath = mc.textField('f14', q=True, text=True)
        self.minTime = mc.timeField('f18', q=True, v=True)
        self.maxTime = mc.timeField('f19', q=True, v=True)
        logging.debug('minTime is %s' % (self.minTime))
        logging.debug('maxTime is %s' % (self.maxTime))
        RenderSetting.jsonRead(path=self.renderSettingPath, start=self.minTime, end=self.maxTime)

    def jobAOVsSetting(self, *args):
        logging.debug('jobAOVsSetting')
        self.AOVsSettingPath = mc.textField('f15', q=True, text=True)
        AOVsReader.AOVsRead(path=self.AOVsSettingPath)

    def jobSubmitDeadline(self, *args):
        logging.debug('jobSubmitDeadline')
        RenderSetting.setCam(shot=self.shotID)
        mel.eval('source "C:/Users/user/PycharmProjects/msJobPitcher/SubmitDeadline.mel";')
        time.sleep(7)
        mel.eval("DeadlineSubmitterOnOk;")


    def jobSetShotID(self, *args):
        logging.debug('jobSetShotID')
        self.shotID = mc.textField('f17', q=True, text=True)
        logging.debug('shotID is %s' % self.shotID)

        self.cam_path = os.path.join(self.projectPath, 'scenes', 'cam', '%s.cam.v1.fbx' %(self.shotID))
        mc.textField('f3', e=True, tx=self.cam_path)
        logging.debug('camera path is %s' %(self.cam_path))

        self.anim_path = os.path.join(self.projectPath, 'scenes', 'shot', '%s.shot.v1.ma' %(self.shotID))
        mc.textField('f4', e=True, tx=self.anim_path)
        logging.debug('animation path is %s' %(self.anim_path))

        self.jobGetTimeRange()
        RenderSetting.setRendableCamera(self.shotID)

    def jobBuildRenderScene(self, *args):
        logging.debug('jobBuildRenderScene')

        if mc.checkBox('c1', q=True, v=True) == True:
            self.jobNewScenes()

        if mc.checkBox('c2', q=True, v=True) == True:
            self.jobOpenStage()

        if mc.checkBox('c3', q=True, v=True) == True:
            self.jobImportCamera()

        if mc.checkBox('c4', q=True, v=True) == True:
            self.jobImportAnimation()

        if mc.checkBox('c5', q=True, v=True) == True:
            self.jobExtra1()

        if mc.checkBox('c6', q=True, v=True) == True:
            self.jobEctra2()

        if mc.checkBox('c7', q=True, v=True) == True:
            self.jobExtra3()

        if mc.checkBox('c8', q=True, v=True) == True:
            self.jobExtra4()

        if mc.checkBox('c9', q=True, v=True) == True:
            self.jobExtra5()

        if mc.checkBox('c10', q=True, v=True) == True:
            self.jobExtra6()

        if mc.checkBox('c11', q=True, v=True) == True:
            self.jobExtra7()

        if mc.checkBox('c12', q=True, v=True) == True:
            self.jobExtra8()

        if mc.checkBox('c13', q=True, v=True) == True:
            self.jobExtra9()

        createRenderNode.create()
        
        if mc.checkBox('c14', q=True, v=True) == True:
            self.jobRenderSettings()

        if mc.checkBox('c15', q=True, v=True) == True:
            self.jobAOVsSetting()

        if mc.checkBox('c17', q=True, v=True) == True:
            self.jobSaveScene()

        if mc.checkBox('c16', q=True, v=True) == True:
            self.jobSubmitDeadline()

    def jobGetTimeRange(self, *args):
        logging.debug('jobGetTimeRange')
        range_list = timerange.getTimerange(csvPath=self.timerangePath, shotID=self.shotID)
        mc.timeField('f18', e=True, v=range_list[0])
        mc.timeField('f19', e=True, v=range_list[1])


    def jobSaveScene(self, *args):
        logging.debug('jobSaveScene')
        saveScene.saveScene(self.shotID, path=self.projectPath)

    def browsStage(self, *args):
        logging.debug('browsStage')
        path = browsFile.search(defPath=self.stagePath)
        mc.textField('f2', e=True, text=path)

    def browsCamera(self, *args):
        logging.debug('browsCamera')
        dir = os.path.join(self.projectPath, 'scenes', 'cam')
        path = browsFile.search(defPath=dir)
        mc.textField('f3', e=True, text=path)

    def browsAnimation(self, *args):
        logging.debug('browsAnimation')
        dir = os.path.join(self.projectPath, 'scenes', 'shot')
        path = browsFile.search(defPath=dir)
        mc.textField('f4', e=True, text=path)

    def browsExtra1(self, *args):
        logging.debug('browsExtra1')
        dir = os.path.join(self.projectPath, 'scenes')
        path = browsFile.search(defPath=dir)
        mc.textField('f5', e=True, text=path)

    def browsExtra2(self, *args):
        logging.debug('browsExtra2')
        dir = os.path.join(self.projectPath, 'scenes')
        path = browsFile.search(defPath=dir)
        mc.textField('f6', e=True, text=path)

    def browsExtra3(self, *args):
        logging.debug('browsExtra3')
        dir = os.path.join(self.projectPath, 'scenes')
        path = browsFile.search(defPath=dir)
        mc.textField('f7', e=True, text=path)

    def browsExtra4(self, *args):
        logging.debug('browsExtra4')
        dir = os.path.join(self.projectPath, 'scenes')
        path = browsFile.search(defPath=dir)
        mc.textField('f8', e=True, text=path)

    def browsExtra5(self, *args):
        logging.debug('browsExtra5')
        dir = os.path.join(self.projectPath, 'scenes')
        path = browsFile.search(defPath=dir)
        mc.textField('f9', e=True, text=path)

    def browsExtra6(self, *args):
        logging.debug('browsExtra6')
        dir = os.path.join(self.projectPath, 'scenes')
        path = browsFile.search(defPath=dir)
        mc.textField('f10', e=True, text=path)

    def browsExtra7(self, *args):
        logging.debug('browsExtra7')
        dir = os.path.join(self.projectPath, 'scenes')
        path = browsFile.search(defPath=dir)
        mc.textField('f11', e=True, text=path)

    def browsExtra8(self, *args):
        logging.debug('browsExtra8')
        dir = os.path.join(self.projectPath, 'scenes')
        path = browsFile.search(defPath=dir)
        mc.textField('f12', e=True, text=path)

    def browsExtra9(self, *args):
        logging.debug('browsExtra9')
        dir = os.path.join(self.projectPath, 'scenes')
        path = browsFile.search(defPath=dir)
        mc.textField('f13', e=True, text=path)

    def browsRenderSettings(self, *args):
        logging.debug('browsRenderSettings')
        path = browsFile.search(defPath=self.renderSettingPath)
        mc.textField('f14', e=True, text=path)

    def browsAOVsSettings(self, *args):
        logging.debug('browsAOVsSettings')
        path = browsFile.search(defPath=self.AOVsSettingPath)
        mc.textField('f15', e=True, text=path)

    def browsDeadlineSettings(self, *args):
        logging.debug('browsDeadlineSettings')
        path = browsFile.search(defPath=self.deadlineSettingPath)
        mc.textField('f16', e=True, text=path)

    def config(self, *args):
        logging.debug('job config')
        a = configSetting.ReadJson()
        a.read()
        self.projectPath = a.config_dict['projectPath']
        self.stagePath = a.config_dict['stagePath']
        self.renderSettingPath = a.config_dict['renderSettingPath']
        self.AOVsSettingPath = a.config_dict['AOVsSettingPath']
        self.timerangePath = a.config_dict['timerangePath']

        logging.debug('projectPath --> %s' %(self.projectPath))
        logging.debug('stagePath --> %s' %(self.stagePath))
        logging.debug('renderSettingPath --> %s' %(self.renderSettingPath))
        logging.debug('AOVsSettingPath --> %s' %(self.AOVsSettingPath))
        logging.debug('timerangePath --> %s' %(self.timerangePath))

    def ui(self, *args):
        logging.debug('shou UI')
        self.config()
        if mc.window('win', ex=True) == True:
            mc.deleteUI('win', window=True)

        self.develop()

        win = mc.window('win', title='mcJobPitcher', widthHeight=(700, 515))
        form = mc.formLayout()

        # my logger
        ml = myLogger.MyLogger(mc)
        cLog = ml.createCheckbox(1)

        mc.radioCollection()
        c1 = mc.checkBox('c1', l='New Scene', v=1)
        c2 = mc.checkBox('c2', l='Open Stage', v=1)
        f2 = mc.textField('f2', w=500, h=20, text=self.stagePath)
        b2 = mc.button(l='Brows', w=50, h=20, c=self.browsStage)
        sp1 = mc.separator(w=680)
        c3 = mc.checkBox('c3', l='Camera', v=1)
        f3 = mc.textField('f3', w=500, h=20, text='')
        b3 = mc.button(l='Brows', w=50, h=20, c=self.browsCamera)
        c4 = mc.checkBox('c4', l='Animation', v=1)
        f4 = mc.textField('f4', w=500, h=20, text='')
        b4 = mc.button(l='Brows', w=50, h=20, c=self.browsAnimation)
        c5 = mc.checkBox('c5', l='Extra 1', v=0)
        f5 = mc.textField('f5', w=500, h=20, text='')
        b5 = mc.button(l='Brows', w=50, h=20, c=self.browsExtra1)
        c6 = mc.checkBox('c6', l='Extra 2', v=0)
        f6 = mc.textField('f6', w=500, h=20, text='')
        b6 = mc.button(l='Brows', w=50, h=20, c=self.browsExtra2)
        c7 = mc.checkBox('c7', l='Extra 3', v=0)
        f7 = mc.textField('f7', w=500, h=20, text='')
        b7 = mc.button(l='Brows', w=50, h=20, c=self.browsExtra3)
        c8 = mc.checkBox('c8', l='Extra 4', v=0)
        f8 = mc.textField('f8', w=500, h=20, text='')
        b8 = mc.button(l='Brows', w=50, h=20, c=self.browsExtra4)
        c9 = mc.checkBox('c9', l='Extra 5', v=0)
        f9 = mc.textField('f9', w=500, h=20, text='')
        b9 = mc.button(l='Brows', w=50, h=20, c=self.browsExtra5)
        c10 = mc.checkBox('c10', l='Extra 6', v=0)
        f10 = mc.textField('f10', w=500, h=20, text='')
        b10 = mc.button(l='Brows', w=50, h=20, c=self.browsExtra6)
        c11 = mc.checkBox('c11', l='Extra 7', v=0)
        f11 = mc.textField('f11', w=500, h=20, text='')
        b11 = mc.button(l='Brows', w=50, h=20, c=self.browsExtra7)
        c12= mc.checkBox('c12', l='Extra 8', v=0)
        f12 = mc.textField('f12', w=500, h=20, text='')
        b12 = mc.button(l='Brows', w=50, h=20, c=self.browsExtra8)
        c13 = mc.checkBox('c13', l='Extra 9', v=0)
        f13 = mc.textField('f13', w=500, h=20, text='')
        b13 = mc.button(l='Brows', w=50, h=20, c=self.browsExtra9)
        sp2 = mc.separator(w=680)
        c14 = mc.checkBox('c14', l='Render Settings', v=1)
        f14 = mc.textField('f14', w=500, h=20, text=self.renderSettingPath)
        b14 = mc.button(l='Brows', w=50, h=20, c=self.browsRenderSettings)
        c15 = mc.checkBox('c15', l='AOVs Settings', v=1)
        f15 = mc.textField('f15', w=500, h=20, text=self.AOVsSettingPath)
        b15 = mc.button(l='Brows', w=50, h=20, c=self.browsAOVsSettings)
        c16 = mc.checkBox('c16', l='Submit to Deadline10', v=1)
        t1 = mc.text(l='shotID :')
        f17 = mc.textField('f17', w=110, h=20, text='sXXcXX')
        t2 = mc.text(l='time range')
        f18 = mc.timeField('f18', w=50, h=20, v=1, s=1)
        f19 = mc.timeField('f19', w=50, h=20, v=100, s=1)
        b17 = mc.button(l='Set shotID', w=180, h=90, c=self.jobSetShotID)
        b18 = mc.button(l='Build Render Scene', w=300, h=90, c=self.jobBuildRenderScene)
        c17 = mc.checkBox('c17', l='save Scene', v=1)

        mc.formLayout(form, edit=True, attachForm=[
            (c1, 'top', 10), (c1, 'left', 10),
            (c2, 'top', 35), (c2, 'left', 10),
            (f2, 'top', 35), (f2, 'left', 130),
            (b2, 'top', 35), (b2, 'left', 640),
            (sp1, 'top', 60), (sp1, 'left', 10),
            (c3, 'top', 70), (c3, 'left', 10),
            (f3, 'top', 70), (f3, 'left', 130),
            (b3, 'top', 70), (b3, 'left', 640),
            (c4, 'top', 95), (c4, 'left', 10),
            (f4, 'top', 95), (f4, 'left', 130),
            (b4, 'top', 95), (b4, 'left', 640),
            (c5, 'top', 120), (c5, 'left', 10),
            (f5, 'top', 120), (f5, 'left', 130),
            (b5, 'top', 120), (b5, 'left', 640),
            (c6, 'top', 145), (c6, 'left', 10),
            (f6, 'top', 145), (f6, 'left', 130),
            (b6, 'top', 145), (b6, 'left', 640),
            (c7, 'top', 170), (c7, 'left', 10),
            (f7, 'top', 170), (f7, 'left', 130),
            (b7, 'top', 170), (b7, 'left', 640),
            (c8, 'top', 195), (c8, 'left', 10),
            (f8, 'top', 195), (f8, 'left', 130),
            (b8, 'top', 195), (b8, 'left', 640),
            (c9, 'top', 220), (c9, 'left', 10),
            (f9, 'top', 220), (f9, 'left', 130),
            (b9, 'top', 220), (b9, 'left', 640),
            (c10, 'top', 245), (c10, 'left', 10),
            (f10, 'top', 245), (f10, 'left', 130),
            (b10, 'top', 245), (b10, 'left', 640),
            (c11, 'top', 270), (c11, 'left', 10),
            (f11, 'top', 270), (f11, 'left', 130),
            (b11, 'top', 270), (b11, 'left', 640),
            (c12, 'top', 295), (c12, 'left', 10),
            (f12, 'top', 295), (f12, 'left', 130),
            (b12, 'top', 295), (b12, 'left', 640),
            (c13, 'top', 320), (c13, 'left', 10),
            (f13, 'top', 320), (f13, 'left', 130),
            (b13, 'top', 320), (b13, 'left', 640),
            (sp2, 'top', 350), (sp2, 'left', 10),
            (c14, 'top', 360), (c14, 'left', 10),
            (f14, 'top', 360), (f14, 'left', 130),
            (b14, 'top', 360), (b14, 'left', 640),
            (c15, 'top', 385), (c15, 'left', 10),
            (f15, 'top', 385), (f15, 'left', 130),
            (b15, 'top', 385), (b15, 'left', 640),
            (c16, 'top', 410), (c16, 'left', 10),
            (t1, 'top', 438), (t1, 'left', 10),
            (f17, 'top', 435), (f17, 'left', 80),
            (t2, 'top', 463), (t2, 'left', 10),
            (f18, 'top', 460), (f18, 'left', 80),
            (f19, 'top', 460), (f19, 'left', 140),
            (b17, 'top', 415), (b17, 'left', 200),
            (b18, 'top', 415), (b18, 'left', 390),
            (cLog, 'top', 485), (cLog, 'left', 10),
            (c17, 'top', 485), (c17, 'left', 80),
        ])

        mc.showWindow(win)
        mc.window('win', e=True, wh=(700,515))
