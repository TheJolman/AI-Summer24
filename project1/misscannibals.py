from search import *

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
    def actions(self, state: tuple[int, int, bool]) -> list[str]:
        """Return list of legal actions in the given state"""
        possible_actions: list[str] = ["CC", "MM", "MC", "C", "M"]

        m_left, c_left, on_left = state
        m_right = self.M - m_left
        c_right = self.C - c_left


        def is_legal(action: str)-> bool:
            """Will be mapped to each element in the set. Simulates each action.
            Returns true if legal. Returns false otherwise."""

            direction = -1 if on_left else 1
            m_moves = action.count("M")
            c_moves = action.count("C")

            new_m_left  = m_left  + direction * m_moves
            new_m_right = m_right - direction * m_moves
            new_c_left  = c_left  + direction * c_moves
            new_c_right = c_right - direction * c_moves

            if all(3 >= people >= 0 for people in [new_m_left, new_m_right, new_c_left, new_c_right]):
                return (new_m_left >= new_c_left or new_c_left == 0 or new_m_left == 0) and \
                        (new_m_right >= new_c_right or new_c_left == 0 or new_m_right == 0)
            return False


        legal_actions = [action for action in possible_actions if is_legal(action)]

        # print(f"state: {state}\tpossible actions: {legal_actions}")

        return legal_actions

        
    def result(self, state: tuple[int, int, bool], action: str) -> tuple[int, int, bool]:
        """Return the state that results from executing the
        given action in the given state. Action must be one
        of self.actions(state)"""
        
        m, c, on_left = state

        # print(f"state before: {state}", end="\t")

        direction = -1 if on_left else 1

        m += direction * action.count("M")
        c += direction * action.count("C")
        on_left = not on_left

        result = (m, c, on_left)

        # print(f"Action done: {action}\t state after: {result}")

        return result
            
    def goal_test(self, state):
        return super().goal_test(state)


if __name__ == "__main__":
    mc = MissCannibals(M=3, C=3)

    # tests
    # should return ['CC', 'C', 'M']

    result = depth_first_graph_search(mc)
    if result is not None:
        path = result.solution()
        print(path)

    result = breadth_first_graph_search(mc)
    if result is not None:
        path = result.solution()
        print(path)
