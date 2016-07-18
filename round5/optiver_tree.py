#!/usr/bin/env python3

from collections import defaultdict
import re


class Error(Exception):
    """ Module-level exception. """


def parse(raw):
    tree = defaultdict(list)
    pairs = set()  # to search for duplicate pairs

    for chunk in raw.split():
        m = re.match("\((\w),(\w)\)", chunk)
        if not m:
            raise Error("E1")  # Malformed Input
        parent, child = m.groups()
        if (parent, child) in pairs:
            raise Error("E2")  # duplicate pair
        pairs.add((parent, child))
        children = tree[parent]
        children.append(child)
        if len(children) > 2:
            raise Error("E3")  # more than two children

    allnodes = set(tree.keys())
    visited = set()
    for node in tree:
        children = tree[node]
        for child in children:
            if child in visited:
                raise Error("E4")  # loop/cycle detected
        visited.update(children)
    roots = allnodes - visited
    if len(roots) > 1:
        raise Error("E5")  # multiple roots
    root = roots.pop()
    return tree, root


def render(node, tree, result):
    result.append('(')
    result.append(node)
    for child in tree[node]:
        result.extend(render(child, tree, []))
    result.append(')')
    return result


if __name__ == '__main__':
    test1 = "(B,D) (D,E) (A,B) (C,F) (E,G) (A,C)"
    test2 = "(A,B) (A,C) (B,D) (D,C)"
    tests = [test1, test2]
    for test in tests:
        try:
            tree, root = parse(test)
            result = "".join(render(root, tree, []))
            print(result)
        except Error as err:
            print(err)
