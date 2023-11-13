import numpy as np

def sum_2_rows( M ):
    return M[::2, :] + M[1::2, :]

def sum_left_right( M ):
    c = M.shape[1] // 2
    return M[:, :c] + M[:, c:]

def sum_upper_lower( M ):
    s = M.shape[0] // 2
    return M[:s, :] + M[s:, :]

def sum_4_quadrants( M ):
    r = M.shape[0] // 2
    c = M.shape[1] // 2
    return M[:r, :c] + M[:r, c:] + M[r:, :c] + M[r:, c:]

def sum_4_cells( M ):
    return M[::2, ::2] + M[1::2, ::2] + M[::2, 1::2] + M[1::2, 1::2]

def count_leap_years( years ):
 # Years is array containing years in Buddhist Era (B.E.)
 years -= 543
 return np.sum( ((years % 4 == 0) & (years % 100 != 0)) | (years % 400 == 0) )

exec(input().strip())