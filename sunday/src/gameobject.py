import pygame
import sys

pygame.mixer.init()
pygame.init()

class GameObject:
    def __init__(self, screen, location: tuple):
        self.screen = screen
        self.mouse = pygame.mouse
        self.location = location

    def render(self):
        pass

    def pos(self):
        return self.location

    def size(self):
        return (0, 0)

class Button(GameObject):
    def __init__(
        self,
        screen,
        location: tuple,
        background_color: tuple,
        dimensions: tuple,
        text: str,
        text_font: pygame.font.SysFont,
        text_color: tuple,
        on_click
    ):
        super().__init__(screen, location)
        self.bg_color = background_color
        self.dim = dimensions
        self.text = text
        self.text_font = text_font
        self.text_color = text_color
        self.on_click = on_click

    def render(self):
        pygame.draw.rect(
            self.screen,
            self.bg_color,
            [
                self.pos()[0] - self.size()[0] / 2,
                self.pos()[1] - self.size()[1] / 2,
                self.size()[0],
                self.size()[1]
            ]
        )
        text_object = self.text_font.render(self.text, True, self.text_color)
        self.screen.blit(text_object, self.text_pos())

    def pos(self):
        return super().pos()

    def text_pos(self):
        return (self.pos()[0] - self.text_size()[0] / 2, self.pos()[1] - self.text_size()[1] / 2)

    def size(self):
        return self.dim

    def text_size(self):
        return self.text_font.size(self.text)

    def click(self):
        if(self.pos()[0] - self.size()[0] / 2) <= self.mouse.get_pos()[0] <= (self.pos()[0] + self.size()[0] / 2) and \
            (self.pos()[1] - self.size()[1] / 2) <= self.mouse.get_pos()[1] <= (self.pos()[1] + self.size()[1] / 2):
                self.on_click()

class TextBox(GameObject):
    def __init__(
        self,
        screen,
        location: tuple,
        text: str,
        text_font: pygame.font.SysFont,
        text_color: tuple,
        has_border: bool=True,
        border_color: tuple=(0, 0, 0),
        border_thickness: float=5
    ):
        super().__init__(screen, location)
        self.text = text
        self.text_font = text_font
        self.text_color = text_color
        self.text_obj = self.text_font.render(self.text, True, self.text_color)
        self.has_border = has_border
        self.border_color = border_color
        if self.has_border:
            self.border_thickness = border_thickness
        else:
            self.border_thickness = 0

    def render(self):
        self.screen.blit(self.text_obj, self.pos())
        if self.has_border:
            pygame.draw.rect(
                self.screen,
                self.border_color,
                [
                    self.screen.get_width() - self.pos()[0] + self.border_thickness,
                    self.pos()[1] - self.text_size()[1] / 2 + self.border_thickness * 2,
                    self.border_thickness,
                    self.size()[1] + self.border_thickness * 2
                ]
            )
            pygame.draw.rect(
                self.screen,
                self.border_color,
                [
                    self.pos()[0] - self.border_thickness * 2,
                    self.pos()[1] - self.text_size()[1] / 2 + self.border_thickness * 2,
                    self.border_thickness,
                    self.size()[1] + self.border_thickness * 2
                ]
            )
            pygame.draw.rect(
                self.screen,
                self.border_color,
                [
                    self.pos()[0] - self.border_thickness * 2,
                    self.pos()[1] - self.border_thickness * 2,
                    self.size()[0] + self.border_thickness * 2,
                    self.border_thickness
                ]
            )
            pygame.draw.rect(
                self.screen,
                self.border_color,
                [
                    self.pos()[0] - self.border_thickness * 2,
                    self.pos()[1] + self.text_size()[1] + self.border_thickness * 2,
                    self.size()[0] + self.border_thickness * 2,
                    self.border_thickness
                ]
            )

    def pos(self):
        return (self.location[0] - self.text_size()[0] / 2, self.location[1] - self.text_size()[1] / 2)

    def size(self):
        return (self.text_size()[0] + self.border_thickness * 2, self.text_size()[1] + self.border_thickness * 2)

    def text_size(self):
        return self.text_font.size(self.text)

    def set_text(self, text):
        self.text = text
        self.text_obj = self.text_font.render(self.text, True, self.text_color)