import numpy as np
import random
from sklearn.neural_network import MLPRegressor as mlp

class Creature:
    name = ''
    #Is our agent alive, dead, or in victory? 
    status = 1
    
    #Keeps track of total reward, also used for status
    dopamine = 0
    
    #This is for the exploration vs exploitation piece of things
    epsilon = 0
    
    #How sad our AI needs to be to lose
    lethal_sadness = -100
    
    #How happy our AI needs to be to win
    super_happy = 500
    
    #This holds the creatures options at any given time
    mov_vec = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0],
                   [0, 1], [1, -1], [1, 0], [1, 1]]
    
    #This will be our value function approximator
    value_function = """We will work through this part together"""
    
    #These values will hold our experience information
    X = []
    y = []
    arr_X = np.ndarray(X)
    arr_y = np.ndarray(y)
    
    #How valueable is the present vs the future?
    discount_factor = .9
    
    #Reward per time step, (-) value indicates punishment
    step_value = -1
    
    def __init__(self, name, step_value):
        self.name = name
        self.step_value = step_value
        
    def reset_life(self):
        self.status = 1
        self.dopamine = 0
        
    def check_status(self):
        if(self.dopamine < self.lethal_sadness):
            self.status = 0
        elif(self.dopamine > self.super_happy):
            self.status = 2
        else:
            self.status = 1

    def random_move(self):
        return [random.randint(-1, 1), random.randint(-1, 1)]
    
    #Implement our actual move function here
    def move(self, positional_state):
        """We will work throught this part together"""
    
    #Implement our learning move function
    """REMOVE THIS FOR DEMO VERSION"""
    def epsilon_greedy_move(self, positional_state):
        """We will work through this part together"""
    
    def get_reward(self, reward):
        self.dopamine += reward
        self.check_status()
        
    #Process experience to form our features
    def process_experience(self, experience):
        c = [experience[0], experience[1]]
        h = [experience[2], experience[3]]
        f = [experience[4], experience[5]]
        X = [
               np.sign(c[0] - h[0]) /  (1 + abs(c[0] - h[0])),
               np.sign(c[1] - h[1]) /  (1 + abs(c[1] - h[1])),
               np.sign(c[0] - f[0]) /  (1 + abs(c[0] - f[0])),
               np.sign(c[1] - f[1]) /  (1 + abs(c[1] - f[1])),
               experience[6],
               experience[7]
              ]
        return X
    
    def process_positional_state(self, positional_state):
        c = [positional_state[0], positional_state[1]]
        h = [positional_state[2], positional_state[3]]
        f = [positional_state[4], positional_state[5]]
        sensors = [
               np.sign(c[0] - h[0]) /  (1 + abs(c[0] - h[0])),
               np.sign(c[1] - h[1]) /  (1 + abs(c[1] - h[1])),
               np.sign(c[0] - f[0]) /  (1 + abs(c[0] - f[0])),
               np.sign(c[1] - f[1]) /  (1 + abs(c[1] - f[1])),
              ]
        return sensors
        
    #Absorb the states the environment gives us into our memory
    def absorb_experience(self, X, y):
        X = self.process_experience(X)
        self.X.append(X)
        self.y.append(y)
        
    #Processing our history, add discount factor
    def process_history(self):
        """We will work through this part together"""
    
    #learning from the experience we've gained
    def learn(self):
        """We will work through this together"""
        
    def adjust_epsilon(self, win_rate):
        self.epsilon =  .1 * (1 - win_rate)
    
