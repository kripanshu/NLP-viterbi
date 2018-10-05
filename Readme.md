Author : Kripanshu Bhargava
NetId : kxb162030
---
The folder should contain:
1. CS 6320 Natural Language Processing.pdf
2. Readme.md
3. viterbi.py
---
**To run the program**
`python Viterbi.py <sequence>`
---
**Sample Output**
Kripanshu-Mac:homework3_kxb162030 kripanshubhargava$ python3 viterbi.py "DDNNCCDND"
state space  ['H', 'F']
observation space  ['N', 'C', 'D']
initial probabilities  {'H': 0.6, 'F': 0.4}
sequence of observations  ['D', 'D', 'N', 'N', 'C', 'C', 'D', 'N', 'D']
transition matrix A {'H': {'H': 0.7, 'F': 0.3}, 'F': {'H': 0.5, 'F': 0.5}}
emission matrix B {'H': {'N': 0.1, 'C': 0.4, 'D': 0.5}, 'F': {'N': 0.6, 'C': 0.3, 'D': 0.1}}
------------------------------ viterbi states and observations ------------------------------
H: Healthy, F: Fever | C: Cold, D: Dizzy, N: Normal
--------------------------------------------- viterbi output ---------------------------------------------
Probability : 5.000939999999999e-06
State :  HHFFHHHFH
---
