import matplotlib.pyplot as plt
from valueiteration import valueiteration

# Initialise the table and available actions and states
S = ["TL", "TR", "BL", "BR"]
A = ["U", "D", "L", "R"]
results = [
    ["TL", "R", "TR", 0.9, -1],
    ["TL", "R", "BL", 0.1, -2],
    ["TL", "D", "BL", 0.9, -2],
    ["TL", "D", "TR", 0.1, -1],
    ["TR", "L", "TL", 0.9, -1.5],
    ["TR", "L", "BR", 0.1, 10],
    ["TR", "D", "BR", 0.8, 15],
    ["TR", "D", "TL", 0.2, -1],
    ["BL", "R", "BR", 0.9, 20],
    ["BL", "R", "TL", 0.1, -2.5],
    ["BL", "U", "TL", 0.8, -0.5],
    ["BL", "U", "BR", 0.2, 5]]

# Access transition probabilty taken from table, as a function 
def P(s_next, s, a):
    for i in results:
        if i[0] == s and i[1] == a and i[2] == s_next:
            return i[3]
    return 0.0

# Access rewards from the table and calculate expected reward, as a function
def R(s, a):
    reward = 0
    for i in results:
        if i[0] == s and i[1] == a:
            reward += i[3]*i[4]
    return reward

pi, V, k, V_hist = valueiteration(S, A, P, R, threshold=1e-6, gamma=0.9)

# Prints the end results for policy and value
print("V(TL)=", V["TL"])
print("V(TR)=", V["TR"])
print("V(BL)=", V["BL"])
print("V(BR)=", V["BR"])
print("pi(TL)=", pi["TL"])
print("pi(TR)=", pi["TR"])
print("pi(BL)=", pi["BL"])
print("pi(BR)=", pi["BR"])

for s in S:
    plt.plot([V[s] for V in V_hist], label=s)

# Plot the results
plt.xlabel("Number of Iterations")
plt.ylabel("Value")
plt.grid()
plt.legend()
plt.show()