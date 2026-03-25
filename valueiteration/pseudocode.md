# valueiteration algorithm

## Parameters
- S: set of states
- A: set of actions
- P(s', s, a): probability transition function
- R(s, a): reward function
- threshold: stopping tolerance
- gamma: discount factor
- maxiters: maximum number of iterations

## Outputs
- π: optimal policy
- V: value function
- k: number of iterations
- V_hist: history of value function


```
# Checks
First, check the parameters are valid:
    gamma is between 0 and 1
    threshold must be positive
    S and A must not be empty

# Memoisation
Create memoised versions of P(s', s, a) and R(s, a) functions, P_cached and R_cached

# Setup
Create V and V_update dictionaries, starting with all states at zero
Create empty dictionary = π for policies  
Set k = 0 and delta = ∞ and V_hist = [V] to record starting values

# Main loop
While delta > threshold and k < maxiters:
    Reset delta = 0
    Increment K for next iteration

    For each state (s) in S:
        Set best value = -∞ and best action = None

        For each action (a) in A:
            Skip invalid actions (for terminal states, i.e. if all P_cached(s', s, a) = 0)
            Setup expected future value = 0 for the action-state pair 
            
            expected future value = sum over all available next states in S of P_cached(s', s, a) * V[s']

            value = R_cached(s, a) + gamma * expected future value
		
            If the current iteration value is greater than the best value:
                Update best value = value and best action = action

        If theres no valid action:
            V_update[s] = V[s]
        Else:
            V_update[s] = best value

        π[s] = best action

        Update delta = max(delta, |V_update[s] - V[s]|) 

    Replace V with V_update and add a copy of V to V_hist

If the number of max iterations is reached before convergence is reached:
    Print hint that max number of iterations was reached

Return π, V, k, V_hist
```
