from typing import List, Dict

class Solution:
    class Node:
        __slots__ = ("name", "children", "deleted")
        def __init__(self, name: str):
            self.name = name
            self.children: Dict[str, 'Solution.Node'] = {}
            self.deleted = False

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        # 1. Build folder tree (trie)
        root = self.Node("")  # dummy root
        for path in paths:
            cur = root
            for part in path:
                if part not in cur.children:
                    cur.children[part] = self.Node(part)
                cur = cur.children[part]

        # 2. Serialize (post-order) and collect occurrences
        serial_map: Dict[str, List['Solution.Node']] = {}

        def serialize(node: 'Solution.Node') -> str:
            if not node.children:
                return ""  # leaf => empty set; not considered for duplicate deletion
            parts = []
            # deterministic ordering
            for name in sorted(node.children.keys()):
                child = node.children[name]
                child_serial = serialize(child)
                # include child name + its serialization
                parts.append(name + child_serial)
            serial = "(" + "".join(parts) + ")"
            serial_map.setdefault(serial, []).append(node)
            return serial

        for child in root.children.values():
            serialize(child)

        # 3. Mark duplicates (serialization appears ≥2 and non-empty)
        for serial, nodes in serial_map.items():
            if len(nodes) > 1:  # serial != "" guaranteed (leaves never added)
                for node in nodes:
                    node.deleted = True

        # 4. Collect remaining paths via DFS (skip deleted subtrees)
        result: List[List[str]] = []

        def dfs(node: 'Solution.Node', path: List[str]):
            if node.deleted:
                return
            if node.name:  # skip dummy root
                result.append(path[:])
            for name, child in node.children.items():
                path.append(name)
                dfs(child, path)
                path.pop()

        for name, child in root.children.items():
            dfs(child, [name])

        return result