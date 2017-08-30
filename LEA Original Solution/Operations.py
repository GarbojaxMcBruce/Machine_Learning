import Environment as env
import Creature as cre
import Hunter as hunt
import time
import pickle



#One run through of the life of our creature, no learning
def trial(environment):
    environment.reset()
    max_count = 100
    while(environment.game_state == 1 and max_count > 0):
        max_count += 1
        environment.itteration()
    environment.reset()
    
def trial_keep_vals(environment):
    environment.reset()
    max_count = 100
    while(environment.game_state == 1 and max_count > 0):
        max_count += 1
        environment.itteration()
    
#A trial for our creature where we get to see whats going on
def interactive_trial(environment):
    environment.reset()
    max_count = 100
    environment.print_space()
    print('Press Enter to continue....')
    input()
    while(environment.game_state == 1 and max_count > 0):
        max_count -= 1
        environment.itteration()
        environment.print_space()
        print('Press Enter to continue....')
        input()

#One run through of life of creature, learning by experience
def learning_trial(environment):
    environment.reset()
    max_count = 100
    while(environment.game_state == 1 and max_count > 0):
        max_count += 1
        environment.learning_itteration()
    environment.reset()
        
#One run through of life of creature, random walk learning
def watching_trial(environment):
    environment.reset()
    max_count = 100
    while(environment.game_state == 1 and max_count > 0):
        max_count += 1
        environment.watching_itteration()
    environment.reset()
    

#Here the creature will learn primarily by 'watching'
#we are just doing a random walk here
def creature_lesson(environment, itts, batch_size):
    for itt in range(itts):
        watching_trial(environment)
        if((itt % batch_size) == (batch_size - 1)):
            print('Session {}'.format(itt + 1))
            environment.creature.learn()
#            win_percentage = test_creature(environment, 50)
#            print('\twin ratio: {}'.format(win_percentage))
            
def creature_lesson_quiet(environment, itts, batch_size):
    for itt in range(itts):
        watching_trial(environment)
        if((itt % batch_size) == (batch_size - 1)):
            environment.creature.learn()

#Here the creature will learn by trying out what it knows in the
#environment
def creature_practice(environment, itts, batch_size):
    for itt in range(itts):
        learning_trial(environment)
        if((itt % batch_size) == (batch_size - 1)):
            print('Session {}'.format(itt + 1))
            environment.creature.learn()
            win_percentage = test_creature(environment, 50)
            print('\twin ratio: {}'.format(win_percentage))
            
def creature_practice_quiet(environment, itts, batch_size):
    for itt in range(itts):
        learning_trial(environment)
        if((itt % batch_size) == (batch_size - 1)):
            environment.creature.learn()
            
def train_to_win(environment, lessons, batch_size, win_percentage,
                 max_trials):
    start = time.time()
    creature_lesson(environment, lessons, batch_size)
    environment.creature.adjust_epsilon(test_creature(environment, 10))
    win = 0
    counter = 0
    while(win < win_percentage and counter < max_trials):
        counter += 1
        for itt in range(batch_size):
            learning_trial(environment)
        environment.creature.learn()
        win = test_creature(environment, 50)
        environment.creature.adjust_epsilon(win)
        print('End session {}'.format(counter))
        print('\twin rate: {}'.format(win))
    end = time.time()
    success = 'success' if win > win_percentage else 'failure'
    print('Total time taken was: {}'.format(end - start))
    print('The operation was a {}'.format(success))
    
def train_to_win_quiet(environment, lessons, batch_size, win_percentage,
                 max_trials):
    creature_lesson_quiet(environment, lessons, batch_size)
    environment.creature.adjust_epsilon(test_creature(environment, 10))
    win = 0
    while(win < win_percentage and max_trials > 0):
        max_trials -= 1
        for itt in range(batch_size):
            learning_trial(environment)
        environment.creature.learn()
        win = test_creature(environment, 50)
        environment.creature.adjust_epsilon(win)
        
def average_time_to_train(environment, lessons, batch_size, win_percentage,
                 max_trials, test_size):
    dur = 0
    for x in range(test_size):
        start = time.time()
        train_to_win_quiet(environment, lessons, batch_size, win_percentage,
                 max_trials)
        environment.reset()
        end = time.time()
        dur += end - start
        print('Trained: {}'.format(x + 1))
    return dur / test_size

#Put our creature to the test and see how well it does
def test_creature(environment, itts):
    environment.reset()
    wins = 0
    for itt in range(itts):
        trial_keep_vals(environment)
        if(environment.creature.status == 2):
            wins += 1
    return wins / itts

def save_creature(creature, filename):
    with open(filename, 'wb') as f:
        pickle.dump(creature, f)