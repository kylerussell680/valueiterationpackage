import matplotlib.pyplot as plt
from valueiteration import valueiteration

# Initialise the table and available actions and states
S = ["healthy", "sick"]
A = ["relax", "party"]
results = [
    ["healthy", "relax", "healthy", 0.95, 7],
    ["healthy", "relax", "sick", 0.05, 7],
    ["healthy", "party", "healthy", 0.70, 10],
    ["healthy", "party", "sick", 0.30, 10],
    ["sick", "relax", "healthy", 0.50, 0],
    ["sick", "relax", "sick", 0.50, 0],
    ["sick", "party", "healthy", 0.10, 2],
    ["sick", "party", "sick", 0.90, 2]]

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

# Run value iteration
pi, V, k, V_hist = valueiteration(S, A, P, R, threshold=1e-6, gamma=0.9, maxiters=1000)

print("V(healthy)=", V["healthy"])
print("V(sick)=", V["sick"])
print("pi(healthy)=", pi["healthy"])
print("pi(sick)=", pi["sick"])

for s in S:
    plt.plot([V[s] for V in V_hist], label=s)

# Plot the results
plt.xlabel("Number of Iterations")
plt.ylabel("Value")
plt.grid()
plt.legend()
plt.show()