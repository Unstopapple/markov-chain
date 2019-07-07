from markov import MarkovChain

dan = MarkovChain('dan.txt')

print(dan.get_new_sentence())
