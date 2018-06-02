import queue

import algorithms.utils as utils


class AST:
    def __init__(self, root_node):
        self.root_node = root_node
        self.node_queue = queue.PriorityQueue()
        self.goal = sorted(self.root_node)
        self.expanded_nodes = set()
        self.node_queue.put(tuple((0, self.root_node)))
        self.solve()

    def heuristic(self, node):
        score = 0
        for goal_position, tile in enumerate(node):
            tile = int(tile)
            if tile != 0:
                score += abs((tile // 3) - (goal_position // 3))
                score += abs((tile % 3) - (goal_position % 3))
        return score

    def expand_node(self, node):
        child_nodes = utils.get_child_nodes(node[1])
        self.expanded_nodes.add(tuple(node[1]))
        for child in child_nodes:
            score = self.heuristic(child)
            if tuple(child) not in self.expanded_nodes:
                self.node_queue.put(tuple((score, child)))

    def solve(self):
        while not self.node_queue.empty():
            node = self.node_queue.get()
            if node[1] == self.goal:
                print("Solved {} \nwith A-Star to achieve {} \nwith {} nodes expanded".format(
                    self.root_node, node[1], len(self.expanded_nodes)))
                return
            self.expand_node(node)
