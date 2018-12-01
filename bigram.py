import unigram
character_set = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# takes as input, the dictionary of character occurance
# and the total number of characters
# returns a dictionary containing character: probability
def generate(dict, uni):
    bigram = {}
    for items in dict.items():
        key = items[0]
        value = items[1]
        bigram[key] = {}

        for c in value.items():
            total_count = uni[c[0]]
            bigram[key][c[0]] = c[1] / (total_count + (len(character_set) * len(character_set)))

    return bigram

# takes as input bigram dict
# generates text file in path
def save(bigram, path):
    with open(path, "w") as f:
        for items in bigram.items():
            key = items[0]
            value = items[1]

            for c in value.items():
                f.write("(%c|%c) => %9.8f\n" % (c[0], key, c[1]))
    print("Saved bigram into ", path)

# returns a dictionary from given bigram file
def load(path):
    bigram = {}

    for c in character_set:
        bigram[c] = {}
        for c2 in character_set:
            bigram[c][c2] = 0
            
    with open(path) as f:
        while True:
            line = f.readline()
            if not line:
                break
            child_key = line[1:2]
            parent_key = line[3:4]
            value = float(line[9::])

            bigram[parent_key][child_key] = value

    return bigram

# takes as input a training file, and outputs the bigram
def train(train_files, smoothing):
    uni = unigram.getcount(train_files, 0)[0]
    train_dict = {}
    bigram_count = 0
    prev_char = ''

    # initialize training dict
    for c in character_set:
        train_dict[c] = {}
        for c2 in character_set:
            train_dict[c][c2] = smoothing

    for path in train_files:
        with open(path) as f:
            while True:
                c = f.read(1)
                if not c:
                    break
                if c in character_set and prev_char in character_set:
                    train_dict[prev_char][c] += 1
                    bigram_count += 1

                prev_char = c
    print("Finished generating bigram for texts: ", train_files)
    return generate(train_dict, uni)
    