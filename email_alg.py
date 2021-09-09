# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 13:54:22 2021

@author: Andrew
"""

import numpy as np
import time

data = np.loadtxt('emails.txt', dtype=str)
np.random.shuffle(data)

def get_uniques_unsorted(arr):
    uniq, index = np.unique(arr, return_index=True)
    return uniq[index.argsort()]

t0 = time.time()
uniques = get_uniques_unsorted(data)
t1 = time.time()

total = t1-t0

