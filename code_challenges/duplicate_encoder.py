#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:29:09 2020

@author: em583r
"""

def duplicate_encode(word):
    word_list = list(word.lower())
    new_word = []
    
    for char in word_list:
        if word_list.count(char) <= 1:
            new_word.append("(")
        else:
            new_word.append(")")
                
    return "".join(new_word)