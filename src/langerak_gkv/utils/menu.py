from menus.base import Modifier
from menus.menu_pool import menu_pool


class SplitMenuNodesModifier(Modifier):
    """
    Modifier that splits the nodes in two columns for display in the template.
    """

    def modify(self, request, nodes, namespace, root_id, post_cut, breadcrumb):
        if breadcrumb:
            return nodes
        if not post_cut:
            return nodes
        left, right = nodes[:len(nodes) / 2], nodes[len(nodes) / 2:]
        for node in left:
            node.left = True
        for node in right:
            node.right = True
        return nodes


menu_pool.register_modifier(SplitMenuNodesModifier)
