import sys
import numpy as np
obs_string = sys.argv[1]
class ViterbiProgram(object):
    def __init__(self, observation_array):
        """The initalization of the required HMM model"""
        self.o1 = "Normal"
        self.o2 = "Cold"
        self.o3 = "Dizzy"
        self.O = ["N", "C","D"]
        self.seq_obs = observation_array # observation space
        self.s1 = "Healthy"
        self.s2 = "Fever"
        self.S = ["H","F"] # state space
        self.pie = {'H':0.6, 'F': 0.4 }# initial probabilities pie[0]=Healthy pie[1]= Fever
        # transition matrix A
        self.A ={
        'H': {'H':0.7, 'F':0.3},
        'F': {'H':0.5, 'F':0.5},
            }
        # emission matrix B
        self.B = {
        'H':{'N':0.1,'C':0.4,'D':0.5},
        'F':{'N':0.6,'C':0.3,'D':0.1}
        }
        # self.display()
        print(self.viterbi_cal(self.S,self.seq_obs,self.pie,self.A,self.B))
    def display(self):
        print("state space ", self.S)
        print("observation space ", self.O)
        print("initial probabilities ", self.pie)
        print("sequence of observations ", self.seq_obs)
        print("transition matrix A", self.A)
        print("emission matrix B", self.B)

    def viterbi_cal(self,S,seq_obs, pie, A, B):

        trellis = [{}]
        path = {}

        for state in S:
            trellis[0][state] = pie[state] * B[state][seq_obs[0]]
            path[state] = [state]
        for i in range(1,len(seq_obs)):
            # Add a new path for the added step in the sequence.
            trellis.append({})
            new_path = {}
            # For each possible state,
            for j in S:
                (probability, possible_state) = max([(trellis[i-1][k] * A[k][j]* B[j][seq_obs[i]], k) for k in S])
                # print(probability)
                # print("#"*4)
                # print(possible_state)
                # print("--"*4)
                # Add the probability of the state occuring at this step of the sequence to the trellis.
                trellis[i][j] = probability
                # Add the state to the current path
                new_path[j] = path[possible_state] + [j]

            path = new_path

        (probability, state) = max([(trellis[len(seq_obs) - 1][state], state) for state in S])
        # The most probable path, and its probability.
        return (probability, path[state])


if __name__ == '__main__':
    # creates an instance of the class
    observation_array = list(obs_string);
    viterb_obj = ViterbiProgram(observation_array)
