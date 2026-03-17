import numpy as np
import matplotlib.pyplot as plt
from valueiteration import valueiteration

TL, TR, BL, BR = 0, 1, 2, 3
S = [TL, TR, BL, BR]
A = ["U", "D", "L", "R"]

transition_table = [
    [TL, "R", TR, 0.9, -1],
    [TL, "R", BL, 0.1, -2],
    [TL, "D", BL, 0.9, -2],
    [TL, "D", TR, 0.1, -1],
    [TR, "L", TL, 0.9, -1.5],
    [TR, "L", BR, 0.1, 10],
    [TR, "D", BR, 0.8, 15],
    [TR, "D", TL, 0.2, -1],
    [BL, "R", BR, 0.9, 20],
    [BL, "R", TL, 0.1, -2.5],
    [BL, "U", TL, 0.8, -0.5],
    [BL, "U", BR, 0.2, 5]]

def P(s_next, s, a):
    for i in transition_table:
        if i[0] == s and i[1] == a and i[2] == s_next:
            return i[3]
    return 0

def R(s, a):
    reward = 0
    for i in transition_table:
        if i[0] == s and i[1] == a:
            reward += i[3]*i[4]
    return reward

pi, V, k, v_hist = valueiteration(S, A, P, R, threshold=1e-6, gamma=0.9)
v_hist = np.array(v_hist)

print("V(TL)=", V[TL])
print("V(TR)=", V[TR])
print("V(BL)=", V[BL])
print("V(BR)=", V[BR])
print("pi(TL)=", pi[TL])
print("pi(TR)=", pi[TR])
print("pi(BL)=", pi[BL])
print("pi(BR)=", pi[BR])

plt.plot(v_hist[:, TL], label="TL")
plt.plot(v_hist[:, TR], label="TR")
plt.plot(v_hist[:, BL], label="BL")
plt.plot(v_hist[:, BR], label="BR")
plt.xlabel("k")
plt.ylabel("value")
plt.legend()
plt.grid()
plt.show()