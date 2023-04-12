# O(n) time || O(n) space
def simplify_path(self, path: str) -> str:
    stack = []
    for p in path.split("/"):
        if p == "..":
            if stack:
                stack.pop()
        elif p == "." or not p:
            pass
        else:
            stack.append(p)

    return "/" + "/".join(stack)
