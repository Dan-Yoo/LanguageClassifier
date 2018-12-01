character_set = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# takes as input, the dictionary of character occurance
# and the total number of characters
# returns a dictionary containing character: probability
def generate(dict, total_words):
    unigram = {}
    total = 0
    for key, value in dict.items():
        total += value
        unigram[key] = value/ (float(total_words) + len(character_set))
    return unigram

# takes as input unigram dict
# generates text file in path
def save(unigram, path):
    with open(path, "w") as f:
        for key, value in unigram.items():
            f.write("(%c) => %f\n" % (key, value))
    print("Saved unigram into ", path)

# returns a dictionary from given unigram file
def load(path):
    unigram = {}

    with open(path) as f:
        while True:
            line = f.readline()
            if not line:
                break
            key = line[1:2]
            value = float(line[7::])
            unigram[key] = value
    return unigram

def getcount(train_files, smoothing):
    train_dict = {}
    char_count = 0

    # initialize training dict
    for c in character_set:
        train_dict[c] = smoothing

    for path in train_files:
        with open(path) as f:
            while True:
                c = f.read(1)
                if not c:
                    break
                if c in character_set:
                    train_dict[c] += 1
                    char_count += 1
    
    return (train_dict, char_count)

# takes as input a training file, and outputs the unigram
def train(train_files, smoothing):
    result = getcount(train_files, smoothing)
    train_dict = result[0]
    char_count = result[1]

    print("Finished generating unigram for texts: ", train_files)
    return generate(train_dict, char_count)
    