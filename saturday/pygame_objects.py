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
        self.size = size
        self.click_event = click_event

    def render(self):
        pygame.draw.rect(self.screen, self.color, [self.loc[0]-self.size[0]/2, self.loc[1]-self.size[1]/2, self.size[0], self.size[1]])

    def on_click(self):
        if (self.loc[0]-self.size[0]/2)<=self.mouse.pos()[0]<=(self.loc[0]+self.size[0]/2) or \
            (self.loc[1]-self.size[1]/2)<=self.mouse.pos()[1]<=(self.loc[1]+self.size[1]/2):
                self.click_event()

    def pos(self):
        return self.loc

    def size(self):
        return self.size


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

    def pos(self):
        location = (self.screen.get_width()/2, self.screen.get_height()/2)
        if self.loc != None:
            location = self.loc
        elif self.loc_obj != None:
            location = self.loc_obj.pos()
        return (location[0]-self.size()[0]/2, location[1]-self.size()[1]/2)

    def size(self):
        return self.font.size(self.text)