import numpy as np
#q_0 - размер накопителя
#q - оптимальный размер партии
p = 44
r = 11
C = 80
C_s = 1100
def task3(p, r, C, C_s, if_print=True):
    q_0 = np.sqrt((2*C_s*r*(p-r))/(C*p))
    t_1 = q_0/(p-r)
    t_2 = p/r*t_1
    t_s = q_0/r + q_0/(p-r)
    q = r*t_2
    D = (C*q_0*t_s/2 + C_s)
    if if_print:
        print(f'\
            q_0 = {q_0}\
            q = {q}\
            t_1 = {t_1}\
            t_2 = {t_2}\
            t_s = {t_s}\
            D = {D}\
        ')
    return (q_0, q, t_1, t_2, t_s, D)

optimum = task3(p,r,C,C_s)