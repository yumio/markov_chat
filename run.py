from markov_python.cc_markov import MarkovChain

import scrapy

mc = MarkovChain()

#add filepath into mc.add_file(filepath) for files created by scrapy

mc.add_file('fetched_text')

#.generate_text() should generate a list of words
listofwords = []
listofwords = mc.generate_text(5)
listofwords = " ".join(listofwords)

print listofwords
