# Cell states
ALIVE = 1
DEAD = 0
DIVIDING = 2
SENESCENT = 3
EMPTY = -1  # New constant for empty spots

# EMT states
E = 'E'  # Epithelial
H = 'H'  # Hybrid
M = 'M'  # Mesenchymal

# # Parameters for probabilities
division_probability = 0.03
hybrid_migration_probability = 0.9
mesenchymal_migration_probability = 0.99
hybrid_senescence_migration_probability = 0.45
death_probability = 0.0003
constant_senescence_probability =[0.1, 0.03]

# Probability of mesenchymal cells turn into epithelial cell
M_to_E_probability = 0.1

# Size of the grid
grid_size_x = 100
grid_size_y = 100

# Number of steps
NUM_STEPS = 300
