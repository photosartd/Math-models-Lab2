import numpy as np
round_to = 5
r = np.array([11,16,5])
C_1 = np.array([40,38,22])
C_s = 28371
T = 42
def task2(r, C_1, C_s, T, t_s=None, if_print=True):
    if t_s is None:
        t_s = round(np.sqrt((2*C_s)/sum(C_1*r)), round_to)
        q = r*t_s
        D = round(sum(C_1*r)*t_s*T/2 + C_s*T/t_s, round_to)
    else:
        q = r*t_s
        D = round(sum(C_1*r)*t_s*T/2 + C_s*T/t_s, round_to)
    if if_print:
        print(f'\
            t_s = {t_s}\
            q_i = {q}\
            D = {D}\
        ')
    return (t_s, q, D)

optimum = task2(r, C_1, C_s, T)
half_ts = task2(r,C_1, C_s,T, t_s=3.5)
two_ts = task2(r,C_1, C_s,T, t_s=14)