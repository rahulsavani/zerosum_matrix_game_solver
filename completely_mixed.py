from fractions import Fraction
from lp_solve import *

def create_game(target):
    """
    Currently only works for dimension 3 (square game)
    TODO: generalise to arbitrary dimension

    Assumes that target a positive vector 

    Creates a zero-sum game with target as the equilibrium of the row player
    """
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("Target:", target)

    A = np.array([
        [0, Fraction(1/target[0]), 0],
        [0, 0, Fraction(1/target[1])],
        [Fraction(1/target[2]), 0, 0]
    ])
    return A

if __name__ == "__main__":

    target_lst = []

    target_lst.append(np.array([0.5,0.25,0.25]))
    target_lst.append(np.array([0.1,0.1,8]))
    target_lst.append(np.array([0.5,0.4,0.1]))
    target_lst.append(np.array([0.2,0.7,0.1]))

    for target in target_lst:
        A = create_game(target)
        solve_for_both_players(A)
