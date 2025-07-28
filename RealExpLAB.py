# -*- coding: utf-8 -*-
"""
@author: Dan Koskiranta
"""

import numpy as np
import matplotlib.pyplot as plt


def real_exp(n, a):
    r = np.zeros(n.size)
    for i in range(0, n.size):
        # Add code to compute values of r[i]
        r[i] = a**i
    return r

def plot_real_exp(n, r):
    fig = plt.figure(figsize = (14, 10))
    ax = fig.add_subplot(2, 1, 1)
    markerlines, stemlines, baseline = ax.stem(n, r, markerfmt='o')
    plt.setp(stemlines, color='k', linewidth=1.0)
    plt.setp(baseline, color='k', linewidth=2.0)
    plt.setp(markerlines, color='k', markersize=5)
    ax.set_xlabel('n', fontsize=20, labelpad=12)
    ax.set_ylabel('x[n]', fontsize=20, labelpad=10)
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.tick_params(axis='both', which='both', labelsize=14, 
                   bottom=False, top=False, labelbottom=True,
                   left=False, right=False, labelleft=True)
    markerlines.set_clip_on(False)
    plt.show()

n = np.arange(0, 20)
# Add code to call real_exp function & compute signal r
r = real_exp(n, .9)
plot_real_exp(n, r)

