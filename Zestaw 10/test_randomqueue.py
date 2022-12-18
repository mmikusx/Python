import pytest
from randomqueue import RandomQueue

def test_is_empty():
    queue = RandomQueue(10)
    assert queue.is_empty() is True
    queue.insert(5)
    assert queue.is_empty() is False
    queue.remove()
    assert queue.is_empty() is True

def test_is_full():
    queue = RandomQueue(10)
    for i in range(10):
        queue.insert(i % 3)
    assert queue.is_full() is True
    queue.remove()
    assert queue.is_full() is False
    queue.insert(8)
    assert queue.is_full() is True

def test_insert():
    queue = RandomQueue(11)
    assert queue.is_empty() is True
    for i in range(11):
        queue.insert(i)
    assert queue.is_full() is True

    with pytest.raises(ValueError):
        queue.insert(11)

def test_remove():
    queue = RandomQueue(11)
    assert queue.is_empty() is True
    for i in range(11):
        queue.insert(i)
    assert queue.is_full() is True
    queue.remove()
    assert queue.is_full() is False
    for i in range(10):
        queue.remove()
    assert queue.is_empty() is True

    with pytest.raises(ValueError):
        queue.remove()

if __name__ == "__main__":
    pytest.main()
