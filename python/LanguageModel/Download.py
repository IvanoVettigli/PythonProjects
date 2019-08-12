from LanguageModel import MarkovChain
import urllib.request

with urllib.request.urlopen('https://www.gutenberg.org/files/521/521-0.txt') as in_text:  # Robinson Crusoe
    print(in_text(100))
#in_text = book.read().replace('\n', '')

#mc = MarkovChain(order=1)
#mc.train(in_text)
#print(mc.generate('t', 100))
