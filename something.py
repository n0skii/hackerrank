def lca(root, v1, v2):
    cur = root

    while 1:
        if (
            (v1 < cur.info and v2 > cur.info)
            or (v1 > cur.info and v2 < cur.info)
            or (cur.info == v1 or cur.info == v2)
        ):
            return cur

        else:
            cur = cur.left if v1 < cur.info else cur.right
