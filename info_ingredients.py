# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 14:43:46 2020

@author: HUGHBR
"""

all_ing = {'flour':
                    {'rx':'(?:(all(?:-| )purpose|coconut|bread|pastry|cake|oat|almond|whole(?:-| )wheat)\s)?flour',
                    'cup_to_g':{'all purpose':120,'coconut':112,'bread':130,'pastry':130,'cake':130,'whole wheat': 128,'oat': 90,'almond':112,'regular':120,'gluten free':120}
                    },
            'sugar':
                    {'rx':'(?:(white|granulated|cane|turbinado|coconut|brown|light(?:-| )brown|dark(?:-| )brown)\s)?sugar',
                     'cup_to_g':{'white':201,'granulated':200,'cane':200,'turbinado':202,'light brown':200,'dark brown':200,'brown':200,'coconut':190,'regular':200}
                     },
            'butter':
                    {'rx':'(?:(unsalted|salted|melted|cold)\s)?butter',
                     'cup_to_g':{'salted':227,'unsalted':227,'melted':227,'cold':227,'regular':227}
                     },
            'oat':
                    {'rx':'()oats*',
                     'cup_to_g':{'regular':90,'gluten free':90}
                     },                    
            'vanilla':
                    {'rx':'()vanilla',
                     'cup_to_g':{'regular':208}
                     },
            'baking soda':
                    {'rx':'()baking soda',
                     'cup_to_g':{'regular':230.4}
                     },
            'baking powder':
                    {'rx':'()baking powder',
                     'cup_to_g':{'regular':192}
                     },
            'salt':
                    {'rx':'()salt',
                     'cup_to_g':{'regular':273}
                     },
            'egg':
                    {'rx':'egg(?: (whites*|yolks*))*',
                     'cup_to_g':{'yolk':(0.51/1.57)*308,'white':(1.06/1.57)*308,'regular':308}
                     },
            'honey':
                    {'rx':'()honey',
                     'cup_to_g':{'regular':340}
                     },
            'syrup':
                    {'rx':'(corn|maple) syrup*',
                     'cup_to_g':{'corn':340,'maple':340,'regular':340}
                     },
            'milk':
                    {'rx':'()milk (?!choc)',
                     'cup_to_g':{'regular':240}
                     },
            'oil':
                    {'rx':'()oil',
                     'cup_to_g':{'regular':218}
                     },
            'water':
                    {'rx':'()oil',
                     'cup_to_g':{'regular':236}
                     },
            'shortening':
                    {'rx':'()shortening',
                     'cup_to_g':{'regular':205}
                     },
            'cornstarch':
                    {'rx':'()cornstarch',
                     'cup_to_g':{'regular':128}
                     },
            'chocolate':
                    {'rx':'(?:(white|dark|milk)\s)?chocolate',
                     'cup_to_g':{'white':180,'milk':178,'dark':180,'regular':178}
                     }
            }