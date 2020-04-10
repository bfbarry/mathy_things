import numpy as np
import matplotlib.pyplot  as plt
import json
import math

def sum_digits(number):
    str_num = str(number)
    root_array = [int(i) for i in str_num]
    sum_step = sum(root_array)
    return sum_step

def dr(number, degree = 'full'):
    """
    returns full digital root unless degree of summation iteration is stated
    """
    root = sum_digits(number)
    if degree == 'full':
        while len(str(root)) != 1:
            root = sum_digits(root)
    else:
        while (degree != 1):
            if degree < 1:
                root = number
                break
            root = sum_digits(root)
            degree-=1

    return root

def compare_polynomial_roots(length, exp_lim):
    all_roots = []
    x_axis = np.arange(1,length + 1)
    exp_range = np.arange(1, exp_lim + 1)

    for exp in exp_range:
        roots = [dr(i**exp) for i in x_axis]
        all_roots.append(roots)

    #Plotting
    plt.figure(figsize=(20,10))
    for exp in exp_range:
        plt.plot(x_axis, all_roots[exp-1], 'o-', label = 'x^' + str(exp))
    plt.legend(loc='best')
    plt.show()

    return all_roots

def plot_digital_roots(num_arrays, verbose = True):
    """
    Allows you to compare multiple arrays given they are same length
    """
    plt.figure(figsize=(20,10))

    for i, array in enumerate(num_arrays):
        x_axis = np.arange(len(array))
        roots = np.array([dr(i) for i in array])
        plt.plot(x_axis, roots, 'o-', label = 'arr' + str(i+1))

        plt.legend(loc='best')

        if verbose == True:
            for unique in np.unique(roots):
                print(str(unique), '@ freq', np.count_nonzero(roots == unique)/len(roots))
            #print('all roots', roots)
            print('unique vals:', np.unique(roots))

    return roots
