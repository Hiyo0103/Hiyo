'''
Hiyo Kobari
02/24/2020
This linear regression shows the relation between SAT score and GPA.
The datasets are from
https://www.dropbox.com/s/lva8qfvqzi39xxt/1.01.%20Simple%20linear%20regression.csv?dl=0
'''

import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x, y):
   #number of observations
    n = np.size(x);

    #finding the mean of x and y vector
    mean_x, mean_y = np.mean(x), np.mean(y)

    #calculating the least squares
    SS_xy = np.sum(y*x) - n * mean_y * mean_x
    SS_xx = np.sum(x*x) - n * mean_x * mean_x

    #regression coefficents
    slope = SS_xy/SS_xx
    yintercept = mean_y - slope * mean_x

    #return m and b
    return(slope, yintercept)

def plot_regression_line(x, y, b):
    #plotting the actual points as a scatter plot
    plt.scatter(x, y, color = "m", marker = "o", s = 30)

    #predicted response vector
    y_pred = b[0] + b[1] + x

    #plotting the regression plot_regression_line
    plt.plot(x, y_pred, color = "g")

    #putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    #function to show plotting
    plt.show()

def main():
    #observations
    x = np.array([2.40, 2.52, 2.54, 2.74, 2.83, 2.91, 3.00, 3.00, 3.01, 3.01, 3.02, 3.07, 3.08, 3.08, 3.12, 3.17, 3.17, 3.17, 3.17, 3.19, 3.19, 3.19, 3.20, 3.21, 3.24, 3.28, 3.28, 3.29, 3.29, 3.31, 3.32, 3.34, 3.37, 3.38, 3.39, 3.40, 3.41, 3.42, 3.44, 3.47, 3.48, 3.49, 3.50, 3.51, 3.52, 3.54, 3.58, 3.59, 3.60, 3.61, 3.62, 3.64, 3.65, 3.71, 3.73, 3.76, 3.81])
    y = np.array([1714, 1664, 1760, 1685, 1693, 1670, 1764, 1764, 1792, 1850, 1735, 1775, 1735, 1712, 1773, 1872, 1755, 1674, 1842, 1786, 1761, 1722, 1663, 1687, 1974, 1826, 1821, 1855, 1880, 1849, 1808, 1954, 1865, 1966, 1990, 1956, 1979, 1907, 1879, 1953, 1891, 1964, 1893, 2041, 1850, 1934, 1931, 1933, 1975, 2021, 2015, 1997, 2020, 1936, 1987, 1962, 2050])

    # estimated coefficients
    b = estimate_coef(x, y)
    print("Estimated coefficients: \n b = {} \ \n m = {}".format(b[0], b[1]))

    #plotting regression line
    plot_regression_line(x, y, b)

#make script importable and executables
if __name__ == "__main__":
    main()
