import random
import pyttsx3


class Speaker:
    def __init__(self):
        self.jokes = []
        self.affirm = []

        self.populate_list_of_jokes("jokes.txt")
        self.populate_list_of_affirmations("affirmations.txt")

    #Populate the list of jokes from affirmation.txt
    def populate_list_of_jokes(self, filename):
        with open(filename, encoding="utf8") as file:
            for line in file:
                self.jokes.append(line)

    #Populate the list of affirmations from affirmations.txt
    def populate_list_of_affirmations(self, filename):
        with open(filename, encoding="utf8") as file:
            for line in file:
                self.affirm.append(line)

    #Receive a random index from each list
    def random_index(self, list_of_words):
        index = random.randint(0, len(list_of_words) - 1)

        return index

    def read_joke(self):
        joke = self.get_joke()
        self.read_text(joke)

    def read_affirm(self):
        affirm = self.get_affirm()
        self.read_text(affirm)

    def read_text(self, text):
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)

        engine.say(text)
        engine.runAndWait()


    def get_joke(self):
        index = self.random_index(self.jokes)
        return self.jokes[index]

    def get_affirm(self):
        index = self.random_index(self.affirm)
        return self.affirm[index]


if __name__ == '__main__':
    sp = Speaker()
    joke = sp.get_joke()
    aff = sp.get_affirm()

    print(joke)

    sp.read_text(joke)
