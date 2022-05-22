# -*- coding: utf-8 -*-
"""
Created on Fri May 20 15:51:30 2022

@author: Carlos Vallejos
"""
import pandas as pd 



def ejercicio():
    a = [['A',42.3,1653062446,'001'],
         ['A',41.3,1653062447,'001'],
         ['A',40.4,1653062448,'002']]
    b = [['B',43.3,1653062450,'001']]

    df_a = pd.DataFrame(data = a) 
    df_a.to_csv('datos_a.csv', sep=';',header=None,index=None) 

    df_b = pd.DataFrame(data = b) 
    df_b.to_csv('datos_b.csv', sep=';',header=None,index=None) 
    
    
    df1 =  pd.read_csv('datos_a.csv', sep=';',header=None);
    df2 =  pd.read_csv('datos_b.csv', sep=';',header=None);
         
    df_final = pd.concat([df1, df2], axis=0)
    df_final.sort_values(by=[2],ascending=True)
    
    print(df_final)


print(ejercicio())
