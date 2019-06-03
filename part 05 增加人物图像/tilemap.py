import pygame as pg
from settings import *
from os import path


class Map:
    def __init__(self,filename):
        self.data = []
        with open(filename,'rt') as f:
                for line in f:
                    self.data.append(line.strip())

        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth  * TILESIZE
        self.height = self.tileheight * TILESIZE
        


class Camera:
    def __init__(self, width, height):
        self.camera = pg.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    def apply(self, entity):
        '''
        moves the rectangle
        move(x, y) -> Rect
        Returns a new rectangle that is moved by the given offset. 
        The x and y arguments can be any integer value, positive or negative.
        '''
        return entity.rect.move(self.camera.topleft)  

    def update(self, target):
        x =  -target.rect.x + int(WIDTH / 2)
        y =  -target.rect.y + int(HEIGHT / 2) 
        
        x = min(0,x) # 左边界
        y = min(0,y) # 上
        x = max(-(self.width - WIDTH), x)  # 右
        y = max(-(self.height - HEIGHT), y)  # 下
        self.camera = pg.Rect(x, y, self.width, self.height)