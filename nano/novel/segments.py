# ~*~coding: utf-8~*~

import random
import sys
from nano import *

'''
Helper functions to generate segments of prose like descriptions of places or
characters.
'''

names = [
    "Steven",
    "Belinda",
    "Moses",
    "Sandeep",
    "Helen"
]

genders = [
    "man",
    "woman",
    "person"
]

ages = [
    "pre-teen",
    "teenage",
    "young",
    "middle-aged",
    "old"
]

hair_colours = [
    "blonde",
    "brown",
    "grey",
    "ginger"
]

eye_colours = [
    "blue",
    "green",
    "grey",
    "hazel",
    "brown"
]

def describe_character(person):
    if not person.name:
        person.name = random.choice(names)
    if not person.gender:
        person.gender = random.choice(genders)
    if not person.age:
        person.age = random.choice(ages)
    result = person.name + " was a " + person.age + " " + person.gender + "."
    return result



if __name__ == "__main__":
    person = nano.novel.Person()
    print describe_character(person)
