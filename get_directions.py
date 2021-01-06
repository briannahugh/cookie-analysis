# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 18:18:59 2020

@author: HUGHBR
"""
import re
from get_ingredients import clean_text

def get_temp(x):
    y = clean_text(x).lower().replace(")","").replace("(","")
    temp = ""
    temp_f_regex = re.compile(r'(?:(\d\d\d) *(f|°|º|degrees*)+ *[^c])')
    mo_f = temp_f_regex.search(y)
    if mo_f:
        temp = int(mo_f.group(1))
    else:
        temp_c_regex = re.compile(r'(?:(\d\d\d) *(c|°|º|degrees*)+(?: (c))*)')
        mo_c = temp_c_regex.search(y)
        if mo_c:
            temp = int(mo_c.group(1))*9/5+32
        else:
            preheat_regex = re.compile(r'(heat[^\.]*?(\d\d\d))')
            mo = preheat_regex.search(y)
            if mo:
                temp = int(mo.group(2))

    return temp

def get_oventime(x):
    y = clean_text(x).lower().replace(")","").replace("(","")
    time = ""
    time_regex = re.compile(r'bake(?: |,)[^\.]*?(\d+)(?:(?: to |-)(\d+))* *min')
    mo = time_regex.search(y)
    if mo:
        if mo.group(1) and mo.group(2):
            time = (int(mo.group(1))+int(mo.group(2)))/2
        else:
            time = int(mo.group(1))
    else:
        time = 0
        
    return time