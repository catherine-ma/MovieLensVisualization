import numpy as np
import matplotlib.pyplot as plt
import json

movie_data = np.loadtxt('data/movies.txt', dtype=str, delimiter='\t')
rating_data = np.loadtxt('data/data.txt', dtype=str, delimiter='\t')

def read_data(dest):
    with open(dest, 'r') as f:
        return json.load(f)

U = read_data('umatrix.txt')
V = read_data('vmatrix.txt')

print U

def process_data(file_name):
    return np.loadtxt(file_name, dtype=str, delimiter='\t')

# U is 2 by n=number of users
def get_random(V):
    movies = {aladdin: 95, pocahontas: 542, hercules: 993, \
    pulp_fiction: 56, reservoir_dogs: 156, jackie_brown: 346, \
    star_wars: 50, empire_strikes: 172, return_jedi: 181}

    X = []
    Y = []

    for key in movies.keys():
        idx = int(movies[key]) - 1
        X.append(V[0][idx])
        Y.append(V[1][idx])

    plt.scatter(X, Y)
    plt.show()

