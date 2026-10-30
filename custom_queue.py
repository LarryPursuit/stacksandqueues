import random

class Queue:
    """A FIFO queue backed by a list: items enter at the back, leave from the front."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the item at the front of the queue (None if empty)."""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """Return the item at the front of the queue without removing it (None if empty)."""
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """Return True if the queue has no items."""
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Randomly selects a winner from the queue.
        Dequeues all items up to and including the winner.
        Returns the name of the winning customer.
        """
        if self.is_empty():
            print("No entries in the raffle - no winner selected.")
            return None

        winner = random.choice(self.items)

        # Process entries in FIFO order: everyone ahead of the winner is
        # dequeued first, and the loop stops once the winner is dequeued.
        while True:
            customer = self.dequeue()
            if customer == winner:
                break

        print(f"Congratulations {winner}, you won the raffle!")
        return winner
