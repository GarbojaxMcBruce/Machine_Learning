from sklearn.neural_network import MLPRegressor as mlp
import Environment as E
import Creature as C
import Hunter as H
import Operations as Op

brain = mlp(hidden_layer_sizes=(100,), max_iter=200,
                         shuffle=True, activation='relu',
                         learning_rate='adaptive')

creature = C.Creature('trained_creature.sav', -1)
hunter = H.Hunter('Problems', -1000)
environment = E.Environment('The Matrix', 15, creature, hunter)

Op.train_to_win(environment, 10000, 100, .95, 10000)
Op.interactive_trial(environment)
Op.save_creature(environment.creature, 'trained_creature.sav')