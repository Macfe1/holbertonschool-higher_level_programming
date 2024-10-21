#!/usr/bin/python3
"""
A module that defines a class
for creating an iterator.
"""


class CountedIterator:
    """
    An iterator that counts how many items have been iterated.

    Attributes:
        iterator(int): An iterator object created from an iterable.
        counter(int): A counter that tracks the number of items iterated.

    Methods:
        get_count(): Returns the number of items that have been iterated.
        __next__(): Retrieves the next item
        from the iterator and increments the counter.
    """
    def __init__(self, list_iter):
        """
        Initializes the CountedIterator with an iterable.

        Args:
            iterable (iterable): A data structure
            that can be iterated (list, tuple, etc.)
        """
        self.iterator = iter(list_iter)
        self.counter = 0

    def get_count(self):
        """
        Returns the number of items that have been iterated.

        Returns:
            int: The number of items iterated so far.
        """
        return self.counter

    def __next__(self):
        """
        Returns the next item from the iterator and increments the counter.

        Returns:
            object: The next item from the iterable.

        Raises:
            StopIteration: If there are no more items to iterate.
        """
        next_item = next(self.iterator)
        self.counter += 1

        return next_item


if __name__ == "__main__":
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()}\
                    items iterated.")
    except StopIteration:
        print("No more items.")
