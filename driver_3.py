import sys

from algorithms import ast, bfs, dfs


def driver():
    algorithm = sys.argv[1]
    root_node = sys.argv[2].split(',')

    if algorithm == "bfs":
        bfs.BFS(root_node)
    elif algorithm == "dfs":
        dfs.DFS(root_node)
    elif algorithm == "ast":
        ast.AST(root_node)


if __name__ == "__main__":
    driver()
