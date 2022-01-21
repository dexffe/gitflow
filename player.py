import pygame
from pygame import *
from main1 import *
from Menu import *
import Menu
import main1
import animation
import os

WIDTH = 22
HEIGHT = 32
file = os.path.dirname(__file__)

ANIMATION_RIGHT = [load_image('r1.png'),
                   '%s/персонаж/r2.png' % file,
                   '%s/персонаж/r3.png' % file,
                   '%s/персонаж/r4.png' % file,
                   '%s/персонаж/r5.png' % file]
ANIMATION_LEFT = ['%s/персонаж/l1.png' % file,
                  '%s/персонаж/l2.png' % file,
                  '%s/персонаж/l3.png' % file,
                  '%s/персонаж/l4.png' % file,
                  '%s/персонаж/l5.png' % file]
ANIMATION_JUMP_LEFT = ['%s/персонаж/jl.png' % file]
ANIMATION_JUMP_RIGHT = ['%s/персонаж/jr.png' % file]
ANIMATION_JUMP = ['%s/персонаж/j.png' % file]
ANIMATION_STAY = ['%s/персонаж/s.png' % file]


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

        self.Anim_Right = animation.Anim(ANIMATION_RIGHT)

        self.Anim_Left = animation.Anim(ANIMATION_LEFT)

        self.Anim_Stay = animation.Anim(ANIMATION_STAY)
        self.Anim_Stay.play()

        self.Anim_Jump_Left = animation.Anim(ANIMATION_JUMP_LEFT)

        self.Anim_Jump_Right = animation.Anim(ANIMATION_JUMP_RIGHT)

        self.Anim_Jump = animation.Anim(ANIMATION_JUMP)

    def update(self, left, right, up, platforms, moneys, stop_lvl):
        if up:
            if self.on_ground:
                self.y = -10
            self.image.fill('black')
            self.Anim_Jump.play()
        if left:
            self.x = -7
            self.image.fill('black')
            if up:
                self.Anim_Jump_Left.play()
            else:
                self.Anim_Left.play()
        if right:
            self.x = 7
            self.image.fill('black')
            if up:
                self.Anim_Jump_Right.play()
            else:
                self.Anim_Right.play()
        if not (left or right):
            self.x = 0
            if not up:
                self.image.fill('black')
                self.Anim_Stay.play()
        if not self.on_ground:
            self.y += 0.35

        self.on_ground = False
        self.rect.y += self.y
        self.collide(0, self.y, platforms)

        self.rect.x += self.x
        self.collide(self.x, 0, platforms)
        self.money(moneys)
        self.stop(stop_lvl)

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

    def money(self, moneys):
        for i in moneys:
            if sprite.collide_rect(self, i):
                Menu.count_money(1)
                moneys.remove(i)

    def stop(self, stop_lvl):
        for i in stop_lvl:
            if sprite.collide_rect(self, i):
                main1.exit_level_t()

