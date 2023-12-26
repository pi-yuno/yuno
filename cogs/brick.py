#!/usr/bin/env python
import os
import time

class Display:
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.display = [["⬛"] * self.width for _ in range(self.height)]

    def draw(self, x, y):
        self.display[x][y] = "🏐"

    def clear(self):
        self.display = [["⬛"] * self.width for _ in range(self.height)]
    def render(self):
        result = ""
        for x in self.display:
            result += "".join(x) + "\n"
        return result

class Ball:
    def __init__(self, width, height):
        self.h = height
        self.w = width
        self.x, self.y = 0, 0
        self.x_v, self.y_v = 1, 1

    def play(self):
        self.x += self.x_v
        self.y += self.y_v

        if self.w <= self.y:
            self.y_v = -abs(self.y_v)
        if self.h <= self.x:
            self.x_v = -abs(self.x_v)
        if self.x <= 0:
            self.x_v = abs(self.x_v)
        if self.y <= 0:
            self.y_v = abs(self.y_v)

        return [self.x, self.y]
