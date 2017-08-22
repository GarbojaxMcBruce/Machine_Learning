import random

class Environment:
    name = ''
    hunter = ''
    hunter_position = [0,0]
    creature = ''
    creature_position = [0,0]
    food_position = [0,0]
    food_value = 100
    size = 10
    
    #Whether the game is in process or over
    game_state = 1
    
    def __init__(self, name, size, creature, hunter):
        self.name = name
        self.size = size
        self.creature = creature
        self.hunter = hunter
        self.game_state = 1
        
        self.food_position = [random.randint(0, self.size - 1), 
                              random.randint(0, self.size - 1)]
        
        self.hunter_position = [random.randint(0, self.size - 1),
                               random.randint(0, self.size - 1)]
        
        self.creature_position = [random.randint(0, self.size - 1), 
                                  random.randint(0, self.size - 1)]
        
    #Resets the playing field, but not the creatures brain
    def reset(self):
        self.creature.reset_life()
        self.game_state = 1
        
        self.food_position = [random.randint(0, self.size - 1), 
                              random.randint(0, self.size - 1)]
        
        self.hunter_position = [random.randint(0, self.size - 1),
                               random.randint(0, self.size - 1)]
        
        self.creature_position = [random.randint(0, self.size - 1), 
                                  random.randint(0, self.size - 1)]
        
    #Returns the present location of creature, hunter, and food as an array
    def get_position_state(self):
        position_state = (self.creature_position + self.hunter_position + 
                          self.food_position)
        return position_state
    
    #Will process reward for this step
    def calculate_reward(self):
        reward = self.creature.step_value
        if(self.food_position == self.creature_position):
            reward += self.food_value
            self.food_position = [random.randint(0, self.size - 1),
                                  random.randint(0, self.size - 1)]
        if(self.creature_position == self.hunter_position):
            reward += self.hunter.value
        return reward
    
    def update_game_state(self):
        if(self.creature.status != 1):
            self.game_state = 0
    
    #Moves a given item, i.e. hunter or creature
    def move_item(self, new_pos):
        if(new_pos[0] > self.size - 1):
            new_pos[0] = self.size - 1
        if(new_pos[0] < 0):
            new_pos[0] = 0
        if(new_pos[1] > self.size - 1):
            new_pos[1] = self.size - 1
        if(new_pos[1] < 0):
            new_pos[1] = 0
        return new_pos
    
    #Update one time step, just for testing
    def itteration(self):
        initial_position_state = self.get_position_state()
        #creature moves
        creature_move = self.creature.move(initial_position_state)
        self.creature_position = self.move_item(
                [sum(pos) for pos in zip(creature_move, self.creature_position)]
                )
        
        #hunter moves
        hunter_move = self.hunter.auto_move()
        self.hunter_position = self.move_item(
                [sum(pos) for pos in zip(hunter_move, self.hunter_position)]
                )
        
        #check reward
        reward = self.calculate_reward()
        self.creature.get_reward(reward)
        
        #update state of game
        self.update_game_state()
        
    #Updates one time step, passes State Action Reward info to creature for 
    #learning
    def learning_itteration(self):
        #Get present positional state
        initial_position_state = self.get_position_state()
        
        #creature move, this will also be our action: q
        creature_move = self.creature.epsilon_greedy_move(initial_position_state)
        self.creature_position = self.move_item(
                [sum(pos) for pos in zip(creature_move, self.creature_position)]
                )
        
        #hunter move
        hunter_move = self.hunter.auto_move()
        self.hunter_position = self.move_item(
                [sum(pos) for pos in zip(hunter_move, self.hunter_position)]
                )
        #check reward
        reward = self.calculate_reward()
        self.creature.get_reward(reward)
        
        #send history information to creature
        X = initial_position_state + creature_move
        y = reward
        self.creature.absorb_experience(X, y)
        
        #Update game state
        self.update_game_state()
        
    #For doing random walks
    def watching_itteration(self):
        #Get present positional state
        initial_position_state = self.get_position_state()
        
        #creature move, this will also be our action: q
        creature_move = self.creature.random_move()
        self.creature_position = self.move_item(
                [sum(pos) for pos in zip(creature_move, self.creature_position)]
                )
        
        #hunter move
        hunter_move = self.hunter.auto_move()
        self.hunter_position = self.move_item(
                [sum(pos) for pos in zip(hunter_move, self.hunter_position)]
                )
        #check reward
        reward = self.calculate_reward()
        self.creature.get_reward(reward)
        
        #send history information to creature
        X = initial_position_state + creature_move
        y = reward
        self.creature.absorb_experience(X, y)
        
        #Update game state
        self.update_game_state()
        pass
        
        
    #Prints the environment to the console so we can visualize it
    def print_space(self):
        print('{}\n\n'.format(self.name + ' space:'))
        for i in range(0, self.size):
            for j in range(0, self.size):
                if(i == self.creature_position[0] and 
                   j == self.creature_position[1]):
                    print('C ', end = '')
                elif(i == self.food_position[0] and 
                     j == self.food_position[1]):
                    print('F ', end = '')
                elif(i == self.hunter_position[0] and
                     j == self.hunter_position[1]):
                    print('H ', end = '')
                else:
                    print('_ ', end = '')
            print('\n')
            