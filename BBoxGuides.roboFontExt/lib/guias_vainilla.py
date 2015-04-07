# EMT BBox guides

# Emtype Foundry, Barcelona.

from vanilla import *
from robofab.world import CurrentFont, CurrentGlyph


class WindowDemo(object):

    def __init__(self):
        self.w = FloatingWindow((115,87), "EMT")
        self.w.myTextBox = TextBox((10, 7, -10, 17), "BBox guides")
        self.w.myButton = Button((10, 30, -10, 20), "+", callback=self.buttonCallback)
        self.w.myButton2 = Button((10, 57, -10, 20), "-", callback=self.button2Callback)
        self.w.open()


    def buttonCallback(self, sender):
        g= CurrentGlyph()
        g.clearGuides()
        g.addGuide((g.box[0], 0), 90,  "left")
        g.addGuide((g.box[2], 0), 90,  "right")
        g.addGuide((0, g.box[1]), 0,  "bottom")
        g.addGuide((0, g.box[3]), 0,  "top")
        g.addGuide(( (g.box[2] + g.leftMargin) /2 , 0), 90,  "center")
        g.addGuide(( 0 ,(g.box[3] + g.box[1] ) /2), 0,  "center")
        g.update()

        for c in g:
            if c.selected == 1:
                g.clearGuides()
                g.addGuide((c.box[0], 0), 90,  "left")
                g.addGuide((c.box[2], 0), 90,  "right")
                g.addGuide((0, c.box[1]), 0,  "bottom")
                g.addGuide((0, c.box[3]), 0,  "top")
                g.addGuide(( (c.box[2] + c.box[0]) /2 , 0), 90,  "center")
                g.addGuide(( 0 ,(c.box[3] + c.box[1] ) /2), 0,  "center")
                g.update()

        for cc in g.components:
            if cc.selected == 1:
                g.clearGuides()
                g.addGuide((cc.box[0], 0), 90,  "left")
                g.addGuide((cc.box[2], 0), 90,  "right")
                g.addGuide((0, cc.box[1]), 0,  "bottom")
                g.addGuide((0, cc.box[3]), 0,  "top")
                g.addGuide(( (cc.box[2] + cc.box[0]) /2 , 0), 90,  "center")
                g.addGuide(( 0 ,(cc.box[3] + cc.box[1] ) /2), 0,  "center")
                g.update()
                
    def button2Callback(self, sender):
        g= CurrentGlyph()
        g.clearGuides()
        g.update()

WindowDemo()


#g.clearGuides()

        #self.w.line = HorizontalLine((10, 10, -10, 1))


    #def __init__(self):
    #    self.w = Window((115,80), "EMT")
    #    #self.w.myTextBox = TextBox((10, 7, -10, 17), "Center guide")
    #    self.w.myButton = Button((10, 15, -10, 20), "+", callback=self.buttonCallback)
    #    self.w.myButton2 = Button((10, 45, -10, 20), "-", callback=self.button2Callback)
    #    self.w.open()