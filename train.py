import unigram
import bigram

# trainEN = ["language_text/en-moby-dick.txt", "language_text/en-the-little-prince.txt"]
# trainFR = ["language_text/fr-le-petit-prince.txt", "language_text/fr-vingt-mille-lieues-sous-les-mers.txt"]
# trainDC = ["language_text/dc-text-1.txt", "language_text/dc-text-2.txt"]
trainEN = []
trainFR = []
trainDC = []
with open("./train/trainEN.txt") as input_file:
    while True:
        input_string = input_file.readline()
        if not input_string:
            break
        input_string = input_string.rstrip('\n')
        trainEN.append(input_string)
with open("./train/trainFR.txt") as input_file:
    while True:
        input_string = input_file.readline()
        if not input_string:
            break
        input_string = input_string.rstrip('\n')
        trainFR.append(input_string)
with open("./train/trainOT.txt") as input_file:
    while True:
        input_string = input_file.readline()
        if not input_string:
            break
        input_string = input_string.rstrip('\n')
        trainDC.append(input_string)



unigramEN_path = "models/unigramEN.txt"
bigramEN_path = "models/bigramEN.txt"
unigramFR_path = "models/unigramFR.txt"
bigramFR_path = "models/bigramFR.txt"
unigramDC_path = "models/unigramDC.txt"
bigramDC_path = "models/bigramDC.txt"

# generate unigrams
en_unigram = unigram.train(trainEN, 0.5)
fr_unigram = unigram.train(trainFR, 0.5)
dc_unigram = unigram.train(trainDC, 0.5)

# save unigrams to txt
unigram.save(en_unigram, unigramEN_path)
unigram.save(fr_unigram, unigramFR_path)
unigram.save(dc_unigram, unigramDC_path)

# generate bigrams
en_bigram = bigram.train(trainEN, 0.5)
fr_bigram = bigram.train(trainFR, 0.5)
dc_bigram = bigram.train(trainDC, 0.5)

# save bigrams to txt
bigram.save(en_bigram, bigramEN_path)
bigram.save(fr_bigram, bigramFR_path)
bigram.save(dc_bigram, bigramDC_path)
