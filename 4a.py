import numpy as np
import matplotlib.pyplot as plt
import json

movie_data = np.loadtxt('data/movies.txt', dtype=str, delimiter='\t')
rating_data = np.loadtxt('data/data.txt', dtype=str, delimiter='\t')

def read_data(dest):
    with open(dest, 'r') as f:
        return json.load(f)

U = read_data('uproj.txt')
V = read_data('vproj.txt')

def process_data(file_name):
    return np.loadtxt(file_name, dtype=str, delimiter='\t')

# U is 2 by n=number of users
def get_random(V):
    movies = {'star_trek1': 227, 'star_trek2': 228, 'star_trek3':229,'star_trek4':230, \
    'pulp_fiction': 56, 'reservoir_dogs': 156, 'jackie_brown': 346, \
    'braveheart': 22, 'schindler_list': 318, 'titanic':313}

    X = []
    Y = []
    labels = movies.keys()


    for key in movies.keys():
        idx = int(movies[key]) - 1
        X.append(V[0][idx])
        Y.append(V[1][idx])

    fig, ax = plt.subplots()
    ax.scatter(X, Y)

    for i, lab in enumerate(labels):
        ax.annotate(lab, (X[i], Y[i]))
    plt.show()

get_random(V)