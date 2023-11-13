import numpy as np
def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):  
        data[i] = [int(e) for e in input().split()]
    return weight, data

def report_lower_than_mean(weight, data):
    scores = np.sum(weight * data[:, 1:], axis = 1)
    mean = np.mean(scores)
    lower = np.where(scores < mean)[0]
    ids = data[lower, 0]
    if len(ids) == 0:
        print("None")
        return
    
    print(", ".join(map(str, ids)))

exec(input().strip())