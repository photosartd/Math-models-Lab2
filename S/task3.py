import numpy as np
#q_0 - размер накопителя
#q - оптимальный размер партии
p = 4
r = 2
C = 60
C_s = 3000
def task3(p, r, C, C_s, q_0 = None, if_print=True):
    if q_0 is None:
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
half_q_0 = task3(p,r,C,C_s, 5)
two_q_0 = task3(p,r,C,C_s, 20)