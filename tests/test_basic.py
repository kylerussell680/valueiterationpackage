import pytest
from valueiteration import valueiteration

def test_valueiteration():
    S = ["A"]
    A = ["a"]

    def P(s_next, s, a): return 1.0
    def R(s, a): return 0.0

    pi, V, _, _ = valueiteration(S, A, P, R, 1e-6, 0.9)

    assert "A" in V
    
def test_maxiters():
    S = ["A"]
    A = ["a"]

    def P(s_next, s, a): return 1.0 if s == s_next == "A" else 0.0
    def R(s, a): return 1.0

    _, _, k, V_hist = valueiteration(S, A, P, R, threshold=1e-30, gamma=0.99, maxiters=3)

    assert k == 3
    assert len(V_hist) == 4

def test_best_a():
    S = ["A", "B"]
    A = ["a", "b"]

    def P(s_next, s, a):
        if s == "A" and a == "a" and s_next == "A":
            return 1.0
        if s == "A" and a == "b" and s_next == "B":
            return 1.0
        if s == "B" and a == "a" and s_next == "B":
            return 1.0
        if s == "B" and a == "b" and s_next == "B":
            return 1.0
        return 0.0

    def R(s, a):
        if s == "A" and a == "a":
            return 1.0
        if s == "A" and a == "b":
            return 2.0
        return 0.0

    pi, V, _, _ = valueiteration(S, A, P, R, threshold=1e-8, gamma=0.5)

    assert pi["A"] == "b"
    
    
def test_grid_world():
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

    def P(s_next, s, a):
        for i in results:
            if i[0] == s and i[1] == a and i[2] == s_next:
                return i[3]
        return 0.0
    
    def R(s, a):
        reward = 0.0
        for i in results:
            if i[0] == s and i[1] == a:
                reward += i[3] * i[4]
        return reward

    pi, V, k, V_hist = valueiteration(S, A, P, R, threshold=1e-6, gamma=0.9)

    assert pi["BR"] is None
    assert V["BR"] == 0.0