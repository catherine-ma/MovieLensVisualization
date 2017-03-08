import numpy as np
import heapq
import json
import operator
import collections
import matplotlib.pyplot as plt

import basic as b

# Read data from a json file
def read_data(dest):
    with open(dest, 'r') as f:
        return json.load(f)

# Grab movie data for 10 best movies
def get_ten_best_movies(movies, ratings):

    # Get average ratings
    movie_ratings = [0 for i in range(len(movies))]
    num_ratings = [0 for i in range(len(movies))]	
    for i in range(len(ratings)):
	idx = int(ratings[i][1]) - 1
	rating = float(ratings[i][2])
	movie_ratings[idx] += rating
	num_ratings[idx] += 1
    avg_ratings = []	
    
    # Calculate 10 best ratings
    for i in range(len(movie_ratings)):
	avg_ratings.append((i, movie_ratings[i] / num_ratings[i]))
    best_ratings = heapq.nlargest(10, avg_ratings, key=operator.itemgetter(1))
    
    # Get best movies
    best_movies = [0 for i in range(len(best_ratings))]
    for i in range(len(best_ratings)):
	movie_idx = best_ratings[i][0]
	best_movies[i] = movies[movie_idx]
    return best_movies

def plot2D(best_movies, V, dest):
    X = [0 for i in range(len(best_movies))]
    Y = [0 for i in range(len(best_movies))]
    names = [0 for i in range(len(best_movies))]
    for i in range(len(best_movies)):
	mov_idx   = int(best_movies[i][0])
	names[i] = best_movies[i][1]
	X[i] = V[mov_idx][0]
	Y[i] = V[mov_idx][1]
    plt.figure(figsize=(12, 12))
    plt.scatter(X, Y)
    plt.title("Ten Best Movies Visualization")
    plt.xlabel(r"$v_1$")
    plt.ylabel(r"$v_2$")
    plt.xlim(-.2, 4.5)
    for name, x, y, in zip(names, X, Y):
	plt.annotate(name, xy=(x, y), xytext=(0, 5), 
	             textcoords='offset points', va='bottom')
    plt.savefig(dest)


def main():
    movies = b.process_data(b.movie_data)
    ratings = b.process_data(b.rating_data)
    V = np.transpose(read_data("vproj.json"))
    best_movies = get_ten_best_movies(movies, ratings)
    plot2D(best_movies, V, "images\\best_movies_2D.png")
    
main()