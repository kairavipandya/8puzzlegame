import numpy as np
import sys


class PuzzleNode():
    def __init__(self, state, parent, action, depth, step_cost, path_cost, heuristic_cost):
        self.state = state 
        self.parent = parent                   
        self.action = action                   
        self.depth = depth                     
        self.step_cost = step_cost             
        self.heuristic_cost = heuristic_cost   
        self.path_cost = path_cost            

        # Children nodes
        self.move_up = None 
        self.move_left = None
        self.move_down = None
        self.move_right = None

    def print_path(self):
        state_trace = [self.state]
        action_trace = [self.action]
        depth_trace = [self.depth]
        step_cost_trace = [self.step_cost]
        path_cost_trace = [self.path_cost]
        heuristic_cost_trace = [self.heuristic_cost]
        
        while self.parent:
            self = self.parent
            state_trace.append(self.state)
            action_trace.append(self.action)
            depth_trace.append(self.depth)
            step_cost_trace.append(self.step_cost)
            heuristic_cost_trace.append(self.heuristic_cost)
            path_cost_trace.append(self.path_cost)
            
        step_counter = 0
        while state_trace:
            print('\n', state_trace.pop())
            print('  depth=', str(depth_trace.pop()), '\taction=', action_trace.pop())

    def is_valid_move(self, direction):
        zero_index = np.where(self.state == 0)
        zero_index = (zero_index[0][0], zero_index[1][0])  # Convert to tuple
        
        if direction == 'up':
            if zero_index[0] == 2:
                return False
            else:
                lower_value = self.state[zero_index[0]+1, zero_index[1]]
                new_state = self.state.copy()
                new_state[zero_index[0], zero_index[1]] = lower_value
                new_state[zero_index[0]+1, zero_index[1]] = 0
                return new_state, lower_value
        
        elif direction == 'down':
            if zero_index[0] == 0:
                return False
            else:
                up_value = self.state[zero_index[0]-1, zero_index[1]]
                new_state = self.state.copy()
                new_state[zero_index[0], zero_index[1]] = up_value
                new_state[zero_index[0]-1, zero_index[1]] = 0
                return new_state, up_value
        
        elif direction == 'left':
            if zero_index[1] == 2:
                return False
            else:
                right_value = self.state[zero_index[0], zero_index[1]+1]
                new_state = self.state.copy()
                new_state[zero_index[0], zero_index[1]] = right_value
                new_state[zero_index[0], zero_index[1]+1] = 0
                return new_state, right_value
        
        elif direction == 'right':
            if zero_index[1] == 0:
                return False
            else:
                left_value = self.state[zero_index[0], zero_index[1]-1]
                new_state = self.state.copy()
                new_state[zero_index[0], zero_index[1]] = left_value
                new_state[zero_index[0], zero_index[1]-1] = 0
                return new_state, left_value
    
    def dfs(self, goal_state):

        stack = [self]               
        visited = set([])           
        max_depth = 0
        states_enqueued = 0

        while stack:
            current_node = stack.pop() 

            if current_node.depth > max_depth:
                max_depth = current_node.depth

            visited.add(tuple(current_node.state.reshape(1, 9)[0]))

            if np.array_equal(current_node.state, goal_state):
                current_node.print_path()
                print("\nNumber of moves = ", current_node.depth)
                print("Maximum stack depth = ", max_depth)
                print("Number of states enqueued =", states_enqueued)
                return True
                
            else:                
                for direction in ['down', 'right', 'up', 'left']:
                    move_result = current_node.is_valid_move(direction)
                    if move_result:
                        new_state, value = move_result
                        if tuple(new_state.reshape(1, 9)[0]) not in visited:
                            stack.append(PuzzleNode(state=new_state,
                                                    parent=current_node,
                                                    action=direction,
                                                    depth=current_node.depth + 1,
                                                    step_cost=value,
                                                    path_cost=current_node.path_cost + value,
                                                    heuristic_cost=0))
                            states_enqueued += 1
        print('Goal state was not found before or at max depth.')
        return False

    def ids(self, goal_state):
        stack = [self]             
        visited = set([])         
        max_depth = 0              
        states_enqueued = 0

        while stack:
            current_node = stack.pop() 

            if current_node.depth > max_depth:
                max_depth = current_node.depth

            visited.add(tuple(current_node.state.reshape(1, 9)[0]))

            if np.array_equal(current_node.state, goal_state):
                current_node.print_path()
                print("\nNumber of moves = ", current_node.depth)
                print("Maximum stack depth = ", max_depth)
                print("Number of states enqueued =", states_enqueued)
                return True

            else:                
                if current_node.depth < 10:
                    for direction in ['down', 'right', 'up', 'left']:
                        move_result = current_node.is_valid_move(direction)
                        if move_result:
                            new_state, value = move_result
                            if tuple(new_state.reshape(1, 9)[0]) not in visited:
                                stack.append(PuzzleNode(state=new_state,
                                                        parent=current_node,
                                                        action=direction,
                                                        depth=current_node.depth + 1,
                                                        step_cost=value,
                                                        path_cost=current_node.path_cost + value,
                                                        heuristic_cost=0))
                                states_enqueued += 1
                else:
                    print('Goal state was not found before or at depth 10.')
                    break
        return False

    def astar(self, goal_state, heuristic_function):
        queue = [(self, 0)]          
        visited = set([])           
        max_depth = 0              
        states_enqueued = 0

        while queue:
            queue = sorted(queue, key=lambda x: x[1])

            current_node = queue.pop(0)[0] 
            visited.add(tuple(current_node.state.reshape(1, 9)[0]))

            if current_node.depth > max_depth:
                max_depth = current_node.depth

            if np.array_equal(current_node.state, goal_state):
                current_node.print_path()
                print("\nNumber of moves = ", current_node.depth)
                print("Maximum priority queue depth = ", max_depth)
                print("Number of states enqueued =", states_enqueued)
                return True
            
            else:     
                if current_node.depth < 10:
                    for direction in ['down', 'right', 'up', 'left']:
                        move_result = current_node.is_valid_move(direction)
                        if move_result:
                            new_state, value = move_result
                            if tuple(new_state.reshape(1, 9)[0]) not in visited:
                                path_cost = current_node.path_cost + value
                                depth = current_node.depth + 1
                                if heuristic_function == 'misplaced':
                                    h_cost = self.h_misplaced_cost(new_state, goal_state)
                                elif heuristic_function == 'manhattan':
                                    h_cost = self.h_manhattan_cost(new_state, goal_state)
                                total_cost = path_cost + h_cost
                                queue.append((PuzzleNode(state=new_state,
                                                         parent=current_node,
                                                         action=direction,
                                                         depth=depth,
                                                         step_cost=value,
                                                         path_cost=path_cost,
                                                         heuristic_cost=h_cost), total_cost))
                                states_enqueued += 1
                else:
                    print('Goal state was not found before or at depth 10.')
                    break
        return False

    def h_misplaced_cost(self, new_state, goal_state):
        cost = np.sum(new_state != goal_state) - 1
        if cost > 0: return cost
        else: return 0 

    def h_manhattan_cost(self, new_state, goal_state):
        current = new_state
        goal_position_dic = {1: (0, 0), 2: (0, 1), 3: (0, 2), 8: (1, 0), 0: (1, 1), 4: (1, 2), 7: (2, 0), 6: (2, 1), 5: (2, 2)} 
        sum_manhattan = 0
        for i in range(3):
            for j in range(3):
                if current[i, j] != 0:
                    sum_manhattan += sum(abs(a - b) for a, b in zip((i, j), goal_position_dic[current[i, j]]))
        return sum_manhattan


def main(argv):
    if len(sys.argv) == 2:
        algorithm_name = sys.argv[1]
    else:
        print('Usage: python puzzle_solver.py <algorithm_name>')
        print('Available algorithm names: dfs, ids, astar1, astar2')
        return

    print("Enter the initial state of the puzzle (use space-separated values, e.g., '1 2 3 4 0 5 6 7 8'):")
    initial_state_input = input().strip()
    initial_state_values = list(map(int, initial_state_input.split()))
    initial_state = np.array(initial_state_values).reshape(3, 3)

    goal_state = np.array([1, 2, 3, 4, 0, 5, 6, 7, 8]).reshape(3, 3)

    root_node = PuzzleNode(state=initial_state,
                           parent=None,
                           action=None,
                           depth=0,
                           step_cost=0,
                           path_cost=0,
                           heuristic_cost=0)

    if algorithm_name == 'dfs':
        root_node.dfs(goal_state)
    elif algorithm_name == 'ids':
        root_node.ids(goal_state)
    elif algorithm_name == 'astar1':
        root_node.astar(goal_state, heuristic_function='misplaced')
    elif algorithm_name == 'astar2':
        root_node.astar(goal_state, heuristic_function='manhattan')
    else:
        print('Invalid algorithm name. Available names: dfs, ids, astar1, astar2')


if __name__ == '__main__':
    main(sys.argv)
