def make_tree():
    """
    prints an Xmas tree
    :return: None
    """
    height = int(input('Hoehe > '))
    line = 1
    while line <= height:
        print('')
        line += 1


if __name__ == '__main__':
    make_tree()
