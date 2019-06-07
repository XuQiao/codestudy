# Optimal Replacement of GMC Bus Engines: An Empirical Model of Harold Zurcher
# Author(s): John Rust
# Source: Econometrica, Vol. 55, No. 5 (Sep., 1987), pp. 999-1033
# Published by: The Econometric Society
# Stable URL: http://www.jstor.org/stable/1911259

# How to use "bottom-up" method to solve optimatization of bus engine replacement problem

# assumptions:
# 

# math prerequisite:

# model details:


# notation
# C(x(t)): Choice set 
# i: One choice from choice set
# eps(t, i): Error term
# x(t): K-dimensional vector variable 
# u(x(t), i, theta1): Single-period utility function
# p(x(t+1), eps(t+1), x(t), eps(t), i, theta2, theta3): transition density
# theta = (beta, theta1, theta2, theta3): vector of parameters
# beta: discount factor

# lf: Full likelihood function 
# l1: Partial transition likelihood function 
# l2: Partial structual likelihood function 
# V: value function
# f(x(t),theta): Markovian replacement policy
# EV: Unknown expected value function
# P1: Old bus scraping value
# P2: New bus replacing cost
# gamma(theta1, theta2): threshold value of mileage


# --------------------- Implementation --------------------------#
# Author: Qiao Xu
# Email: qiao.xu@vanderbilt.edu
# Version: v0.0 
# Date: Aug. 30, 2016

import 
