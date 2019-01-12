import matplotlib.pyplot as plt
import numpy as np
from GaussianProcess.gaussian_process.plot_func import get_plot as get_plot_gauss
from Simple_Regression.regression import get_plot as get_plot_poly


fig, (ax1, ax2) = plt.subplots(2, 1)

def f(X):
    return np.sin(X) + X

x_prior = np.linspace(-5, 10, 10)
x_domain = np.linspace(-5, 10, 100)

gauss_plot = get_plot_gauss(ax1, f, x_prior, x_domain)

degree = 5
poly_plot  = get_plot_poly(ax2, f, x_domain, degree)


plt.show()


fig, (ax1, ax2) = plt.subplots(2, 1)

def f(X):
    return np.sin(X)

x_prior = np.linspace(-5, 10, 10)
x_domain = np.linspace(-5, 10, 100)

gauss_plot = get_plot_gauss(ax1, f, x_prior, x_domain)

degree = 5
poly_plot  = get_plot_poly(ax2, f, x_domain, degree)


plt.show()


