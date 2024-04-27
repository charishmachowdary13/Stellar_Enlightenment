import warnings
warnings.filterwarnings('ignore')

import cv2 as cv
import numpy as np
import os
import pandas as pd
import pickle
import plotly.express as px
import random
import sklearn

features = ['alpha', 'delta', 'u', 'g', 'r', 'i', 'z', 'redshift']
df = None
with open(file='scaling.pkl', mode='rb') as s_pkl:
        scaling = pickle.load(file=s_pkl)

with open(file='stacking_classifier.pkl', mode='rb') as m_pkl:
            clf  = pickle.load(file=m_pkl)



