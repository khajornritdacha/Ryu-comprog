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
    res = []
    for i in range(len(A)):
        new_row = []
        for j in range(len(B[0])):
            cur = 0
            for k in range(len(A[0])):
                cur += A[i][k] * B[k][j]
            new_row.append(cur)
        res.append(new_row)
    return res

exec(input().strip())