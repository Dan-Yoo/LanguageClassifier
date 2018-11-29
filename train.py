import unigram
import bigram

trainEN = ["language_text/en-moby-dick.txt", "language_text/en-the-little-prince.txt"]
trainFR = ["language_text/fr-le-petit-prince.txt", "language_text/fr-vingt-mille-lieues-sous-les-mers.txt"]

unigramEN_path = "models/unigramEN.txt"
bigramEN_path = "models/bigramEN.txt"
unigramFR_path = "models/unigramFR.txt"
bigramFR_path = "models/bigramFR.txt"

# generate unigrams
en_unigram = unigram.train(trainEN)
fr_unigram = unigram.train(trainFR)

# save unigrams to txt
unigram.save(en_unigram, unigramEN_path)
unigram.save(fr_unigram, unigramFR_path)

# generate bigrams
en_bigram = bigram.train(trainEN)
fr_bigram = bigram.train(trainFR)

# save bigrams to txt
bigram.save(en_bigram, bigramEN_path)
bigram.save(fr_bigram, bigramFR_path)
