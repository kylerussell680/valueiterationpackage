import pytest
from valueiteration import valueiteration

def test_valueiteration():
    S = ["A"]
    A = ["a"]

    def P(s_next, s, a): return 1.0
    def R(s, a): return 0.0

    pi, V, k, V_hist = valueiteration(S, A, P, R, 1e-6, 0.9)

    assert "A" in V
    assert "A" in V_hist[0]
    assert "A" in V_hist[-1]
    assert len(V_hist) == k + 1
    assert pi["A"] == "a"
    assert V["A"] == 0.0
    
def test_maxiters():
    S = ["A"]
    A = ["a"]

    def P(s_next, s, a): return 1.0
    def R(s, a): return 1.0

    _, _, k, V_hist = valueiteration(S, A, P, R, threshold=1e-50, gamma=0.99, maxiters=3)

    assert k == 3
    assert len(V_hist) == 4

def test_gamma():
    S = ["A"]
    A = ["a"]

    def P(s_next, s, a): return 1.0
    def R(s, a): return 0.0

    with pytest.raises(ValueError):
        valueiteration(S, A, P, R, 1e-6, 0.0)

    with pytest.raises(ValueError):
        valueiteration(S, A, P, R, 1e-6, 1.0)

def test_threshold():
    S = ["A"]
    A = ["a"]

    def P(s_next, s, a): return 1.0
    def R(s, a): return 0.0

    with pytest.raises(ValueError):
        valueiteration(S, A, P, R, 0.0, 0.9)
        
def test_states():
    A = ["a"]

    def P(s_next, s, a): return 0.0
    def R(s, a): return 0.0

    with pytest.raises(ValueError):
        valueiteration([], A, P, R, 1e-6, 0.9)

def test_empty_actions():
    S = ["A"]

    def P(s_next, s, a): return 0.0
    def R(s, a): return 0.0

    with pytest.raises(ValueError):
        valueiteration(S, [], P, R, 1e-6, 0.9)
        
def test_best_a():
    S = ["A", "B"]
    A = ["a", "b"]

    results = [
        ["A", "a", "A", 1.0, 1.0],
        ["A", "b", "B", 1.0, 2.01],
        ["B", "a", "B", 1.0, 0.0],
        ["B", "b", "B", 1.0, 0.0]]

    def P(s_next, s, a):
        for i in results:
            if i[0] == s and i[1] == a and i[2] == s_next:
                return i[3]
        return 0.0
    
    def R(s, a):
        reward = 0
        for i in results:
            if i[0] == s and i[1] == a:
                reward += i[3]*i[4]
        return reward

    pi, V, _, _ = valueiteration(S, A, P, R, threshold=1e-6, gamma=0.5)

    assert pi["A"] == "b"
    assert pi["B"] in A
    assert V["A"] == 2.01
    assert V["B"] == 0.0
    
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
        reward = 0
        for i in results:
            if i[0] == s and i[1] == a:
                reward += i[3]*i[4]
        return reward

    pi, V, k, V_hist = valueiteration(S, A, P, R, threshold=1e-6, gamma=0.9)
    
    assert pi["TL"] is not None
    assert pi["TR"] is not None
    assert pi["BL"] is not None
    assert pi["BR"] is None
    assert V["BR"] == 0.0
