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

        write_data("umatrix.json", U.tolist())
        write_data("vmatrix.json", V.tolist())
        write_data("err.json", err)

def problem5part1projection():
    V = read_data("vmatrix.json")
    U = read_data("umatrix.json")
    
    A, S, B = np.linalg.svd(V)
    twocol = A.T[:2]
    Uproj = np.dot(twocol, np.array(U).T)
    Vproj = np.dot(twocol, V)
    
    print Uproj
    print Vproj

    write_data("uproj.json", Uproj.tolist())
    write_data("vproj.json", Vproj.tolist())

    
if __name__ == "__main__":
    problem5part1projection()

