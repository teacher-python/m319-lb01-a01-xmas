def make_tree():
    """
    prints an Xmas tree
    :return: None
    """
    step1()

def step1():
    height = int(input('Höhe des Baums'))
    lines = 1
    while lines <= height:
        print()
        lines += 1

def step2():
    height = int(input('Höhe des Baums'))
    lines = 1
    while lines <= height:
        symbols = 0
        while symbols < (height - lines):
            print('.', end='')
            symbols += 1
        print()
        lines += 1

def step3():
    height = int(input('Höhe des Baums'))
    lines = 1
    while lines <= height:
        symbols = 0
        while symbols < (height - lines):
            print('.', end='')
            symbols += 1
        counter = 0
        while counter < (lines * 2 - 1):
            print('*', end='')
            counter += 1
        print()
        lines += 1

def step4():
    height = int(input('Höhe des Baums '))
    lines = 1
    while lines <= height:
        symbols = 0
        while symbols < (height - lines):
            print('.', end='')
            symbols += 1
        counter = 0
        while counter < (lines * 2 - 1):
            print('*', end='')
            counter += 1
        print()
        lines += 1

    indent = 0
    while indent < (height - 1):
        print('.', end='')
        indent += 1
    print ('|')
if __name__ == '__main__':
    make_tree()
