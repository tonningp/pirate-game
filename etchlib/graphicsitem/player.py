#!/usr/bin/env python3
from etchlib.graphicsitem import svg

class Item(svg.Item):
    def __init__(self,file,scale=1.0,parent=None):
        super(Item, self).__init__(file,scale,parent)
