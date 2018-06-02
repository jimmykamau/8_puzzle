import queue

import algorithms.utils as utils


class BFS:
    def __init__(self, root_node):
        self.root_node = root_node
        self.node_queue = queue.Queue()
        self.goal = sorted(self.root_node)
        self.expanded_nodes = set()
        self.node_queue.put(self.root_node)
        self.solve()

    def expand_node(self, node):
        child_nodes = utils.get_child_nodes(node)
        self.expanded_nodes.add(tuple(node))
        for child in child_nodes:
            if tuple(child) not in self.expanded_nodes:
                self.node_queue.put(child)

    def solve(self):
        while not self.node_queue.empty():
            node = self.node_queue.get()
            if node == self.goal:
                print("Solved {} \nwith BFS to achieve {} \nwith {} nodes expanded".format(
                    self.root_node, node, len(self.expanded_nodes)))
                return
            self.expand_node(node)
