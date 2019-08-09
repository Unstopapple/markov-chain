from markov import MarkovChain

dan = MarkovChain('dan.txt')
# baldur = MarkovChain('baldur.txt')

print(dan.get_new_sentence(12).upper())
# print(baldur.get_new_sentence(15))
