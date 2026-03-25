# Value Iteration Algorithm for Markov Decision Processes

A python package for implementing the synchronous value iteration algorithm for use with Markov decision processes.

## Installation

Install from Github:

  ```bash
  pip install git+https://github.com/kylerussell680/value_iteration.git
  ```
## Parameters

S - list of possible states

A - list of possible actions

P - function outputting the probability of transition to s' from s because of a P(s',s,a)

R - function outputting the expected reward for taking action a in state s R(s,a)

threshold - convergence threshold, iterations stop when difference between subsequent iterations is less than this

gamma - discount factor between 0.0 and 1.0

maxiters - maximum number of iterations before terminating algorithm.

## Outputs

pi - optimal policy

V - value function, optimal expected value return

k - number of iterations

V_hist - history of value function over iterations

## Dependencies

Python >= 3.7

## Example Usage
```
from valueiteration import valueiteration

S = ["A", "B"]
A = ["a", "b"]

def P(s_next, s, a): return 1.0 if s_next == s else 0.0
    
def R(s, a): return 1.0
    
pi, V, k, V_hist = valueiteration(S, A, P, R, threshold=1e-6, gamma=0.9, maxiters=1000)

print("Final Policy:", pi)
print("Final Value Dictionary:", V)
print("Iterations Required:", k)
print("Value History:", V_hist)
```

## Overview

This algorithm was develop from the start point of the [****](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.SS2.html) Figure 9.16 alghorithm with some significant changes to improve the performance, or to overcome the gaps in the pseudocode.

-Firstly, the pseudocode says to assign V0(s) arbitrarily, I choose zeros as its an easy startpoint and also should help to show the convergence nicely. 

-Next, the pseudocode stores the sequence of value fucntions in Line 11, I do this differently by using two dictionaries, V and V_update, as this is the synchronous version, I didnt want to update the value of the V in the loop as that would make it asynchronous, V holds the previous iterations value functions and V_update holds the new iterations value functions and then it is switched at the end of the iteration so that the values are stored for the next iteration. 

-Next is the termination, the pseudocode leaves this ambiguous to how to do this, but I believe the best way to do this is to use the max change between iterations and then once this falls below a threshold, termiate, so that the algorithm has sufficiently converged and further iterations provide negligible convergence, it was also important to me to make this adaptable and therefore this threshold can be altered as a parameter, as different setups may require far more or less convergence and hence differing levels of computational complexity. In addition, to avoid very long algorithms, there is also a termination if the number of iterations goes above a maxiters threshold, therefore stoppping the algorithm and returning the values at that iteration.

-Next, the pseudocode calculates the best policy in an entirely seperate loop, I thought that wasnt really necessary as the best action was already being calculated as part of the loop and to save some computational power. 

-Next, I used an additional check for the terminal states as I found it necessary to be able to detect them and output the correct response, as before they would just return the first state, therfore I added a check to see if the states have all zero transition probabilities and could then classify them as terminal states. 

-Moreover, the final major addition was the additional parameters and outputs, I have already mentioned threshold, however gamma is an important addition as to represent differing levels of long-run/short-run value, I also added k and V_hist as outputs to be able to help visualise and understand the convergence better, as to know how many iterations and how that tracks with the value function.

When it comes to the representation of the inputs, In my code, the states and actions could be represented as either strings, tuples or integers with minor changes to the MDP formulation. In addition, delta is set to be arbitrarily large for the first iteration to ensure that at least two iteration occurs.

