from spoon import spoon

def tokenize_txt(filename):
    try:
        with open("testidata.txt", encoding="utf-8") as f:
            tokens = f.read().lower().split()

        return tokens

    except FileNotFoundError:
        print("File not found")

def main():

    '''
    while True:
        w1, w2 = input("Anna kaksi sanaa välilyönnillä erotettuna: ").split()
        print(spoon(w1, w2))
    '''

    list_of_tokens = tokenize_txt("testidata.txt")
    #list_of_tokens = tokenize_vrt()

    bigrams = []
    for i in range(len(list_of_tokens)-1):
        bigrams.append((list_of_tokens[i], list_of_tokens[i+1]))

    # tähän bigrammisetin teko
    bigram_set = set(bigrams)


    spoonerisms = []
    for a, b in bigrams:
        sp = spoon(a, b) # palauttaa nyt listan
        #if sp in bigram_set:
        #    spoonerisms.append(sp)
        if sp:
            for candidate in sp:
                spoonerisms.append(candidate)
    

    with open("output.txt", "w", encoding="utf-8") as f:
        for s in spoonerisms:
            f.write(s[0] + " " + s[1] + "\n")



main()
