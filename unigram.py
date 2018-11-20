# takes as input, the dictionary of character occurance
# and the total number of characters
# returns a dictionary containing character: probability
def generate(dict, total_words):
    unigram = {}
    for key, value in dict.items():
        unigram[key] = value/ float(total_words)
        
    return unigram

# takes as input unigram dict
# generates text file in path
def save(unigram, path):
    with open(path, "w") as f:
        for key, value in unigram.items():
            f.write("(%c) => %f\n" % (key, value))

# takes as input a training file, and outputs the unigram
def train(train_file, character_set):
    train_dict = {}
    char_count = 0

    for c in character_set:
        train_dict[c] = 0

    with open(train_file) as f:
        while True:
            c = f.read(1)
            if not c:
                print("Reached end of " + train_file)
                break
            if c in character_set:
                train_dict[c] += 1
                char_count += 1

    return generate(train_dict, char_count)
    