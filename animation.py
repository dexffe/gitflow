import pygame
from Menu import *


class Anim(pygame.sprite.Sprite):
    def __init__(self, frames):
        super().__init__()
        self.frames = frames
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

    def play(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]