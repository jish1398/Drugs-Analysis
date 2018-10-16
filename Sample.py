# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 21:57:17 2018

@author: jishn
"""

import pandas as pd

# Reading the file 
data=pd.read_csv('C:/Users/jishn/Desktop/DP/DATA/drugsComTest_raw.tsv',delimiter='\t',encoding='utf-8')
print(data.head)


