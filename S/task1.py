from math import sqrt

print('Задача 1 в задаче 1:\n')
def task1(R, T, C_1, C_s, q_0=None, if_print=True):
    if q_0 is None:
        q_0 = round(sqrt(2*R*C_s/(T*C_1)), 5)
        t_so = round(T*q_0/R, 5)
        D = round(C_1*T*q_0/2 + C_s*R/q_0, 5)
    else:
        t_so = round(T*q_0/R, 5)
        D = round(C_1*T*q_0/2 + C_s*R/q_0, 5)
    
    if if_print:
        print(f'\
        q_0 = {q_0}\
        t_s0 = {t_so}\
        D = {D}\
        ')
    return (q_0, t_so, D)

R = 330
T = 110
C_1 = 10
C_s = 60
optimal = task1(R, T, C_1, C_s)

half_q_0 = task1(R, T, C_1, C_s, optimal[0]/2)
two_q_0 = task1(R, T, C_1, C_s, optimal[0]*2)

print('Задача 2 в задаче 1: \n')
def task2(R, T, C_1, C_2, C_s, s_0=None, t_s0=None, t_1=None, t_2=None, if_print=True):
    if s_0 is None:
        q_0 = round(sqrt(2*C_s*R/(C_1*T)) * sqrt((C_1+C_2)/C_2),8)
        t_s0 = round(sqrt((2*T*C_s)/(R*C_1)) * sqrt((C_1 + C_2)/C_2),8)
        s_0 = round(sqrt((2*C_s*R)/(C_1*T)) * sqrt(C_2/(C_1 + C_2)),8)
        D = round((s_0**2 * C_1 * T)/(2*q_0) + (q_0-s_0)**2 * C_2 * T/(2*q_0) + C_s*R/q_0,8)
        t_1 = round(s_0/q_0 * t_s0, 8)
        t_2 = t_s0 - t_1
    else:
        q_0 = round(s_0/t_1*t_s0, 8)
        D = round((s_0**2 * C_1 * T)/(2*q_0) + (q_0-s_0)**2 * C_2 * T/(2*q_0) + C_s*R/q_0,8)

    if if_print:
       print(f'\
        q_0 = {q_0}\
        t_s0 = {t_s0}\
        t_1 = {t_1}\
        t_2 = {t_2}\
        s_0 = {s_0}\
        D = {D}\
        ')
    return (q_0, t_s0, t_1, t_2, s_0, D)

R = 760
T = 190
C_1 = 16
C_2 = 64
C_s = 8122
optimum_s2 = task2(R, T, C_1, C_2, C_s)
half_s2 = task2(R,T,C_1,C_2,C_s, optimum_s2[4]/2, optimum_s2[1], optimum_s2[2], optimum_s2[3])
two_s2 =  task2(R,T,C_1,C_2,C_s, optimum_s2[4]*2, optimum_s2[1], optimum_s2[2], optimum_s2[3])