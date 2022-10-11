from collections import namedtuple, Counter
from pathlib import Path

Node = namedtuple("Node", ("path", "unit"))


def biggestPath(x: dict) -> str:
    start = Node(Path("/"), x)
    queue_nodes: list[Node] = [start]
    visited: list[str] = [start.path]
    while queue_nodes:
        current_node: Node = queue_nodes.pop(0)
        if node_is_dict := isinstance(current_node.unit, dict):
            for root, nodes in current_node.unit.items():
                if isinstance(nodes, dict):
                    if is_nodes_empty := not nodes.items():
                        visited.append(current_node.path / root)
                    else:
                        new_node = Node(current_node.path / root, nodes)
                        queue_nodes.append(new_node)
                        visited.append(new_node.path)
                elif node_is_list := isinstance(nodes, list):
                    nodes_without_doubles = [k for k, v in Counter(nodes).items() if v == 1]
                    if is_nodes_empty := not nodes_without_doubles:
                        visited.append(current_node.path / root)
                    else:
                        for i in nodes:
                            visited.append(current_node.path / root / i)

    visited.sort(key=lambda path: len(path.as_posix().split("/")), reverse=True)
    result = visited.pop(0).as_posix()
    return result