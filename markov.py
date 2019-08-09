from random import choice


class MarkovChain:

    def __init__(self, file_name):
        self.file_name = file_name  # without this being first, it doesn't know what the file name is.
        self._input = self.__input_builder()
        self._sentence = []  # this will ultimately be the list of words that we use as our final output.

    def __input_builder(self):

        """This translates each line of text from the input file into a list of words we will run info from."""

        sentence = list()  # This is a nifty function in general. .split() is fucking great. I only use this once when the object is created, but yea.
        with open(self.file_name, 'r') as file:
            for line in file:
                sentence.append((line.upper().split()))
        return sentence

    def __first_word(self):

        """Generates a list of first words from the input text using words the person has actually started their sentences with."""

        first = list()  # why is this even a function? I only use it once. Might as well shove it somewhere, but it works, I guess.
        for line in self._input:
            first.append(line[0])
        return first

    def __chain_builder(self, chain_length=1):

        """Builds the sentence up by calling the next_word function repeatedly until we get the sentence we want."""

        # I'm going to be honest. I have no idea how this even works. I wanted it to just build a chain of words, but somewhere in the entire class
        # there is a part where generating a new sentence clears the old one. I don't know where or how, but it does. It's fucking magic.
        if not self._sentence:
            self._sentence.append(choice(self.__first_word()))
        for _ in range(chain_length + 1):
            self.__next_word()  # in all reality, chain_builder is an encapsulating forloop for next_word. I wanted it to be more "functional" but

    # I guess this is what we get.

    def __next_word(self):

        """This looks at each word we previously used in our sentence, then finds every word used after the previous word and chooses one from that list."""

        if self._sentence:
            previous_word = self._sentence[-1]
            potential_words = []  # enumeration nation hashtag end my life.
            for line in self._input:
                for i, word in enumerate(line):  # these for loops are what will make this program lag when I have thousands of lines of example text.
                    if word == previous_word:  # tbh, I couldn't care less. This is my first project. It wont be marketed. whatever.
                        if (i + 1) < len(line):  # also, someone's probably done it better than I have. If not, wtf is wrong with everyone.
                            potential_words.append(line[i + 1])  # learn from my mistakes. if line[i+1] is replaced with word, then it will just be shit.
            if potential_words:
                self._sentence.append(choice(potential_words))  # I tried making this just output the next word, but apparently this is what works.
        else:
            return None  # god smite me if this ever gets called. I don't know how, but this else clause is just here for backup.

    def get_new_sentence(self, size=1):

        """This generates a new sentence, then parses it to a string for output."""

        self.__chain_builder(size)
        if self._sentence:
            return " ".join(word for word in self._sentence)
        else:
            return False

    def get_last_sentence(self):

        """this just outputs the sentence we last built as a string if it exists."""

        if self._sentence:
            return " ".join(word for word in self._sentence)
        else:
            return None
