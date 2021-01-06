# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 16:46:06 2020

@author: HUGHBR
"""
import pprint

def ing_percent(x,ing):
    total = 0
    for recipe in x.values():
        if type(recipe) == dict:
            if recipe['type'] == ing:
                total += recipe['grams']
    grand_total = x['total']
    return total/grand_total  

def subing_percent(x,ing):
    total = 0
    for ing_name in x.keys():
        if ing_name == ing:
            total += x[ing_name]['grams']
    grand_total = x['total']
    return total/grand_total  

def filter_dict(x,ing):
    new = {}
    for recipe in x.values():
        if type(recipe) == dict:
            if recipe['type'] == ing:
                new.setdefault(recipe['subtype']+' '+recipe['type'],recipe)
    new = pprint.pformat(new)
    return new

def water_percent(x):
    total = 0
    for recipe in x.values():
        if type(recipe) == dict:
            if recipe['type'] == 'butter':
                total += recipe['grams']*0.17
            elif recipe['type'] == 'egg':
                total += recipe['grams']*0.74
            elif recipe['type'] == 'vanilla':
                total += recipe['grams']*0.52             
            elif recipe['type'] == 'milk':
                total += recipe['grams']*0.877  
            elif recipe['type'] == 'honey':
                total += recipe['grams']*0.17
            elif recipe['type'] == 'syrup':
                total += recipe['grams']*0.33
            elif recipe['type'] == 'honey':
                total += recipe['grams']*0.18
    grand_total = x['total']
    return total/grand_total
                
def fat_percent(x):
    total = 0
    for recipe in x.values():
        if type(recipe) == dict:
            if recipe['type'] == 'butter':
                total += recipe['grams']*0.81
            elif recipe['type'] == 'egg':
                total += recipe['grams']*0.11
            elif recipe['type'] == 'milk':
                total += recipe['grams']*0.034                 
            elif recipe['type'] == 'oil':
                total += recipe['grams']*1      
            elif recipe['type'] == 'shortening':
                total += recipe['grams']*1        
    grand_total = x['total']
    return total/grand_total  


def sugar_percent(x):
    total = 0
    for recipe in x.values():
        if type(recipe) == dict:
            if recipe['type'] == 'sugar':
                total += recipe['grams']*1
            elif recipe['type'] == 'syrup':
                total += recipe['grams']*0.67
            elif recipe['type'] == 'honey':
                total += recipe['grams']*0.82
       
    grand_total = x['total']
    return total/grand_total  

def protein_percent(x):
    total = 0
    for recipe in x.values():
        if type(recipe) == dict:
            if recipe['type'] == 'egg':
                total += recipe['grams']*0.128
            elif recipe['type'] == 'oat':
                total += recipe['grams']*0.169
            elif recipe['type'] == 'flour':
                if recipe['subtype'] == 'cake' or recipe['subtype'] == 'pastry':
                    total += recipe['grams']*0.08
                elif recipe['subtype'] == 'all purpose' or recipe['subtype'] == 'regular':
                    total += recipe['grams']*0.10
                elif recipe['subtype'] == 'almond':
                    total += recipe['grams']*0.07
                elif recipe['subtype'] == 'whole wheat':
                    total += recipe['grams']*0.13
                elif recipe['subtype'] == 'oat':
                    total += recipe['grams']*0.147
                elif recipe['subtype'] == 'coconut':
                    total += recipe['grams']*0.18
                elif recipe['subtype'] == 'bread':
                    total += recipe['grams']*0.127
                elif recipe['subtype'] == 'gluten free':
                    total += recipe['grams']*0.08
                                                         
    grand_total = x['total']
    return total/grand_total    

def gluten_percent(x):
    total = 0
    for recipe in x.values():
        if type(recipe) == dict:
            if recipe['type'] == 'oat':
                if recipe['subtype'] == 'gluten free':
                    total += recipe['grams']*0
                else:
                    total += recipe['grams']*0.169
            elif recipe['type'] == 'flour':
                if recipe['subtype'] == 'cake' or recipe['subtype'] == 'pastry':
                    total += recipe['grams']*0.08
                elif recipe['subtype'] == 'all purpose' or recipe['subtype'] == 'regular':
                    total += recipe['grams']*0.10
                elif recipe['subtype'] == 'almond':
                    total += recipe['grams']*0.07
                elif recipe['subtype'] == 'whole wheat':
                    total += recipe['grams']*0.13
                elif recipe['subtype'] == 'oat':
                    total += recipe['grams']*0.147
                elif recipe['subtype'] == 'coconut':
                    total += recipe['grams']*0.18
                elif recipe['subtype'] == 'bread':
                    total += recipe['grams']*0.127
                elif recipe['subtype'] == 'gluten free':
                    total += recipe['grams']*0
                                                         
    grand_total = x['total']
    return total/grand_total 

def starch_percent(x):
    total = 0
    for recipe in x.values():
        if type(recipe) == dict:
            if recipe['type'] == 'flour':
                total += recipe['grams']*0.73
            elif recipe['type'] == 'oat':
                total += recipe['grams']*0.6
                                                         
    grand_total = x['total']
    return total/grand_total                


def aeration(x):
    max_bs = 0
    bs = 0
    bp = 0
    total = 0
    for recipe in x.values():
        if type(recipe) == dict:
            if recipe['type'] == 'sugar' and recipe['subtype'] == 'brown':
                max_bs += recipe['grams']*(4.8/200)
            elif recipe['type'] == 'baking soda':
                bs += recipe['grams']*1
            elif recipe['type'] == 'baking powder':
                bp += recipe['grams']*(1/4)
    
    total = min(max_bs,bs) + bp 
    return total
                
def score(x):
    max_bs = 0
    bs = 0
    bp = 0
    total = 0
    for recipe in x.values():
        if type(recipe) == dict:
            if recipe['type'] == 'sugar' and recipe['subtype'] == 'brown':
                max_bs += recipe['grams']*(4.8/200)
            elif recipe['type'] == 'baking soda':
                bs += recipe['grams']*1
            elif recipe['type'] == 'baking powder':
                bp += recipe['grams']*(1/4)
    
    total = min(max_bs,bs) + bp 
    return total
                           