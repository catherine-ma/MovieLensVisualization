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

# Returns list of 10 movies of genre "genre"
def get_genre_ratings(movies, ratings, genre):
    
    # Grab index corresponding to this genre in ratings data
    if genre == "animation":
	movie_ids = [71,  # Lion King, The 
	             542, # Pocahontas 
	             1,   # Toy Story 
	             99,  # Snow White and the Seven 
	             596, # Hunchback of Notre Dame, The 
	             501, # Dumbo
	             432, # Fantasia  
	             422, # Aladdin and the King of Thieves
	             418, # Cinderella
	             95   # Aladdin
	             ]
    elif genre == "drama":
	movie_ids = [1115, # Twelfth Night
	             173,  # Princess Bride, The
	             151,  # Willy Wonka and the Chocolate Factory 
	             69,   # Forrest Gump 
	             399,  # Three Musketeers, The
	             319,  # Everyone Says I Love You
	             585,  # Son in Law
	             655,  # Stand by Me 
	             739,  # Pretty Woman 
	             535,  # Addicted to Love
	             ]
    elif genre == "horror":
	movie_ids = [671,  # Bride of Frankenstein
	             208,  # Young Frankenstein 
	             561,  # Mary Shelley's Frankenstein 
	             219,  # Nightmare on Elm Street, A 
	             183,  # Alien
	             343,  # Alien: Resurrection 
	             665,  # Alien 3 
	             185,  # Psycho 
	             98,   # Silence of the Lambs, The
	             234   # Jaws
	             ]
	
    # Grab all movies of this genre
    genre_movies = []
    for mov in movies:
	if int(mov[0]) in movie_ids:
	    genre_movies.append(mov)
    
    return genre_movies

def plot2D(movies, V, dest, title, xlo=None, xhi=None, ylo=None, yhi=None):
    X = [0 for i in range(len(movies))]
    Y = [0 for i in range(len(movies))]
    names = [0 for i in range(len(movies))]
    for i in range(len(movies)):
	mov_id   = int(movies[i][0])
	names[i] = movies[i][1]
	X[i] = V[mov_id][0]
	Y[i] = V[mov_id][1]
    plt.figure(figsize=(12, 12))
    plt.scatter(X, Y)
    plt.title(title + " Genre Visualization")
    plt.xlabel(r"$v_1$")
    plt.ylabel(r"$v_2$")
    if xlo and xhi:
	plt.xlim(xlo, xhi)
    if ylo and yhi:
	plt.ylim(ylo, yhi)
    for name, x, y, in zip(names, X, Y):
	plt.annotate(name, xy=(x, y), xytext=(0, 5), 
	             textcoords='offset points', va='bottom')
    plt.savefig(dest)


def main():
    movies = b.process_data(b.movie_data)
    ratings = b.process_data(b.rating_data)
    V = np.transpose(read_data("vproj.json"))
    animations = get_genre_ratings(movies, ratings, "animation")
    drama      = get_genre_ratings(movies, ratings, "drama")
    horror     = get_genre_ratings(movies, ratings, "horror")
    plot2D(animations, V, "images\\animations_2D.png", "Animations", 
           1.9, 3.55, -1.2, 1.7)
    plot2D(drama, V, "images\\drama_2D.png", "Drama", 1.6, 3.6, -1.1, 1.2)
    plot2D(horror, V, "images\\horror_2D.png", "Horror", 1.4, 3.1)
    
    for m in movies:
	if m[7]=='1':
	    print m[:2]
main()