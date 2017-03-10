'''
CS155 4b.py
Miniproject MovieLensVisualization
'''

import numpy as np
import matplotlib.pyplot as plt
import json

movie_data = np.loadtxt('data/movies.txt', dtype=str, delimiter='\t')
rating_data = np.loadtxt('data/data.txt', dtype=str, delimiter='\t')
ratings = []
for r in rating_data:
    ratings.append(map(int, r))
rating_data = np.array(ratings)

def read_data(dest):
    with open(dest, 'r') as f:
        return json.load(f)

U = read_data('umatrix.json')
V = read_data('vproj.json')


def process_data(file_name):
    return np.loadtxt(file_name, dtype=str, delimiter='\t')

def get_popular(V):
    n = 1682 + 1 # number of movies
    count = np.array([0 for _ in range(n)])
    for r in rating_data:
        count[r[1]] += 1

    poplar = count.argsort()[-10:][::-1]
    titles = [movie_data[p - 1][1] for p in poplar]
    idxes = [int(movie_data[p - 1][0]) for p in poplar]

    X = []
    Y = []

    for idx in idxes:
        X.append(V[0][idx])
        Y.append(V[1][idx])

    plt.scatter(X, Y)
    plt.title('Most Popular Movies')

    for name, x, y, in zip(titles, X, Y):
        if x < 2.35:
            plt.annotate(name, xy=(x, y), xytext=(0, 5), 
                 textcoords='offset points', va='bottom')
        else:
            plt.annotate(name, xy=(x - 0.25, y), xytext=(0, 5), 
                 textcoords='offset points', va='bottom')


    plt.show()


get_popular(V)




