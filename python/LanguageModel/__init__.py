from collections import defaultdict, Counter
from numpy import cumsum, sum, searchsorted
from numpy.random import rand

class MarkovChain(object):
    def __init__(self, order=1):
        """
        Initializes a Markov Chain of the given order.
        """
        self._transitions = defaultdict(int)
        self._order = order

    def train(self, sequence):
        """
        Trains the model using sequence.
        """
        self._symbols = list(set(sequence))
        for i in range(len(sequence)-self._order):
            self._transitions[sequence[i:i+self._order], sequence[i+self._order]] += 1

    def predict(self, symbol):
        """
        Takes in input a string and predicts the next character.
        """
        if len(symbol) != self._order:
            raise ValueError('Expected string of %d chars, got %d' % (self._order, len(symbol)))
        probs = [self._transitions[(symbol, s)] for s in self._symbols]
        return self._symbols[self._weighted_pick(probs)]

    def generate(self, start, n):
        """
        Generates n characters from start.
        """
        result = start
        for i in range(n):
            new = self.predict(start)
            result += new
            start = start[1:] + new
        return result

    @staticmethod
    def _weighted_pick(weights):
        """
          Weighted random selection returns n_picks random indexes.
          The chance to pick the index i is given by weights[i].
        """
        return searchsorted(cumsum(weights), rand()*sum(weights))