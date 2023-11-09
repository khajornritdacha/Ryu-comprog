def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    return [ [c*x for x in row] for row in A ]

def mult(A, B):
    """
    Generate the product of two matrices A and B.
    """
    return [ [ sum([A[i][k]*B[k][j] for k in range(len(B))]) for j in range(len(B[0])) ] for i in range(len(A))]

exec(input().strip())
