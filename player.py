from pygame import *
import pyganim
import os

WIDTH = 22
HEIGHT = 32
file = os.path.dirname(__file__)

ANIMATION_RIGHT = [('%s/персонаж/r1.png' % file),
                   ('%s/персонаж/r2.png' % file),
                   ('%s/персонаж/r3.png' % file),
                   ('%s/персонаж/r4.png' % file),
                   ('%s/персонаж/r5.png' % file)]
ANIMATION_LEFT = [('%s/персонаж/l1.png' % file),
                  ('%s/персонаж/l2.png' % file),
                  ('%s/персонаж/l3.png' % file),
                  ('%s/персонаж/l4.png' % file),
                  ('%s/персонаж/l5.png' % file)]
ANIMATION_JUMP_LEFT = [('%s/персонаж/jl.png' % file, 0.1)]
ANIMATION_JUMP_RIGHT = [('%s/персонаж/jr.png' % file, 0.1)]
ANIMATION_JUMP = [('%s/персонаж/j.png' % file, 0.1)]
ANIMATION_STAY = [('%s/персонаж/s.png' % file, 0.1)]


class Player(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = 0
        self.start_pos_x = x
        self.start_pos_y = y
        self.y = 0
        self.on_ground = False
        self.image = Surface((WIDTH, HEIGHT))
        self.rect = Rect(x, y, WIDTH, HEIGHT)

        s1 = []
        for i in ANIMATION_RIGHT:
            s1.append((i, 0.1))
        self.Anim_Right = pyganim.PygAnimation(s1)
        self.Anim_Right.play()

        s1 = []
        for i in ANIMATION_LEFT:
            s1.append((i, 0.1))
        self.Anim_Left = pyganim.PygAnimation(s1)
        self.Anim_Left.play()

        self.Anim_Stay = pyganim.PygAnimation(ANIMATION_STAY)
        self.Anim_Stay.play()
        self.Anim_Stay.blit(self.image, (0, 0))

        self.Anim_Jump_Left = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.Anim_Jump_Left.play()

        self.Anim_Jump_Right = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.Anim_Jump_Right.play()

        self.Anim_Jump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.Anim_Jump.play()

    def update(self, left, right, up, platforms):
        if up:
            if self.on_ground:
                self.y = -10
            self.image.fill('black')
            self.Anim_Jump.blit(self.image, (0, 0))
        if left:
            self.x = -7
            self.image.fill('black')
            if up:
                self.Anim_Jump_Left.blit(self.image, (0, 0))
            else:
                self.Anim_Left.blit(self.image, (0, 0))
        if right:
            self.x = 7
            self.image.fill('black')
            if up:
                self.Anim_Jump_Right.blit(self.image, (0, 0))
            else:
                self.Anim_Right.blit(self.image, (0, 0))
        if not (left or right):
            self.x = 0
            if not up:
                self.image.fill('black')
                self.Anim_Stay.blit(self.image, (0, 0))
        if not self.on_ground:
            self.y += 0.35

        self.on_ground = False
        self.rect.y += self.y
        self.collide(0, self.y, platforms)

        self.rect.x += self.x
        self.collide(self.x, 0, platforms)

    def collide(self, x, y, platforms):
        for i in platforms:
            if sprite.collide_rect(self, i):
                if x > 0:
                    self.rect.right = i.rect.left
                if x < 0:
                    self.rect.left = i.rect.right
                if y > 0:
                    self.rect.bottom = i.rect.top
                    self.on_ground = True
                    self.y = 0
                if y < 0:
                    self.rect.top = i.rect.bottom
                    self.y = 0
