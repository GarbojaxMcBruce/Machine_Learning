import numpy as np
import random
from sklearn.neural_network import MLPRegressor as mlp

class Creature:
    name = ''
    status = 1
    dopamine = 0
    epsilon = 0
    lethal_sadness = -100
    super_happy = 200
    
    #This holds the creatures options at any given time
    mov_vec = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0],
                   [0, 1], [1, -1], [1, 0], [1, 1]]
    
    #This will be our value function approximator
    """REMOVE THIS FOR DEMO VERSION"""
    value_function = mlp(hidden_layer_sizes=(100,), max_iter=200,
                         shuffle=True, activation='relu',
                         learning_rate='adaptive')
    
    #These values will hold our experience information
    X = []
    y = []
    arr_X = np.ndarray(X)
    arr_y = np.ndarray(y)
    discount_factor = .9
    step_value = -1
    
    def __init__(self, name, step_value):
        self.name = name
        #self.value_function = brain,
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
    """REMOVE THIS FOR DEMO VERSION"""
    def move(self, positional_state):
        positional_state = self.process_positional_state(positional_state)
        
        r_vec = []
        for mov in self.mov_vec:
            x = np.array(positional_state + mov).reshape(1, -1)
            r_vec.append(self.value_function.predict(x))
            
        return self.mov_vec[r_vec.index(max(r_vec))]
    
    #Implement our learning move function
    """REMOVE THIS FOR DEMO VERSION"""
    def epsilon_greedy_move(self, positional_state):
        positional_state = self.process_positional_state(positional_state)
        
        if(random.random() < self.epsilon):
            return self.mov_vec[random.randint(0, len(self.mov_vec) - 1)]
        r_vec = []
        for mov in self.mov_vec:
            x = np.array(positional_state + mov).reshape(1, -1)
            r_vec.append(self.value_function.predict(x))
        return self.mov_vec[r_vec.index(max(r_vec))]
    
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
        
    #Processing our history
    """REMOVE THIS FOR DEMO VERSION"""
    def process_history(self):
        #Adding our discount factor to our reward history
        for idx in range(len(self.y)):
            a = 0
            for rem in range(idx, len(self.y)-1):
                self.y[idx] += self.y[rem] * self.discount_factor**a
                a += 1
                if(a > 40):
                    break
        
        self.arrX = np.array(self.X).reshape(len(self.X), len(self.X[0]))
        self.arry = np.array(self.y).reshape(len(self.y), )
    
    #learning from the experience we've gained
    """REMOVE THIS FOR DEMO VERSION"""
    def learn(self):
        self.process_history()
        self.value_function.partial_fit(self.arrX, self.arry)
        self.X = []
        self.y = []
        
    def adjust_epsilon(self, win_rate):
        self.epsilon =  .1 * (1 - win_rate)
    
    def get_random(self):
        return random.randint(0, 100)
