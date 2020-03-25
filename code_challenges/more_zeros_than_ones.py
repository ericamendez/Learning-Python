#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:56:45 2020

Create a moreZeros function which will receive a string for input, and return an array containing only the characters from that string whose binary representation of its ASCII value consists of more zeros than ones.

You should remove any duplicate characters, keeping the first occurence of any such duplicates, so they are in the same order in the final array as they first appeared in the input string.

Examples

'abcde' === ["1100001", "1100010", "1100011", "1100100", "1100101"]
               True       True       False      True       False

        --> ['a','b','d']

'DIGEST'--> ['D','I','E','T']
All input will be valid strings of length > 0. Leading zeros in binary should not be counted.

@author: em583r
"""

#condition_if_true if condition else condition_if_false

def more_zeros(s):
    unique_list = []
    
    for char in s:
        binary = format(ord(char), 'b')
        if char not in unique_list and list(binary).count("0") > 3:
            unique_list.append(char)
        else:
            None
    return unique_list





str = 'eabcdea'
print(more_zeros(str))