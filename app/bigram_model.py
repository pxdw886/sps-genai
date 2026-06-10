import random

class BigramModel:
    def __init__(self, corpus):
        self.bigram_dict = {}

        for sentence in corpus:
            words = sentence.lower().split()

            for i in range(len(words) - 1):
                current_word = words[i]
                next_word = words[i + 1]

                if current_word not in self.bigram_dict:
                    self.bigram_dict[current_word] = []

                self.bigram_dict[current_word].append(next_word)

    def generate_text(self, start_word, length):
        current_word = start_word.lower()
        generated_words = [current_word]

        for _ in range(length - 1):
            if current_word not in self.bigram_dict:
                break

            current_word = random.choice(
                self.bigram_dict[current_word]
            )

            generated_words.append(current_word)

        return " ".join(generated_words)