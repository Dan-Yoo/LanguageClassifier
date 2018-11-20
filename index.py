import unigram
# train unigram and bigram model for
# -English
# -French
# -My Choice

# Use language_text book text to train model

# Program Input
# trainFR.txt
# trainEN.txt
# trainOT.txt

# Program Output
# unigramFR.txt
# bgramFR.txt
# unigramEN.txt
# bgramEN.txt
# unigramOT.txt
# bgramOT.txt

trainFR = "language_text/fr-le-petit-prince.txt"
trainEN = "language_text/en-moby-dick.txt"

unigramFR_path = "models/unigramFR.txt"
bigramFR = "models/bigramFR.txt"
unigramEN_path = "models/unigramEN.txt"
bigramEN = "models/unigramEN.txt"

character_set = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# generate en unigram
en_unigram = unigram.train(trainEN, character_set)
fr_unigram = unigram.train(trainFR, character_set)
# save en unigram
unigram.save(en_unigram, unigramEN_path)
unigram.save(fr_unigram, unigramFR_path)


