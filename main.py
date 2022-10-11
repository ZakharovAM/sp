import heapq
from collections import namedtuple, Counter
from pathlib import Path

Node = namedtuple("Node", ("path", "unit"))


def biggestPath(x: dict) -> str:
    start = Node(Path("/"), x)
    queue_nodes: list[Node] = [start]
    visited: list[str] = [start.path]
    while queue_nodes:
        current_node: Node = heapq.heappop(queue_nodes)
        if isinstance(current_node.unit, dict):
            for root, nodes in current_node.unit.items():
                if isinstance(nodes, dict):
                    if is_nodes_empty := not nodes.items():
                        visited.append(current_node.path / root)
                    else:
                        new_node = Node(current_node.path / root, nodes)
                        heapq.heappush(queue_nodes, new_node)
                        visited.append(new_node.path)
                elif isinstance(nodes, list):
                    nodes_without_doubles = [k for k, v in Counter(nodes).items() if v == 1]
                    if is_nodes_empty := not nodes_without_doubles:
                        visited.append(current_node.path / root)
                    else:
                        for i in nodes:
                            visited.append(current_node.path / root / i)

    if b_path_in_list := heapq.nlargest(1, visited, key=lambda path: len(path.as_posix().split("/"))):
        return b_path_in_list[0]
    else:
        return start.path.as_posix()


if __name__ == "__main__":
    d1 = {"dir1": {}, "dir2": ["file1"], "dir3": {"dir4": ["file2"], "dir5": {"dir6": {"dir7": {}}}}}
    print(biggestPath(d1))
    d2 = {"dir1": ["file1", "file1"]}
    print(biggestPath(d2))
    d3 = {"dir1": ["file1", "file2", "file2"]}
    print(biggestPath(d3))
