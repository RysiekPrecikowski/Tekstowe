def returnValue(root):
    return root.value
def returnKey(root):
    return root.key


def display_tree(root, keys = True, values = False, whatToPrint = None):
    if whatToPrint is None:
        if keys is True and values is False:
            whatToPrint = returnKey
        else:
            whatToPrint = returnValue

    def print_tree(root,keys):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if root.right is None and root.left is None:
            # if keys is True and values is False:
            #     line = '%s' % root.key
            # else:
            #     line = '%s' % root.value

            line = '%s' % whatToPrint(root)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if root.right is None:
            lines, n, p, x = print_tree(root.left,keys)

            # if keys is True and values is False:
            #     s = '%s' % root.key
            # else:
            #     s = '%s' % root.value

            s = '%s' % whatToPrint(root)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if root.left is None:
            lines, n, p, x = print_tree(root.right,keys)

            # if keys is True and values is False:
            #     s = '%s' % root.key
            # else:
            #     s = '%s' % root.value

            s = '%s' % whatToPrint(root)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = print_tree(root.left,keys)
        right, m, q, y = print_tree(root.right,keys)

        # if keys is True and values is False:
        #     s = '%s' % root.key
        # else:
        #     s = '%s' % root.value

        s = '%s' % whatToPrint(root)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    print()
    lines, _, _, _ = print_tree(root,keys)
    for line in lines:

        print(line)
    print()