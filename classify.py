import unigram
import bigram
import math

inputFilePath = "./input.txt"
outputFilePath = "./outputs/out"
outputFileCount = 1
unigrams = {
    'en': unigram.load('./models/unigramEN.txt'),
    'fr': unigram.load('./models/unigramFR.txt'),
    'ot': unigram.load('./models/unigramDC.txt')
}
bigrams = {
    'en': bigram.load('./models/bigramEN.txt'),
    'fr': bigram.load('./models/bigramFR.txt'),
    'ot': bigram.load('./models/bigramDC.txt')
}

en_prob_sum = 0
fr_prob_sum = 0
ot_prob_sum = 0
en_prob = 0
fr_prob = 0
ot_prob = 0

def getlanguage():
    language = "English"

    if fr_prob_sum > en_prob_sum and fr_prob_sum > ot_prob_sum:
        language = "French"
    if ot_prob_sum > en_prob_sum and ot_prob_sum > fr_prob_sum:
        language = "Dutch"

    return language

def writestep(file, c):
    file.write("FR: P(%c) = %f ==> log prob of sentence so far: %f\n" % (c, en_prob, en_prob_sum))
    file.write("EN: P(%c) = %f ==> log prob of sentence so far: %f\n" % (c, fr_prob, fr_prob_sum))
    file.write("OT: P(%c) = %f ==> log prob of sentence so far: %f\n" % (c, ot_prob, ot_prob_sum))
    file.write("\n")

def resetprobability():
    global en_prob_sum
    global fr_prob_sum
    global ot_prob_sum
    global en_prob
    global fr_prob
    global ot_prob
    en_prob_sum = 0
    fr_prob_sum = 0
    ot_prob_sum = 0
    en_prob = 0
    fr_prob = 0
    ot_prob = 0

with open(inputFilePath) as input_file:
    while True:
        input_string = input_file.readline()
        if not input_string:
            break
        
        outputPath = outputFilePath + str(outputFileCount) + ".txt"
        with open(outputPath, "w") as f:
            f.write(input_string)
            f.write("\n")
            # UNIGRAM
            f.write("UNIGRAM MODEL:\n")
            for c in input_string:
                c = c.lower()
                if c in unigram.character_set:
                    en_prob = unigrams['en'][c]
                    fr_prob = unigrams['fr'][c]
                    ot_prob = unigrams['ot'][c]

                    #make sure the prob are not zero
                    if en_prob > 0:
                        en_prob_sum += math.log(en_prob)
                    if fr_prob > 0:
                        fr_prob_sum += math.log(fr_prob)
                    if fr_prob > 0:
                        ot_prob_sum += math.log(ot_prob)

                    f.write("UNIGRAM: %c\n" % c)
                    writestep(f, c)
                
            unigram_language = getlanguage()
            f.write("According to the unigram model, the sentence is %s\n" % unigram_language)
            f.write("------------------------------------------------------\n")

            resetprobability()

            previous_char = None
            
            #BIGRAM
            f.write("BIGRAM MODEL:\n")
            for c in input_string:
                c = c.lower()

                if previous_char in bigram.character_set and c in bigram.character_set:
                    # u have previous and current so you can now get bigram probability
                    en_prob = bigrams['en'][previous_char][c]
                    fr_prob = bigrams['fr'][previous_char][c]
                    ot_prob = bigrams['ot'][previous_char][c]
                    
                    if en_prob > 0:
                        en_prob_sum += math.log(en_prob)
                    if fr_prob > 0:
                        fr_prob_sum += math.log(fr_prob)
                    if ot_prob > 0:
                        ot_prob_sum += math.log(ot_prob)
                
                previous_char = c

                f.write("BIGRAM: %c\n" % c)
                writestep(f, c)

            bigram_language = getlanguage()
            f.write("According to the unigram model, the sentence is %s\n" % bigram_language)


            print(input_string)
            print("Unigram => %s" % unigram_language)
            print("Bigram => %s" % bigram_language)
            print("-----")
            outputFileCount += 1
            resetprobability()
