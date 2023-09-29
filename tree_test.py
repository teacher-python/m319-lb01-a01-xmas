import sys

import pytest

import tree as tree


def test_A(find_step, monkeypatch, capsys):
    inputs = iter(['1'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tree.make_tree()
    output = capsys.readouterr().out

    if find_step == 4:
        assert output == '*\n|\n'
    elif find_step == 3:
        assert output == '*\n'
    else:
        assert output == "\n"



def test_B(find_step, monkeypatch, capsys):
    inputs = iter(['5'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tree.make_tree()
    captured = capsys.readouterr()
    if find_step == 4:
        assert captured.out == '....*\n...***\n..*****\n.*******\n*********\n....|\n'
    elif find_step == 3:
        assert captured.out == '....*\n...***\n..*****\n.*******\n*********\n'
    elif find_step == 2:
        assert captured.out == '....\n...\n..\n.\n\n'
    else:
        assert captured.out == "\n\n\n\n\n"


def test_C(find_step, monkeypatch, capsys):
    if find_step == 1:
        pytest.skip('Skipping this test for step 1')
    inputs = iter(['3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tree.make_tree()
    captured = capsys.readouterr()
    if find_step == 4:
        assert captured.out == '..*\n.***\n*****\n..|\n'
    elif find_step == 3:
        assert captured.out == '..*\n.***\n*****\n'
    else:
        assert captured.out == '..\n.\n\n'

def test_D(find_step, monkeypatch, capsys):
    if find_step <= 2:
        pytest.skip('Skipping this test for step 1 & 2')
    inputs = iter(['4'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tree.make_tree()
    captured = capsys.readouterr()
    if find_step == 4:
        assert captured.out == '...*\n..***\n.*****\n*******\n...|\n'
    else:
        assert captured.out == '...*\n..***\n.*****\n*******\n'

def test_E(find_step, monkeypatch, capsys):
    if find_step < 4:
        pytest.skip('Skipping this test for step 1-3')
    inputs = iter(['7'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tree.make_tree()
    captured = capsys.readouterr()
    assert captured.out == '......*\n.....***\n....*****\n...*******\n..*********\n.***********\n*************\n......|\n'

@pytest.fixture
def find_step(monkeypatch, capsys):
    inputs = iter(['3'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    tree.make_tree()
    output = capsys.readouterr().out
    if output[0] == '\n':
        step = 1
    elif output[0:3] == '..\n':
        step =  2
    elif output[0:4] == '..*\n' and output[-2] != '|':
        step = 3
    elif output[0:4] == '..*\n' and output[-2] == '|':
        step = 4
    else:
        print ('Cannot determine the step you are working on.', file=sys.stderr)
        return 4

    print (f'Executing tests for step {step}', file=sys.stderr)
    return step