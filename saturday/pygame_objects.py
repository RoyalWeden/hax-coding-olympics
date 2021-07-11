import pygame
import sys

pygame.mixer.init()
pygame.init()

class PGObject:
    def __init__(self):
        pass

    def render(self):
        pass

    def pos(self):
        return (0, 0)

    def size(self):
        return (0, 0)


class PGMouse(PGObject):
    def __init__(self):
        self.mouse = pygame.mouse

    def render(self):
        return super().render()

    def pos(self):
        return self.mouse.get_pos()

    def size(self):
        return super().size()


class PGButton(PGObject):
    def __init__(self, screen, mouse:PGMouse, color:tuple, loc:tuple, size:tuple, click_event):
        self.screen = screen
        self.mouse = mouse
        self.color = color
        self.loc = loc
        self._size = size
        self.click_event = click_event

    def render(self):
        pygame.draw.rect(self.screen, self.color, [self.pos()[0]-self.size()[0]/2, self.pos()[1]-self.size()[1]/2, self.size()[0], self.size()[1]])

    def on_click(self):
        if (self.pos()[0]-self.size()[0]/2)<=self.mouse.pos()[0]<=(self.pos()[0]+self.size()[0]/2) and \
            (self.pos()[1]-self.size()[1]/2)<=self.mouse.pos()[1]<=(self.pos()[1]+self.size()[1]/2):
                self.click_event()

    def move(self, vec:tuple, spd:float):
        self.loc = (self.pos()[0] + vec[0] * spd, self.pos()[1] + vec[1] * spd)

    def pos(self):
        return self.loc

    def size(self):
        return self._size

    def in_bounds(self):
        return 0<=self.pos()[0]<=self.screen.get_width() and 0<=self.pos()[1]<=self.screen.get_height()

    def in_bounds_dir(self, dir):
        if self.pos()[0]-self.size()[0]/2<0:
            dir = (1, dir[1])
        if self.pos()[0]+self.size()[0]/2>self.screen.get_width():
            dir = (-1, dir[1])
        if self.pos()[1]-self.size()[1]/2<0:
            dir = (dir[0], 1)
        if self.pos()[1]+self.size()[1]/2>self.screen.get_height():
            dir = (dir[0], -1)
        return dir

class PGText(PGObject):
    def __init__(self, screen, font:pygame.font.SysFont, text:str, color:tuple, loc:tuple=None, loc_obj:PGObject=None):
        self.screen = screen
        self.font = font
        self.text = text
        self.color = color
        self.loc = loc
        self.loc_obj = loc_obj
        self.text_obj = self.font.render(self.text, True, self.color)

    def render(self):
        self.screen.blit(self.text_obj, self.pos())

    def move(self, vec:tuple):
        self.loc = (self.pos()[0] + vec[0], self.pos()[1] + vec[1])

    def pos(self):
        location = (self.screen.get_width()/2, self.screen.get_height()/2)
        if self.loc != None:
            location = self.loc
        elif self.loc_obj != None:
            location = self.loc_obj.pos()
        return (location[0]-self.size()[0]/2, location[1]-self.size()[1]/2)

    def size(self):
        return self.font.size(self.text)

    def in_bounds(self):
        return 0<=self.pos()[0]<=self.screen.get_width() and 0<=self.pos()[1]<=self.screen.get_height()

    def in_bounds_dir(self, dir):
        if self.pos()[0]-self.size()[0]<0:
            dir = (1, dir[1])
        if self.pos()[0]+self.size()[0]>self.screen.get_width():
            dir = (-1, dir[1])
        if self.pos()[1]-self.size()[1]<0:
            dir = (dir[0], 1)
        if self.pos()[1]+self.size()[1]>self.screen.get_height():
            dir = (dir[0], -1)
        return dir