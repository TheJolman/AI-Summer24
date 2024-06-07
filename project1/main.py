# from os import walk
from search import *
# from typing import Tuple, Set

class MissCannibals(Problem):
    """Uses generic class `Problem` from search.py
    There are M missionaries and C cannibals on the left side of a
    river bank along with a boat.
    This class attemps to get all people to the right river bank while
    obeying the following rules:
        -- The cannibals can never outnumber the missionaries on either bank
        -- The boat can hold two people at a time and needs one person to operate it"""

    def __init__(self, M: int=3, C: int=3, goal=(0, 0, False)):
        """
        M: number of missionaries currently on left bank
        C: number of cannibals currently on left bank
        goal: number of desired missionaries and cannibals 
        on the left bank in the end, as well as the position of the boat
        """

        initial = (M, C, True)
        self.M = M
        self.C = C
        super().__init__(initial, goal)

    # Methods: actions, result, path_cost, value
    def actions(self, state: tuple[int, int, bool]) -> set[str]:
        """Return list of legal actions in the given state"""
        possible_actions: set[str] = {"CC", "MM", "CM", "C", "M"}

        M_left, C_left, on_left = state
        M_right = self.M - M_left
        C_right  = self.C - C_left

        # funct that simlates each action in the list and determines if it is legal
        def is_legal(action: str) -> bool:
            """Will be mapped to each element in the set. Simulates each action.
            Returns true if legal. Returns false otherwise."""

            m_left, m_right, c_left, c_right = M_left, M_right, C_left, C_right
            direction = -1 if on_left else 1

            m_left += direction * action.count("M")
            m_right -= direction * action.count("M")

            c_left += direction * action.count("C")
            c_right -= direction * action.count("C")

            if all(x >= 0 for x in [m_left, m_right, c_left, c_right]):
                if (m_left >= c_left) or (c_left == 0):
                    if (m_right >= c_right) or (c_right == 0):
                        return True
            return False

        for action in possible_actions:
            if not is_legal(action):
                possible_actions.discard(action)

        return possible_actions

        
    def result(self, state: tuple[int, int, bool], action: str) -> tuple[int, int, bool]:
        """Return the state that results from executing the
        given action in the given state. Action must be one
        of self.actions(state)"""
        
        M, C, on_left = state

        direction = -1 if on_left else 1

        M += direction * action.count("M")
        M += direction * action.count("C")

        return (M, C, on_left)
            

    def goal_test(self, state):
        super().goal_test(state)


if __name__ == "__main__":
    mc = MissCannibals(M=3, C=3)

    # tests
    # should return ['CC', 'C', 'M']

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
