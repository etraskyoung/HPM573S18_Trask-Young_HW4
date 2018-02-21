import HW4Q1 as Q1

TAILS_PROB = 0.6 #heads probability is
NUMBER_OF_FLIPS = 20
NUMBER_OF_GAMES = 1000

#create 1000 games
myGame = Q1.LotsOfGames(id = 1, NumberOfGames = NUMBER_OF_GAMES, tails_prob = TAILS_PROB)

myGame.simulate(NUMBER_OF_FLIPS)

print("Average return is ", myGame.get_ave_total())

oneGame = Q1.Game(id = 1, tails_prob= TAILS_PROB)

print(oneGame.simulate(NumberOfFlips=NUMBER_OF_FLIPS))
