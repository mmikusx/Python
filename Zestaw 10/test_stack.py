import pytest
from stack import Stack


def test_is_full():
    stack = Stack(6)
    for i in range(6):
        stack.push(i)

    assert stack.is_full() is True
    stack.pop()
    assert stack.is_full() is False
    stack.push(6)
    assert stack.is_full() is True

def test_is_empty():
    stack = Stack(4)
    assert stack.is_empty() is True
    stack.push(2)
    assert stack.is_empty() is False
    stack.pop()
    assert stack.is_empty() is True

def test_push():
    stack = Stack(10)
    assert stack.is_empty() is True
    for i in range(10):
        stack.push(i)
    assert stack.is_empty() is False

    with pytest.raises(ValueError):
        stack.push(11)

def test_pop():
    stack = Stack(20)
    assert stack.is_empty() is True
    for i in range(20):
        stack.push(i)
    assert stack.is_full() is True
    for i in range(20):
        stack.pop()
    assert stack.is_empty() is True

    with pytest.raises(ValueError):
        stack.pop()

if __name__ == "__main__":
    pytest.main()
