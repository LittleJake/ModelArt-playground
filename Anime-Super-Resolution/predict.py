# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 20:28:04 2019

@author: wmy
"""

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
from keras import backend as K
from keras.losses import mean_absolute_error, mean_squared_error
from keras.models import load_model
from keras.optimizers import Adam
import random
import os
from model import wdsr_a, wdsr_b
from utils import DataLoader

model = wdsr_b(scale=4, num_res_blocks=32)
model.load_weights('./weights/wdsr-b-32-x4.h5')

data_loader = DataLoader(scale=4)

def predict(model, fp, sp):
    lr = Image.open(fp)
    lr = np.asarray(lr)
    x = np.array([lr])
    y = model.predict(x)
    y = np.clip(y, 0, 255)
    y = y.astype('uint8')
    sr = Image.fromarray(y[0])
    sr.save(sp)
    pass

def resize(fp, sp, scale=4):
    lr = Image.open(fp)
    lr = lr.resize((scale*lr.size[0], scale*lr.size[1]))
    lr.save(sp)
    pass

def downsampling(fp, sp):
    hr = data_loader.imread(fp)
    lr = data_loader.downsampling(hr)
    lr.save(sp)
    pass

def copy(fp, sp):
    if not os.path.exists(sp):
        lr = Image.open(fp)
        lr.save(sp)
        return True
    return False
    pass

def predict_testset(setpath='datasets/test/'):
    files = os.listdir(setpath)
    print("Pending file count:", len(files))
    for file in files:
        if copy(fp=(setpath+file), sp='outputs/lr_' + file + '.png'):
            try:
                predict(model, fp='outputs/lr_' + file + '.png', sp='outputs/sr_' + file + '.png')
                os.remove(setpath+file)
                print("procceed:", 'sr_' + file + '.png')
            except Exception as e:
                print(e)
        else:
            print("skip:", 'lr_' + file + '.png')
        pass
    pass


