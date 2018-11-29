import unigram
import bigram
import math

inputFilePath = "./input.txt"
outputFilePath = "./outputs/out"
outputFileCount = 1
unigrams = {
    'en': unigram.load('./models/unigramEN.txt'),
    'fr': unigram.load('./models/unigramFR.txt')
}
bigrams = {
    'en': bigram.load('./models/bigramEN.txt'),
    'fr': bigram.load('./models/bigramFR.txt')
}

en_prob_sum = 0
fr_prob_sum = 0
en_prob = 0
fr_prob = 0


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

                    #make sure the prob are not zero
                    if en_prob > 0:
                        en_prob_sum += math.log(en_prob)
                    if fr_prob > 0:
                        fr_prob_sum += math.log(fr_prob)

                    f.write("UNIGRAM: %c\n" % c)
                    f.write("FR: P(%c) = %f ==> log prob of sentence so far: %f\n" % (c, en_prob, en_prob_sum))
                    f.write("EN: P(%c) = %f ==> log prob of sentence so far: %f\n" % (c, fr_prob, fr_prob_sum))
                    f.write("\n")
                
            unigram_language = "English"
            if fr_prob_sum > en_prob_sum:
                unigram_language = "French"
            f.write("According to the unigram model, the sentence is %s\n" % unigram_language)
            f.write("------------------------------------------------------\n")

            en_prob_sum = 0
            fr_prob_sum = 0
            en_prob = 0
            fr_prob = 0

            previous_char = None
            
            #BIGRAM
            f.write("BIGRAM MODEL:\n")
            for c in input_string:
                c = c.lower()

                if previous_char in bigram.character_set and c in bigram.character_set:
                    # u have previous and current so you can now get bigram probability
                    en_prob = bigrams['en'][previous_char][c]
                    fr_prob = bigrams['fr'][previous_char][c]
                    
                    if en_prob > 0:
                        en_prob_sum += math.log(en_prob)
                    if fr_prob > 0:
                        fr_prob_sum += math.log(fr_prob)
                
                previous_char = c

                f.write("BIGRAM: %c\n" % c)
                f.write("FR: P(%c) = %f ==> log prob of sentence so far: %f\n" % (c, fr_prob, fr_prob_sum))
                f.write("EN: P(%c) = %f ==> log prob of sentence so far: %f\n" % (c, en_prob, en_prob_sum))
                f.write("\n")

            bigram_language = "English"
            if fr_prob_sum > en_prob_sum:
                bigram_language = "French"
            f.write("According to the unigram model, the sentence is %s\n" % bigram_language)

            outputFileCount += 1

            print(input_string)
            print("Unigram => %s" % unigram_language)
            print("Bigram => %s" % bigram_language)
            print("-----")