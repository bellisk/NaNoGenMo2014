# coding: utf-8

import json
import random

import nano

class Person():
    def __init__(self, name=None, gender=None, age=None):
        self.name = name
        self.gender = gender
        self.age = age
        self.objects = []
        self.clothing = []
    def take_object(self, obj):
        self.objects.append(obj)
    def lose_object(self, obj):
        self.objects.remove(obj)
    def take_clothing(self, clothing):
        self.clothing.append(clothing)
    def lose_clothing(self, clothing):
        self.clothing.remove(clothing)


class Location():
    def __init__(self, name=None, loc_type=None):
        self.name = name
        self.loc_type = loc_type


class Object():
    def _init_(self, obj_type):
        self.type = obj_type
