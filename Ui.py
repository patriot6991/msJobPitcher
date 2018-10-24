# coding:UTF-8
import maya.cmds as mc

def ui():
    if mc.window('win', ex=True) == True:
        mc.deleteUI('win', window=True)

    win = mc.window('win', title='mcJobPitcher', widthHeight=(300, 700))
    form = mc.formLayout()

    mc.radioCollection()
    c1 = mc.checkBox(l='New Scene', v=0)
    c2 = mc.checkBox(l='Stage', v=1)
    f2 = mc.textField('f2', w=500, h=20, text='\\172.29.44.4\cg\ms06\renderProj\scenes\stage\Shibuya.evening.v1.mb')
    b2 = mc.button(l='Brows', w=50, h=20)
    sp1 = mc.separator(w=680)
    c3 = mc.checkBox(l='Camera', v=1)
    f3 = mc.textField('f3', w=500, h=20, text='')
    b3 = mc.button(l='Brows', w=50, h=20)
    c4 = mc.checkBox(l='Animation', v=1)
    f4 = mc.textField('f4', w=500, h=20, text='')
    b4 = mc.button(l='Brows', w=50, h=20)
    c5 = mc.checkBox(l='Extra 1', v=0)
    f5 = mc.textField('f5', w=500, h=20, text='')
    b5 = mc.button(l='Brows', w=50, h=20)
    c6 = mc.checkBox(l='Extra 2', v=0)
    f6 = mc.textField('f6', w=500, h=20, text='')
    b6 = mc.button(l='Brows', w=50, h=20)
    c7 = mc.checkBox(l='Extra 3', v=0)
    f7 = mc.textField('f7', w=500, h=20, text='')
    b7 = mc.button(l='Brows', w=50, h=20)
    c8 = mc.checkBox(l='Extra 4', v=0)
    f8 = mc.textField('f8', w=500, h=20, text='')
    b8 = mc.button(l='Brows', w=50, h=20)
    c9 = mc.checkBox(l='Extra 5', v=0)
    f9 = mc.textField('f9', w=500, h=20, text='')
    b9 = mc.button(l='Brows', w=50, h=20)
    c10 = mc.checkBox(l='Extra 6', v=0)
    f10 = mc.textField('f10', w=500, h=20, text='')
    b10 = mc.button(l='Brows', w=50, h=20)
    c11 = mc.checkBox(l='Extra 7', v=0)
    f11 = mc.textField('f11', w=500, h=20, text='')
    b11 = mc.button(l='Brows', w=50, h=20)
    c12 = mc.checkBox(l='Extra 8', v=0)
    f12 = mc.textField('f12', w=500, h=20, text='')
    b12 = mc.button(l='Brows', w=50, h=20)
    c13 = mc.checkBox(l='Extra 9', v=0)
    f13 = mc.textField('f13', w=500, h=20, text='')
    b13 = mc.button(l='Brows', w=50, h=20)
    sp2 = mc.separator(w=680)
    c14 = mc.checkBox(l='Render Settings', v=1)
    f14 = mc.textField('f14', w=500, h=20, text='')
    b14 = mc.button(l='Brows', w=50, h=20)
    c15 = mc.checkBox(l='AOVs Settings', v=1)
    f15 = mc.textField('f15', w=500, h=20, text='')
    b15 = mc.button(l='Brows', w=50, h=20)
    c16 = mc.checkBox(l='Deadline Settings', v=0)
    f16 = mc.textField('f16', w=500, h=20, text='')
    b16 = mc.button(l='Brows', w=50, h=20)
    t1 = mc.text(l='shotID :')
    f17 = mc.textField('f17', w=100, h=20, text='sXXcXX')
    b17 = mc.button(l='Set shotID', w=220, h=40)
    b18 = mc.button(l='Build Render Scene', w=450, h=70)

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
        (b18, 'top', 435), (b18, 'left', 240)
    ])

    mc.showWindow(win)

