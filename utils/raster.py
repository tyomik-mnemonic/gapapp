import rasterio as rst
import pandas as pd
import numpy as np
import geopandas as gpd
import shapely
import os



class RastEater:
    def __init__(self, path, frmt):
        self.path = path
        self.frmt = frmt
    
    def reading(self):
        files = os.listdir(self.path)
        rastset = []
        for f in files:
            if f.endswith(self.frmt):
                opn = rst.open(self.path + f)
                rastset.append(opn)
        return(rastset)
    
    def read_out(self):
        img_set = [rst.open(r).read(1) for r in self.reading()]
        return img_set
    def metainfo(self):
        for r in self.reading():
            try:
                print(r.name, r.meta)
            except:
                print('Error. Check than file format')
            
    def statinfo(self):
        for r in self.reading():
            try:
                print(r.name, 'mean: ',r.read().mean(), 'max: ',r.read().max(), 'min: ',r.read().min())
                     
            except:
                print('Error. Check than you use single band image')
        
        return self.reading()