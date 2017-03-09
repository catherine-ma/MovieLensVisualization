import numpy as np
import heapq
import operator
import collections
import matplotlib.pyplot as plt

movie_data = 'data/movies.txt'
rating_data = 'data/data.txt'

# Returns numpy arrays of data in file_name
def process_data(file_name):
	return np.loadtxt(file_name, dtype=str, delimiter='\t')

# Returns numpy array of all ratings
def get_all_ratings(ratings):
	temp_ratings = ratings[:, 2]
	return temp_ratings.astype(float)

# Returns list of ratings of most popular movies
def get_ten_pop_movies(movies, ratings):
	num_ratings = [0 for i in range(len(movies))]

	for i in range(len(ratings)):
		idx = int(ratings[i][1]) - 1
		num_ratings[idx] += 1

	for i in range(len(num_ratings)):
		num_ratings[i] = (i, num_ratings[i])

	pop_movies = heapq.nlargest(10, num_ratings, key=operator.itemgetter(1))
	pop_movies = [pop_movies[i][0] for i in range(len(pop_movies))]

	pop_ratings = []

	for i in range(len(ratings)):
		if int(ratings[i][1]) - 1 in pop_movies:
			pop_ratings.append(float(ratings[i][2]))

	return pop_ratings

# Returns list of ratings of best movies
def get_ten_best_movies(movies, ratings):
	movie_ratings = [0 for i in range(len(movies))]
	num_ratings = [0 for i in range(len(movies))]

	for i in range(len(ratings)):
		idx = int(ratings[i][1]) - 1
		rating = float(ratings[i][2])
		movie_ratings[idx] += rating
		num_ratings[idx] += 1

	avg_ratings = []

	for i in range(len(movie_ratings)):
		avg_ratings.append((i, movie_ratings[i] / num_ratings[i]))

	best_movies = heapq.nlargest(10, avg_ratings, key=operator.itemgetter(1))
	best_movies = [best_movies[i][0] for i in range(len(best_movies))]

	best_ratings = []

	for i in range(len(ratings)):
		if int(ratings[i][1]) - 1 in best_movies:
			best_ratings.append(float(ratings[i][2]))

	return best_ratings

# Returns list of ratings of movies of genre "genre"
def get_genre_ratings(movies, ratings, genre):
	genre_ratings = []

	for i in range(len(ratings)):
		movie = int(ratings[i][1]) - 1

		if movies[movie][genre] == '1':
			genre_ratings.append(float(ratings[i][2]))

	return genre_ratings


def hist_ratings(ratings, xylabel, dest):
	n, bins, patches = plt.hist(ratings, bins=5, range=(0.5, 5.5), facecolor='green')
	mean = np.mean(ratings)
	med  = np.median(ratings)
	plt.xlabel('rating')
	plt.ylabel('count')
	plt.text(xylabel[0], xylabel[1], "mean   = " + str(mean) + "\nmedian = " + str(med))
	plt.savefig(dest)
	plt.show()
	
if __name__ == '__main__':
	movies = process_data(movie_data)
	ratings = process_data(rating_data)

	animation = 5
	drama = 7
	horror = 13

	all_ratings = get_all_ratings(ratings)
	pop_ratings = get_ten_pop_movies(movies, ratings)
	best_ratings = get_ten_best_movies(movies, ratings)
	animation_ratings = get_genre_ratings(movies, ratings, animation)
	drama_ratings = get_genre_ratings(movies, ratings, drama)
	horror_ratings = get_genre_ratings(movies, ratings, horror)

	# hist_ratings(all_ratings, [.2, 30000], "images\\all_ratings_hist.png")
	# hist_ratings(pop_ratings, [.2, 1600], "images\\pop_ratings_hist.png")
	# hist_ratings(best_ratings, [.2, 14], "images\\best_ratings.png")
	# hist_ratings(animation_ratings, [.2, 1200], "images\\animation_ratings_hist.png")
	# hist_ratings(drama_ratings, [.2, 9000], "images\\drama_ratings_hist.png")
	# hist_ratings(horror_ratings, [.2, 1600], "images\\horror_ratings.png")






