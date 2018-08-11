#!/usr/bin/env python
# -*- coding: utf-8 -*-

from control.matlab import *
import matplotlib.pyplot as plt
import numpy as np

def pid(Kp=0.6, Ki=0.03, Kd=0.03):
    # 引数：比例ゲイン，積分ゲイン，微分ゲイン

    # Controller
    num = [Kd, Kp, Ki]
    den = [1, 0]
    K = tf(num, den) # num/defの伝達関数，例えば分母はdef[0]*s^n + def[1]*s^(n-1) + ... + def[n-1]*s^1 + def[n]:s^0

    # Plant
    Kt = 1
    J = 0.01
    C = 0.1
    num = [Kt]
    den = [J, C, 0]
    G = tf(num, den)

    # Feedback loop
    sys = feedback(K*G, 1)

    # Drawing
    t = np.linspace(0, 3, 1000)
    y, T = step(sys, t)
    plt.plot(T, y)
    plt.grid()
    plt.axhline(1, color="b", linestyle="--")
    plt.xlim(0, 3)

if __name__ == "__main__":
  pid()
