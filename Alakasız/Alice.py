import string

wordcounts = {}

with open("alice.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.rstrip()
        for punc in string.punctuation:
            line = line.replace(punc, "")
        words = line.split()
        for word in words:
            if word.isalpha():
                word = word.lower()
                if word in wordcounts:        # zaten olmaması gerekiyor ki içine girebilsin.
                    wordcounts[word] += 1
                else:                         # else'i iptal edince hiçbir kelime dictionary'e girmiyor.
                    wordcounts[word] = 1      # demekki böyle yapınca dictionary içine kelime giriyormuş.
    print(wordcounts)
    for word in sorted(wordcounts.keys()):
        print(word + ":" + str(wordcounts.get(word)) + "\n", end="")