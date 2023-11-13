import numpy as np
def p( X ):
    logit = -3.98 + 0.1*X[:, 0] + 0.5*X[:, 1]
    return 1.0 / (1.0 + np.exp(-logit))

exec(input().strip()) 