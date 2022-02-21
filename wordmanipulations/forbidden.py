import os

from R import unspeakable
from wordmanipulations.hidevowels import hidevowels

def forbidden(letters):
    # novowels = hidevowels(letters)

    for group in unspeakable:
        if group in letters:
            return ""
    return letters