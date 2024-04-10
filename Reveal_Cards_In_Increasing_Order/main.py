class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q_indices = deque(range(len(deck))) # indices queue
        ans = [0] * len(deck) 

        for card in deck:
            # reveal the top card
            ind = q_indices.popleft()

            #revealed and taking out of the deck
            ans[ind] = card

            # if all the cards are not revealed
            if q_indices:
                #putting the next top card of the deck at the bottom of the deck
                ind = q_indices.popleft()
                q_indices.append(ind)
            
        return ans
