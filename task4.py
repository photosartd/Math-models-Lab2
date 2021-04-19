import numpy as np
price_0 = 183
fine_0 = 3970
probs_0 = [0.94, 0.04, 0.01, 0.01, 0, 0]

price_1 = 194
fine_1 = 3350
probs_1 = [0.94, 0.05, 0.01, 0, 0, 0]
def task4(price, fine, probs):
    Q_s = []
    for s in range(len(probs)):
        sum1 = 0
        sum2 = 0
        for r in range(s + 1):
            sum1 += price*(s-r)*probs[r]
        for r in range(s+1, len(probs)):
            sum2 += fine*(r-s)*probs[r]
        Q_s.append(sum1+sum2)
    return Q_s

details_0 = task4(price_0, fine_0, probs_0)
print(details_0)
details_1 = task4(price_1, fine_1, probs_1)
print(details_1)