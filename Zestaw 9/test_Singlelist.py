from Singlelist import SingleList
from Singlelist import Node
import pytest


def test_remove_tail():
    list = SingleList()
    list.insert_tail(Node(2))
    list.insert_tail(Node(4))
    list.insert_tail(Node(6))
    list.insert_tail(Node(8))

    assert list.remove_tail().next is None
    assert list.remove_tail().data == 6
    assert list.remove_tail().data == 4
    assert list.count() == 1


def test_clear():
    list = SingleList()
    list.insert_tail(Node(2, 4))
    list.insert_tail(Node(4, 6))
    assert list.count() == 2

    list.clear()

    assert list.count() == 0
    assert list.head is None
    assert list.tail is None


def test_join():
    list = SingleList()
    list2 = SingleList()
    list.insert_tail(Node(2))
    list2.insert_tail(Node(4))
    list.insert_tail(Node(6))
    list.insert_tail(Node(10))
    list2.insert_tail(Node(8))
    list.join(list2)

    assert list2.count() == 0
    assert list.count() == 5
    assert list.remove_head().data == 2
    assert list.remove_tail().data == 8

if __name__ == "__main__":
    pytest.main()
