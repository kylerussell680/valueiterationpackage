import matplotlib.pyplot as plt
from valueiteration import valueiteration

# Example state and action space
S = ["A", "B", "C", "D"]
A = ["X", "Y", "Z"]

# Different representation of possible transitions and respective rewards
results = {
    ("A", "X"): [("B", 0.8, 2), ("C", 0.2, 1)],
    ("A", "Y"): [("C", 0.7, 1), ("A", 0.3, 0)],
    ("A", "Z"): [("D", 0.6, 1), ("B", 0.4, 2)],
    ("B", "X"): [("C", 0.9, 3), ("A", 0.1, 5)],
    ("B", "Y"): [("A", 0.6, 4), ("B", 0.4, 5)],
    ("B", "Z"): [("D", 0.7, 9), ("C", 0.3, 8)],
    ("C", "X"): [("A", 0.5, 14), ("B", 0.5, 12)],
    ("C", "Y"): [("B", 0.8, 20), ("C", 0.2, 14)],
    ("C", "Z"): [("D", 0.9, 6), ("A", 0.1, 8)],
    ("D", "X"): [("A", 0.6, 9), ("C", 0.4, 6)],
    ("D", "Y"): [("B", 0.7, 4), ("D", 0.3, 7)],
    ("D", "Z"): [("C", 0.8, 8), ("A", 0.2, 9)]}

# Function to collect the probabilities from the dictionaries for each respective transition
def P(s_next, s, a):
    for next_state, p, r in results.get((s, a),[]):
        if next_state == s_next:
            return p
    return 0.0

# Function to calculate the expected reward
def R(s, a):
    reward = 0
    for next_state, p, r in results.get((s, a),[]):
        reward += p*r
    return reward

# Use maxiters parameter to allow more iterations
pi, V, k, V_hist = valueiteration(S, A, P, R, threshold=1e-6, gamma=0.9, maxiters=200)

# Print results 
print("Converged after",k,"iterations")
print("V(A)=", V["A"])
print("V(B)=", V["B"])
print("V(C)=", V["C"])
print("V(D)=", V["D"])
print("pi(A)=", pi["A"])
print("pi(B)=", pi["B"])
print("pi(C)=", pi["C"])
print("pi(D)=", pi["D"])

for s in S:
    plt.plot([V[s] for V in V_hist], label=s)
    
# Plot results
plt.xlabel("Number of Iterations")
plt.ylabel("Value")
plt.grid()
plt.legend()
plt.show()