# EMT BBox guides Robofont 3

# Emtype Foundry, Barcelona.
from mojo.roboFont import OpenWindow
from vanilla import *

WIN_KEY = 'test'

class WindowDemo(object):
    __name__ = WIN_KEY

    def __init__(self):
        self.w = FloatingWindow((115,87), "EMT")
        self.w.myTextBox = TextBox((10, 7, -10, 17), "BBox guides")
        self.w.myButton = Button((10, 30, -10, 20), "+", callback=self.buttonCallback)
        self.w.myButton2 = Button((10, 57, -10, 20), "-", callback=self.button2Callback)
        self.w.open()


    def buttonCallback(self, sender):
        g= CurrentGlyph()
        g.clearGuidelines()
        g.appendGuideline((g.box[0], 0), 90,  "left", color=(0.5, 0.0, 1, 1.0))
        g.appendGuideline((g.box[2], 0), 90,  "right", color=(0.5, 0.0, 1, 1.0))
        g.appendGuideline((0, g.box[1]), 0,  "bottom", color=(0.5, 0.0, 1, 1.0))
        g.appendGuideline((0, g.box[3]), 0,  "top", color=(0.5, 0.0, 1, 1.0))
        g.appendGuideline(( (g.box[2] + g.leftMargin) /2 , 0), 90,  "center", color=(0.5, 0.0, 1, 1.0))
        g.appendGuideline(( 0 ,(g.box[3] + g.box[1] ) /2), 0,  "center", color=(0.5, 0.0, 1, 1.0))
        g.update()

        for c in g:
            if c.selected == 1:
                g.clearGuidelines()
                g.appendGuideline((c.box[0], 0), 90,  "left", color=(0.5, 0.0, 1, 1.0))
                g.appendGuideline((c.box[2], 0), 90,  "right", color=(0.5, 0.0, 1, 1.0))
                g.appendGuideline((0, c.box[1]), 0,  "bottom", color=(0.5, 0.0, 1, 1.0))
                g.appendGuideline((0, c.box[3]), 0,  "top", color=(0.5, 0.0, 1, 1.0))
                g.appendGuideline(( (c.box[2] + c.box[0]) /2 , 0), 90,  "center", color=(0.5, 0.0, 1, 1.0))
                g.appendGuideline(( 0 ,(c.box[3] + c.box[1] ) /2), 0,  "center", color=(0.5, 0.0, 1, 1.0))
                g.update()

        for cc in g.components:
            if cc.selected == 1:
                g.clearGuidelines()
                g.appendGuideline((cc.box[0], 0), 90,  "left", color=(0.5, 0.0, 1, 1.0))
                g.appendGuideline((cc.box[2], 0), 90,  "right", color=(0.5, 0.0, 1, 1.0))
                g.appendGuideline((0, cc.box[1]), 0,  "bottom", color=(0.5, 0.0, 1, 1.0))
                g.appendGuideline((0, cc.box[3]), 0,  "top", color=(0.5, 0.0, 1, 1.0))
                g.appendGuideline(( (cc.box[2] + cc.box[0]) /2 , 0), 90,  "center", color=(0.5, 0.0, 1, 1.0))
                g.appendGuideline(( 0 ,(cc.box[3] + cc.box[1] ) /2), 0,  "center", color=(0.5, 0.0, 1, 1.0))
                g.update()
                
    def button2Callback(self, sender):
        g= CurrentGlyph()
        g.clearGuidelines()
        g.update()

WindowDemo()
