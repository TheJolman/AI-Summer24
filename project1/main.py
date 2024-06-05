from search import *

class MissCannibals(Problem):
    """Uses Problem template class from search.py
    There are M missionaries and C cannibals on the left side of a
    river bank along with a boat.
    This class attemps to get all people to the right river bank while
    obeying the following rules:
        -- The cannibals can never outnumber the missionaries on either bank
        -- The boat can hold two people at a time and needs one person to operate it"""

    def __init__(self, M=3, C=3, goal=(0, 0, False)):
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

    # fill out class here
    # Methods: actions, result, path_cost, value
    def actions(self, state):
        """Return list of legal actions in the given state"""
        print("actions")

    def result(self, state, action):
        """Return the state that results from executing the
        given action in the given state. Action must be one
        of self.actions(state)"""
        print("state")

    def goal_test(self, state):
        super().goal_test(self, state)
    


if __name__ == "__main__":
    mc = MissCannibals(M=3, C=3)

    # tests
    # should return ['CC', 'C', 'M']

    path = depth_first_graph_search(mc).solution()
    print(path)
    path = breadth_first_graph_search(mc).solution()
    print(path)
