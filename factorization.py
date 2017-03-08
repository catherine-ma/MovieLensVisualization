'''
Matrix Factorization
CS155 MovieLensVisualization
'''

import numpy as np
from prob2utils import train_model
import json

def write_data(dest, data):
    with open(dest, 'w') as f:
        json.dump(data, f)
def read_data(dest):
    with open(dest, 'r') as f:
        return json.load(f)

def train():
    n = 1682 + 1

    with open("data/data.txt",'r') as f:
        _data = np.genfromtxt(f, delimiter='\r', dtype=None)
        # I'm being dumb and can't parse the data easily for some reason
        data = []
        for _line in _data:
            line = map(int, _line.split('\t'))
            data.append(line)
            
        users = np.asarray(data).T[0]
        m = max(users) + 1

        Y = []
        for d in data:
            Y.append((d[0], d[1], d[2]))
        Y = np.array(Y)

        k = 20
        reg = 10**-3
        eta = 0.03
        U, V, err = train_model(m, n, k, eta, reg, Y)

        print U
        print V
        print err

        write_data("umatrix.txt", U.tolist())
        write_data("vmatrix.txt", V.tolist())
        write_data("err.txt", err)


if __name__ == "__main__":
    train()


