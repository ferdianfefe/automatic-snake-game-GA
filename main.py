from players import *
from game import *

size = 10
num_snakes = 10
players = [RandomPlayer(0)]

gui_size = 800

# game = Game(size, num_snakes, players, gui=None, display=True, max_turns=100)
# gui = Gui(game, gui_size)
# game.play(True, termination=False)

pop_size = 200
num_generations = 500
num_trails = 1
window_size = 7
hidden_size = 15
board_size = 10

gen_player = GeneticPlayer(
    pop_size,
    num_generations,
    num_trails,
    window_size,
    hidden_size,
    board_size,
    mutation_chance=0.3,
    mutation_size=0.3,
    crossover_chance=0.6,
    crossover_alpha=0.6,
)
gen_player.evolve_pop()

# Try different parameters
# Constant
# num_generations = 500
# window_size = 7
# hidden_size = 15
# board_size = 10
# # Varying
# pop_sizes = [100, 300, 500]
# num_trails = [1, 3, 5]
# mutation_chances = [0.1, 0.3, 0.5]
# crossover_chances = [0.6, 0.7, 0.8]

# records = []
# for pop_size in pop_sizes:
#     for num_trail in num_trails:
#         for mutation_chance in mutation_chances:
#             for crossover_chance in crossover_chances:
#                 gen_player = GeneticPlayer(
#                     pop_size,
#                     num_generations,
#                     num_trail,
#                     window_size,
#                     hidden_size,
#                     board_size,
#                     mutation_chance=mutation_chance,
#                     mutation_size=mutation_chance,
#                     crossover_chance=crossover_chance,
#                     crossover_alpha=crossover_chance,
#                 )
#                 score = gen_player.evolve_pop()
#                 records.append(
#                     (
#                         pop_size,
#                         num_trail,
#                         mutation_chance,
#                         crossover_chance,
#                         score,
#                     )
#                 )

# print("pop_size\tnum_trail\tmutation_size\tcrossover_chance\tscore")
# for record in records:
#     print(
#         record[0],
#         "\t\t",
#         record[1],
#         "\t\t",
#         record[2],
#         "\t\t",
#         record[3],
#         "\t\t\t",
#         record[4],
#     )
