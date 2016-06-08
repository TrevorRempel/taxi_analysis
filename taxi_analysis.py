import pandas as pd
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from haversine import haversine
import numpy as np
import math
import os
import scipy as sp
import matplotlib as mpl 
import matplotlib.cm as cm 
import matplotlib.pyplot as plt 
import datetime
import seaborn as sns
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Circle
import glob
import shapefile
import pandas as pd
import mpl_toolkits.basemap.pyproj as pyproj
from sklearn import cluster
from IPython import display
from collections import defaultdict
import pickle

def select_vals(df,year, month = (1,12), day = (0,6), time=(0,24)):
    idx = pd.IndexSlice
    yL,yR = year
    mL,mR = month
    dL,dR = day
    tL,tR = time
    return df.loc[idx[yL:yR,mL:mR,dL:dR,tL:tR],idx[:,:]]




