# Problem: Reveal Cards In Increasing Order

# Method: Queue-based Index Simulation

# Logic:
         """First sort the deck array in ascending order to process cards from smallest to largest
            Create a Queue filled with the array indices (0 to N-1) Simulate the card-revealing
            process using the index queue: for each sorted card pop the front index from the queue and place
            the card at that position in the result array If the queue is not empty move the next
            index from the front to the back of the queue"""


class Solution:
    def deckRevealedIncreasing(self, deck): 
        deck.sort()
        
        queue = deque(range(len(deck)))
        ans = [0] * len(deck)

        for i in deck:
            idx = queue.popleft()
            ans[idx] = i

            if queue:
                queue.append(queue.popleft())

        return ans  
