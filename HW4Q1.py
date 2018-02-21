from enum import Enum
import numpy as np

#Create Class Game that has a method attribute Simulate()
#flips coin 20 times

class Game(object):
    #what happens with each coin flip
    def __init__(self, id, tails_prob):
        self._id = id
        self._rnd = np.random #random number generator for this coin flip
        self._rnd.seed(self._id) # specifying seed number generator for coin

        self._tailsProb = tails_prob
        self._results = []
        self.arrays = []
        self._win = 100
        self._entry_fee = 250

    def simulate (self, NumberOfFlips):
        toss = 0
        while toss < NumberOfFlips:
            if self._rnd.sample() < self._tailsProb:
                result = 1 #tails is 1
            else:
                result = 0 #heads is 0
            self._results.append(result)
            toss += 1
        return self._results

    def get_reward(self):
        i = 0
        value = -250
        win = [1, 1, 0]
        for i in self._results:
            array = self._results[i:i+3]
            self.arrays.append(array)
            i += 1

        for i in self.arrays:
            if i == win:
                value +=100
        return value

class LotsOfGames:
    def __init__(self, id, NumberOfGames, tails_prob):
        self._games = []
        self._value = []
        for game in range(NumberOfGames):
            game = Game(id, tails_prob)
            self._games.append(game)

    def simulate(self, NumberOfFlips):
        for game in self._games:
            game.simulate(NumberOfFlips)
            value = game.get_reward()
            self._value.append(value)

    def get_ave_total(self):
        return sum(self._value) / len(self._value)

