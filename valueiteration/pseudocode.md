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

## Changes from original Pseudocode 

This algorithm was develop from the start point of the [Figure 9.16](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.SS2.html) Figure 9.16 alghorithm with some significant changes to improve the performance, or to overcome the gaps in the pseudocode.

- Firstly, the pseudocode says to assign V0(s) arbitrarily, I choose zeros as its an easy startpoint and also should help to show the convergence nicely. 

- Next, the pseudocode stores the sequence of value fucntions in Line 11, I do this differently by using two dictionaries, V and V_update, as this is the synchronous version, I didnt want to update the value of the V in the loop as that would make it asynchronous, V holds the previous iterations value functions and V_update holds the new iterations value functions and then it is switched at the end of the iteration so that the values are stored for the next iteration. 

- Next is the termination, the pseudocode leaves this ambiguous to how to do this, but I believe the best way to do this is to use the max change between iterations and then once this falls below a threshold, termiate, so that the algorithm has sufficiently converged and further iterations provide negligible convergence, it was also important to me to make this adaptable and therefore this threshold can be altered as a parameter, as different setups may require far more or less convergence and hence differing levels of computational complexity. In addition, to avoid very long algorithms, there is also a termination if the number of iterations goes above a maxiters threshold, therefore stoppping the algorithm and returning the values at that iteration.

- Next, the pseudocode calculates the best policy in an entirely seperate loop, I thought that wasnt really necessary as the best action was already being calculated as part of the loop and to save some computational power. 

- Moreover, I used memoisation in the code to cache the transition probability and the reward functions to avoid repeated calculations.

- Using map allowed me to calculate the expected value from future states, instead of using a 'for' loop.
 
- Next, I used an additional check for the terminal states as I found it necessary to be able to detect them and output the correct response, as before they would just return the first state, therfore I added a check to see if the states have all zero transition probabilities and could then classify them as terminal states. 

- Moreover, the final major addition was the additional parameters and outputs, I have already mentioned threshold, however gamma is an important addition as to represent differing levels of long-run/short-run value, I also added k and V_hist as outputs to be able to help visualise and understand the convergence better, as to know how many iterations and how that tracks with the value function.

## Notes

My implementation of the algorithm assumes a finite MDP with well defined transition probabilities, except for terminal states.

When it comes to the representation of the inputs, In my code, the states and actions could be represented as either strings, tuples or integers with minor changes to the MDP formulation. In addition, delta is set to be arbitrarily large for the first iteration to ensure that at least two iteration occurs. The threshold parameter effectively defines the termination criterion, and offers a balance between computational complexity and accuracy, smaller values allow for greater precision at the cost of more complexity, and vice versa. To counteract this, maxiters stops significantly large runtimes.


When it comes to the use of functional patterns decribed on the course, I have not included too many, this was firstly because when making the code I wanted to keep the code easy to understand to begin with. In addition, from the patterns mentioned on the course, a few are possible, such as filter for the terminal states, reduce and partial application could be used in some way fro the expected value, however I chose only to use memoisation and map, as I found them the most useful when starting from already working code. In regards to the other fucntional patterns, I didnt find a place where they would be appropriate that would vastly improve the code, and possibly only disadvantaged the readability of the code. 
  
