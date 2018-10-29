# coding:UTF-8
import maya.cmds as mc
import os
import logging
import myLogger
import RenderSetting
import AOVsReader
import browsFile
import createRenderNode
import configSetting
import importScenes


class UiClass(object):
    def __init__(self):
        self.develop()
        self.shotID = r''
        self.cam_path = r''
        self.anim_path = r''
        self.projectPath = r''
        self.stagePath = r''
        self.renderSettingPath = r''
        self.AOVsSettingPath = r''
        self.deadlineSettingPath = r''


    def develop(self, *args):
        reload(myLogger)
        reload(RenderSetting)
        reload(AOVsReader)
        reload(browsFile)
        reload(createRenderNode)
        reload(configSetting)
        reload(importScenes)

    def jobNewScenes(self, *args):
        logging.debug('jobNewScenes')
        mc.file(f=True, new=True)

    def jobOpenStage(self, *args):
        logging.debug('jobOpenStage')
        print self.stagePath
        mc.file(self.stagePath, open=True)

    def jobImportCamera(self, *args):
        logging.debug('jobImportCamera')
        importScenes.importScenes(self.cam_path)

    def jobImportAnimation(self, *args):
        logging.debug('jobImportAnimation')
        importScenes.importScenes(self.anim_path)

    def jobExtra1(self, *args):
        logging.debug('jobExtra1')

    def jobEctra2(self, *args):
        logging.debug('jobExtra2')

    def jobExtra3(self, *args):
        logging.debug('jobExtra3')

    def jobExtra4(self, *args):
        logging.debug('jobExtra4')

    def jobExtra5(self, *args):
        logging.debug('jobExtra5')

    def jobExtra6(self, *args):
        logging.debug('jobExtra6')

    def jobExtra7(self, *args):
        logging.debug('jobExtra7')

    def jobExtra8(self, *args):
        logging.debug('jobExtra8')

    def jobExtra9(self, *args):
        logging.debug('jobExtra9')

    def jobRenderSettings(self, *args):
        logging.debug('jobRenderSetting')
        RenderSetting.jsonRead()

    def jobAOVsSetting(self, *args):
        AOVsReader.AOVsRead()
        logging.debug('jobAOVsSetting')

    def jobSubmitDeadline(self, *args):
        logging.debug('jobSubmitDeadline')

    def jobSetShotID(self, *args):
        logging.debug('jobSetShotID')
        self.shotID = mc.textField('f17', q=True, text=True)
        logging.debug('shotID is %s' % self.shotID)

        self.cam_path = os.path.join(self.projectPath, 'scenes', 'cam', '%s.cam.v1.fbx' %(self.shotID))
        mc.textField('f3', e=True, tx=self.cam_path)
        logging.debug('camera path is %s' %(self.cam_path))

        self.anim_path = os.path.join(self.projectPath, 'scenes', '%s.render.v1.ma' %(self.shotID))
        mc.textField('f4', e=True, tx=self.anim_path)
        logging.debug('animation path is %s' %(self.anim_path))

        print self.anim_path

    def jobBuildRenderScene(self, *args):
        logging.debug('jobBuildRenderScene')

        self.jobSetShotID(self)

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

        if mc.checkBox('c16', q=True, v=True) == True:
            self.jobSubmitDeadline()

    def jobTest(self, *args):
        logging.debug('test')
        print browsFile.search()

    def browsStage(self, *args):
        logging.debug('browsStage')

    def browsCamera(self, *args):
        logging.debug('browsCamera')

    def browsAnimation(self, *args):
        logging.debug('browsAnimation')

    def browsExtra1(self, *args):
        logging.debug('browsExtra1')

    def browsExtra2(self, *args):
        logging.debug('browsExtra2')

    def browsExtra3(self, *args):
        logging.debug('browsExtra3')

    def browsExtra4(self, *args):
        logging.debug('browsExtra4')

    def browsExtra5(self, *args):
        logging.debug('browsExtra5')

    def browsExtra6(self, *args):
        logging.debug('browsExtra6')

    def browsExtra7(self, *args):
        logging.debug('browsExtra7')

    def browsExtra8(self, *args):
        logging.debug('browsExtra8')

    def browsExtra9(self, *args):
        logging.debug('browsExtra9')

    def browsRenderSettings(self, *args):
        logging.debug('browsRenderSettings')

    def browsAOVsSettings(self, *args):
        logging.debug('browsAOVsSettings')

    def browsDeadlineSettings(self, *args):
        logging.debug('browsDeadlineSettings')

    def config(self, *args):
        logging.debug('job config')
        a = configSetting.ReadJson()
        a.read()
        self.projectPath = a.config_dict['projectPath']
        self.stagePath = a.config_dict['stagePath']
        self.renderSettingPath = a.config_dict['renderSettingPath']
        self.AOVsSettingPath = a.config_dict['AOVsSettingPath']
        self.deadlineSettingPath = a.config_dict['deadlineSettingPath']

        logging.debug('projectPath --> %s' %(self.projectPath))
        logging.debug('stagePath --> %s' %(self.stagePath))
        logging.debug('renderSettingPath --> %s' %(self.renderSettingPath))
        logging.debug('AOVsSettingPath --> %s' %(self.AOVsSettingPath))
        logging.debug('deadlineSettingPath --> %s' %(self.deadlineSettingPath))

    def ui(self, *args):
        logging.debug('shou UI')
        self.config()
        if mc.window('win', ex=True) == True:
            mc.deleteUI('win', window=True)

        self.develop()

        win = mc.window('win', title='mcJobPitcher', widthHeight=(300, 700))
        form = mc.formLayout()

        # my logger
        ml = myLogger.MyLogger(mc)
        cLog = ml.createCheckbox(1)

        mc.radioCollection()
        c1 = mc.checkBox('c1', l='New Scene', v=0)
        c2 = mc.checkBox('c2', l='Open Stage', v=1)
        f2 = mc.textField('f2', w=500, h=20, text=self.stagePath)
        b2 = mc.button(l='Brows', w=50, h=20)
        sp1 = mc.separator(w=680)
        c3 = mc.checkBox('c3', l='Camera', v=1)
        f3 = mc.textField('f3', w=500, h=20, text='')
        b3 = mc.button(l='Brows', w=50, h=20)
        c4 = mc.checkBox('c4', l='Animation', v=1)
        f4 = mc.textField('f4', w=500, h=20, text='')
        b4 = mc.button(l='Brows', w=50, h=20)
        c5 = mc.checkBox('c5', l='Extra 1', v=0)
        f5 = mc.textField('f5', w=500, h=20, text='')
        b5 = mc.button(l='Brows', w=50, h=20)
        c6 = mc.checkBox('c6', l='Extra 2', v=0)
        f6 = mc.textField('f6', w=500, h=20, text='')
        b6 = mc.button(l='Brows', w=50, h=20)
        c7 = mc.checkBox('c7', l='Extra 3', v=0)
        f7 = mc.textField('f7', w=500, h=20, text='')
        b7 = mc.button(l='Brows', w=50, h=20)
        c8 = mc.checkBox('c8', l='Extra 4', v=0)
        f8 = mc.textField('f8', w=500, h=20, text='')
        b8 = mc.button(l='Brows', w=50, h=20)
        c9 = mc.checkBox('c9', l='Extra 5', v=0)
        f9 = mc.textField('f9', w=500, h=20, text='')
        b9 = mc.button(l='Brows', w=50, h=20)
        c10 = mc.checkBox('c10', l='Extra 6', v=0)
        f10 = mc.textField('f10', w=500, h=20, text='')
        b10 = mc.button(l='Brows', w=50, h=20)
        c11 = mc.checkBox('c11', l='Extra 7', v=0)
        f11 = mc.textField('f11', w=500, h=20, text='')
        b11 = mc.button(l='Brows', w=50, h=20)
        c12= mc.checkBox('c12', l='Extra 8', v=0)
        f12 = mc.textField('f12', w=500, h=20, text='')
        b12 = mc.button(l='Brows', w=50, h=20)
        c13 = mc.checkBox('c13', l='Extra 9', v=0)
        f13 = mc.textField('f13', w=500, h=20, text='')
        b13 = mc.button(l='Brows', w=50, h=20)
        sp2 = mc.separator(w=680)
        c14 = mc.checkBox('c14', l='Render Settings', v=1)
        f14 = mc.textField('f14', w=500, h=20, text='')
        b14 = mc.button(l='Brows', w=50, h=20)
        c15 = mc.checkBox('c15', l='AOVs Settings', v=1)
        f15 = mc.textField('f15', w=500, h=20, text='')
        b15 = mc.button(l='Brows', w=50, h=20)
        c16 = mc.checkBox('c16', l='Deadline Settings', v=0)
        f16 = mc.textField('f16', w=500, h=20, text='')
        b16 = mc.button(l='Brows', w=50, h=20)
        t1 = mc.text(l='shotID :')
        f17 = mc.textField('f17', w=100, h=20, text='sXXcXX')
        b17 = mc.button(l='Set shotID', w=220, h=40, c=self.jobSetShotID)
        b18 = mc.button(l='Build Render Scene', w=450, h=70, c=self.jobBuildRenderScene)
        b19 = mc.button(l='test', w=450, h=70, c=self.jobTest)

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
            (f16, 'top', 410), (f16, 'left', 130),
            (b16, 'top', 410), (b16, 'left', 640),
            (t1, 'top', 438), (t1, 'left', 80),
            (f17, 'top', 435), (f17, 'left', 130),
            (b17, 'top', 465), (b17, 'left', 10),
            (b18, 'top', 435), (b18, 'left', 240),
            (b19, 'top', 520), (b19, 'left', 10),
            (cLog, 'top', 520), (cLog, 'right', 10),
        ])

        mc.showWindow(win)
