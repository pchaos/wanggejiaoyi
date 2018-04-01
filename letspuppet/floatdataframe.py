# coding: utf-8
"""
Created on Wed Sep 20 23:00:44 2017

@author: 久久为功
"""

def floatdataframe(df,changecollist):
    for col in df.columns:
        if col in changecollist:
            df[col]=df[col].apply(lambda x:0 if x=='' else float(x))
    return df

if __name__=='__main__':
    print('no demo code')
