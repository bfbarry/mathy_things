import numpy as np

def metropolis_ising(T,runtime,N=None,grid=None):
    """grid: if you choose to initialize with previous image"""
    J = 1 #strength of interaction (Joules)
    k = 1 # Joules per kelvin
    if grid is not None:
        N = grid.shape[0]
    else:
        grid = 2*np.random.randint(2, size = (N,N)) - 1 #random initial configuration with 1s and -1s
        
    for t in range(runtime):
        #sum of interactions at each spin site (vectorized!)
        interactions = sum([np.roll(grid,shift =(0, 1), axis = 1),
                            np.roll(grid,shift =(0, -1), axis = 1),
                            np.roll(grid,shift =(1, 0), axis = 0), # have to change axis because unlike MATLAB's circshift, np.roll sees shifts (0,1) == (1,0)
                            np.roll(grid,shift =(-1, 0), axis = 0)])
        # change in energy of flipping a spin
        DeltaE = 2 * J * (grid * interactions) # element wise multiplication
        # transition probabilities
        p_trans = np.exp(-DeltaE/(k * T)) # according to the Boltzmann distribution
        # accepting or rejecting spin flips in one fell swoop!
        # assigning uniformly distributed values to each site, then checking if they are less than transition prob or less than 0.1?
        transitions = (np.random.random((N,N)) < p_trans ) * (np.random.random((N,N)) < 0.1) * -2 + 1
        grid = grid * transitions

        
    return grid