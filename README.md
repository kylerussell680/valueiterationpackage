# Value Iteration Algorithm for Markov Decision Processes

A Python package for implementing the synchronous value iteration algorithm for use with Markov decision processes.

## Installation

Install from GitHub:

  ```bash
  pip install git+https://github.com/kylerussell680/value_iteration.git
  ```
  
## Tests

To run the unit tests:

  ```bash
  python -m pytest
  ```
  
## Parameters

S - list of possible states

A - list of possible actions

P - transition probability function

R - reward function

threshold - convergence threshold, iterations stop when difference between subsequent iterations falls below this

gamma - discount factor between 0.0 and 1.0

maxiters - maximum number of iterations before terminating the algorithm.

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

This algorithm was develop from the start point of the [Figure 9.16](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.SS2.html) alghorithm with some significant changes to improve the performance, or to overcome the gaps in the pseudocode.

See /examples for 3 more detailed examples with more advanced setups, including; the Grid World Problem, Example 1 is a madeup example with a slightly different formulation of problem and Example 2 highlights the package usage for exercise [9.27](https://artint.info/2e/html2e/ArtInt2e.Ch9.S5.html#Ch9.Thmciexamplered27).


## Repository

Source files and examples for this package can be found in the GitHub repository:

```
https://github.com/kylerussell680/value_iteration
```


## References

Poole, D.L. and Mackworth, A.K., 2010. Artificial Intelligence: foundations of computational agents. Cambridge University Press.
