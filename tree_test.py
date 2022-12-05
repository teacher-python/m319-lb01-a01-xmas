import tree as tree


def test_A(monkeypatch, capsys):
    inputs = iter(['1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tree.make_tree()
    captured = capsys.readouterr()

    if len(captured.out) >= 2 and captured.out[-2] == '|':
        print('Step 4')
        assert captured.out == '*\n|\n'
    elif captured.out == '*\n':
        print('Step 3')
        assert captured.out == '*\n'
    else:
        print('Step 1 & Step 2')
        assert captured.out == "\n"



def test_B(monkeypatch, capsys):
    inputs = iter(['5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tree.make_tree()
    captured = capsys.readouterr()
    if len(captured.out) >= 2 and  captured.out[-2] == '|':
        print('Step 4')
        assert captured.out == '....*\n...***\n..*****\n.*******\n*********\n....|\n'
    elif captured.out[0:5] == '....*' and captured.out[-3] == '.*\n':
        print('Step 3')
        assert captured.out == '....*\n...***\n..*****\n.*******\n*********\n'
    elif captured.out[0:5] == '....\n':
        print('Step 2')
        assert captured.out == '....\n...\n..\n.\n\n'
    else:
        print('Step 1')
        assert captured.out == "\n\n\n\n\n"


def test_C(monkeypatch, capsys):
    inputs = iter(['3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tree.make_tree()
    captured = capsys.readouterr()
    if len(captured.out) >= 2 and  captured.out[-2] == '|':
        print('Step 4')
        assert captured.out == '..*\n.***\n*****\n..|\n'
    elif captured.out[0:3] == '..*':
        print('Step 3')
        assert captured.out == '..*\n.***\n*****\n'
    else:
        print('Step 2')
        assert captured.out == '..\n.\n\n'

def test_D(monkeypatch, capsys):
    inputs = iter(['4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tree.make_tree()
    captured = capsys.readouterr()
    if len(captured.out) >= 2 and  captured.out[-2] == '|':
        print('Step 4')
        assert captured.out == '...*\n..***\n.*****\n*******\n...|\n'
    else:
        print('Step 3')
        assert captured.out == '...*\n..***\n.*****\n*******\n'

def test_E(monkeypatch, capsys):
    inputs = iter(['7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tree.make_tree()
    captured = capsys.readouterr()
    assert captured.out == '......*\n.....***\n....*****\n...*******\n..*********\n.***********\n*************\n......|\n'