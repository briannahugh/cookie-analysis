# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 21:29:50 2020

@author: HUGHBR
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plt_3d(df,col_x,col_y,col_z):
    
    df_crispy = df[df['crispiness']=="crispy"]
    df_chewy = df[df['crispiness']=="chewy"]
        
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    #Crispy
    X1 = df_crispy[col_x]
    Y1 = df_crispy[col_y]
    Z1 = df_crispy[col_z]
    
    ax.scatter(X1, Y1, Z1, c='r', marker='o')
    
    X2 = df_chewy[col_x]
    Y2 = df_chewy[col_y]
    Z2 = df_chewy[col_z]
     
    ax.scatter(X2, Y2, Z2, c='b', marker='+')
 
    ax.set_xlabel(col_x)
    ax.set_ylabel(col_y)
    ax.set_zlabel(col_z)
    
    plt.show()


def plt_2d(df,col_x,col_y):
    
    df_crispy = df[df['crispiness']=="crispy"]
    df_chewy = df[df['crispiness']=="chewy"]
    
    plt.scatter(df_crispy[col_x], df_crispy[col_y], color='red', marker='o', label='crispy')
    plt.scatter(df_chewy[col_x], df_chewy[col_y], color='blue', marker='+', label='chewy')
    
    plt.legend(loc='upper right')
    plt.title(col_x+' vs '+col_y)
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    
    plt.savefig(col_x+'_vs_'+col_y+'.png')    
    plt.show()
    

def plt_violin(df,col):

    df_crispy = df[df['crispiness']=="crispy"]
    df_chewy = df[df['crispiness']=="chewy"]
           
    fig, ax = plt.subplots(1,2,sharey=True)
    
    ax[0].violinplot(df_crispy[col], showmeans=True, showmedians=True)
    ax[1].violinplot(df_chewy[col], showmeans=True, showmedians=True)
    
    crispy_mean = np.average(df_crispy[col])
    crispy_median = np.median(df_crispy[col])
    chewy_mean = np.average(df_chewy[col])
    chewy_median = np.median(df_chewy[col])
    
    fig.suptitle(col,fontsize='x-large',fontweight='bold',y=1.05)              
    ax[0].set_title('Crispy\nMedian: '+'{:.2%}'.format(crispy_median)+'\nMean: '+'{:.2%}'.format(crispy_mean))
    ax[1].set_title('Chewy\nMedian: '+'{:.2%}'.format(chewy_median)+'\nMean: '+'{:.2%}'.format(chewy_mean))
    
    plt.tight_layout()
    plt.savefig(col+'.png',pad_inches=0.5,bbox_inches='tight')    
    plt.show()

def plt_values(x,y1,y1_name,y2,y2_name,title):
    
    plt.plot(x, y1, color='red',label=y1_name)
    plt.plot(x, y2, color='blue',label=y2_name)
    plt.xscale('log')
    
    plt.legend(loc='upper right')
    plt.title(title)
    plt.xlabel(x)
    
    plt.savefig(y1_name+' vs '+y2_name+'_boxplot.png')    
    plt.show()
 

