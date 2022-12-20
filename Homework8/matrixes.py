#!/usr/bin/env python
# coding: utf-8

# In[4]:


import multiprocessing as mp
import time


def read_csv(path):
    csv_to_list = []
    with open(path) as my_data:
        for line in my_data:
            row_list = []
            for val in line.split(';'):
                val = int(val.strip())
                row_list.append(val)
            csv_to_list.append(row_list)
    return csv_to_list


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        print(time.time() - start_time)
        return res
    return wrapper


def empty_mat(cols_b, rows_a):
    return [[0 for row in range(cols_b)] for col in range(rows_a)]


def mult(el_a, el_b):
    return el_a * el_b


@time_decorator
def matmul(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])
    if cols_a != rows_b:
        print('wrong sizes')
    else:
        res = empty_mat(cols_b, rows_a)
        # fill zeros
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    res[i][j] += mult(a[i][k], b[k][j])

        tmp = list(map(str, res))
        s = '\n'.join([' '.join((l1, l2)) for l1, l2 in zip(tmp[::2], tmp[1::2])])
        print(s)


@time_decorator
def pro_matmul(a, b, n):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])
    if cols_a != rows_b:
        print('wrong sizes')
    else:
        res = empty_mat(cols_b, rows_a)

        with mp.Pool(n) as p:
            for i in range(rows_a):
                for j in range(cols_b):
                    for elem_mul in p.starmap(mult, zip(a[i], [row[j] for row in b])):
                        res[i][j] += elem_mul
    
        tmp = list(map(str, res))
        s = '\n'.join([' '.join((l1, l2)) for l1, l2 in zip(tmp[::2], tmp[1::2])])
        print(s)


if __name__ == "__main__":
    m1 = read_csv('./matrix_1.csv')
    m2 = read_csv('./matrix_2.csv')
    matmul(m1, m2)
    print('start pro')
    for n in (range(1, mp.cpu_count() + 1)):
        pro_matmul(m1, m2, n)


# In[ ]:




