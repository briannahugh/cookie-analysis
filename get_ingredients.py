# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:40:56 2020

@author: HUGHBR
"""
import re
from info_ingredients import all_ing
import unicodedata

def fraction_finder(s):
    n = s
    for c in s:
        try:
            name = unicodedata.name(c)
        except ValueError:
            continue
        if name.startswith('VULGAR FRACTION'):
            normalized = unicodedata.normalize('NFKC', c)
            numerator, _slash, denominator = normalized.partition('⁄')
            n = n.replace(c,str(int(numerator))+"/"+str(int(denominator)))   
    return n
            
def convert_to_decimal(raw_string):
    total = 0
    qty_string = raw_string.replace('and',' ')
        
    nums = qty_string.split()
    for num in nums:
        frac_regex = re.compile(r'(\d)*(\d)\/(\d)')
        mo = frac_regex.search(num)
        if mo:
            if mo.group(1):
                num_converted = float(mo.group(1)) + float(mo.group(2))/float(mo.group(3))
            else:
                num_converted = float(mo.group(2))/float(mo.group(3))
        else:
            num_converted = float(num)
        total = total + num_converted
    return total


def convert_to_grams(ing,qty,units,ing_type):
    if units == "g" or units == "gr" or units == "gms" or units == "gram" or units == "grams":
        grams = qty
    elif units == "o" or units == "oz" or units == "ounce" or units == "ounces":
        grams = qty*28.3495
    else:
        if units == "c" or units == "cup" or units == "cups":
            cups = qty
        elif units == "tbsp" or units == "tablespoon" or units == "tablespoons" or units == "tbls":
            cups = qty*0.0625
        elif units == "tsp" or units == "teaspoon" or units == "teaspoons":
            cups = qty*0.020833
        elif units == "stick" or units == "sticks": #butter specific
            cups = qty*0.5
        elif units == "" and ing == "egg": #egg specific
            units = "medium"
        elif units == "large": #egg specific
            cups = qty*3*0.0625
        elif units == "medium": #egg specific
            cups = qty*(6/7)*3*0.0625
        elif units == "small": #egg specific
            cups = qty*(6/8)*3*0.0625
        else:
            cups = 0
        grams = cups*all_ing[ing]['cup_to_g'][ing_type]
    return grams

def clean_text(x):
    y = fraction_finder(x).lower()
    y = y.encode("ascii","ignore").decode()
    return y
   
def get_ing(x):
    y = clean_text(x)
    ing_details = {}
    total = 0
    for ing in all_ing.keys():
        ing_regex = re.compile(r'(((?:\d+(?:\s|\/|and)*)+)(\w*)(?:\)|\.)?.*?'+all_ing[ing]['rx']+')')
        mo = ing_regex.findall(y)
        if mo:
            for match in mo:
                qty = convert_to_decimal(match[1])
                units = match[2]
                if ing == "egg" and (units == "" or units == "whole"):
                    units = "medium"
                if match[3]:
                    ing_type = match[3].replace('-',' ').rstrip('s')
                else:
                    ing_type = 'regular'
                gluten_regex = re.compile('gluten free')
                mo_gl = gluten_regex.search(match[0])
                if mo_gl: 
                    ing_type = 'gluten free'
                grams = round(convert_to_grams(ing,qty,units,ing_type),2)
                total += grams
                ing_details.setdefault(ing_type+' '+ing,{'qty':qty,'units':units,'type':ing,'grams':grams,'subtype':ing_type})

        
    ing_details.setdefault('total',total)
    return ing_details

