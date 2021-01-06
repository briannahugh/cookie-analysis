# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:20:00 2020

@author: HUGHBR
"""

import pandas as pd
import os
import pprint
from get_ingredients import get_ing
from get_directions import get_temp, get_oventime
from get_composition import ing_percent,water_percent,fat_percent,protein_percent,aeration
from plot_recipes import plt_3d, plt_2d
from cookie_classify import logistic_regression, linear_SVC
#from ingredients_info import all_ing


os.chdir(r'C:\Users\HUGHBR\Documents\Brianna\Clustering\Project\cookies 3')
df = pd.read_csv('cookies_scraped_test.csv', encoding='latin1')

#Get ingredients
df['ing_dict'] = df['ingredients'].apply(lambda x: get_ing(x))
df['ing_list'] = df['ing_dict'].apply(lambda x: pprint.pformat(x))

#Get directions
df['temp'] = df['directions'].apply(lambda x: get_temp(x))
df['time'] = df['directions'].apply(lambda x: get_oventime(x))

#Calculate main ingredient qty
main_ing = ['flour','butter','sugar','egg','baking soda']
for ing in main_ing:
    df[ing+'%'] = df['ing_dict'].apply(lambda x: ing_percent(x,ing))

#Calculate composition
df['water%'] = df['ing_dict'].apply(lambda x: water_percent(x))
df['fat%'] = df['ing_dict'].apply(lambda x: fat_percent(x))
df['protein%'] = df['ing_dict'].apply(lambda x: protein_percent(x))
df['dry%/wet%'] = df['protein%']/df['water%']
df['heat'] = df['temp']*df['time']
df['%of_sugar_dissolved'] = df.apply(lambda x: min(x['water%']*1.75, x['sugar%']), axis=1)
df['%leavening'] = df['ing_dict'].apply(lambda x: aeration(x))

'''
#Plot main ingredients
plt_3d(df,'flour%','sugar%','butter%')
plt_2d(df,'flour%','sugar%')
plt_2d(df,'butter%','sugar%')
plt_2d(df,'flour%','butter%')

#Plot composition
plt_3d(df,'water%','fat%','protein%')
plt_2d(df,'protein%','fat%')
plt_2d(df,'protein%','water%')
plt_2d(df,'fat%','water%')
plt_2d(df,'heat','water%')

#Logistic Regression
logistic_regression(df,['flour%','butter%','sugar%','egg%','baking soda%'])
logistic_regression(df,['water%','fat%','protein%','heat','%leavening'])

#Linear SVC
linear_SVC(df,['flour%','butter%','sugar%','egg%','baking soda%'])
linear_SVC(df,['water%','fat%','protein%','heat','%leavening'])
'''
#Average values
df_group = df.drop(['ingredients','directions'], axis=1)
df_mean = df_group.groupby('crispiness').agg(np.average)
df_max = df_group.groupby('crispiness').agg(np.max)
df_min = df_group.groupby('crispiness').agg(np.min)

#smooth versus cracked
#df_mean.to_csv('cookies_mean.csv')
#os.startfile('cookies_mean.csv')    
#df_max.to_csv('cookies_max.csv')
#os.startfile('cookies_max.csv')  
#df_min.to_csv('cookies_min.csv')
#os.startfile('cookies_min.csv')  
df.to_csv('cookies_cleaned_test.csv')
os.startfile('cookies_cleaned_test.csv')

