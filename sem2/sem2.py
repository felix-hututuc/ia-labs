from copy import deepcopy
import queue
import math


class Jug:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.filled = 0
    
    def get_filled(self):
        return self.filled

    def set_filled(self, filled):
        self.filled = filled

    def fill(self):
        self.filled = self.capacity

    def get_free(self):
        return self.capacity - self.filled


def is_final(state, k):
    if k in [jug.get_filled() for jug in state]:
        return True
    return False


def initialize(m, n):
    return (Jug(m), Jug(n))


def fill_A(state):
    new_state = deepcopy(state)
    new_state[0].fill()
    return new_state


def fill_B(state):
    new_state = deepcopy(state)
    new_state[1].fill()
    return new_state


def empty_A(state):
    new_state = deepcopy(state)
    new_state[0].set_filled(0)
    return new_state


def empty_B(state):
    new_state = deepcopy(state)
    new_state[1].set_filled(0)
    return new_state


def pour_A2B(state):
    new_state = deepcopy(state)
    if state[0].get_filled() < state[1].get_free():
        new_state[1].set_filled(state[1].get_filled() + state[0].get_filled())
        new_state[0].set_filled(0)
    elif state[0].get_filled() > state[1].get_free():
        new_state[0].set_filled(state[0].get_filled() - state[1].get_free())
        new_state[1].fill()
    else:
        new_state[0].set_filled(0)
        new_state[1].fill()
    return new_state


def pour_B2A(state):
    new_state = deepcopy(state)
    if state[1].get_filled() < state[0].get_free():
        new_state[0].set_filled(state[0].get_filled() + state[1].get_filled())
        new_state[1].set_filled(0)
    elif state[1].get_filled() > state[0].get_free():
        new_state[1].set_filled(state[1].get_filled() - state[0].get_free())
        new_state[0].fill()
    else:
        new_state[1].set_filled(0)
        new_state[0].fill()
    return new_state
        

def fill_A_is_valid(state):
    if state[0].get_free() == 0:
        return False
    return True


def fill_B_is_valid(state):
    if state[1].get_free() == 0:
        return False
    return True


def empty_A_is_valid(state):
    if state[0].get_filled() == 0:
        return False
    return True


def empty_B_is_valid(state):
    if state[1].get_filled() == 0:
        return False
    return True


def pour_A2B_is_valid(state):
    if state[0].get_filled() == 0 or state[1].get_free() == 0:
        return False
    return True


def pour_B2A_is_valid(state):
    if state[1].get_filled() == 0 or state[0].get_free() == 0:
        return False
    return True


def print_state(state):
    print(f"({state[0].get_filled()},  {state[1].get_filled()}) ")


def is_visited(state, visited):
    for vis_state in visited:
        if state[0].get_filled() == vis_state[0].get_filled() and state[1].get_filled() == vis_state[1].get_filled():
            return True
    return False


def bkt(state, k, solution):
    if is_final(state, k):
        return True
    
    if fill_A_is_valid(state):
        new_state = fill_A(state)
        if not is_visited(new_state, solution):
            solution.append(new_state)
            if bkt(new_state, k, solution):
                return True
            solution.pop()

    if fill_B_is_valid(state):
        new_state = fill_B(state)
        if not is_visited(new_state, solution):
            solution.append(new_state)
            if bkt(new_state, k, solution):
                return True
            solution.pop()

    if empty_A_is_valid(state):
        new_state = empty_A(state)
        if not is_visited(new_state, solution):
            solution.append(new_state)
            if bkt(new_state, k, solution):
                return True
            solution.pop()

    if empty_B_is_valid(state):
        new_state = empty_B(state)
        if not is_visited(new_state, solution):
            solution.append(new_state)
            if bkt(new_state, k, solution):
                return True
            solution.pop()

    if pour_A2B_is_valid(state):
        new_state = pour_A2B(state)
        if not is_visited(new_state, solution):
            solution.append(new_state)
            if bkt(new_state, k, solution):
                return True
            solution.pop()

    if pour_B2A_is_valid(state):
        new_state = pour_B2A(state)
        if not is_visited(new_state, solution):
            solution.append(new_state)
            if bkt(new_state, k, solution):
                return True
            solution.pop()
    
    return False


def solve_bkt(m, n, k):
    state = initialize(m, n)
    solution = [state]
    if bkt(state, k, solution):
        [print_state(st) for st in solution]
    else:
        print("No solution found!")


def bfs(m, n, k):
    q = queue.Queue()
    state = initialize(m, n)
    q.put(state)
    parent = {state: -1}
    solution = []

    while not q.empty():
        curr_state = q.get()

        if is_final(curr_state, k):
            while parent[curr_state] != -1:
                solution.append(curr_state)
                curr_state = parent[curr_state]
            solution.append(curr_state)
            return solution[::-1]

        if fill_A_is_valid(curr_state):
            new_state = fill_A(curr_state)
            parent[new_state] = curr_state
            q.put(new_state)
        if fill_B_is_valid(curr_state):
            new_state = fill_B(curr_state)
            parent[new_state] = curr_state
            q.put(new_state)
        if empty_A_is_valid(curr_state):
            new_state = empty_A(curr_state)
            parent[new_state] = curr_state
            q.put(new_state)
        if empty_B_is_valid(curr_state):
            new_state = empty_B(curr_state)
            parent[new_state] = curr_state
            q.put(new_state)
        if pour_A2B_is_valid(curr_state):
            new_state = pour_A2B(curr_state)
            parent[new_state] = curr_state
            q.put(new_state)
        if pour_B2A_is_valid(curr_state):
            new_state = pour_B2A(curr_state)
            parent[new_state] = curr_state
            q.put(new_state)
    
    return False


def solve_bfs(m, n, k):
    solution = bfs(m, n, k)
    if solution:
        [print_state(st) for st in solution]
    else:
        print("No solution found!")


def is_solvable(m, n, k):
    if m == 0 and n == 0 and k == 0:
        return True

    return (m + n >= k and k % math.gcd(m, n) == 0)


def cli_menu():
    m = int(input("Insert first jug capacity: "))
    n = int(input("Insert second jug capacity: "))
    k = int(input("Insert wanted volume: "))

    if not is_solvable(m, n, k):
        print("Not solvable!")
        return

    print("[1] Backtracking")
    print("[2] BFS")
    print("[3] Hillclimbing")
    print("[4] A*")

    choice = int(input("Choose an algorithm: "))
    if choice == 1:
        print("Solving using Backtracking...")
        solve_bkt(m, n, k)
    elif choice == 2:
        print("Solving using BFS...")
        solve_bfs(m, n, k)
    elif choice == 3:
        print("Solving using Hillclimbing...")
        print("Algorithm not yet implemented")
    elif choice == 4:
        print("Solving using A*...")
        print("Algorithm not yet implemented")
    else:
        print("Not a valid choice!")


if __name__ == '__main__':
    cli_menu()

# print_state(state)

# fill_A(state)
# fill_B(state)
# pour_A2B(state)
# print_state(state)

# fill_A(state)
# print_state(state)

# pour_A2B(state)
# print_state(state)

# empty_B(state)
# print_state(state)

# pour_A2B(state)
# print_state(state)

# fill_A(state)
# print_state(state)

# pour_A2B(state)
# print_state(state)

# print(is_final(state, k))
        