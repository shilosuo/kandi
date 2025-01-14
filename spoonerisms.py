from spoon import spoon

def tokenize_txt(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            tokens = f.read().lower().split()

        return tokens

    except FileNotFoundError:
        print("File not found")

def tokenize_vrt(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            lines = [f.readline().lower() for i in range(100)]
            tokens = [line.split()[0] for line in lines if line]

        return tokens

    except FileNotFoundError:
        print("File not found")

def main():

    '''
    while True:
        w1, w2 = input("Anna kaksi sanaa välilyönnillä erotettuna: ").split()
        print(spoon(w1, w2))
    '''

    #list_of_tokens = tokenize_txt("testidata.txt")
    list_of_tokens = tokenize_vrt("testidata.txt")

    bigrams = []
    for i in range(len(list_of_tokens)-1):
        bigrams.append((list_of_tokens[i], list_of_tokens[i+1]))

    # tähän bigrammisetin teko
    bigram_set = set(bigrams)

    sp_dict = {}
    spoonerisms = [] 
    for (a, b) in bigrams:
        if not (a, b) in sp_dict:
            sp_dict[(a, b)] = set()
            candidates = spoon(a, b) # palauttaa nyt listan
            if candidates:
                for candidate in candidates:
                    # seuraavalla rivillä ensin huolehditaan että mukaan ei tule degeneroituneita
                    # tai samat sanat eri järjestyksessä
                    if not(candidate == (a, b) or candidate == (b, a)) and candidate in bigram_set:
                        sp_dict[(a, b)].add(candidate)
        for cand in sp_dict[(a, b)]:
            spoonerisms.append((a, b, cand))
        

        #spoonerisms[(a, b)]["counter"] += 1
        
    

    with open("output.txt", "w", encoding="utf-8") as f:
        #for s in spoonerisms:
        for a, b, cand in spoonerisms:
            #f.write(s[0] + " " + s[1] + "\n")
            f.write(a + " " + b + " --> " + cand[0] + " " + cand[1] + "\n")



main()
