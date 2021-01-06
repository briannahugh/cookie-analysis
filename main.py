# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 11:20:00 2020

@author: HUGHBR
"""

import pandas as pd
import  numpy as np
import os
from get_ingredients import get_ing
from get_directions import get_temp, get_oventime
from get_composition import ing_percent,water_percent,fat_percent,protein_percent,sugar_percent,aeration
from plot_recipes import plt_2d

os.chdir(r'C:\Users\HUGHBR\Documents\Brianna\Clustering\Project\cookies 3')
df = pd.read_csv('cookies_scraped_data.csv', encoding='latin1')
df.index.name = 'recipe_no'

#Extract ingredients & directions
df['ing_dict'] = df['ingredients'].apply(lambda x: get_ing(x))
df['temp'] = df['directions'].apply(lambda x: get_temp(x))
df['time'] = df['directions'].apply(lambda x: get_oventime(x))

#Calculate quantities
main_ing = ['flour','butter','sugar','egg','baking soda']
for ing in main_ing:
    df[ing+'%'] = df['ing_dict'].apply(lambda x: ing_percent(x,ing))

#Calculate composition
df['water%'] = df['ing_dict'].apply(lambda x: water_percent(x))
df['fat%'] = df['ing_dict'].apply(lambda x: fat_percent(x))
df['protein%'] = df['ing_dict'].apply(lambda x: protein_percent(x))
df['sucrose%'] = df['ing_dict'].apply(lambda x: sugar_percent(x))
df['dry%/wet%'] = df['protein%']/df['water%']
df['heat'] = df['temp']*df['time']
df['%of_sugar_dissolved'] = df.apply(lambda x: min(x['water%']*1.75, x['sucrose%']), axis=1)
df['%leavening'] = df['ing_dict'].apply(lambda x: aeration(x))

#Calculate score
main_props = ['water%','fat%','protein%','sucrose%','%leavening','%of_sugar_dissolved']
for prop in main_props:
    df[prop+'_score'] = (df[prop]-df[prop].min())/(df[prop].max()-df[prop].min())

df['crispy_calc'] = df['fat%_score']+df['sucrose%_score']+(1-df['protein%_score'])
df['smooth_calc'] = df['%of_sugar_dissolved_score']
df['thickness_calc'] = df['protein%_score']+(1-df['fat%_score'])

df['crispy_score'] = (df['crispy_calc']-df['crispy_calc'].min())/(df['crispy_calc'].max()-df['crispy_calc'].min())
df['smooth_score'] = (df['smooth_calc']-df['smooth_calc'].min())/(df['smooth_calc'].max()-df['smooth_calc'].min())
df['thickness_score'] =(df['thickness_calc']-df['thickness_calc'].min())/(df['thickness_calc'].max()-df['thickness_calc'].min())

del df['crispy_calc']
del df['smooth_calc']
del df['thickness_calc']

#Plot main ingredients
plt_2d(df,'flour%','sugar%')
plt_2d(df,'butter%','sugar%')
plt_2d(df,'flour%','butter%')

#Plot composition
plt_2d(df,'protein%','fat%')
plt_2d(df,'protein%','sugar%')
plt_2d(df,'fat%','sugar%')

#Average values
df_group = df.drop(['ingredients','directions'], axis=1)
df_mean = df_group.groupby('crispiness').agg(np.average)
df_max = df_group.groupby('crispiness').agg(np.max)
df_min = df_group.groupby('crispiness').agg(np.min)

#Output
df.to_csv('cookies_cleaned.csv')
os.startfile('cookies_cleaned.csv')

